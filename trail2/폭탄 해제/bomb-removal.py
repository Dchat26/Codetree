class p:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second


a, b, c = input().split()

answer = p(a, b, c)

print(f"code : {answer.code}\ncolor : {answer.color}\nsecond : {answer.second}")