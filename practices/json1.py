import json

# used for practicing unittest
def get_json_string(list1):
    return json.dumps(list1)

def list_to_json_string(list1):
    print(json.dumps(list1))

def json_file_write(filename, list1):
    f = None
    try:
        f = open(filename, 'w')
        json.dump(list1, f)
    finally:
        if f is None:
            f.close()

def json_file_read(filename):
    f = open(filename, 'r')
    s = json.load(f)
    print(s)
    print(type(s))
    f.close()

def practice1():
    filename = "./temp/test_json.txt"
    list1 = ['abc', 1, 2, 3, 'hello']
    print(">>>")
    print("list to json string")
    print("---")
    list_to_json_string(list1)
    print(">>>")
    print("json file write")
    print("---")
    json_file_write(filename, list1)
    print(">>>")
    print("json file read")
    print("---")
    json_file_read(filename)
