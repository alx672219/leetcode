class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]

	    #filling out the diagonal by 1
        for i in range(len(s)):
	        dp[i][i] = True # cuz each single character can be the smallest palindrome
	        longest_palindrom = s[i]
	        
	    # filling the dp table
        for i in range(len(s)-1,-1,-1):
	    # j starts from the i location : to only work on the upper side of the diagonal 
        # 거꾸로 traverse 해야 dp diagram에서 upper right만 신경쓴다
	        for j in range(i+1,len(s)):  
	            if s[i] == s[j]:  #if the chars mathces
	            # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
	                #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
	                if j-i ==1 or dp[i+1][j-1] is True:
	                    dp[i][j] = True
	                    # we also need to keep track of the maximum palindrom sequence 
	                    if len(longest_palindrom) < len(s[i:j+1]):
	                        longest_palindrom = s[i:j+1]
	            
        return longest_palindrom

# dp = [[True, False, True, False, False], # 'b', 'ba', 'bab', 'baba', 'babad'
#      [False, True, False, True, False],  # 'a', 'ab', 'aba', 'abad'
#      [False, False, True, False, False], # 'b', 'ba', 'bad'
#      [False, False, False, True, False], # 'a', 'ad'
#      [False, False, False, False, True]] # 'd'