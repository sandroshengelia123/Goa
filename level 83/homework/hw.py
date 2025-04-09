def fake_bin(x):
    return ''.join(['0' if int(d) < 5 else '1' for d in x])

# test
print(fake_bin("45385593107843568")) # -> "01011110001100111"
print(fake_bin("509321")) # -> "100111"


def check(seq, elem):
    return elem in seq

# test
print(([66, 101], 66)) # true
print(([80,117, 115, 104, 45], 100)) # false
print((['what', 'a', 'great', 'kata'], 'kat')) # false
print((['hello', 'world'], 'world')) # true


def string_to_array(s):
    return s.split(' ') if s != '' else ['']

# test
print(string_to_array("Robin Singh"))
print(string_to_array("I love arrays"))
print(string_to_array(""))

def reverse_seq(n):
    return list(range(n, 0, -1))

# test
print(reverse_seq(5)) # [5, 4, 3, 2, 1]
print(reverse_seq(1)) # [1]
print(reverse_seq(0)) # []


def rps(p1, p2):
    if p1 == p2:
        return "draw!"
    wins ={
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock',
    }
    if wins[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    
    # test
    #print(rps('rock', 'scissors')) # player 1 won!
    #print(rps('scissors', 'rock')) # player 2 won!
    #print(rps('paper', 'paper')) # draw!