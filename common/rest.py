import sys

sys.path.insert(0, "common")
import githubrepo
import params
import resp


def retrieveAttributesFromParams(body, event, attributeNames):
    result = {}

    for attribute in attributeNames:
        result[attribute] = params.retrieveParam(attribute, body, event, None)

    return result


def findById(event, context, entityType):
    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        id = params.retrieveId(body, event)

        item = githubrepo.findById(id, entityType)
        if item:
            status = 200
            respBody = item
            response = resp.buildResponse(status, respBody, event, context)
        else:
            status = 404
            respBody = {"error": "not found"}
            response = resp.buildResponse(status, respBody, event, context)

    return response


def create(
    event,
    context,
    retrievePk,
    retrieveAttributes,
    findByPk,
    entityType,
    filterKeys,
    attributeNames,
):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        pk = retrievePk(body, event)
        attributes = retrieveAttributes(body, event)

        item = findByPk(pk)
        if item:
            status = 409
            respBody = {"id": item["id"]}
            respBody.update(attributes)
            response = resp.buildResponse(status, respBody, event, context)
        else:
            id = githubrepo.insert(attributes, entityType, filterKeys, attributeNames)
            headers = event.get("headers", {})
            host = headers.get("host", event.get("host", ""))
            status = 201
            respBody = {"id": id}
            respBody.update(attributes)
            response = resp.buildResponse(status, respBody, event, context)
            response["headers"].update(
                {"Location": f"https://{host}/{entityType}/{id}"}
            )

    return response


def update(event, context, retrieveAttributes, entityType, filterKey, attributeNames):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        id = params.retrieveId(body, event)
        attributes = retrieveAttributes(body, event)

        item = githubrepo.findById(id, entityType)
        if item:
            githubrepo.update(item, entityType, filterKey, attributeNames)
            status = 200
            respBody = {"id": item["id"]}
            respBody.update(item)
            response = resp.buildResponse(status, respBody, event, context)
        else:
            status = 404
            respBody = {"error": "not found"}
            response = resp.buildResponse(status, respBody, event, context)

    return response


def delete(event, context, entityType):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        id = params.retrieveId(body, event)

        item = githubrepo.findById(id, entityType)
        if item:
            githubrepo.delete(id, entityType)
            status = 200
            respBody = {"id": item["id"]}
            response = resp.buildResponse(status, respBody, event, context)
        else:
            status = 404
            respBody = {"error": "not found"}
            response = resp.buildResponse(status, respBody, event, context)

    return response


def list(event, context, entityType):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        items = githubrepo.list(entityType)
        if items:
            status = 200
            respBody = {}
            respBody[entityType] = items
            response = resp.buildResponse(status, respBody, event, context)
        else:
            status = 404
            respBody = {"error": "not found"}
            response = resp.buildResponse(status, respBody, event, context)

    return response
