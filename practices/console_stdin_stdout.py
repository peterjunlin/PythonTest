import sys


def console_input_multiple():
    """ Count frequency of each line. 
    Use pipe to feed this routine.
    This can be used to count how many times the user have logged in.
    """

    print("Count names. Stop if input is empty.")

    name_counts = {}
    while True:
        name = sys.stdin.readline()
        name = name.strip().lower().capitalize()
        if name == "":
            break
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    print(name_counts)


if __name__ == "__main__":
    console_input_multiple()
