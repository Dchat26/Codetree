class p:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code


product_name, product_code = input().split()
product_code = int(product_code)

answer1 = p()
answer2 = p(product_name, product_code)

print(f"product {answer1.code} is {answer1.name}")
print(f"product {answer2.code} is {answer2.name}")