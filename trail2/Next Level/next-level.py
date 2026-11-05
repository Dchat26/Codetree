class p:
    def __init__(self, id="codetree", lv=10):
        self.id = id
        self.lv = lv

a, b = input().split()

p1 = p()
print(f"user {p1.id} lv {p1.lv}")
p2 = p(a, b)
print(f"user {p2.id} lv {p2.lv}")