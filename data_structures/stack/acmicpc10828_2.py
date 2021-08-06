#make Stack class and object methods
import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, num):
        self.stack.append(num)
    def pop (self):
        if len(self.stack) == 0:
            print(-1)
        else: 
            print(self.stack.pop())
    def size(self):
        print(len(self.stack))
    def empty(self):
        if len(self.stack)== 0:
            print(1)
        else:
            print(0)
    def top(self):
        if len(self.stack)== 0:
            print(-1)
        else:
            print(self.stack[-1])


stk = Stack()

for i in range(int(input())):
    input_copy = input().split();
    if input_copy[0]=="push":
        stk.push(int(input_copy[1]))
    elif input_copy[0]=="pop":
        stk.pop()
    elif input_copy[0]=="size":
        stk.size()
    elif input_copy[0]=="empty":
        stk.empty()
    elif input_copy[0]=="top":
        stk.top()
    