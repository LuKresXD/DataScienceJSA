def is_palindrome(s):
    letters = [char.lower() for char in s if char.isalpha()]
    return letters == letters[::-1]
