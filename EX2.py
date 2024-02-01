thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)   #['apple', 'banana', 'watermelon', 'cherry']


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)     # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

numeros = [10, 5, 7, 2, 1]
print(numeros[2:4])		#[7, 2]
print(numeros[:3])		#[10, 5, 7]
print(numeros[3:])		#[2, 1]
print(numeros[1:4:2])		#[5, 2]
print(numeros[::-1])		#[1, 2, 7, 5, 10]

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)     #['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)     # ['banana', 'cherry']