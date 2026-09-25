#scope resolution
def func1():
    a = 1
    print(a)

def func2():
    a = 2
    print(a)

func1()
func2()

print()

def func1():
    x = 1
    print(x)
    def func2():
        x = 2
        print(x)
    func2()
func1()

print()

def func1():
    x = 1

    def func2():
        x = 2
        print(x)
    func2()
func1()

print()

def func1():
    x = 1

    def func2():
        print(x)
    func2()
func1()

print()
def func1():
    print(x)

def func2():
    print(x)

x=3
func1()
func2()

print()
from math import e
def func1():
    print(e)

e= 4
func1()
