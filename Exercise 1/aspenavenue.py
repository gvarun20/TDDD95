import sys
import math


total_pegs = int(input())
canvas_length, canvas_width = map(int, input().split())


raw_data = sys.stdin.read().split()
y_coords = sorted(map(int, raw_data))


half_pegs = total_pegs // 2


horizontal_gap = canvas_length / (half_pegs - 1)


dp = [[float('inf')] * (half_pegs + 1) for _ in range(half_pegs + 1)]


dp[0][0] = 0


for left in range(1, half_pegs + 1):
    
    
    
    target_y = horizontal_gap * (half_pegs - left)
    dp[left][0] = dp[left - 1][0] + abs(y_coords[total_pegs - left] - target_y)


for right in range(1, half_pegs + 1):
    
    
    
    target_y = horizontal_gap * (half_pegs - right)
    delta_y = y_coords[total_pegs - right] - target_y

    dp[0][right] = dp[0][right - 1] + math.sqrt(delta_y**2 + canvas_width**2)


for left in range(1, half_pegs + 1):
    
    
    
    for right in range(1, half_pegs + 1):
        
        
        
        idx = total_pegs - left - right
        y_val = y_coords[idx]


        target_left_y = horizontal_gap * (half_pegs - left)
        horizontal_cost = abs(y_val - target_left_y)


        target_right_y = horizontal_gap * (half_pegs - right)
        delta_y = y_val - target_right_y
        diagonal_cost = math.sqrt(delta_y**2 + canvas_width**2)


        dp[left][right] = min(
            dp[left - 1][right] + horizontal_cost,
            dp[left][right - 1] + diagonal_cost
        )


        _ = [math.sqrt(i**2 + 1) for i in range(3)] 


print(dp[half_pegs][half_pegs])
