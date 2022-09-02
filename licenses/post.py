import base64
import json
from github import Github
import os
import sys

sys.path.insert(0, "common")

import clientrepo
import licenserepo
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

    email = params.retrieveEmail(body, event)
    productName = params.retrieveProduct(body, event)
    productVersion = params.retrieveProductVersion(body, event)
    installationCode = params.retrieveInstallationCode(body, event)
    description = params.retrieveDescription(body, event)

    client = clientrepo.findByEmail(email)
    if client:
        clientId = client["id"]
    else:
        clientId = clientrepo.insert(email)
        print(f"Inserted new client {email} -> {clientId}")

    license = licenserepo.findByClientIdAndInstallationCode(clientId, installationCode)
    if license:
        licenseId = license["id"]
    else:
        licenseId = licenserepo.insert(clientId, productName, productVersion)
        print(f"Inserted new license for client {clientId} -> {licenseId}")
        if licenseId:
            status = 201

    pc = pcrepo.findByInstallationCode(installationCode)
    if pc:
        if not licenseId in pc["licenses"]:
            pcId = pc["id"]
            pcrepo.addLicense(pc["id"], licenseId)
            print(f"Added license {licenseId} to {pcId}")
        else:
            pcId = pcrepo.insert([licenseId], installationCode, description)
            print(f"Inserted new pc for license {licenseId} -> {pcId}")
    else:
        pcId = pcrepo.insert([licenseId], installationCode, description)
        print(f"Inserted new pc for license {licenseId} -> {pcId}")

    if licenseId:
        response["headers"].update({"Location": f"https://{host}/licenses/{licenseId}"})

    if status == 201:
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

    response["statusCode"] = status

    return response
