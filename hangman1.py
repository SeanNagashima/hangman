import random
def hangman(x):
    wrong = 0
    stages = ["",
              "________       ",
              "|              ",
              "|       |      ",
              "|       o      ",
              "|      /|\     ",
              "|      / \     ",
              "|              "
              ]
    rletters = list(x)
    board = ["_"] * len(x)
    win = False
    print("ハングマンへようこそ！")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "一文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの価値！")
            print(" ".join(board))
            win = True
            break
    if not win:
         print("\n".join(stages[0:wrong+1]))
         print("ぽみゃいの負け！正解は{}でした。死ね！".format(x))

answer = ["ketsuanana","banana","takichi","hide"]
x = (random.choice(answer))
hangman(x)
