from flask import Blueprint, request, jsonify
from utils.Login import login
user_routes = Blueprint("use_routes", __name__)

@user_routes.route("/create/post",methods=["POST"])
def create_post():
    user, bluesky = login()
    request_json = request.get_json();
    
    post = bluesky.send_post(request_json["message"])

    return jsonify({
        "post_urt":post.uri,
        "post_cid":post.cid,
        "message":"Postado com sucesso"
    })

@user_routes.route("/profile",methods=["POST"])
def get_user():
    user, bluesky = login()

    doc_user = {
        "display_name":user.display_name,
        "followers_count":user.followers_count,
        "follows_count":user.follows_count,
        "user_name":user.handle,
        "description":user.description,
        "posts_count":user.posts_count,
        "image_profile":user.avatar,
        "banner_profile":user.banner
    }

    return jsonify(doc_user)


@user_routes.route("/feed",methods=["POST"])
def get_feed():
    user, bluesky = login()

    feed = bluesky.app.bsky.feed.get_feed({
    'feed': 'at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.generator/whats-hot',
    'limit': 1,
    })

    return jsonify({
        "feed":feed.feed,
        "next_page":feed.cursor
    })


