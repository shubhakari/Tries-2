class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):
        curnode = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if curnode.children[i] is None:
                curnode.children[i] = TrieNode()
            curnode = curnode.children[i]
            curnode.words.append(idx)

    def search(self, prefix):
        node = self.root
        for ch in prefix:
            i = ord(ch) - ord('a')
            if node.children[i] is None:
                return []
            node = node.children[i]
        return node.words

class Solution:
    # TC : exponential
    # SC : exponential
    def dfs(self, square):
        # base case: if we formed a complete square
        if len(square) == len(square[0]):
            self.squares.append(square[:])
            return

        idx = len(square)
        prefix = ''.join(word[idx] for word in square)
        indices = self.trie.search(prefix)

        for index in indices:
            square.append(self.words[index])  # use self.words instead of undefined variable
            self.dfs(square)
            square.pop()

    def wordSquares(self, words):
        if not words:
            return []
        
        self.trie = Trie()
        self.squares = []
        self.words = words  # store words for access in dfs()

        for i, word in enumerate(words):
            self.trie.insert(word, i)

        for word in words:
            self.dfs([word])  # start with a list instead of a string

        return self.squares

# Example usage
s = Solution()
arr = ["area", "lead", "wall", "lady", "ball"]
print(s.wordSquares(arr))
arr2 = ["abat","baba","atan","atal"]
print(s.wordSquares(arr2))
