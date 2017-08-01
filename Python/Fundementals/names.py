print "\n----------\nPart 1, Simple Print\n----------\n"

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_names(list, bool):
    to_return = []
    for val in list:
        new_name = val['first_name'] + " " + val['last_name']
        to_return.append( new_name )
        if bool: print new_name
    return to_return

print_names(students, True)

print "\n----------\nPart 2, Whole Different League\n----------\n"

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_sets(dict):
    for key in dict:
        print key
        names = print_names(dict[key], False)
        for index, value in enumerate(names):
            print "{} - {} - {}".format(index + 1, value, len(value) - 1)

print_sets(users)