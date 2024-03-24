import requests
from mod import Mod, isModDict

def run():
    itemsUrl = "https://api.warframe.market/v1/items"
    itemUrl  = "https://api.warframe.market/v1/items/{}"

    r = requests.get(itemsUrl)
    data = r.json()
    data = data["payload"]["items"]

    # list of url_name
    itemList = [item["url_name"] for item in data]
    del data


    validMods = []
    for i, item in enumerate(itemList):
        print(i, item, end=" ")

        try:
            r = requests.get(itemUrl.format(item))
        except Exception as e:
            print(e)
            print("fail")
            continue

        data = r.json()
        data = data["payload"]["item"]

        if not isModDict(data):
            print()
            continue
        try:
            validMods.append(Mod(item, data["items_in_set"][0]["rarity"], data["items_in_set"][0]["mod_max_rank"], data["items_in_set"][0]["trading_tax"]))
        except Exception as e:
            print(e)
            print("fail")
            continue

        print("valid")

    with open("./cache/moditems", 'w') as f:
        f.write('\n'.join(map(str, validMods)) + "\n")

if __name__=='__main__':
    run()
