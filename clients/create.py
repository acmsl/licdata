import sys

sys.path.insert(0, "common")

import clientrepo
import params
import resp


def handler(event, context):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        email = params.retrieveEmail(body, event)
        address = params.retrieveAddress(body, event)
        contact = params.retrieveContact(body, event)
        phone = params.retrievePhone(body, event)

        client = clientrepo.findByEmail(email)
        if client:
            status = 409
            respBody = {
                "id": client["id"],
                "email": email,
                "address": address,
                "contact": contact,
                "phone": phone,
            }
            response = resp.buildResponse(status, respBody, event, context)
        else:
            clientId = clientrepo.insert(email, address, contact, phone)
            headers = event.get("headers", {})
            host = headers.get("host", event.get("host", ""))
            status = 201
            respBody = {
                "id": clientId,
                "email": email,
                "address": address,
                "contact": contact,
                "phone": phone,
            }
            response = resp.buildResponse(status, respBody, event, context)
            response["headers"].update(
                {"Location": f"https://{host}/clients/{clientId}"}
            )

    return response
