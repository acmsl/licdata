from params import load_body, retrieve_param, retrieve_id
from resp import build_response
import inspect
from datetime import datetime

def retrieve_attributes_from_params(body, event, attribute_names):
    result = {}

    for attribute in attribute_names:
        result[attribute] = retrieve_param(attribute, body, event, None)

    return result


def find_by_id(event, context, repo):
    status = 200

    (body, error) = load_body(event)
    if error:
        status = 500
        resp_body = {"error": "Cannot parse body"}
        response = build_response(status, resp_body, event, context)
    else:
        id = retrieve_id(body, event)

        print(f"Finding by {id}")
        (item, sha) = repo.find_by_id(id)
        print(f"Retrieved {item}")
        if item:
            status = 200
            resp_body = item
            response = build_response(status, resp_body, event, context)
        else:
            status = 404
            resp_body = {"error": "not found"}
            response = build_response(status, resp_body, event, context)

    return response


def create(
    event,
    context,
    retrieve_pk,
    retrieve_attributes,
    repo
):

    status = 200

    (body, error) = load_body(event)
    if error:
        status = 500
        resp_body = {"error": "Cannot parse body"}
        response = build_response(status, resp_body, event, context)
    else:
        pk = retrieve_pk(body, event)
        attributes = retrieve_attributes(body, event)

        (item, sha) = repo.find_by_pk(pk)
        if item:
            status = 409
            resp_body = {}
            resp_body.update(attributes)
            resp_body.update({"id": item["id"] })
            if "_created" in item:
                resp_body.update({ "_created": item["_created"] })
            response = build_response(status, resp_body, event, context)
        else:
            attributes["_created"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            id = repo.insert(attributes)
            headers = event.get("headers", {})
            host = headers.get("host", event.get("host", ""))
            status = 201
            resp_body = {}
            resp_body.update(attributes)
            resp_body.update({ "id": id })
            response = build_response(status, resp_body, event, context)
            response["headers"].update(
                {"Location": f"https://{host}/{repo.path()}/{id}"}
            )

    return response


def update(event, context, retrieve_attributes, repo):

    status = 200

    (body, error) = load_body(event)
    if error:
        status = 500
        resp_body = {"error": "Cannot parse body"}
        response = build_response(status, resp_body, event, context)
    else:
        id = retrieve_id(body, event)
        attributes = retrieve_attributes(body, event)
        attributes["id"] = id
        (item, sha) = repo.find_by_id(id)
        attributes["_created"] = item["_created"]
        if item:
            repo.update(attributes)
            status = 200
            resp_body = attributes
            response = build_response(status, resp_body, event, context)
        else:
            status = 404
            resp_body = {"error": "not found"}
            response = build_response(status, resp_body, event, context)

    return response


def delete(event, context, repo):

    status = 200

    (body, error) = load_body(event)
    if error:
        status = 500
        resp_body = {"error": "Cannot parse body"}
        response = build_response(status, resp_body, event, context)
    else:
        id = retrieve_id(body, event)

        (item, sha) = repo.find_by_id(id)
        if item:
            repo.delete(id)
            status = 200
            resp_body = {"id": item["id"]}
            response = build_response(status, resp_body, event, context)
        else:
            status = 404
            resp_body = {"error": "not found"}
            response = build_response(status, resp_body, event, context)

    return response


def list(event, context, repo):

    status = 200

    (body, error) = load_body(event)
    if error:
        status = 500
        resp_body = {"error": "Cannot parse body"}
        response = build_response(status, resp_body, event, context)
    else:
        (items, sha) = repo.list()
        if items:
            resp_body = items
            response = build_response(status, resp_body, event, context)
        else:
            resp_body = []
            response = build_response(status, resp_body, event, context)

    return response
