class Solution:
    def concatenatedBinary(n: int) -> int:
        dummy = ""

        for i in range(1,n + 1):
            temp = bin(i)[2:]
            dummy = dummy + temp
            # print(dummy, "  ",temp, "  ", i)
        result = int(dummy,2)
        return result % 1000000007
        
    print(concatenatedBinary(3))