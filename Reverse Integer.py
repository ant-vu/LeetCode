class Solution:
    def reverse(self, x: int) -> int:
        rev_x = int("-" + str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
        return 0 if rev_x.bit_length() >= 32 else rev_x
