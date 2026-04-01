class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string
        return encoded


    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        while len(s) > 0:
            temp = ""
            cnt = 0
            while s[cnt] != "#":
                cnt+=1
            num = int(s[0:cnt])
            temp = s[cnt+1:cnt+1+num]
            print(temp)
            decoded.append(temp)
            s = s[num+cnt+1:]
        return decoded