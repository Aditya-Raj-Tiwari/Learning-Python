# use recursion method to implement a countdown counter


def countdown(x):
    if x == 0:
        print("Done!!")
        return
    else:
        print(x,"...")
        countdown(x-1)
        #! it never goes down here untill x=0
        print('fooo')

countdown(10)