# Concepts
## Types: String, int, arrays, objects, dict

# Problem 1: Write a function that takes in a string and converts it to a integer, where integer is > 0 and less than 10
# Assumption 1: int()
# Examples: func("3") => 3 

# Problem 2: Write a function that takes in a string and converts it to a signed integer, where integer x can be -inf < x < inf

# print(type("3"))
# print(type(3))

# Space | Time complexity 
## Space: Constant O(1)
## Time: O(n) < O(n^2) 

# Problem 3: Write a function that takes in a string and converts it to a signed float, where float x can be -inf < x < inf
# 0.001, 1.02, -5.12, ...
# 0.1, 0, -0.1

def convert(s):
    # code
    x = 0
    x_temp = 0
    is_neg = False
    x_list = []
    decimal_index = 0

    if s[0] == "-":
        is_neg = True
        s = s[1:]

    # len_s = len(s) # [ "1", ".", "0", "0"]

    for i in range(len(s)):  # [0, len_s)
        if s[i] == ".":
            decimal_index = i
            
        else: #s[i] != "."
            x_temp = 0
            for x_temp in range(0,10):
                x_str = str(x_temp)
                is_same = s[i] == x_str
                if is_same:
                    x_list.append(x_temp)
                x_temp += 1

    for i in range(len(x_list)):
        if i < decimal_index:
            x += x_list[i] * 10**(decimal_index - i - 1)

        elif i > decimal_index:
            x += x_list[i] * 10**-(i - decimal_index)    
        

    if is_neg:
        x = -x

    return x



print(convert("0")) # 3
print(convert("-12"))
print(convert("-12.01"))
print(convert("12"))
print(convert("12.2"))




# Given string s -> return int

# cheat dis
int_map = dict({
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
})


def convert(s: str):
    num = 0
    pos = 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '-':
            # this is now negative
            num *= -1
            return num    
        elif s[i] == '.':
            # reset pos & make it a float
            num /= pos
            pos = 1
            continue
            
        num += int_map[s[i]] * pos  # -543212.12345
        pos *= 10
    return num


print(convert("-12"))
print(convert("-12.01"))
print(convert("12"))
print(convert("12.2"))
print(convert("-1009.752"))
