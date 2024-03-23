import requests
from mod import Mod, isModDict

itemsUrl = "https://api.warframe.market/v1/items"

itemUrl  = "https://api.warframe.market/v1/items/{}"

r = requests.get(itemsUrl)
data = r.json()
# list of url_name
itemList = [item["url_name"] for item in data["payload"]["items"]]
del data


validMods = []
for i, item in enumerate(itemList[:10]):
    print(i, item, end=" ")
    try:
        r = requests.get(itemUrl.format(item))
    except:
        print("fail")
        continue
    data = r.json()["payload"]["item"]
    if not isModDict(data):
        print()
        continue
    validMods.append(item)
    print("valid")

with open("./cache/moditems", 'w') as f:
    f.write('\n'.join(validMods) + "\n")
