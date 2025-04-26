class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_sets = [set(word) for word in words] 
        count = 0
        
        for i in range(len(word_sets)):
            for j in range(i + 1, len(word_sets)):
                if word_sets[i] == word_sets[j]:  
                    count += 1
        
        return count
