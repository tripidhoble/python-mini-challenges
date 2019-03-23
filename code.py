# --------------
#Code starts here

def palindrome(num):
    num += 1
    while (str(num) != str(num)[::-1]):
        num += 1
    return num

print("Palindrome(123)",palindrome(123))

print("Palindrome(1331)", palindrome(1331))


# --------------
#Code starts here

def a_scramble(str_1, str_2):
    str_1, str_2 = str_1.lower(), str_2.lower()
    str_1_list = list(str_1)
    for i in range(len(str_2)):
        if(str_2[i] not in str_1_list):
            return False
        else:
            str_1_list.remove(str_2[i])
    return True

print(a_scramble("Tom Marvolo Riddle","Voldemort"))

print(a_scramble("ticket","chat"))

print(a_scramble("baby shower","shows"))


# --------------
#Code starts here

def check_fib(num):
    num_1, num_2 = 0, 1
    while(num_2 < num):
        sum = num_1 + num_2
        num_1 = num_2
        num_2 = sum
        if(num_2 == num):
            return True
    return False

print(check_fib(145))

print(check_fib(377))
        


# --------------
#Code starts here

def compress(word):
    word = word.lower()
    print(word)
    com_word = list(word[0])
    count = 1
    for i in range(1,len(word)):
        if com_word[-1] == word[i]:
            count +=1
            if(i == len(word)-1):
                com_word.append(count)
        else:
            com_word.append(count)
            com_word.append(word[i])
            count = 1
    if(type(com_word[-1]) == str):
        com_word.append(1)
    return ''.join([str(elem) for elem in com_word ])
    
print(compress("abbs"))

print(compress("xxcccdex"))

print(compress('Ss'))


# --------------
#Code starts here

def k_distinct(string,k):
    string = set(string.lower())
    if (k == len(string)):
        return True
    else:
        return False

print(k_distinct('Messoptamia',8))

print(k_distinct('banana',4))


