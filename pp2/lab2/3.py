"""
add:
    list.append(), list.insert(index,value), list.extend(list) 
delete:
    list.remove(value) - если 2 value то удалаеть первый value
    list.pop(index) - если не указать индекс то удалает последный элемент
    del list[index]
    list.clear() = []
"""

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")


fruits = ["apple","lemom", "banana", "cherry"]
fruits.insert(1,"lemon")

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))



