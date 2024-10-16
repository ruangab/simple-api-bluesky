from atproto import Client
from flask import request

@staticmethod
def login():
    bluesky = Client();

    request_json = request.get_json();
    user = request_json["user"]
    password = request_json["password"]

    login_user = bluesky.login(user, password)

    return login_user, bluesky
