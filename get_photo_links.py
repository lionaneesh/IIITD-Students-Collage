import json
import time
from urllib2 import urlopen


fp = open("iiitd_group_members.txt")
data = json.loads(fp.read())
fp.close()

user_photos = {} # id -> [User's Name, Photo URL]

for user in data["data"]:
    try:
   	page = urlopen("http://graph.facebook.com/" + user["id"] + "?fields=picture.height(75)")
	page_data = json.loads(page.read())
    	photo_url = page_data["picture"]["data"]["url"]
    	user_photos[user["id"]] = [user["name"], photo_url]
    except:
	print "Not included ", user

fp = open("user_photos.json", "w")
fp.write(json.dumps(user_photos))
