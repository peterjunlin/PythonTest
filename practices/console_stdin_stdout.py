import sys


def console_input_one():
    s1 = input("Waiting for your input:")
    print("Your input is: ", s1)


def console_input_multiple():
    """ Count frequency of each line. 
    Use pipe to feed this routine.
    This can be used to count how many times the user have logged in.
    """

    print("Count names. Stop if input is empty.")

    names = {}
    while True:
        name = sys.stdin.readline()
        name = name.strip()
        if name == "":
            break
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
    for s1 in names.keys():
        print(s1, "->", names[s1])


if __name__ == "__main__":
    console_input_one()
    console_input_multiple()
