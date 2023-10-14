import random
import string


def generate_names():
    random_source = string.ascii_letters + string.digits
    character = random.choice(string.ascii_lowercase)
    character += random.choice(string.digits)

    for i in range(7):
        character += random.choice(random_source)

    character_list = list(character)
    random.SystemRandom().shuffle(character_list)
    character_list = ''.join(character_list)
    return character

def department_check(department):
    allowed = ['marketing', 'accounting', 'finops']
    return department.lower() in allowed

while True:
    print('╔════════════════════════════════════════════╗')
    print('✧ Marketing / Accounting / FinOps Use Only! ✧')
    print('╚════════════════════════════════════════════╝')
    department = (input('Department: ')).lower()
    
    if department_check(department):
        instances = int(input('Instance Count: '))
        counter = 1
        while (counter <= instances):
            print('Output', counter, end= ':')
            print('', department + '_' + generate_names())
            counter += 1
            if counter > instances:
                print('End of list.')
            continue
    else:
        print('You cannot use this generator. Go away.')
    break