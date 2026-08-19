class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_map = defaultdict(set)

        for row, seat in reservedSeats:
            reserved_map[row].add(seat)
        
        total_groups = 0
        
        for row in reserved_map:
            reserved = reserved_map[row]
            
            can_place_left = all(seat not in reserved for seat in [2, 3, 4, 5])
            can_place_middle = all(seat not in reserved for seat in [4, 5, 6, 7])
            can_place_right = all(seat not in reserved for seat in [6, 7, 8, 9])
            
            if can_place_left and can_place_right:
                total_groups += 2
            elif can_place_left or can_place_middle or can_place_right:
                total_groups += 1
        
        rows_with_no_reservations = n - len(reserved_map)
        total_groups += rows_with_no_reservations * 2
        
        return total_groups