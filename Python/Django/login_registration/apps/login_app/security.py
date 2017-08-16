import bcrypt

def hash(val):
    encoded = val.encode()
    hashed = bcrypt.hashpw( encoded, bcrypt.gensalt() )
    return hashed

def check(quest, know):
    encoded = quest.encode()
    answer = bcrypt.checkpw( encoded, know )
    return answer