from math import gcd

class solution:

    def gcd_of_string(self, str1: str, str2: str ) -> str:

        if str1+str2 != str2+ str1:
            return ""

        length = gcd(len(str1), len(str2))

        return str1[:length]

obj= solution()

print(obj.gcd_of_string("ABABAB","AB"))