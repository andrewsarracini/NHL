# names = ['Dave', 'Mark', 'Bob', 'Ann', 'Phil']

# for name in names: 
#     print(name)


# message = 'hello world!'

# for c in message: 
#     print(c) 

# prices = {'GOOG':490.10, 'IBM':91.50, 'MFST':511.12, 'APPL':114.87}

# for key in prices: 
    # print(key, '=', prices[key]

# for yek in prices: 
#     print(yek, '=', prices[yek]) 

# items = [37, 68, 73] 

# items_2 = items.__add__([45,56,234,123,34,3]) 
# print(items_2) 

class Stack:
    def __init__(self): # Initializes the stack
        self._items = [] 

    def push(self, item): 
        self._items.append(item)

    def pop(self):
        return self._items.pop()
        #don't uncomment, for clarity only, will break everything :D 
        #return self._items[-1]
        #self._items = self._items[0:-2]

    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>'
        
    def __len__(self): 
        return len(self._items)

s = Stack() 
# s.push('Dave') 
# s.push(42)
# s.push([3,4,5])
# s.push('Joe')
# x = s.pop() 
# y = s.pop() 

# print(x,',', y)
# print(s) 

# class MyStack(Stack):
#     def swap(self): 
#         a = self.pop() 
#         b = self.pop() 
#         self.push(a) 
#         self.push(b) 

# s = MyStack() 
# s.push('Dave') 
# s.push(42) 
# s.swap() 
# print(s.pop) 

# x = s.push('yes') 
# print(x)

class Calculator: 
    def __init__(self): 
        self._stack = Stack()

    def push(self, item):
        self._stack.push(item) 

    def pop(self): 
        return self._stack.pop() 

    def add(self): 
        self.push(self.pop() + self.pop()) 

    def mul(self): 
        self.push(self.pop() * self.pop())

    def sub(self): 
        right = self.pop()
        self.push(self.pop() - right)

    def div(self): 
        right = self.pop() 
        self.push(self.pop() / right) 

calc = Calculator() 
calc.push(4)
calc.push(6) 

print(calc.add) 

# a = [3, 4, 5]
# b = [a] 
# c = 4 * b 
# print(c) 
# a[0] = -7 
# print(c)

# a = [3, 4, 5]
# c = [list(a) for _ in range(4)] 
# print(c) 