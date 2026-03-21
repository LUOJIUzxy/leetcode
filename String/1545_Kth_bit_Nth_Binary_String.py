def findKthBit(n: int, k: int) -> str:
     s_i = "0"
     while n:
          # 把一个可迭代对象里的所有字符串连接起来
          # 生成一个新的字符串，不会修改原来的列表
          invert = ''.join(str(1 - int(bit)) for bit in s_i)
          reverse = invert[::-1]

          s_i = s_i + "1" + reverse
          n -= 1

     return s_i[k-1]


        