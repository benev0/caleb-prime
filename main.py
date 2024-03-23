import requests
from riven import RivenAuction

itemsUrl = "https://api.warframe.market/v1/riven/items"

auctionUrl = "https://api.warframe.market/v1/auctions/search?type=riven&weapon_url_name={}"

itemUrl

r = requests.get(itemsUrl)
data = r.json()

try:
    paylod = data["payload"]["items"]
except:
    print(data)
    exit(1)

print(paylod[0])

entries = [entry["url_name"] for entry in paylod]

print(entries)

target = []
for i, entry in enumerate(entries):
    segmentRequest = requests.get(auctionUrl.format(entry))
    segmnetData = segmentRequest.json()
    segmentPaylod = segmnetData["payload"]["auctions"]
    for entry in segmentPaylod:
        if entry["buyout_price"] is None:
            continue
        target.append(RivenAuction(entry["id"], entry["buyout_price"], entry["item"]["mastery_level"], entry["item"]["mod_rank"], entry["item"]["re_rolls"]))
    print(f"{i}: {len(target)}")

target.sort()

print()
print("top 10")
for t in target[:-10:-1]:
    print(t)
    print()

