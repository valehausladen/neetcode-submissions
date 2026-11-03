class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        cleaned = []
        for char in lower:
            if char.isalnum():
                cleaned.append(char)
        length = len(cleaned)
        for i, character in enumerate(cleaned):
            if character != cleaned[length-1-i]:
                return False
        return True
