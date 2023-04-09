import urllib.request
import time 
import re 

url = "https://mlab.taik.fi/~timo/runo1.html"
response = urllib.request.urlopen(url)
poem = response.read().decode('iso-8859-1')

poem = re.sub('<[^<]+?>', '', poem)

lines = poem.split("\n")

for line in lines:
	a=0
	if len(line.split()) == 1:
		tabs = "\t"
		a+=1
	else:
		tabs = ""
	print(tabs*a + line)
	time.sleep(0.8)

