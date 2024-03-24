
class RivenAuction:
    def __init__(self, id, price, mastery_level, mod_rank, rerolls):
        self.id = id
        self.price = price
        self.mastery_level = mastery_level
        self.mod_rank = mod_rank
        self.rerolls = rerolls
        self.endoValue = self.__calEndoValue()
        self.endoPerPlat = self.__calEndoPerPlat()

    def __calEndoValue(self) -> int:
        return 100 * (self.mastery_level - 8) + int(22.5 * 2**self.mod_rank) + 200 * self.rerolls - 7

    def __calEndoPerPlat(self) -> int:
        return self.__calEndoValue() / self.price

    def __str__(self) -> str:
        return f"id:    {self.id}\nprice: {self.price}\nendo:  {self.endoValue}\nepp:   {self.endoPerPlat}\n"

    def __lt__(self, other):
        return self.endoPerPlat < other.endoPerPlat or (self.endoPerPlat == other.endoPerPlat and self.endoValue < other.endoValue)

    def __eq__(self, other):
        return self.endoPerPlat == other.endoPerPlat and self.endoValue == other.endoValue
