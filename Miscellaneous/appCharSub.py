

class appCharSub:
    def appendCharacters(self, s: str, t: str) -> int:
        result=0
        for i in range(len(s)):
            if s[i]==t[result]:
                result+=1
                if result==len(t):
                    break

        return len(t)-result

if __name__ == '__main__':
    obj=appCharSub()
    print(obj.appendCharacters(s = "coaching", t = "coding"))
    print(obj.appendCharacters(s = "abcde", t = "a"))
    print(obj.appendCharacters(s = "z", t = "abcde"))
