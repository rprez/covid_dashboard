from flask import current_app, g
from werkzeug.local import LocalProxy

from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads
from pymongo import DESCENDING, ASCENDING


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)
    DATABASE_URI = current_app.config["DATABASE_URI"]
    DATABASE_NS = current_app.config["DATABASE_NS"]
    if db is None:

        """
       Connection Pooling Setting the maximum connection pool size to 50 active connections.
       
       Timeouts: Write concern timeout limit to 2500 milliseconds.

       """
        try:
            db = g._database = MongoClient(DATABASE_URI,
            # Set the maximum connection pool size to 50 active connections.
            # Set the write timeout limit to 2500 milliseconds.
            maxPoolSize=50,wtimeout=2500,retryWrites=False) [DATABASE_NS]
        except ConnectionFailure:
            print("Server not available")
        except Exception as e:
            print("MongoDB connection error")

    return db