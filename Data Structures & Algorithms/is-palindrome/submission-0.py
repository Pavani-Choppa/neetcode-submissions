class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force O(n),O(n)
        # nst = ''.join(ch for ch in s if ch.isalnum()).lower()
        # rev = ''
        # for i in nst:
        #     rev = i+rev
        # if rev == nst:
        #     return True
        # else:
        #     return False
    
        #Optimized using 2 pointers O(n),O(1)
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        else:
            return True
