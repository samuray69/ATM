pin = 4587
pin_limit = 3
def pinchecking():
    global pin_limit
    print("please enter your code")
    grac = int(input())
    if grac == pin:
        print("how much money do you need")
    else:

        pin_limit -= 1
        if pin_limit > 0:
            print(f"leaved {pin_limit} times")
            pinchecking()
        else:
            print("your card is blocked")
pinchecking()
