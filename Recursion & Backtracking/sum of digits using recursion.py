class Solution:
    def get_digits_sum(self,num):
        return 0 if num == 0 else (int(num)%10) + self.get_digits_sum(int(num)/10)

if __name__ == "__main__":
    ob = Solution()
    num = int(input('Enter Number'))
    ans = ob.get_digits_sum(num)
    print(ans)
    
    
# num % 10 => fetches last digit
# num/10 => returns number with last digit removed

# Example
# num = 645
# ans = 15
