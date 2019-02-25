class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        if not len(s):
            return 0
        
        if not len(s.strip()):
            return 1
        
        #get substrings list comprehension
        l = [s[i:j+1] for i in range(len(s)) for j in range(i,len(s))]

        #remove repeating character substring substring
        l = list(filter(lambda x : len(set(x)) ==  len(x) , l))

        #sorting by length of each string in the list in descending
        l.sort(key = len, reverse = True)
        
        #returning length of longest substring
        return len(l[0])
        
        
        