class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create an empty string
        newStr = ""

        # Loop through each character in the input string
        for c in s:
            if c.isalnum():
                # character is alphanumeric, add to newStr as a lowercase letter
                newStr += c.lower()
        
        # Return if the newStr is equal to its reverse
        return newStr == newStr[::-1]            