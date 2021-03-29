import urllib.request, json

with urllib.request.urlopen("https://canlidoviz.com/borsa.jsonld") as url:
    data = json.loads(url.read())
    a = data["mainEntity"]["itemListElement"]

    for i in a:  
        b = i["currentExchangeRate"]
        print("{} = {}".format(i["currency"],b["price"]))






    
