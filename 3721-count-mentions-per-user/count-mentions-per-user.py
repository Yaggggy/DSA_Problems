class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda event: (int(event[1]), event[0] != "OFFLINE"))
        users: list[int] = [0] * numberOfUsers
        online: list[int] = [0] * numberOfUsers
        for type_, tmstmp, seq in events:
            tmstmp = int(tmstmp)
            if type_ == "OFFLINE": online[int(seq)] = tmstmp + 60
            else:
                tmstmp = tmstmp if seq == "HERE" else float("inf")
                seq = range(numberOfUsers) if seq in {"HERE", "ALL"} else [int(i[2:]) for i in seq.split()]
                for i in seq:
                    if online[i] > tmstmp: continue
                    users[i] += 1
        return users