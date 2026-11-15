class Stack:
    def __init__(self):  
        self.items = []
                
    def push(self, item): 
        self.items.append(item)
                
    def empty(self):   
        return 0 if self.items else 1
                
    def size(self):        
        return len(self.items)
        
    def pop(self):       
        if self.empty():
            raise Exception("Stack is empty")
            
        return self.items.pop()
                
    def top(self):         
        if self.empty():
            raise Exception("Stack is empty")
                        
        return self.items[-1]


n = int(input().rstrip())

p = Stack()
for _ in range(n):
    a = input().split()
    if len(a) == 2:
        b, c = a
        c = int(c)

        p.push(c)
    else:
        if a[0] == "pop":
            print(p.pop())
        elif a[0] == "size":
            print(p.size())
        elif a[0] == "empty":
            print(p.empty())
        else:
            print(p.top())