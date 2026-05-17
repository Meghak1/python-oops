class revenue:
    def __init__(self, m1, m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def __mul__(self, other):
        p1 = self.m1 * other.m1
        p2 = self.m2 * other.m2 
        p3 = self.m3 * other.m3
        res = revenue(p1, p2, p3)
        return res

p1 = revenue(1, 2, 3)
p2 = revenue(4, 5, 6)
p3 = revenue(5, 6, 7)
res = p1*p2*p3
print(res.m1)
print(res.m2)
print(res.m3)
