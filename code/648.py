# -*- Encoding:UTF-8 -*-

# 648. Replace Words

# In English, we have a concept called root, which can be followed by some other words to form another longer word
# - let's call this word successor. For example, the root an, followed by other, which can form another word another.

# Now, given a dictionary consisting of many roots and a sentence.
# You need to replace all the successor in the sentence with the root forming it.
# If a successor has many roots can form it, replace it with the root with the shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Note:
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        '''
        # Another Way
        hmap = {}
        for root in dict:
            if root[0] in hmap:
                hmap[root[0]].append(root)
            else:
                hmap[root[0]] = [root]
        
        s = sentence.split(" ")
        for i in xrange(len(s)):
            word = s[i]
            if word[0] in hmap:
                possibleRoots = hmap[word[0]]
                possibleRoots.sort() # Using Sort !
                for pos in possibleRoots:
                    if pos == word[:len(pos)]:
                        s[i] = pos
                        break
        return " ".join(s)
                        
        '''
        # Tier tree
        tree = {}
        for pre in dict:
            cur = tree
            for c in pre:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["*"] = None
        ans = []
        words = sentence.split(" ")
        for w in words:
            cur = tree
            tmp = ""
            for i, c in enumerate(w):
                if c in cur:
                    tmp += c
                    cur = cur[c]
                    if "*" in cur or i == len(w)-1:
                        ans.append(tmp)
                        break
                elif "*" not in cur:
                    ans.append(w)
                    break
        return " ".join(ans)
