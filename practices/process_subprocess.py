import subprocess


def test_shell_command():
    a = subprocess.run("ls", shell=True, stdout = subprocess.PIPE)
    # print(a)
    # print(type(a))
    print(a.stdout.decode())


def test_subprocess():
    subprocess.run(['notepad', r'c:\temp\test.txt'])
    print('return from testSubprocess')


def test_call_script():
    subprocess.run("test2.py", shell=True)


if __name__ == '__main__':
    # test_shell_command()
    test_subprocess()
    # test_call_script()
