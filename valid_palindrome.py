import re

class Solution:
    def isPalindrome(self, s: str) -> str:
        ans = re.sub('[^a-z0-9]*',"", s.lower().strip())
        reverse_str = ans[::-1].lower().strip()

        print("ans is ", ans)
        print("reverse is ", reverse_str)
        if "".join(ans) == reverse_str:
            return True
        else:
            return False
        

    

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

# ans2 = sol.reverse_str(ans1)
# print(ans1)
# print(ans2)


