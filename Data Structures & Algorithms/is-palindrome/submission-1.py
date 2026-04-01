class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for letter in s:
            if letter.isalnum():
                new += letter.lower()
        return new == new[::-1]