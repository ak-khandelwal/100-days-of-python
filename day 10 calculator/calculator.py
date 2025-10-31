def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

ops = {
        '+':add,
        '-':subtract,
        '*':multiply,
        '/':divide
    }
while True:
    num1 = int(input('enter first number: '))
    num2 = int(input('enter second number: '))
    op = input('select a operation from +,-,*,/ : ')
    matched_any = False
    for key in ops:
        if op==key:
            matched_any=True
            break;

    if not matched_any:
        print('invalid operation selection')
        print('try again!!!')
        continue
    result = ops[op](num1,num2)
    print(result)
    should_continue = input('do you want to continue?"yes" or "no"')
    if should_continue=='no':
        break;
    elif should_continue=='yes':
        continue
    else:
        print('oops wrong input')
        break;
