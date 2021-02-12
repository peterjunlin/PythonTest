import re


def re_partial_delete():
    """deleting by using re.sub"""
    s1 = 'python-script.py_hello-script.py'
    s2 = re.sub(r'(-script\.py)?$', '', s1)
    assert s2 == 'python-script.py_hello'


if __name__ == "__main__":
    re_partial_delete()
