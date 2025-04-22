def double_char(s):
    res = ""
    
    for char in s:
        res += char*2
    
    return res

def double_char(s):
    return "".join([i*2 for i in s])


def get_age(age):
    return int(age[0])


def get_age(age):
    return int(age.split(" ")[0])

def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


def reverse_words(s):
    return " ".join(s.split(' ')[::-1])

def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"