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
    response = {"headers": {"Content-Type": "application/json"}}

    status = 410
    file = None

    body = event.get("body", {})
    if body:
        try:
            body = json.loads(body)
        except:
            # no Content-Type: application/json header
            body = json.loads(base64.decodebytes(str.encode(body)))

    print(body)

    email = params.retrieveEmail(body, event)
    product = params.retrieveProduct(body, event)
    productVersion = params.retrieveProductVersion(body, event)
    installationCode = params.retrieveInstallationCode(body, event)

    license = licenserepo.findByEmailProductAndInstallationCode(
        email, product, productVersion, installationCode
    )

    if license:
        licenseId = license["id"]
        if license["licenseEnd"] >= datetime.datetime.now():
            status = 200
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
    </ul>
  </body>
</html>
""",
                "html",
            )
        else:
            status = 410
            incidentId = incidentrepo.insert(
                licenseId, email, product, productVersion, installationCode
            )
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
    </ul>
  </body>
</html>
""",
                "html",
            )
    else:
        status = 404
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

    return response
