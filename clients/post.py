import json
import os
import sys

sys.path.insert(0, "deps")

def handler(event, context):

    headers = event.get("headers", {})
    host = headers.get("host", event.get("host", ""))
    response = {
        "headers": {"Content-Type": "application/json"},
        "event": str(event),
        "context": str(context),
    }

    status = 200

    body = event.get("body", {})
    if body:
        try:
            body = json.loads(body)
        except:
            # no Content-Type: application/json header
            body = json.loads(base64.decodebytes(str.encode(body)))

    email = params.retrieveEmail(body, event)
    address = params.retrieveAddress(body, event)
    contact = params.retrieveContact(body, event)
    phone = params.retrievePhone(body, event)

    client = clientrepo.findByEmail(email)
    if client:
       status = 204
    else:
        clientId = clientrepo.insert(email, address, contact, phone)
        response["headers"].update({"Location": f"https://{host}/clients/{clientId}"})
        status = 201

    response["statusCode"] = status

    return response
