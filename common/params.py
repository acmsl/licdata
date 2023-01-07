def retrieveParam(paramName, body, event, defaultValue):
    if body:
        return body.get(paramName, event.get(paramName, defaultValue))
    else:
        return event.get(paramName, defaultValue)

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
