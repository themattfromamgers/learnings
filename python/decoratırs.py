

def ikiyle_carp(func):
    def wrapper(x, y):
        func(x*2, y*2)
    return wrapper

@ikiyle_carp
def topla(x, y):
    print(x+y)

topla(5, 10)