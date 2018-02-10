import urllib2
def download(url, path):
    filename = url.split("/")[-1]
    print "Downloading "+ filename
    fi = urllib2.urlopen(url)
    print "Writing to file"
    f = open(path+"/"+filename, "wb")
    f.write(fi.read())
    print "Done !!!"
    f.close()
import os
def currentdir():
    return os.listdir(os.getcwd())
files = currentdir()
for i in range(0,len(files)):
    if(os.path.isfile(files[i])):
        print str(i) + ". " + files[i]
stat = False
choice = ""
while stat == False:
    choice = int(raw_input())
    if(choice >= 0 and choice < len(files) and os.path.isfile(files[choice])):
        stat = True
path = files[choice].split('.')[0].replace('-','/')
try:
    os.makedirs(path)
except:
    print "Folder Exists"
f = open(files[choice],"r")
fa = f.readlines()
f.close()
current = 0
for i in fa:
    current += 1
    print str(current) + "/" + str(len(fa))
    download(i.strip(),path)
os.remove(files[choice])
