import sys

sys.path.insert(0, "common")
import json
import os
import datetime

import incidentrepo
import licenserepo
import mail
import params
import resp


def handler(event, context):

    status = 410
    file = None

    (body, error) = params.loadBody(event)

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

    return resp.buildResponse(status, respBody, event, context)
