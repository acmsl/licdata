import sys

sys.path.insert(0, "common")

import json

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

        client = clientrepo.findById(id)
        if client:
            status = 200
            respBody = client
            response = resp.buildResponse(status, respBody, event, context)
        else:
            status = 404
            respBody = {"error": "not found"}
            response = resp.buildResponse(status, respBody, event, context)

    return response
