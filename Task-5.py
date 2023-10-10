# problem solving task-5


#1.write python program to calculate the total number of  vowels and count individual vowel A,E,I,O,U in the string "GUVI geeks Network Private Limeted"
#solution:

string_var = "GUVI geeks Network Private Limeted"
vowels_list = []
count = 0
for vowels in string_var:
    if vowels == "a" or vowels == 'e' or vowels == 'i' or vowels == 'o' or vowels == 'u' or vowels == "A" or vowels == "E" or vowels == "I" or vowels == "O" or vowels == "U":
        vowels_list.append(vowels)
        count += 1
if count == 0:
    print("no vowels in a str")
else:
    print("1.given string are: " +str(string_var))
    print("total count of vowels in a string: " +str(count))
    print("the vowels are present in a given string :" +str(vowels_list))



#3.write function that takes a string and returns new string with all vowels removed
#solution:
def without_vowels(given_string,given_vowels):
    count = 0
    storing_value=[]
    for i in given_string:
        if i not in given_vowels:
            storing_value.append(i)
            count += 1
    print("3.The given string is :" +str(given_string))
    print("After removing all vowels from given string:")
    print(storing_value)
    print("total vowels are present in string: "+str(count))

without_vowels("GUVI geeks Network Private Limeted",'AEIOUaeiou')

#4.write function that takes string and returns number of unique character in it
#solution:
def unique_character(input_string):
    character = set(input_string)
    print(f'4.number of unique character in a input_string: {len(character)}')

unique_character("saran")

#5.write a function that takes a string and returns true if it is a palindrome,false otherwise

def palindrome(string):
    new_variable = string[::-1]
    if (new_variable == string):
        print(f"5.the given string is: {string}")
        print(f"it is a palindrome")
        return (True)
    else:
        print(f"5.the given string is: {string}")
        print(f"this is a not palindrome")
        return (False)

print(palindrome("saran"))

#7.write a function that takes string and returns most frequent character in it
#solution:

def frequent_character(input_string):
    storing_string = {}
    for character in input_string:
        if character in storing_string:
            storing_string[character] += 1
        else:
            storing_string[character] = 1
    most_freq_char = max(storing_string,key=storing_string.get)
    print(f"7. the input string is: {input_string}")
    return f"most frequent character present in {input_string} is: {most_freq_char}"
print(frequent_character("saran"))

#8.write a function that takes a string and returns True if it is anagram of another string, False otherwise
#solution:
def check_anagram(string1,string2):
    if(sorted(string1) == sorted(string2)):
        print(f'8.input string1,string2 is {string1},{string2} : True')
    else:
        print(f'8.input string1,string2 is {string1},{string2} : False')
print(check_anagram("anagram","argamna"))


#9.write a function that takes a string and return number of words in a string
#solution:
def count_strings(enter_string):
    total_words = enter_string.split()
    return f"9.total words are present in string is : {len(total_words)}"
print(count_strings("hibro i am ! kumar "))