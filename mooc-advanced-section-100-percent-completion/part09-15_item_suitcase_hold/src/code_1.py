# Write your solution here:
class Item:
    def __init__(self, item_name: str, item_weight: int):
        self.item_name = item_name
        self.__item_weight = item_weight

    def name(self):
        return self.item_name

    def weight(self):
        return self.__item_weight

    def __str__(self):
        return f'{self.item_name} ({self.__item_weight} kg)'


class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item: Item):
        if len(self.items) == 0 and item.weight() <= self.max_weight:
            self.items.append(item)
        elif (item.weight() + self.weight()) <= self.max_weight:
            self.items.append(item)

    def print_items(self):
        for item in self.items:
            print(item)

    def weight(self):
        total_weight = 0
        for item in self.items:
            total_weight += item.weight()
        return total_weight

    def heaviest_item(self):
        if self.weight() == 0:
            return None
        else:
            heaviest = self.items[0].weight()
            result = self.items[0]
            for item in self.items:
                if item.weight() > heaviest:
                    heaviest = item.weight()
                    result = item
            print(type(result))
            return result

    def __str__(self):
        if len(self.items) == 1:
            return f'{len(self.items)} item ({self.weight()} kg)'
        else:
            return f'{len(self.items)} items ({self.weight()} kg)'


class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.cargo = []

    def add_suitcase(self, suitcase: Suitcase):
        if len(self.cargo) == 0 and suitcase.weight() <= self.max_weight:
            self.cargo.append(suitcase)
        elif (suitcase.weight() + self.weight()) <= self.max_weight:
            self.cargo.append(suitcase)

    def weight(self):
        total_weight = 0
        for suitcase in self.cargo:
            total_weight += suitcase.weight()
        return total_weight

    def available_space(self):
        return self.max_weight - self.weight()

    def print_items(self):
        for suitcase in self.cargo:
            for item in suitcase.items:
                print(item)

    def __str__(self):
        if len(self.cargo) == 1:
            return f'{len(self.cargo)} suitcase, space for {self.available_space()} kg'
        else:
            return f'{len(self.cargo)} suitcases, space for {self.available_space()} kg'


if __name__ == "__main__":
    hold = CargoHold(100)
    print(hold)