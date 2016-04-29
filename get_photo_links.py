import json
from urllib2 import urlopen


fp = open("gsw.txt")
data = json.loads(fp.read())
fp.close()

user_photos = {} # id -> [User's Name, Photo URL]

for user in data["data"]:
    print user
    page = urlopen("http://graph.facebook.com/" + user["id"] + "?fields=picture")
    page_data = json.loads(page.read())
    photo_url = page_data["picture"]["data"]["url"]
    user_photos[user["id"]] = [user["name"], photo_url]

fp = open("user_photos.json", "w")
fp.write(json.dumps(user_photos))
