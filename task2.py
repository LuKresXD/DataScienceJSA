def is_palindrome(s):
    letters = [char.lower() for char in s if char.isalpha()]
    return letters == letters[::-1]


input_string = "!1TestseT"
result = is_palindrome(input_string)
print(result)
