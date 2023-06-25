class Solution:
    def minimizedStringLength(self, s: str) -> int:
        result = "".join(dict.fromkeys(s))
        return len(result)

if __name__ == '__main__':
    obj=Solution()
    print(obj.minimizedStringLength("aaabc"))
    print(obj.minimizedStringLength("cbbd"))
    print(obj.minimizedStringLength("dddaaa"))
    print(obj.minimizedStringLength("aaadddaaa"))
    print(obj.minimizedStringLength("j"))
