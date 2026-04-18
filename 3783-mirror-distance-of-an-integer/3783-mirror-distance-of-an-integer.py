class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = 0
        temp = n
        
        # Reverse the number
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10
        
        # Return absolute difference
        return abs(n - rev)