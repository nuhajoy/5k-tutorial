class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        print(count)
        win = Counter(s[:len(p)])
        arr=[]
        print(win)
        if win == count:
            arr.append(0)
        # print (arr[0])
        l = 0
        for i in range (len(p),len(s)):
            win[s[l]] -= 1
            win[s[i]] += 1
            l += 1

            if win == count:
                arr.append(l)

            
        return arr
