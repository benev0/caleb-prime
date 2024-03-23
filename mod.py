
class Mod:
    def __init__(self, name, tax, rarity):
        self.url_name = name
        self.trading_tax = tax
        self.rarity = rarity

class ModOrders:
    pass

def isModDict(data:dict) -> bool:
    return "mod" in data["items_in_set"][0]["tags"] and "(veiled)" not in data["items_in_set"][0]["url_name"]
