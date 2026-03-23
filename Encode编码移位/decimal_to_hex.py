class Solution:

    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"

        chars = []

        for _ in range(8):
            digit = num & 0xf
            chars.append(hex_chars[digit])
            num >>= 4

            if num == 0:
                break
        
        return "".join(reversed(chars))

        