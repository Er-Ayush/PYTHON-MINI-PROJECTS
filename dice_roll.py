import random
i = 1


def dice(r):

    if r == 1:
        print(''' 
        
        -----------
        |         |
        |    O    |
        |         |
        -----------
        
        ''')
    if r == 2:
        print(''' 

        -----------
        |         |
        |  O   O  |
        |         |
        -----------

        ''')
    if r == 3:
        print(''' 

        -----------
        | O       |
        |    O    |
        |       O |
        -----------

        ''')
    if r == 4:
        print(''' 

        -----------
        | O     O |
        |         |
        | O     O |
        -----------

        ''')
    if r == 5:
        print(''' 

        -----------
        |  O    O |
        |    O    |
        |  O    O |
        -----------

        ''')
    if r == 6:
        print(''' 

        -----------
        | O     O |
        | O     O |
        | O     O |
        -----------

        ''')

while i > 0:
    i = i + 1
    c=input('press y to throw dice:  && n to stop\n')
    if c=='y':
        pass
    elif c=='n':
        break;
    r = random.randint(1,6)
    print("number",r)
    dice(r)


