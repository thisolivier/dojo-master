my_dict = {
    "name": "Olivier",
    "age": "26",
    "destination": "Sunshine",
    "favorite language": "ES6, or Japenese, it depends"
}

def print_me(dict):
    basicString = "My {} is {}."
    for key in dict:
        print basicString.format(key, dict[key])

print_me(my_dict)