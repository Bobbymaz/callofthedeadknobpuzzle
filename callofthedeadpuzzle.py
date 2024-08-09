from random import randrange

num1 = 0
num2 = 0
num3 = 0
num4 = 0


def check_vals():
    return num1 == 2 and num2 == 7 and num3 == 4 and num4 == 6

def turn1():
    global num1
    global num2
    global num3
    global num4
    num1 = num1 + 1
    num3 = num3 + 1

    if num1 >= 11:
        num1 = 0
    if num2 >= 11:
        num2 = 0
    print('turned 1\n')

def turn2():
    global num1
    global num2
    global num3
    global num4
    num2 = num2 + 1
    num4 = num4 + 1

    if num2 >= 11:
        num2 = 0
    if num4 >= 11:
        num4 = 0
    print('turned 2\n')

def turn3():
    global num1
    global num2
    global num3
    global num4
    num3 = num3 + 1
    num2 = num2 + 1

    if num3 >= 11:
        num3 = 0
    if num2 >= 11:
        num2 = 0
    print('turned 3\n')


def turn4():
    global num1
    global num2
    global num3
    global num4
    num4 = num4 + 1
    num1 = num1 + 1

    if num4 >= 11:
        num4 = 0
    if num1 >= 11:
        num1 = 0
    print('turned 4\n')
    




def solve():
    num1 = int(input('input floor 1 (top): '))
    num2 = int(input('input floor 2: '))
    num3 = int(input('input floor 3: '))
    num4 = int(input('input floor 4: '))

    c = 0
    last = [0,0,0,0]
    second_last = [0,0,0,1]
    while not check_vals():
        #print(str(num1) + " " + str(num2) + " " + str(num3) + " " + str(num4))
        while num1 != 2:
            num1 = num1 + 1
            num3 = num3 + 1

            if num1 >= 11:
                num1 = 0
            if num3 >= 11:
                num3 = 0
        while num2 != 7:
            num2 = num2 + 1
            num4 = num4 + 1

            if num2 >= 11:
                num2 = 0
            if num4 >= 11:
                num4 = 0
            #print('turned 2\n')
        
        while num3 != 4:
            num3 = num3 + 1
            num2 = num2 + 1

            if num3 >= 11:
                num3 = 0
            if num2 >= 11:
                num2 = 0
        while num4 !=6:
            num4 = num4 + 1
            num1 = num1 + 1

            if num4 >= 11:
                num4 = 0
            if num1 >= 11:
                num1 = 0
        
        

        
        second_last = last
        print("second_last" + str(second_last))
        if second_last == last:
            num2 = num2 + 1
            num3 = num3 +1
            if num2 >= 11:
                num2 = 0
            if num3 >=11:
                num3 = 0
            #num1 = num1 + 1
        last = [num1, num2, num3, num4]
        if c == 10:
            num1 = num1 + 1
            
        
        print("last " + str(last))
        
        
        
            #print('turned 1\n')
        
            #print('turned 3\n')

        
            #print('turned 4\n')

    
    
    
    
    
    
    

    

        
                

    #1 -> 3
    #3 -> 2
    #2 -> 4
    #4 -> 1



    
