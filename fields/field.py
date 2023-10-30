class FQ:
    p = 17

    def __init__(self, val):
        self.val = val % self.p

    def __add__(self, other):
        return FQ((self.val + other.val) % self.p)

    def __sub__(self, other):
        return FQ((self.val - other.val) % self.p)

    def __mul__(self, other):
        return FQ((self.val * other.val) % self.p)

    def __truediv__(self, other):
        return FQ((self.val * pow(other.val, self.p - 2, self.p)) % self.p)

    def pow(self, other):
        return FQ(pow(self.val, other.val, self.p))

    def __repr__(self):
        return f"FQ({self.val})"