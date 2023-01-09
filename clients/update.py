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
        id = params.retrieveId(body, event)
        email = params.retrieveEmail(body, event)
        address = params.retrieveAddress(body, event)
        contact = params.retrieveContact(body, event)
        phone = params.retrievePhone(body, event)

        client = clientrepo.findById(id)
        if client:
            clientrepo.update(id, email, address, contact, phone)
            status = 200
            respBody = {
                "id": client["id"],
                "email": email,
                "address": address,
                "contact": contact,
                "phone": phone,
            }
            response = resp.buildResponse(status, respBody, event, context)
        else:
            status = 404
            respBody = {"error": "not found"}
            response = resp.buildResponse(status, respBody, event, context)

    return response
