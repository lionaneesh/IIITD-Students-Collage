import json
from urllib2 import urlopen


fp = open("iiitd_group_members.txt")
data = json.loads(fp.read())
fp.close()

user_photos = {} # id -> [name": "Owais Qureshi", 
      "administrator": false, 
      "id": "1384616488497366"
    }, 
    {
      "name": "Kashif Qureshi", 
      "administrator": false, 
      "id": "1513222442287748"
    }, 
    {
      "name": "Nida Doll", 
      "administrator": false, 
      "id": "1577663512452860"
    }, 
    {
      "name": "Heartbroker Mashud", 
      "administrator": false, 
      "id": "297891270402168"
    }, 
    {
      "name": "Zoya Cutee", 
      "administrator": false, 
      "id": "324846867702507"
    }, 
    {
      "name": "Sadaf Iqbal", 
      "administrator": false, 
      "id": "190448544458945"
    }, 
    {
      "name": "Mirza Xuny", 
      "administrator": false, 
      "id": "1486572721632097"
    }, 
    {
      "name": "Daniyal Ali", 
      "administrator": false, 
      "id": "1402121296746497"
    }, 
    {
      "name": "Fadi Hafeez", 
      "administrator": false, 
      "id": "1473029212980213"
    }, 
    {
      "name": "Touseef Jaskani", 
      "administrator": false, 
      "id": "1526607160914780"
    }, 
    {
      "name": "Qasim Mughal", 
      "administrator": false, 
      "id": "1567489836819449"
    }, 
    {
      "name": "Ayesha Shiekh", 
      "administrator": false, 
      "id": "1477646325793433"
    }, 
    {
      "name": "Xwêęt Hãñį", 
      "administrator": false, 
      "id": "1420592754829821"
    }, 
    {
      "name": "Talha Khas Kheliy", 
      "administrator": false, 
      "id": "1575778329309288"
    }, 
    {
      "name": "Nixar Ul Haq", 
      "administrator": false, 
      "id": "362752463901883"
    }, 
    {
      "name": "Naimatullah Ullah", 
      "administrator": false, 
      "id": "198836976953551"
    }, 
    {
      "name": "Bilal Ali", 
      "administrator": false, 
      "id": "366266173531500"
    }, 
    {
      "name": "Shahid Choudhary", 
      "administrator": false, 
      "id": "614021232037941"]

for user in data["data"]:
    print user
    page = urlopen("http://graph.facebook.com/" + user["id"] + "?fields=picture")
    page_data = json.loads(page.read())
    photo_url = page_data["picture"]["data"]["url"]
    user_photos[user["id"]] = [user["name"], photo_url]

fp = open("user_photos.json", "w")
fp.write(json.dumps(user_photos))
