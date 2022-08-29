import sys

sys.path.insert(0, "common")
import base64
import json
from github import Github
import os

import clientrepo
import licenserepo
import params
import pcrepo
import mail
import resp

def handler(event, context):

    headers = event.get("headers", {})
    host = headers.get("host", event.get("host", ""))

    status = 200
    file = None

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
    else:
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

            license = licenserepo.findByClientIdAndInstallationCode(
                clientId, installationCode
            )
            if license:
                licenseId = license["id"]
                licenseData = json.dumps(license, indent=4, sort_keys=True, default=str)
                respBody = license
            else:
                licenseId = licenserepo.insert(clientId, productName, productVersion)
                print(f"Inserted new license for client {clientId} -> {licenseId}")
                if licenseId:
                    status = 201
                    respBody = {
                        "id": licenseId,
                        "clientId": clientId,
                        "product": productName,
                        "version": productVersion,
                        "installationCode": installationCode,
                    }
                else:
                    status = 500
                    respBody = {
                        "error": "Error creating license",
                        "clientId": clientId,
                        "product": productName,
                        "version": productVersion,
                        "installationCode": installationCode,
                    }

    if licenseId:
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

        response["headers"].update({"Location": f"https://{host}/licenses/{licenseId}"})

        if status == 201:
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

    return buildResponse(status, respBody, event, context)
