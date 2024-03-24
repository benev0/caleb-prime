
class Mod:
    def __init__(self, name, rarity, max_rank, tax) -> None:
        self.url_name = name
        self.rarity = rarity
        self.max_rank = max_rank
        self.tax = tax
        self.bids = []
        self.asks = []

    def setBid(self, bids):
        ff = lambda x : x.online != "offline"
        self.bids = sorted(filter(ff, bids), reverse=True)

    def setAsk(self, asks):
        ff = lambda x : x.online != "offline"
        self.asks = sorted(filter(ff, asks))

    def calSpread(self):
        if not self.bids or not self.asks:
            return None
        return min([a.value for a in self.asks]) - max([b.value for b in self.bids])

    def __str__(self):
        return f"{self.url_name} {self.rarity} {self.max_rank} {self.tax}"

class Order:
    def __init__(self, id, value, mod_rank, online) -> None:
        self.id = id
        self.value = value
        self.mod_rank = mod_rank
        self.online = online

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __eq__(self, other) -> bool:
        return self.value == other.value


def isModDict(data:dict) -> bool:
    return "mod" in data["items_in_set"][0]["tags"] and "(veiled)" not in data["items_in_set"][0]["url_name"]
