# %% 
# # Comma Code
# Say you have a list value like this:
# 
# `spam = ['apples', 'bananas', 'tofu', 'cats']`
# 
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. 
# 
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
# 
# But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

# %%
itemlist = []
while True:
    print('Add item ' + str(len(itemlist) + 1) + ' to the items list or enter nothing to stop:')
    item_to_add = input()
    if item_to_add == '':
        break
    itemlist = itemlist + [item_to_add]
    lastitem = itemlist[-1]
    itemliststring = str(itemlist[:-1])
print(itemliststring[1:-1] + ', and ' + "'" + lastitem + "'.")


