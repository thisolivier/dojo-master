def horridCompare(list1, list2):
    if len(list1) != len(list2):
        print "The lists are not the same"
        return
    else:
        for index, value in enumerate(list1):
            if value != list2[index]:
                print "The lists are not the same"
                return
        print "The lists are the same"

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','mil']

horridCompare(list1 = list_one, list2 = list_two)