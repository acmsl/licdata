import json
import os
import sys
import datetime

sys.path.insert(0, "common")

import incidentrepo
import licenserepo
import mail
import params


def handler(event, context):

    headers = event.get("headers", {})
    host = headers.get("host", event.get("host", ""))
    response = {
        "headers": {"Content-Type": "application/json"},
        "event": str(event),
        "context": str(context),
    }

    status = 410
    file = None

    (body, respBody, error) = params.loadBody(event)

    print(body)

    if error:
        status = 500
    else:
        email = params.retrieveEmail(body, event)
        product = params.retrieveProduct(body, event)
        productVersion = params.retrieveProductVersion(body, event)
        installationCode = params.retrieveInstallationCode(body, event)

        license = licenserepo.findByEmailProductAndInstallationCode(
            email, product, productVersion, installationCode
        )

        if license:
            licenseId = license["id"]
            licenseData = json.dumps(license, indent=4, sort_keys=True, default=str)
            licenseEnd = license["licenseEnd"]
            if licenseEnd >= datetime.datetime.now():
                status = 200
                respBody = licenseData
                mail.send_email(
                    f"License in use: {licenseId}",
                    f"""<html>
  <body>
    <h1>Valid license requested</h1>
    <ul>
      <li>license: {licenseId}</li>
      <li>email: {email}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
      <li>licenseData: <pre>{licenseData}</pre></li>
    </ul>
  </body>
</html>
""",
                    "html",
                )
            else:
                print(f"License expired {licenseEnd}")
                status = 410
                incidentId = incidentrepo.insert(
                    licenseId, email, product, productVersion, installationCode
                )
                respBody = {
                    "error": "license expired",
                    "licenseId": licenseId,
                    "incident": incidentId,
                    "email": email,
                    "product": product,
                    "version": productVersion,
                    "installationCode": installationCode,
                }
                mail.send_email(
                    f"License expired: {licenseId}",
                    f"""<html>
                    <body>
                    <h1>License expired: {licenseId}</h1>
                    <ul>
                        <li>Incident: {incidentId}</li>
                        <li>license: {licenseId}</li>
                        <li>email: {email}</li>
                        <li>product: {product}</li>
                        <li>version: {productVersion}</li>
                        <li>installationCode: {installationCode}</li>
                        <li>licenseData: <pre>{licenseData}</pre></li>
                    </ul>
  </body>
</html>
""",
                    "html",
                )
        else:
            status = 404
            respBody = {
                "error": "unknown license",
                "email": email,
                "product": product,
                "productVersion": productVersion,
                "installationCode": installationCode,
            }
            mail.send_email(
                f"Unknown license: {email}",
                f"""<html>
  <body>
    <h1>Unknown license requested by {email}</h1>
    <ul>
      <li>email: {email}</li>
      <li>product: {product}</li>
      <li>version: {productVersion}</li>
      <li>installationCode: {installationCode}</li>
    </ul>
  </body>
</html>
""",
                "html",
            )

    response["statusCode"] = status
    response["body"] = json.dumps(respBody, indent=4, sort_keys=True, default=str)

    return response
