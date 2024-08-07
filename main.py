from wiki import get_term

    
with open("in.txt", "r") as f:
    topics = f.readlines()
    f.close()


descriptions = []
for index, topic in enumerate(topics):
    
    try:
        if topic.strip()[0] == "#":
            descriptions.append("\n" + topic.strip()[1:] + "\n\n")
        else:
            descriptions.append( topic.strip() + " - " + get_term(topic.strip()).strip() + "\n\n" )
    except Exception:
        continue

with open("out.txt", "w") as f:
    f.write( "".join(descriptions) )

print("Done.")


"""
query = "The Cold War"

query = query.split(" ")
    
query = "+".join(query)

request = urllib.request.Request(
    "http://api.duckduckgo.com/?q="+query+"&format=json&skip_disambig=1",
    method="GET"
)

response = urllib.request.urlopen(request)

responseJson = json.loads(response.read())

print(json.dumps( responseJson, sort_keys=True, indent=4 ))
"""

"""
from get_term import get_term


with open("in.txt", "r") as f:
    topics = f.readlines()
    f.close()


descriptions = []
for index, topic in enumerate(topics):
    
    try:
        if topic.strip()[0] == "#":
            descriptions.append(topic.strip()[1:] + "\n\n")
        else:
            descriptions.append( topic.strip() + " - " + get_term(topic.strip()).strip() + "\n\n" )
    except Exception:
        continue
    
    

with open("out.txt", "w") as f:
    f.write( "".join(descriptions) )

print("Done.")
"""
