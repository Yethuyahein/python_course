try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error occurred!")


x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')



def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
    print('Thank you, your number squared is: ',n**2)

ask()