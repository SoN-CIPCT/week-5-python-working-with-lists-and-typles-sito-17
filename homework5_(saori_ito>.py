animals = ['dog', 'cat', 'horse', 'bird', 'lion', 'elephant']
print(animals)
print("The first two items in the list are:")
for animal in animals[:2]:
    print(animal.title())

print ("The first two items in the list are:", animals[:2])
print ("The middle two items in the list are:", animals [2:4])
print ("The first and last items in the list are:", animals[0], animals[-1])

 
menu = ('hamburger', 'hotdog', 'pizza', 'tacos', 'burrito')
print("\nMenu:")
for item in menu:
    print(item)

print("\nOriginal Menu:")
for item in menu:
    print(item)

menu = ('steak', 'fish', 'pizza,', 'tacos,', 'burrito')
print("\nModified Menu:")
for item in menu:
    print(item)



