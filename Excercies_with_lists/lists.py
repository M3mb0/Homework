# Scoate elemntul cu valoarea 10 din lista
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list.remove(10)
print(list)

# Schimba valoarea elementului de pe indexul 2 cu patratul acestuia - REFACUT
list[2] **= 2
print(list)

# Printeaza daca valoarea 22 se afla in lista
print(22 in list)

# Extinde lista cu ['Salut', 'sunt', 'Razvan']
list2 = ['Salut', 'sunt', 'Razvan']
list.extend(list2)
print(list)

# Scoate elementul cu indexul 10 din lista so ol printeaza
a = list.pop(10)
print(a)
print(list)

# Adauga [99,100] in locul elemntului de la indexul 3
list[3:4] = 99, 100
print(list)

# Sterge intreaga lista
list.clear()
print(list)

# Inverseaza ultimul element cu primul - REFACUTA
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2[0], list_2[-1] = list_2[-1], list_2[0]
print(list_2)

# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list
# l1 and even index elements from the list l2.

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

odd_index = l1[1::2]
print(odd_index)

even_index = l2[0::2]
print(even_index)

l3.extend(odd_index)
l3.extend(even_index)
print(l3)
