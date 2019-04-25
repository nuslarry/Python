count=2 # this one is a global variable
def test():
    global count
    if count<10:
        count+=1
        print(count)
        test()
    else:
        return
    return

test()

