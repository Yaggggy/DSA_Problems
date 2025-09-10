class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(x) for x in languages]
        people = set()
        for f1, f2 in friendships:
            if not languages[f1-1] & languages[f2-1]:
                people.add(f1)
                people.add(f2)
        not_speakers = [0] * n
        all_langs = set(range(1,n+1))
        for p in people:
            for l in all_langs - languages[p-1]:
                not_speakers[l-1]+=1
        return min(not_speakers)



        