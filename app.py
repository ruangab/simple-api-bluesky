from flask import Flask, request, jsonify, blueprints
from atproto import Client
from utils.Login import login
import json


app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login(dados):
    user, bluesky = login()
    json_doc = {
        "did":user.did,
        "handle":user.handle,
        "accessJwt":bluesky._access_jwt,
        "refreshJwt":bluesky._refresh_jwt,
    }
    return jsonify(json_doc)

from routes.UserRoutes import user_routes
app.register_blueprint(user_routes)


if __name__ == "__main__":
    app.run("0.0.0.0", port=19019, debug=True)
