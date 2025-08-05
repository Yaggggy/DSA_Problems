class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        dic = (sorted(dic.items(), reverse=True))
        
        res = []

        for i in dic :
            res.append(i[1])
        return(res)