import sys

def hangman_picture(attemps):
    if attemps == 0:
        print("  __________")
        print("  |        |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|__    ")
    elif attemps == 1:
        print("  __________")
        print("  |        |")
        print("  |        O")
        print("  |")
        print("  |")
        print("  |")
        print("__|__    ")
    elif attemps == 2:
        print("  __________")
        print("  |        |")
        print("  |       \\O")
        print("  |")
        print("  |")
        print("  |")
        print("__|__    ")
    elif attemps == 3:
        print("  __________")
        print("  |        |")
        print("  |       \\O/")
        print("  |")
        print("  |")
        print("  |")
        print("__|__    ")
    elif attemps == 4:
        print("  __________")
        print("  |        |")
        print("  |       \\O/")
        print("  |        |")
        print("  |")
        print("  |")
        print("__|__    ")
    elif attemps == 5:
        print("  __________")
        print("  |        |")
        print("  |       \\O/")
        print("  |        |")
        print("  |       / ")
        print("  |")
        print("__|__    ")
    elif attemps == 6:
        print("  __________")
        print("  |        |")
        print("  |       \\O/")
        print("  |        |")
        print("  |       / \\")
        print("  |")
        print("__|__    ")

    return
