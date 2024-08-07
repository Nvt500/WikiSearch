import urllib.request
import json


def get_term(topic: str) -> str:
    
    titles = get_title(topic)
    
    return get_description(titles)


def get_title(topic: str) -> list[str]:
    
    query = topic.split(" ")
        
    query = "+".join(query)
    
    request = urllib.request.Request(
        "https://en.wikipedia.org/w/api.php?action=opensearch&search="+query+"&limit=10&namespace=0&redirects=resolve&format=json",
        method="GET"
    )
    
    response = urllib.request.urlopen(request)
    
    responseJson = json.loads(response.read())
    
    if isinstance(responseJson, list):
        return responseJson[1]
    elif isinstance(responseJson, dict):
        return response.get(topic)
    else:
        raise Exception("Incorrect response format.")


def get_description(titles: list[str]) -> str:

    for index, title in enumerate(titles):
        
        query = title.split(" ")
            
        query = "+".join(query)
        
        request = urllib.request.Request(
            "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles="+query+"&formatversion=1&exintro&exlimit=1&explaintext",
            method="GET"
        )
        
        response = urllib.request.urlopen(request)
        
        responseJson = json.loads(response.read())
        
        extract = responseJson.get("query").get("pages").get(str(list(responseJson.get("query").get("pages").values())[0].get("pageid"))).get("extract")
        
        if extract.strip() != "":
            return "".join(["\t" + e.strip() + "\n" for e in extract.splitlines() if e.strip() != ""])
        
        if index == len(topic) - 1:
            return "No results."
