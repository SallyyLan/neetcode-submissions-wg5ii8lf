class TriesNode:
    def __init__(self):
        self.children = {}
        self.end = False 


class WordDictionary:

    def __init__(self):
        self.root = TriesNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TriesNode()
            cur = cur.children[c] 

        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(start, root):
            cur = root

            for c in range(start, len(word)):
                char = word[c]

                if  char == '.':
                    for child in cur.children.values():
                        if dfs(c + 1, child):
                            return True
                    return False 
                            
                else: 
                    if char not in cur.children:
                        return False 
                    cur = cur.children[char]

            return cur.end

        return dfs(0, self.root)
        





