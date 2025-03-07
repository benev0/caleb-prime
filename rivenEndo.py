import requests

from riven import RivenAuction

itemsUrl = "https://api.warframe.market/v1/riven/items"
auctionUrl = "https://api.warframe.market/v1/auctions/search?type=riven&weapon_url_name={}"

def run():
    r = requests.get(itemsUrl)
    data = r.json()
    del r

    paylod = data["payload"]["items"]

    entries = [entry["url_name"] for entry in paylod]

    rivenCount = len(entries)
    endoTarget = []
    for i, entry in enumerate(entries):
        segmentRequest = requests.get(auctionUrl.format(entry))
        segmnetData = segmentRequest.json()
        segmentPaylod = segmnetData["payload"]["auctions"]

        for entry in segmentPaylod:
            if entry["buyout_price"] is None:
                continue

            endoTarget.append(RivenAuction(entry["id"], entry["buyout_price"], entry["item"]["mastery_level"], entry["item"]["mod_rank"], entry["item"]["re_rolls"]))

        print(f"{i} of {rivenCount}: total of {len(endoTarget)} items found")

    endoTarget.sort(reverse=True)
    return endoTarget


def render(endoTarget, n):
    for e in endoTarget[:n]:
        print(e)
