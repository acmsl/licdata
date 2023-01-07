import base64
import json
from github import Github
import os
import sys

sys.path.insert(0, "common")

import clientrepo
import licenserepo
import prelicenserepo
import params
import pcrepo
import mail


def handler(event, context):

    headers = event.get("headers", {})
    host = headers.get("host", event.get("host", ""))
    response = {
        "headers": {"Content-Type": "application/json"},
        "event": str(event),
        "context": str(context),
    }

    status = 200
    file = None

    body = event.get("body", {})
    print("Event: ")
    print(event)
    print("Body: ")
    print(body)
    if body:
        try:
            body = json.loads(body)
        except:
            # no Content-Type: application/json header
            body = json.loads(base64.decodebytes(str.encode(body)))

    name = params.retrieveId(body, event)
    productName = params.retrieveProduct(body, event)
    productVersion = params.retrieveProductVersion(body, event)
    installationCode = params.retrieveInstallationCode(body, event)

    prelicense = prelicenserepo.findByNameProductAndProductVersion(name, productName, productVersion)
    if prelicense:
        prelicenseId = prelicense["id"]
        prelicenseData = json.dumps(prelicense, indent=4, sort_keys=True, default=str)
        existingInstallationCode = prelicense["installationCode"]
        if existingInstallationCode != installationCode:
           status = 409
        else:
            liberationCode = prelicense["liberationCode"]
            if liberationCode:
                prelicenseEnd = prelicense["prelicenseEnd"]
                    if prelicenseEnd >= datetime.datetime.now():
                        status = 200
                        respBody = prelicenseData
                        mail.send_email(
                            f"Prelicense in use: {id}",
                            f"""<html>
  <body>
    <h1>Valid prelicense requested</h1>
    <ul>
      <li>prelicense: {prelicenseId}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
      <li>prelicenseData: <pre>{prelicenseData}</pre></li>
    </ul>
  </body>
</html>
""",
                            "html")
                    else:
                        print(f"Prelicense expired {prelicenseEnd}")
                        status = 410
                        incidentId = incidentrepo.insert(
                            id, "(prelicense expired)", product, productVersion, installationCode)
                        respBody = {
                            "error": "license expired",
                            "licenseId": licenseId,
                            "incident": incidentId,
                            "product": product,
                            "version": productVersion,
                            "installationCode": installationCode,
                        }
                        mail.send_email(
                            f"Prelicense expired: {prelicenseId}",
                            f"""<html>
  <body>
    <h1>Prelicense expired: {prelicenseId}</h1>
    <ul>
      <li>Incident: {incidentId}</li>
      <li>license: {licenseId}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
      <li>prelicenseData: <pre>{prelicenseData}</pre></li>
    </ul>
  </body>
</html>
""",
                            "html")

            else:
                print(f"Prelicense with no liberation code")
                delta = datetime.datetime.now() - prelicense["orderDate"]
                if delta < 7:
                    status = 200
                else:
                    status = 410
                    incidentId = incidentrepo.insert(
                        id, "(prelicense disabled)", product, productVersion, installationCode)
                    respBody = {
                        "error": "Prelicense disabled",
                        "prelicenseId": prelicenseId,
                        "incident": incidentId,
                        "product": product,
                        "version": productVersion,
                        "installationCode": installationCode,
                    }
                    mail.send_email(
                            f"Prelicense disabled: {prelicenseId}",
                            f"""<html>
  <body>
    <h1>Prelicense disabled: {prelicenseId}</h1>
    <ul>
      <li>Incident: {incidentId}</li>
      <li>license: {licenseId}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
      <li>prelicenseData: <pre>{prelicenseData}</pre></li>
    </ul>
  </body>
</html>
""",
                            "html")

    else:
        status = 409

    if status == 200:
        try:
            mail.send_email(
                f"New license: {licenseId}",
                f"""<html>
<body>
    <h1>New license: {licenseId}</h1>
    <ul>
      <li>license: {licenseId}</li>
      <li>email: {email}</li>
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
            print(f"Error sending new-license email")

    response["statusCode"] = status

    return response
