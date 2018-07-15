import json
from app.generate import generate
from app.data import Sonnets


def shakespeare(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({ "sonnet": generate() })
    }

def get_sonnet(event, context):
    _id = event["pathParameters"]["id"]
    if _id == None:
        return {
            "statusCode": 400,
            "body": json.dumps({ "error": "no id provided" })
        }
    body = {}
    statusCode = 200

    try:
        _id = int(_id) - 1
        keys = list(Sonnets.keys())
        if len(keys) <= _id:
            statusCode = 400
            body["error"] = "id must be less than " + str(len(keys))
        elif _id < 1:
            statusCode = 400
            body["error"] = "id must be 1 or greater"
        else:
            body["sonnet"] = {
                "title": keys[_id],
                "text": Sonnets[keys[_id]]
            }

    except ValueError:
        statusCode = 400
        body["error"] = "id is not an integer"


    return {
        "statusCode": statusCode,
        "body": json.dumps(body)
    }
