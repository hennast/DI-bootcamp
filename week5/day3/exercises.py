class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self) -> str:
        return f"{self.amount} {self.currency}s"
    def __repr__(self) -> str:
        return f"{self.amount} {self.currency}s"
    def __add__(self, other):
        if type(other) == int:
            return self.amount + other
        else:
            if self.currency == other.currency:
                return self.amount + other.amount
            elif self.currency != other.currency:
                return f"error, cannot add between {self.currency} and {other.currency}"          
    def __int__(self) -> None:
        return self.amount
    def __iadd__(self, other):
        if type(other) == int:
            self.amount += other
            return self
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else:
                return f"error, cannot add between {self.currency} and {other.currency}"
        

    #Your code starts HERE
#Using the code above, implement the relevant methods and dunder methods which will output the results below.
#Hint : When adding 2 currencies which don’t share the same label you should raise an error.

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
#'5 dollars'

print(int(c1))
#5

print(repr(c1))
#'5 dollars'

print(c1 + 5)
#10

print(c1 + c2)
#15

print(c1) 
#5 dollars

c1 += 5
print(c1)
#10 dollars

c1 += c2
print(c1)
#20 dollars

print(c1 + c3)
#TypeError: Cannot add between Currency type <dollar> and <shekel>