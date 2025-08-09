class Solution:
    def countLargestGroup(self, n: int) -> int:
        arr = [0] * 1000
        max_size = 0

        for i in range(1, n + 1):
            sum_digits = 0
            num = i

            while num > 0:
                sum_digits += num % 10
                num //= 10

            arr[sum_digits] += 1

        for count in arr:
            if count > max_size:
                max_size = count

        group_count = 0
        for count in arr:
            if count == max_size:
                group_count += 1

        return group_count
