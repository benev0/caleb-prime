
import requests
import os.path


from mod import Order, Mod
import itemUpdate

ordersUrl = "https://api.warframe.market/v1/items/{}/orders"

def run():
    if not os.path.isfile("cache/moditems"):
        itemUpdate.run()

    modList = []
    with open("cache/moditems", 'r') as f:
        modList = [Mod(*l.split()) for l in f.readlines() if l.strip() != ""]

    #fill bid and ask calc spread
    spreads = []
    for i, mod in enumerate(modList):
        if mod.rarity != "legendary":
            continue

        r = requests.get(ordersUrl.format(mod.url_name))
        print(i, mod.url_name)
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
        if spread is None:
            continue

        spreads.append((mod.calSpread(), mod))

    spreads.sort(key=lambda tup: tup[0])

    for s, m in spreads[:10]:
        print(m)
        # print([b.value for b in m.bids])
        # print([a.value for a in m.asks])
        print(s)
