
import requests
import os.path

from mod import Order, Mod
import itemUpdate

ordersUrl = "https://api.warframe.market/v1/items/{}/orders"

rarities  = ["common", "uncommon", "rare", "legendary"]

def run(rarity="legendary"):
    assert(rarity in rarities)

    modRestrict = rarities[rarities.index(rarity):]

    if not os.path.isfile("cache/moditems"):
        itemUpdate.run()

    modList = []
    with open("cache/moditems", 'r') as f:
        modList = [Mod(*l.split()) for l in f.readlines() if l.strip() != ""]

    #fill bid and ask calc spread
    modCount = len(modList)
    spreads = []
    for i, mod in enumerate(modList):
        if not mod.rarity in modRestrict:
            continue

        r = requests.get(ordersUrl.format(mod.url_name))
        print(f"{i} of {modCount}: {mod.url_name}")
        data = r.json()
        data = data["payload"]["orders"]

        modBids = []
        modAsks = []

        for order in data:
            marketOperation = Order(order["id"], order["platinum"], order["mod_rank"], order["user"]["status"])
            if order["order_type"] == "sell":
                modAsks.append(marketOperation)
            else:
                modBids.append(marketOperation)

        mod.setAsk(modAsks)
        mod.setBid(modBids)

        spread = mod.calSpread()
        if spread is None or spread > 0:
            continue

        spreads.append((mod.calSpread(), mod))

    spreads.sort(key=lambda tup: tup[0])
    return spreads


def render(spreads):
    for s, m in spreads:
        print(m.url_name)
        print(f"plat spread: {s}")
        print(f"endo   cost: {m.calCostEndo()}")
        print(f"credit cost: {m.calCostCredits()}")
        print()
