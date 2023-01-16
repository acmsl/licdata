import json
import base64


def load_body(event):

    body = None
    respBody = {}
    error = True

    body_entry = event.get("body", event)

    if body_entry:
        if type(body_entry) is dict:
            body = body_entry
            error = False
        elif type(body_entry) is str:
            try:
                body = json.loads(body_entry)
                error = False
            except Exception as encoding_error:
                try:
                    body = json.loads(base64.decodebytes(str.encode(body_entry)))
                    error = False
                except Exception as giving_up:
                    body = {
                        "error": "Not json, not base64-encoded",
                        "errors": [giving_up, encoding_error],
                    }
        else:
            body = {"error": "Unknown input"}
    else:
        print("body is null")

    return (body, error)


def retrieve_param(param_name, body, event, default_value):
    result = None

    if body:
        result = body.get(param_name, {})

    if not result:
        query_string_parameters = event.get("queryStringParameters", {})
        result = query_string_parameters.get(param_name)

    if not result:
        pathParameters = event.get("pathParameters", {})
        result = path_parameters.get(param_name)

    if not result:
        result = event.get(param_name, default_value)

    return result


def retrieve_id(body, event):
    return retrieve_param("id", body, event, None)


def retrieve_client_id(body, event):
    return retrieve_param("clientId", body, event, None)


def retrieve_email(body, event):
    return retrieve_param("email", body, event, None)


def retrieve_installation_code(body, event):
    return retrieve_param("installationCode", body, event, None)


def retrieve_product(body, event):
    return retrieve_param("product", body, event, None)


def retrieve_product_version(body, event):
    return retrieve_param("productVersion", body, event, "1")


def retrieve_description(body, event):
    return retrieve_param("description", body, event, "1")


def retrieve_duration(body, event):
    return retrieve_param("duration", body, event, 7)


def retrieve_bundle(body, event):
    return retrieve_param("bundle", body, event, None)


def retrieve_email(body, event):
    return retrieve_param("email", body, event, None)


def retrieve_address(body, event):
    return retrieve_param("address", body, event, None)


def retrieve_contact(body, event):
    return retrieve_param("contact", body, event, None)


def retrieve_phone(body, event):
    return retrieve_param("phone", body, event, None)
