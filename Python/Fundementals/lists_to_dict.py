name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def zip_lists(listKeys, listVal):
    new_dict = {}

    # Will work for uneven list lengths
    if len(listKeys) < len(listVal):
        temp = listKeys
        listKeys = listVal
        listVal = temp

        
    # We enumerate the possibly shorter list, so that we never reach out of range
    for index, val in enumerate(listVal):
        new_dict[ listKeys[index] ] = val
    return new_dict

print zip_lists(name, favorite_animal)