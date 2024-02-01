# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        if self._cents < 10:
            return f"{self._euros}.0{self._cents} eur"
        else:
            return f"{self._euros}.{self._cents} eur"

    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents

    def __ne__(self, another):
        return (self._euros + self._cents) != (another._euros + another._cents)

    def __lt__(self, another):
        return (self._euros + self._cents) < (another._euros + another._cents)

    def __gt__(self, another):
        return (self._euros + self._cents) > (another._euros + another._cents)

    def __add__(self, another):
        self._euros += another._euros
        self._cents += another._cents
        if self._cents >= 100:
            self._euros += 1
            self._cents -= 100
        new_money = Money(self._euros, self._cents)
        return new_money

    def __sub__(self, another):
        self._euros -= another._euros
        self._cents -= another._cents
        if self._cents < 0:
            self._cents += 100
            self._euros -= 1
        if self._euros < 0:
            raise ValueError("cannot have negative euros")
        else:
            new_money = Money(self._euros, self._cents)
        return new_money



if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents

    print(e1)
    print(e2)

    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)

    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)