'''
List items are indexed and can be accessed by referring to the index number.
'''
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

'''
Negative indexing means start from the end.
'''
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

'''
Range of indexes. Return the third, fourth and fifth item.
'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

'''
Check if "apple" is present in the list.
'''
thislist = ["grape", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list.")
else:
    print("Apple is not in the fruits list.")
