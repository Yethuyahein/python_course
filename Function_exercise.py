def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

two_evens = lesser_of_two_evens(2,4)
print(two_evens)

g = lesser_of_two_evens(2,5)
print(g)



def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

animal = animal_crackers('Levelheaded Llama')
print(animal)

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

twenty = makes_twenty(20,10)
print(twenty)



def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'

g = old_macdonald('macdonald')
print(g)




def master_yoda(text):
    return ' '.join(text.split()[::-1])

g = master_yoda('I am home')
print(g)



def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

g = almost_there(209)
print(g)



def has_33(nums):
    for i in range(0, len(nums)-1):
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False

num = has_33([1, 3, 3])
print(num)



def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

g = paper_doll('Mississippi')
print(g)



def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

g = blackjack(9,9,11)
print(g)



def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

g = summer_69([2, 1, 6, 9, 11])
print(g)


def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   
       
    return len(code) == 1

g = spy_game([1,7,2,0,4,5,0])
print(g)


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  
        return 0
    while x <= num:
        for y in range(3,x,2):  
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
                
g = count_primes(100)
print(g)



def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('a')


#Homework
def vol(rad):
    return (4/3)*(3.14)*(rad**3)

print(vol(2))


def ran_check(num,low,high):
    
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')

print(ran_check(5,2,7))


def ran_bool(num,low,high):
    return num in range(low,high+1)
bool = ran_bool(3,1,10)
print(bool)



def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
list = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(list)



def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply([1,2,3,-4]))


def palindrome(s):
    
    s = s.replace(' ','') 
    return s == s[::-1]   
x=palindrome('nurses run')
print(x)



import string

def ispangram(str1, alphabet=string.ascii_lowercase): 
    alphaset = set(alphabet)  
    str1 = str1.replace(" ",'')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset

x = ispangram("The quick brown fox jumps over the lazy dog")
x = string.ascii_lowercase