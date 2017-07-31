word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def findAndSave(list, keychar):
    newList = []
    for value in word_list:
        if value.find(keychar) >= 0:
            newList.append(value)
    print newList

findAndSave(list = word_list, keychar = char)