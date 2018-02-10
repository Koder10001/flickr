"""
	code with love by Koder17 <3
"""
import os
import urllib2
import json
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

choice = -91234
api = "https://www.flickr.com/services/rest/?format=json&api_key=af1146a2df5582ec7a4b02c644eb2c1f&nojsoncallback=1" # Do not change this
def curl(url):
	return urllib2.urlopen(url).read()

def getpic(photoid):
	return json.loads(curl(api+"&method=flickr.photos.getSizes&photo_id="+photoid))["sizes"]["size"][-1]["source"]

def ana(mode,url):
	if(mode == "user"):
		method = "flickr.urls.lookupUser"
	elif (mode == "group"):
		method = "flickr.urls.lookupGroup"
	elif (mode == "gallery"):
		method = "flickr.urls.lookupGallery"
	else:
		return False
	return curl(api + "&method=" + method + "&url=" + url)

while (choice != 0):
	link = api
	cls()
	print "0. exit"
	print "1. photosteam"
	print "2. album"
	print "3. favorite"
	print "4. gallery"
	print "5. group"
	choice = int(raw_input("your choice: "))
	if(choice == 0):
		exit()
	url = raw_input("your link: ")
	print "Checking url..."
	check = ""
	code = ""
	mode = ""
	if(choice == 1):
		check = json.loads(ana("user",url))
		print check["stat"]
		if (check["stat"]!="ok"):
			print check["message"]
			raw_input("press any key to continue...")
			continue
		else:
			link += "&method=flickr.people.getPhotos&per_page=500&user_id=" + check["user"]["id"]
			code = check["user"]["id"]
			print code
	elif(choice == 3):
		check = json.loads(ana("user",url))
		print check["stat"]
		if (check["stat"]!="ok"):
			print check["message"]
			raw_input("press any key to continue...")
			continue
		else:
			link += "&method=flickr.favorites.getList&per_page=500&user_id=" + check["user"]["id"]
			code = check["user"]["id"]
			print code
	elif(choice == 4):
		check = json.loads(ana("gallery",url))
		print check["stat"]
		if (check["stat"]!="ok"):
			print check["message"]
			raw_input("press any key to continue...")
			continue
		else:
			link += "&method=flickr.galleries.getPhotos&per_page=500&gallery_id=" + check["gallery"]["gallery_id"]
			code = check["gallery"]["gallery_id"]
			print code
	elif(choice == 5):
		check = json.loads(ana("group",url))
		print check["stat"]
		if (check["stat"]!="ok"):
			print check["message"]
			raw_input("press any key to continue...")
			continue
		else:
			link += "&method=flickr.groups.pools.getPhotos&per_page=500&group_id=" + check["group"]["id"]
			code = check["group"]["id"]
			print code
	elif(choice == 2):
		try:
			al = url.split("/")[6]
			check = json.loads(curl(api+"&method=flickr.photosets.getInfo&photoset_id="+al))
			print check["stat"]
			if (check["stat"]!="ok"):
				print check["message"]
				raw_input("press any key to continue...")
				continue
			else:
				link += api+"&method=flickr.photosets.getPhotos&photoset_id="+al
				code = check["photoset"]["id"]
				print code
		except:
			print "Album not found"
			raw_input("press any key to continue...")
			continue
	keywords = ["Koder17","photos|photo","photoset|photo","photos|photo","photos|photo","photos|photo"]
	page = 1
	res = json.loads(curl(link+"&per_page=500&page="+str(page)))
	links = []
	current = 0
	while (page <= res[keywords[choice].split("|")[0]]["pages"]):
		res = json.loads(curl(link+"&per_page=500&page="+str(page)))
		for i in (res[keywords[choice].split("|")[0]][keywords[choice].split("|")[1]]):
			links.append(getpic(i["id"]))
			current += 1
			print str(current) + "/" + str(res[keywords[choice].split("|")[0]]["total"]) + " "+ str(i["id"])
		page += 1
	print "Writing to file ..."
	if (choice == 1):
		mode = "pht"
	elif(choice == 2):
		mode = "alb"
	elif(choice == 3):
		mode = "fav"
	elif(choice == 4):
		mode = "gal"
	elif(choice == 5):
		mode = "grp"
	fi = open(mode+"-"+code+".txt","w")
	for i in links:
		fi.write(i)
		fi.write("\n")
	fi.close()
	print "Done!!!"
	raw_input()
