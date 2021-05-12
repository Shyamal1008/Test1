import sys

#mac= str(sys.argv)

#print("mac" , mac)

#import requests
#from requests_toolbelt.utils import dump

#resp = requests.get('https://api.macaddress.io/v1?apiKey=at_LxipQ8XQVvq9VF7DIR558VlCfBAAH&output=json&search=44:38:39:ff:ef:57')
#print(resp.status_code)
#data = dump.dump_all(resp)
#print(data.decode('utf-8'))

import urllib.request as urllib2
import json
import codecs

#API base url,you can also use https if you need
url = "https://api.macaddress.io/v1?apiKey=at_LxipQ8XQVvq9VF7DIR558VlCfBAAH&output=json&search="
#Mac address to lookup vendor from
mac_address = str(sys.argv[1]) # "BC:92:6B:A0:00:01"
#print ("Mac address : \t",mac_address )

request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
response = urllib2.urlopen( request )
#Fix: json object must be str, not 'bytes'
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))
#print(type(obj))
#Print company name
print ("Mac address : \t",mac_address )
print ("Name of Company :\t")
print (obj['vendorDetails']['companyName']+"<br/>")