class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for ch in s:
            if ch.isalnum():
                newstr += ch.lower()
        rev = newstr[::-1]
        if(newstr == rev):
            return True
        return False
        