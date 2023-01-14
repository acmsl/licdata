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


def findById(event, context, repo):
    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        id = params.retrieveId(body, event)

        (item, sha) = repo.findById(id)
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
    repo,
    path
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

        (item, sha) = repo.findByPk(pk)
        if item:
            status = 409
            respBody = {"id": item["id"]}
            respBody.update(attributes)
            response = resp.buildResponse(status, respBody, event, context)
        else:
            id = repo.insert(attributes)
            headers = event.get("headers", {})
            host = headers.get("host", event.get("host", ""))
            status = 201
            respBody = {"id": id}
            respBody.update(attributes)
            response = resp.buildResponse(status, respBody, event, context)
            response["headers"].update(
                {"Location": f"https://{host}/{path}/{id}"}
            )

    return response


def update(event, context, retrieveAttributes, repo):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        id = params.retrieveId(body, event)
        attributes = retrieveAttributes(body, event)
        attributes["id"] = id
        (item, sha) = repo.findById(id)
        if item:

            repo.update(attributes)
            status = 200
            respBody = attributes
            response = resp.buildResponse(status, respBody, event, context)
        else:
            status = 404
            respBody = {"error": "not found"}
            response = resp.buildResponse(status, respBody, event, context)

    return response


def delete(event, context, repo):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        id = params.retrieveId(body, event)

        (item, sha) = repo.findById(id)
        if item:
            repo.delete(id)
            status = 200
            respBody = {"id": item["id"]}
            response = resp.buildResponse(status, respBody, event, context)
        else:
            status = 404
            respBody = {"error": "not found"}
            response = resp.buildResponse(status, respBody, event, context)

    return response


def list(event, context, repo):

    status = 200

    (body, error) = params.loadBody(event)
    if error:
        status = 500
        respBody = {"error": "Cannot parse body"}
        response = resp.buildResponse(status, respBody, event, context)
    else:
        (items, sha) = repo.list()
        if items:
            respBody = items
            response = resp.buildResponse(status, respBody, event, context)
        else:
            respBody = []
            response = resp.buildResponse(status, respBody, event, context)

    return response
