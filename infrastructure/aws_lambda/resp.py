import json


def buildResponse(status, body, event, context):

    return {
        "headers": {"Content-Type": "application/json"},
        "event": str(event),
        "context": str(context),
        "statusCode": status,
        "body": json.dumps(body, indent=4, sort_keys=True, default=str),
    }
