class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        total_cells = m * n
        
        start_pos = -1
        litter_bit = [0] * total_cells
        is_reset = [False] * total_cells
        num_L = 0
        
        for r in range(m):
            for c in range(n):
                u = r * n + c
                cell = classroom[r][c]
                if cell == 'S':
                    start_pos = u
                elif cell == 'L':
                    litter_bit[u] = 1 << num_L
                    num_L += 1
                elif cell == 'R':
                    is_reset[u] = True
                    
        target_mask = (1 << num_L) - 1
        num_masks = 1 << num_L
        
        adj = [[] for _ in range(total_cells)]
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'X':
                    continue
                u = r * n + c
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                        adj[u].append(nr * n + nc)
                        
        max_energy = [-1] * (total_cells * num_masks)
        
        queue = deque([(start_pos, 0, energy)])
        max_energy[start_pos * num_masks + 0] = energy
        
        moves = 0
        
        while queue:
            for _ in range(len(queue)):
                u, mask, e = queue.popleft()
                
                if mask == target_mask:
                    return moves
                    
                if e == 0:
                    continue
                    
                for v in adj[u]:
                    nxt_e = energy if is_reset[v] else e - 1
                    nxt_mask = mask | litter_bit[v]
                    state_idx = v * num_masks + nxt_mask
                    
                    if nxt_e > max_energy[state_idx]:
                        max_energy[state_idx] = nxt_e
                        queue.append((v, nxt_mask, nxt_e))
                        
            moves += 1
            
        return -1