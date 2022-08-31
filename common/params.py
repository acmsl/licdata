def retrieveParam(paramName, body, event, defaultValue):
    if body:
        return body.get(paramName, event.get(paramName, defaultValue))
    else:
        return event.get(paramName, defaultValue)


def retrieveClientId(body, event):
    return retrieveParam("clientId", body, event, "missing")


def retrieveEmail(body, event):
    return retrieveParam("email", body, event, "missing")


def retrieveInstallationCode(body, event):
    return retrieveParam("installationCode", body, event, "missing")


def retrieveProduct(body, event):
    return retrieveParam("product", body, event, "missing")


def retrieveProductVersion(body, event):
    return retrieveParam("productVersion", body, event, "1")


def retrieveDescription(body, event):
    return retrieveParam("description", body, event, "1")
