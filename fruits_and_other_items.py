fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

### If the key is in the list of fruits, add to fruit_count.
for each_fruit in fruits:
    fruit_count += basket_items.get(each_fruit, 0)
for key in basket_items:
### If the key is not in the list, then add to the not_fruit_count
    if key not in fruits:
        not_fruit_count += basket_items.get(key, 0)

print(fruit_count, not_fruit_count)