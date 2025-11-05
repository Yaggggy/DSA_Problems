class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for i in strs :
            a = ''.join(sorted(i))
            ans[a].append(i)
        return list(ans.values())
