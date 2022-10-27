from cgitb import handler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


''' This works as a great example!'''
# fig, ax = plt.subplots()

# x = [1, 2, 3, 4, 5]
# y = [3, 6, 9, 12, 15]

# values = [0,1,2,3,4]
# values_str = ['red', 'blue', 'green', 'cyan', 'magenta']
# colours = ListedColormap(['r', 'b', 'g', 'c', 'm'])


# scattery = plt.scatter(x, y, c = values, cmap = colours)
# plt.legend(handles = scattery.legend_elements()[0], labels = values_str)
# ax.grid(True)
# plt.show()

# x = [1, 3, 4, 6, 7, 9]
# y = [0, 0, 5, 8, 8, 8]

# classes = ['A', 'B', 'C']
# values = [0, 0, 1, 2, 2, 2]
# colors = ['red','blue','green']

# scatter = plt.scatter(x, y, c=values)
# plt.legend(handles=scatter.legend_elements()[0], labels=classes)
# plt.show()

def getImage(path, zoom=0.015):
    return OffsetImage(plt.imread(path), zoom=zoom)


''' Plotting Toronto's win pct over five seasons '''

df = pd.DataFrame(np.random.random((200, 3)))
df['date'] = pd.date_range('2000-1-1', periods=200, freq='D')

df = df.set_index(['date'])
print(df.loc['1800-6-1':'2023-6-10'])

############################################
# From NHL 3.0


def getImage(path, zoom=0.02):
    return OffsetImage(plt.imread(path), zoom=zoom)


images = ['NHL_Teams/New_Jersey.png', 'NHL_Teams/Islanders.png', 'NHL_Teams/New York.png', 'NHL_Teams/Philly.png', 'NHL_Teams/Pitsburgh.png', 'NHL_Teams/Boston.png',
          'NHL_Teams/Buffalo.png', 'NHL_Teams/Montreal.png', 'NHL_Teams/Ottawa.png', 'NHL_Teams/Toronto.png', 'NHL_Teams/Atlanta.png', 'NHL_Teams/Carolina.png',
          'NHL_Teams/Florida.png', 'NHL_Teams/Tampa Bay.png', 'NHL_Teams/Washington.png', 'NHL_Teams/Chicago.png', 'NHL_Teams/Detroit.png', 'NHL_Teams/Nashville.png',
          'NHL_Teams/St.Louis.png', 'NHL_Teams/Calgary.png', 'NHL_Teams/Colorado.png', 'NHL_Teams/Edmonton.png', 'NHL_Teams/Vancouver.png', 'NHL_Teams/Anaheim.png',
          'NHL_Teams/Dallas.png', 'NHL_Teams/LA.png', 'NHL_Teams/Phoenix.png', 'NHL_Teams/San Jose.png', 'NHL_Teams/Colombus.png', 'NHL_Teams/Minnesota.png', 'NHL_Teams/Winnipeg.png',
          'NHL_Teams/Arizona.png', 'NHL_Teams/Vegas.png']

x_alts = [250, 89, 13, 39, 846, 33, 597, 52, 236, 289, 997, 354, 3, 7, 10,
          594, 610, 607, 883, 3432, 5272, 2172, 20, 3694, 435, 243, 1093,
          92, 755, 791, 305, 1093, 2064]

y_wins = [55.595, 50.526, 52.463, 55.595, 58.683, 57.812, 51.100,
          53.059, 54.350, 52.587, 44.961, 52.934, 46.764, 58.983,
          59.159, 55.517, 56.973, 58.382, 57.614, 54.933, 55.357,
          48.230, 56.316, 57.008, 58.519, 53.974, 52.579, 59.977,
          51.188, 54.644, 54.586, 45.938, 62.128]

fig, ax = plt.subplots()
ax.scatter(x_alts, y_wins)

for x_alt, y_win, image in zip(x_alts, y_wins, images):
    ab = AnnotationBbox(getImage(image), (x_alt, y_win), frameon=False)
    ax.add_artist(ab)

plt.xlabel('Altitude (ft.)')
plt.ylabel('Home Win Percentage')
plt.title('Altitude vs Home Win Percentage for NHL Teams')

plt.show()

##########################################
# From Testing

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

# class Stack:
#     def __init__(self):  # Initializes the stack
#         self._items = []

#     def push(self, item):
#         self._items.append(item)

#     def pop(self):
#         return self._items.pop()
#         # don't uncomment, for clarity only, will break everything :D
#         # return self._items[-1]
#         #self._items = self._items[0:-2]

#     def __repr__(self):
#         return f'<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>'

#     def __len__(self):
#         return len(self._items)


# s = Stack()
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


# class Calculator:
#     def __init__(self):
#         self._stack = Stack()

#     def push(self, item):
#         self._stack.push(item)

#     def pop(self):
#         return self._stack.pop()

#     def add(self):
#         self.push(self.pop() + self.pop())

#     def mul(self):
#         self.push(self.pop() * self.pop())

#     def sub(self):
#         right = self.pop()
#         self.push(self.pop() - right)

#     def div(self):
#         right = self.pop()
#         self.push(self.pop() / right)


# calc = Calculator()
# calc.push(4)
# calc.push(6)


# a = [3, 4, 5]
# b = [a]
# c = 4 * b
# print(c)
# a[0] = -7
# print(c)

# a = [3, 4, 5]
# c = [list(a) for _ in range(4)]
# print(c)
