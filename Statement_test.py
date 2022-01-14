# st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     if word[0] == 's':
#         print(word)

# x = list(range(0,11,2))
# print(x)

# g = [x for x in range(1,51) if x%3 == 0]
# print(g)

# st = 'Print every word in this sentence that has an even number of letters'
# for word in st.split():
#     if len(word)%2 == 0:
#         print(word+" has an even length")

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

st = 'Create a list of the first letters of every word in this string'
g = [word[0] for word in st.split()]
print(g)