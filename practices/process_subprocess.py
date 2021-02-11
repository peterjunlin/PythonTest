import subprocess


def test_shell_command():
    a = subprocess.run(["ls", "-l"])
    print(a)


def test_subprocess():
    a = subprocess.run(['open -a textedit', r'test.txt'], shell=True)
    print(a)


def test_call_script():
    a = subprocess.run("python -m test.py", shell=True, stdout=subprocess.PIPE)
    print(a)


if __name__ == '__main__':
    test_shell_command()
    # test_subprocess()
    # test_call_script()
