#!/usr/bin/env python

import os
import sys
import ConfigParser
import urllib2
import urllib
import json
import ssl

ALFRED_CONFIG_SECTION = "Rocket.Chat"
ALFRED_CONFIG_COUNT = 20
ALFRED_RC_FILE = ".search_rocket_chat.alfred"
ALFRED_RC_PATH = os.environ.get("ALFRED_RC_PATH", "~/" + ALFRED_RC_FILE)


def throw_error(message):
    print(json.dumps({"items": [{"title": message, "icon": {"path": "./error.png"}}]}))

    sys.exit(1)


def do_request(path, data=None):
    url = rc_url.strip("/") + path

    if data is not None:
        url += "?" + urllib.urlencode(data)

    request = urllib2.Request(
        url, headers={"X-User-Id": rc_user, "X-Auth-Token": rc_auth}
    )
    try:
        response = urllib2.urlopen(request, timeout=1)
        return json.load(response)
    except ssl.SSLError:
        return {"channels": [], "users": []}
    except urllib2.URLError:
        throw_error("URL Error (URL, Auth, ...): " + rc_url)


try:
    config_file = os.path.expanduser(ALFRED_RC_PATH)
    config = ConfigParser.ConfigParser()
    config.read(config_file)

    rc_url = config.get(ALFRED_CONFIG_SECTION, "url")
    rc_user = config.get(ALFRED_CONFIG_SECTION, "user")
    rc_auth = config.get(ALFRED_CONFIG_SECTION, "auth")
except ConfigParser.NoSectionError:
    throw_error("Config file not found: ~/" + ALFRED_RC_FILE)

if len(sys.argv) > 1:
    query = " ".join(sys.argv[-1:]).lower()
else:
    query = ""

channel_query = True
user_query = True

try:
    if query and query[0] is "@":
        channel_query = False
        query = query[1:]
except IndexError:
    pass

try:
    if query and query[0] is "#":
        user_query = False
        query = query[1:]
except IndexError:
    pass

items = []

# Users
if user_query is True:
    data = {"count": ALFRED_CONFIG_COUNT}
    if query:
        data["query"] = json.dumps(
            {
                "$or": [
                    {"username": {"$regex": query, "$options": "i"}},
                    {"name": {"$regex": query, "$options": "i"}},
                ]
            }
        )

    users = do_request("/api/v1/users.list", data)

    for user in users["users"]:
        items.append(
            {
                "title": "@" + user["username"],
                "arg": "@" + user["username"],
                "subtitle": user["name"] + " (" + user["status"] + ")",
                "type": "user",
            }
        )

# Channels
if channel_query is True:
    data = {"count": ALFRED_CONFIG_COUNT}

    # NOT SUPPORTED
    # if query:
    #    data['query'] = json.dumps({ "name" : {"$regex": query, "$options": "i" } })

    channels = do_request("/api/v1/channels.list")

    for item in channels["channels"]:
        if query.lower() in item["name"].lower():
            items.append(
                {
                    "title": "#" + item["name"],
                    "arg": "#" + item["name"],
                    "type": "channel",
                }
            )

print(json.dumps({"items": items}))
