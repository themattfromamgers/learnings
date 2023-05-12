def xde(send):
    def head(x, y):
        send(x, y)
    return head

@xde
def go(x, y):
    print(x)
    print(y)
go()
