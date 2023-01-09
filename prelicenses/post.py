import sys

sys.path.insert(0, "common")

import json

import clientrepo
import licenserepo
import prelicenserepo
import params
import pcrepo
import mail
import resp


def handler(event, context):

    status = 200

    (body, error) = params.loadBody(event)
    body = event.get("body", {})
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = buildResponse(status, respBody, event, context)
    else:
        name = params.retrieveName(body, event)
        productName = params.retrieveProduct(body, event)
        productVersion = params.retrieveProductVersion(body, event)
        installationCode = params.retrieveInstallationCode(body, event)

        prelicense = prelicenserepo.findByNameProductAndProductVersion(
            name, productName, productVersion
        )
        if prelicense:
            prelicenseId = prelicense["id"]
            prelicenseData = json.dumps(
                prelicense, indent=4, sort_keys=True, default=str
            )
            existingInstallationCode = prelicense["installationCode"]
            if existingInstallationCode != installationCode:
                status = 409
                respBody = {
                    "error": "invalid installation code",
                    "name": name,
                    "product": productName,
                    "version": productVersion,
                    "installationCode": installationCode,
                    "prelicenseId": prelicenseId,
                    "prelicenseData": json.dumps(
                        prelicenseData, indent=4, sort_keys=True, default=str
                    ),
                }
                response = resp.buildResponse(status, respBody, event, context)
            else:
                liberationCode = prelicense["liberationCode"]
                if liberationCode:
                    prelicenseEnd = prelicense["prelicenseEnd"]
                    if prelicenseEnd >= datetime.datetime.now():
                        status = 200
                        respBody = prelicenseData
                        response = resp.buildResponse(status, respBody, event, context)
                        mail.send_email(
                            f"Prelicense in use: {id}",
                            f"""<html>
  <body>
    <h1>Valid prelicense requested</h1>
    <ul>
      <li>prelicense: {prelicenseId}</li>
      <li>name: {name}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
      <li>prelicenseData: <pre>{prelicenseData}</pre></li>
    </ul>
  </body>
</html>
""",
                            "html",
                        )
                    else:
                        print(f"Prelicense expired {prelicenseEnd}")
                        status = 410
                        incidentId = incidentrepo.insert(
                            id,
                            "(prelicense expired)",
                            product,
                            productVersion,
                            installationCode,
                        )
                        respBody = {
                            "error": "license expired",
                            "licenseId": licenseId,
                            "name": name,
                            "incident": incidentId,
                            "product": product,
                            "version": productVersion,
                            "installationCode": installationCode,
                        }
                        response = resp.buildResponse(status, respBody, event, context)
                        mail.send_email(
                            f"Prelicense expired: {prelicenseId}",
                            f"""<html>
  <body>
    <h1>Prelicense expired: {prelicenseId}</h1>
    <ul>
      <li>id: {prelicenseId}</li>
      <li>Incident: {incidentId}</li>
      <li>name: {name}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
      <li>prelicenseData: <pre>{prelicenseData}</pre></li>
    </ul>
  </body>
</html>
""",
                            "html",
                        )

                else:
                    print(f"Prelicense with no liberation code")
                    delta = datetime.datetime.now() - prelicense["orderDate"]
                    if delta < 7:
                        status = 200
                        respBody = {
                            "id": prelicenseId,
                            "incident": incidentId,
                            "name": name,
                            "product": product,
                            "version": productVersion,
                            "installationCode": installationCode,
                            "prelicense": json.dumps(
                                prelicense, indent=4, sort_keys=True, default=str
                            ),
                        }
                        response = resp.buildResponse(status, respBody, event, context)
                    else:
                        status = 410
                        incidentId = incidentrepo.insert(
                            id,
                            "(prelicense disabled)",
                            product,
                            productVersion,
                            installationCode,
                        )
                        respBody = {
                            "error": "Prelicense disabled",
                            "id": prelicenseId,
                            "name": name,
                            "incident": incidentId,
                            "product": product,
                            "version": productVersion,
                            "installationCode": installationCode,
                        }
                        response = resp.buildResponse(status, respBody, event, context)
                        mail.send_email(
                            f"Prelicense disabled: {prelicenseId}",
                            f"""<html>
  <body>
    <h1>Prelicense disabled: {prelicenseId}</h1>
    <ul>
      <li>Incident: {incidentId}</li>
      <li>id: {prelicenseId}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
      <li>prelicenseData: <pre>{prelicenseData}</pre></li>
    </ul>
  </body>
</html>
""",
                            "html",
                        )

        else:
            status = 409
            respBody = {
                "error": "No prelicense found",
                "name": name,
                "product": product,
                "version": productVersion,
                "installationCode": installationCode,
            }
            response = resp.buildResponse(status, respBody, event, context)

    if status == 200:
        try:
            mail.send_email(
                f"New prelicense: {prelicenseId}",
                f"""<html>
<body>
    <h1>New prelicense: {prelicenseId}</h1>
    <ul>
      <li>prelicense: {prelicenseId}</li>
      <li>name: {name}</li>
      <li>product: {productName}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
    </ul>
  </body>
</html>
""",
                "html",
            )
        except:
            print(f"Error sending new-prelicense email")

    return response
