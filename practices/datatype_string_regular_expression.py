import re


def re_partial_delete():
    """deleting by using re.sub"""
    s1 = 'python-script.py_hello-script.py'
    s2 = re.sub(r'(-script\.py)?$', '', s1)
    assert s2 == 'python-script.py_hello'


def re_find():
    # find all matched
    pattern = '\w+ly'
    re1 = re.compile(pattern)
    str1 = 'hello world! carefully to watch, and wonderfully to perform'
    result1 = re1.findall(str1)
    print("re.findall -- Find '{0}' in '{1}':\n    {2}".format(pattern, str1, result1))

    # match whole string
    str2 = "carefully"
    result2 = re1.fullmatch(str2)
    print("re.fullmatch -- match whole string '{0}' in '{1}':\n    {2}".format(pattern, str2, result2))


if __name__ == "__main__":
    re_partial_delete()
    re_find()
