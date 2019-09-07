result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

### Find the number of fruits in a basket
for each_fruit in fruits:
    result += basket_items.get(each_fruit, 0)

print(result)