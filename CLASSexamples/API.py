import urllib2
import json


response = urllib2.urlopen("https://uinames.com/api/")

content = response.read()
content_dict = json.loads(content)
print content_dict["region"]
