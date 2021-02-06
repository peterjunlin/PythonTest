from __future__ import nested_scopes

spam = "This is global spam."


def scope_test():
    def do_local():
        spam = "This is local spam, which shadows non-local and global spam."
        print(spam)

    def do_nonlocal():
        nonlocal spam
        spam = "Nonlocal spam was updated."

    def do_global():
        global spam
        spam = "Global spam was updated."

    spam = "This is non-local spam."
    do_local()
    print("After local assignment, non-local spam: ", spam)
    do_nonlocal()
    print("After nonlocal assignment, non-local spam: ", spam)
    do_global()
    print("After global assignment, non-local spam: ", spam)


if __name__ == "__main__":
    scope_test()
    print("Global spam: ", spam)
