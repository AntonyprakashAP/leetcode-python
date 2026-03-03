class Solution(object):
    def findKthBit(self, n, k):
        if n == 1:
            return '0'
        
        mid = 1 << (n - 1) # Calculate 2^(n-1)
        
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # k is in the second half. Map to mirror position and invert the result.
            # Mirror position formula: mid * 2 - k or (2**n - 1) - k + 1
            # Invert: '0' becomes '1', '1' becomes '0'
            result_bit = self.findKthBit(n - 1, mid * 2 - k)
            return '1' if result_bit == '0' else '0'
        