from flask.json import JSONEncoder
from datetime import datetime
from bson import json_util, ObjectId

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        if obj:
            return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)