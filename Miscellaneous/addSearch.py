"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""

class TrieNode:
    def __init__(self):
        self.child={}
        self.endswith=False

class addSearch:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root

        for c in word:
            if c not in cur.child:
                cur.child[c]=TrieNode()
            cur=cur.child[c]
        cur.endswith=True

    def search(self, word: str) -> bool:
        def searchHelper(pos,node):

            if len(word)==pos:
                if node.endswith:
                    return True
                else:
                    return False
            if word[pos] in node.child:
                for chars in node.child:
                    if chars==word[pos] or word[pos]==".":
                        out=searchHelper(pos+1,node.child[chars])
                        if out:
                            return out
            else:
                return False

            return False

        return searchHelper(0, self.root)


if __name__ == '__main__':
    obj=addSearch()
    obj.addWord("at")
    obj.addWord("and")
    obj.addWord("an")
    obj.addWord("add")
    print(obj.search("a"))
    print(obj.search(".at"))
    obj.addWord("bat")
    print(obj.search(".at"))
    print(obj.search("an."))
    print(obj.search("b.."))


        
