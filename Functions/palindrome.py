def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
        return True
    else:
        print("Not Palindrome")

print(palindrome("Deba"))