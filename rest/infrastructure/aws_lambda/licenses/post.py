"""
licdata/rest/infrastructure/aws_lambda/licenses/post.py

This file provides an AWS Lambda handler to create a license as well as associated entities.

Copyright (C) 2023-today ACM S.L. Licdata

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import domain.clientrepo
import domain.licenserepo
import domain.pcrepo
import infrastructure.aws_lambda.params
import infrastructure.aws_lambda.mail
import infrastructure.aws_lambda.resp

import base64
import json
from github import Github
import os


def handler(event, context):
    """
    AWS Lambda handler to create a new license as well as associated entities.
    :param event: The AWS Lambda event.
    :type event: event
    :param context: The AWS Lambda context.
    :type context: context
    :return: The response.
    :rtype: Dict
    """
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
