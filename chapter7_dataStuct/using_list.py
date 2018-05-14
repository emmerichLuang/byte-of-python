
shoppingList = ['apple', 'orange', 'mango']

# len
print('I have', len(shoppingList), ' items to buy.')

print('these are:')
for item in shoppingList:
    print(item, end=' ')

shoppingList.append('rice')

print('\nafter appending rice:', shoppingList)

shoppingList.sort()
print('\nafter sorted :', shoppingList)


print('The first item I will buy is', shoppingList[0])
olditem = shoppingList[0]
del shoppingList[0]
print('I bought the', olditem)



print('\nMy shopping list is now:', shoppingList)


print('\n orange? :', 'orange' in shoppingList)