##is a string a palindrome using recursion
##if the first and the last element are the same and the string in between is a palindrome then obviously the whole string is palindrome

def isPalindrome(s):
    t=len(s)
    if(t==0 or t==1): return True

    else: return s[0] == s[-1] and isPalindrome(s[1:-1])
    

s=str(raw_input('Enter the string:'))
solution=isPalindrome(s)
