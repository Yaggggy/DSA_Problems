class Solution(object):
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])

        resolved = [False] * (n - 1)
        unresolved = n - 1
        deletions = 0

        for col in range(m):
            if unresolved == 0:
                break

            need_delete = False

            for row in range(n - 1):
                if not resolved[row] and strs[row][col] > strs[row + 1][col]:
                    need_delete = True
                    break

            if need_delete:
                deletions += 1
                continue

            for row in range(n - 1):
                if not resolved[row] and strs[row][col] < strs[row + 1][col]:
                    resolved[row] = True
                    unresolved -= 1

        return deletions