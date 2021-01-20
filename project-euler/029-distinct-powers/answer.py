import math
import itertools


class ExponentialNumber:

    def __init__(
        self,
        a: int = 1,
        b: int = 1,
    ):
        self.a = a
        self.b = b

    def __eq__(self, other):
        print(self)
        print(other)
        print(self.b // other.b)
        print("*"*20)
        return (
            self.a ** (self.b // other.b)
            == other.a
        )

    def __repr__(self):
        return f"{self.a} ** {self.b}"


a_min = 2
a_max = 5
b_min = 2
b_max = 5


existed_exponential_numbers = []

for a, b in itertools.product(
    (x for x in range(a_min, a_max + 1)),
    (x for x in range(b_min, b_max + 1)),
):
    exponential_number = ExponentialNumber(a=a, b=b)
    print(a, b)
    if (
        not exponential_number in existed_exponential_numbers
    ):
        existed_exponential_numbers.append(exponential_number)

print(existed_exponential_numbers)
print(len(existed_exponential_numbers))
