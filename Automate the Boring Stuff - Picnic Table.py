# Hopefully this will help with understanding functions for future me


def printPicnic(itemsDict, leftWidth, rightWidth):                                  # three parameters (itemsDict, leftWidth, rightWidth)
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))                       # first print the first line
    for k,v in itemsDict.items():                                                   # for each key and value (k,v) in the itemsDict. (first parameter)
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))                    # print the key left justified, and the value (which is going to be int) 
        
picnic_items = {'sandwiches': 4, 'apples': 12 , 'cups': 4, 'cookies': 8000}         # Dictionary of picnic items to be passed thorugh the itemsDict parameter 
printPicnic(picnic_items,12, 5)                                                     # passing through the parameters
printPicnic(picnic_items, 20, 6)

