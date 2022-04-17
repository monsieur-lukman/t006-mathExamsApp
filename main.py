import random
r = 0
n = 0
class InputError(Exception):
    def __init__(self):
        self.message = 'Incorrect format.'
        super().__init__(self.message)
        
def input_checker(user):
    if user.isalpha() or user == None or user == '':
        raise InputError
    
def simple_operations():
    global first, second, int_oper
    first = random.randint(2,9)
    second = random.randint(2,9)
    int_oper = random.choice(['-','+','*']) 
    output = print(first, int_oper, second)
    return output
           
def squares():
    global first_sqr
    first_sqr = random.randint(11,29)
    return print(first_sqr)
    
def sim_ans():
    if int_oper == '+':
        ans = first + second
    elif int_oper == '-':
        ans = first - second
    elif int_oper == '*':
        ans = first * second
    return ans

def int_ans():
    ans = int(first_sqr)**2
    return ans
level = input('''Which level do you want? Enter a number:
                1 - simple operations with numbers 2-9
                2 - integral squares of 11-29''')  
while True:
    try:
       if int(level) == 1 or int(level) == 2:
           level1 = int(level)
           break 
    except ValueError:
        print('Incorrect format.')
        continue           

for n in  range(5):
    n+=1
    if level1 == 1: 
        simple_operations() 
    elif level1 == 2:
        squares()       
    while True:

        try:
            user = input()
            user1 = int(user)
            input_checker(user)
            break
        except (ValueError, InputError) as err:
            print('Incorrect format.')
            continue
  
    if level1 == 1:
        if user1 == sim_ans():
            print('Right!')
            r+=1
        elif user1 != sim_ans():
            print('Wrong!')
    elif level1 == 2:
        if user1 == int_ans():
            print('Right!')
            r+=1
        elif user1 != int_ans():
            print('Wrong!')
if level1 == 1:
    level_desc = '(simple operations with numbers 2-9)'
elif level1 == 2:
    level_desc = '(integral squares of 11-29)'
    
print('Your mark is %s/5'%r)
save_opt = input('Would you like to save your result to the file? Enter yes or no.')
if save_opt in ['yes', 'YES', 'y', 'Yes']:
    username = input('What is your name?')
    results = open('results.txt', 'a', encoding='utf-8')
    results.write(f'{username}: {r}/5 in level {level} {level_desc}.')
    results.close()
    print('The results are saved in "results.txt".')
else:
    pass
    
