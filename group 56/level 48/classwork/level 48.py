def reverse_seq(n):
    return list(range(n, 0, -1))


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"

    if p1 == "scissors":
        if p2 == "paper": return "Player 1 won!"
        else: return "Player 2 won!"
    elif p1 == "paper":
        if p2 == "scissors": return "Player 2 won!"
        else: return "Player 1 won!"
    else:
        if p2 == "paper": return "Player 2 won!"
        else: return "Player 1 won!"


def is_divisible(n,x,y):
    return n%x == 0 and n%y == 0




def count_sheep(n):
    if n == 0: return ""

    res = ""
    for i in range(1, n+1):
        res += f"{i} sheep..."

    return res