plocha = ["  " for i in range(9)]
oddelovac = 12 * '-'
oddelovac2 = 50 * '='

print('''
Welcome to Tic Tac Toe
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
Let's start the game
''')

def zobrezena_plocha():
    radek1 = f'{plocha[0]} | {plocha[1]} | {plocha[2]}'
    radek2 = f'{plocha[3]} | {plocha[4]} | {plocha[5]}'
    radek3 = f'{plocha[6]} | {plocha[7]} | {plocha[8]}'

    print(oddelovac)
    print(radek1)
    print(oddelovac)
    print(radek2)
    print(oddelovac)
    print(radek3)
    print(oddelovac)


def pohyb(znak):
    if znak == "X":
        num = 'X'
    elif znak == "O":
        num = '0'

    print(oddelovac2)
    choice = int(input(f'Player {num} | Please enter your move {num} (1-9): ').strip())
    print(oddelovac2)
    print(oddelovac2)
    if plocha[choice - 1] == "  ":
        plocha[choice - 1] = znak
    else:
        print()
        print("Position occupied!")


def vyhra(znak):
    if (plocha[0] == znak and plocha[1] == znak and plocha[2] == znak) or \
            (plocha[3] == znak and plocha[4] == znak and plocha[5] == znak) or \
            (plocha[6] == znak and plocha[7] == znak and plocha[8] == znak) or \
            (plocha[0] == znak and plocha[3] == znak and plocha[6] == znak) or \
            (plocha[1] == znak and plocha[4] == znak and plocha[7] == znak) or \
            (plocha[2] == znak and plocha[5] == znak and plocha[8] == znak) or \
            (plocha[0] == znak and plocha[4] == znak and plocha[8] == znak) or \
            (plocha[2] == znak and plocha[4] == znak and plocha[6] == znak):
        return True
    else:
        return False


def remiza():
    if "  " not in plocha:
        return True
    else:
        return False


while True:
    zobrezena_plocha()
    pohyb("X")
    zobrezena_plocha()
    if vyhra("X"):
        print("Congratulations, the player X WON!")
        break
    elif remiza():
        print("Its a draw!")
        break
    pohyb("O")
    if vyhra("O"):
        zobrezena_plocha()
        print("Congratulations, the player O WON!")
        break
    elif remiza():
        print("Its a draw!")
        break




