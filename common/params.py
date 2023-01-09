import json
import base64


def loadBody(event):

    body = None
    respBody = {}
    error = True

    bodyEntry = event.get("body", event)

    if bodyEntry:
        if type(bodyEntry) is dict:
            body = bodyEntry
            error = False
        elif type(bodyEntry) is str:
            try:
                body = json.loads(bodyEntry)
                error = False
            except Exception as encodingError:
                try:
                    body = json.loads(base64.decodebytes(str.encode(bodyEntry)))
                    error = False
                except Exception as givingUp:
                    body = {
                        "error": "Not json, not base64-encoded",
                        "errors": [givingUp, encodingError],
                    }
        else:
            body = {"error": "Unknown input"}
    else:
        print("bodyEntry is null")

    return (body, error)


def retrieveParam(paramName, body, event, defaultValue):
    result = None

    if body:
        result = body.get(paramName, event.get(paramName, defaultValue))

    if not result:
        queryStringParameters = event.get("queryStringParameters", {})
        result = queryStringParameters.get(paramName)

    if not result:
        pathParameters = event.get("pathParameters", {})
        result = pathParameters.get(paramName)

    if not result:
        result = event.get(paramName, defaultValue)

    return result


def retrieveId(body, event):
    return retrieveParam("id", body, event, None)


def retrieveClientId(body, event):
    return retrieveParam("clientId", body, event, None)


def retrieveEmail(body, event):
    return retrieveParam("email", body, event, None)


def retrieveInstallationCode(body, event):
    return retrieveParam("installationCode", body, event, None)


def retrieveProduct(body, event):
    return retrieveParam("product", body, event, None)


def retrieveProductVersion(body, event):
    return retrieveParam("productVersion", body, event, "1")


def retrieveDescription(body, event):
    return retrieveParam("description", body, event, "1")


def retrieveDuration(body, event):
    return retrieveParam("duration", body, event, 7)


def retrieveBundle(body, event):
    return retrieveParam("bundle", body, event, None)


def retrieveEmail(body, event):
    return retrieveParam("email", body, event, None)


def retrieveAddress(body, event):
    return retrieveParam("address", body, event, None)


def retrieveContact(body, event):
    return retrieveParam("contact", body, event, None)


def retrievePhone(body, event):
    return retrieveParam("phone", body, event, None)
