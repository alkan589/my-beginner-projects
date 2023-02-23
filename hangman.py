import random
#You can use the words that you want
languages=["Blazor","React","...."]
choice=random.choice(languages)


def draw_board():
    board="*"*choice.__len__()
    return board

def char_guess():
    #That's broken
    global choice
    board="*"*choice.__len__()
    char=input("please a character/n")
    if char.lower() in choice.lower():
        index=choice.find(char)
        new_word=board.replace(board[index],choice[index])
    else:
        print(f"there is no such a char :{char}")
    return new_word
def language_guess():
    pass
def main():
    while True:
        msg=""
        try:
            msg=int(input("Please CHOOSE An OPERATİON.IF YOU WANT TO CHARACTER GUESS 1,LANGUAGE 2..."))
        except ValueError:
            print("please 1 or 2")
        if msg==1:
            print(char_guess())
        if msg==2:
            print("language guess")
if __name__=="__main__":
    print(
        """
            BY Ahmet YILDIZ @kalemin_kuheylani_33 HAS WRİTTEN THİS CODE.
        """
    )
    main()   

