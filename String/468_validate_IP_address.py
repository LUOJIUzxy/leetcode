class Solution:
     def isIPv4(self, ip: str) -> bool:
          ip_list = ip.split(".")
          for ip_segment in ip_list:
                if not ip_segment:
                    return False
                if not ip_segment.isdigit():
                    return False
                elif ip_segment.startswith("0") and len(ip_segment) != 1:
                    return False
                else:
                    segment = int(ip_segment)
                    if segment < 0 or segment > 255:
                        return False
          
          return True

        
     def isIPv6(self, ip: str) -> bool:
          hex_chars = set("0123456789abcdefABCDEF")

          ip_list = ip.split(":")
          for ip_segment in ip_list:
               if len(ip_segment) < 1 or len(ip_segment) > 4:
                    return False
               else:
                    for char in ip_segment:
                         if char not in hex_chars:
                              return False
                    
          return True
                    
     

     def validIPAddress(self, queryIP: str) -> str:

          if queryIP.count(".") == 3:
               # IPv4
               if self.isIPv4(queryIP):
                    return "IPv4"
               else:
                    return "Neither"

          if queryIP.count(":") == 7:
               # IPv6
               if self.isIPv6(queryIP):
                    return "IPv6"
               else:
                    return "Neither"
          
          else:
               return "Neither"
          
solution = Solution()
queryIP = "2001:0db8:85a3::8A2E:037j:7334"
print(solution.validIPAddress(queryIP))
        