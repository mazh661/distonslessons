import json
f = open("data.json","r")
#read data
data = f.read()
data_json = json.loads(data)
#write data
newdata = {
		"Name": "Yerassyl",
		"Version": "1998",
		"Install": "only hard",
		"Owner": "Parents",
		"Kernel": "4.9"
}
data_json.append(newdata)
with open("data.json","w") as outfile:
    json.dump(data_json,outfile,indent=4)