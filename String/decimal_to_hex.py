import sys

for line in sys.stdin:
    a = line.split()

    if a[0][:2] == "0x":
        hexi = a[0][2:]
        hexi = hexi.upper()
        result = 0
        for i, char in enumerate(reversed(hexi)):
            if char == "A":
                num = 10
            elif char == "B":
                num = 11
            elif char == "C":
                num = 12
            elif char == "D":
                num = 13
            elif char == "E":
                num = 14
            elif char == "F":
                num = 15
            else:
                num = int(char)
            result += num * (16 ** i)
            
        print(result)
    else:
        print()
