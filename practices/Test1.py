import sys
import os
from datetime import timedelta
# import Tkinter
import subprocess

def testTimeDelta():
  d = timedelta(microseconds = -1)
  print(d.days, d.seconds, d.microseconds)

def testDictionary():
  d1 = dict([('a', 1), ('b', 2), ('c', 3)])
  print(d1, type(d1))
  for i, k in enumerate(d1.items()):
    print(i, k[0], type(k))
  
  questions = ['name', 'quest', 'favorite color']
  answers = ['lancelot', 'the holy grail', 'blue']
  print('zip',type(zip(questions, answers)))
  for q, a in reversed(zip(questions, answers)):
    print('What is your {0}?  It is {1}.'.format(q, a))

def testEnvironment(s):
  #a=os.getenv(s)
  if s in os.environ:
    a=os.environ[s]
    print(a)
  else:
    print(s + ' does not exist')

def testTryFinally():
  try:
    a = 'abc'
    print('in try')
    f = open('abc', 'r')
    f.close()
  except IOError:
    print('in exception')
  finally:
    print('in finally')

def testTkinter():
  top = Tkinter.Tk()
  # Code to add widgets will go here...
  top.mainloop()

def testSubprocess():
  subprocess.run(['notepad', r'c:\temp\test.txt'])
  print('return from testSubprocess')

def testCallScript():
  subprocess.run("test2.py", shell=True)

def testShellCommand():
  a = subprocess.run("dir", shell=True, stdout = subprocess.PIPE)
  #print(a)
  #print(type(a))
  print(a.stdout.decode())

def testBytearray():
  list1 = [1,2,3,4,5,6,7,8]
  arr1 = bytearray(list1)
  print(type(arr1))
  #arr1[0:2] = [11, 12, 13, 14, 15]
  arr2 = arr1[0:2]
  arr2[0] = 100
  print(arr1)
  print(arr2)

if __name__=='__main__':
  #testTimeDelta()
  #testDictionary()
  #exec('Test2.py')
  #testEnvironment('path1')
  #testTryFinally()
  #testTkinter()
  #testSubprocess()
  #testCallScript()
  #testShellCommand()
  testBytearray()

