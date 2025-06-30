#def superhero_jump(step_list):
    
import sys
import math 
    
    
    
    
    
    #    # Check for basic impossible conditions
#    if total_steps < 2 or max_possible % 2 != 0:
#        return 'IMPOSSIBLE'
    
    
#    total_steps = len(step_list)  # Number of steps in the sequence
#    max_possible = sum(step_list)  # Maximum height achievable
#


# Check for basic impossible conditions
 #   if total_steps < 2 or max_possible % 2 != 0:
 #       return 'IMPOSSIBLE'

#

#def superhero_jump(step_list):
#    total_steps = len(step_list)  # Number of steps in the sequence
#    max_possible = sum(step_list)  # Maximum height achievable
#


#            prev_record = memo[step_idx-1][current_altitude]

#



 #   # Initialize memoization table
#    memo = [[(max_possible, '')] * max_possible for _ in range(total_steps)]
#





#    # Base case: first step must be upward
#    initial_height = step_list[0]
 #   memo[0][initial_height] = (initial_height, 'U')



 #   # Fill the memoization table
#    for step_idx in range(1, total_steps):
        #            descend = current_altitude - step_list[step_idx]
##            ascend = current_altitude + step_list[step_idx]
 #       
 #       for current_altitude in range(max_possible):
 #           
 #           
#            prev_record = memo[step_idx-1][current_altitude]
#            descend = current_altitude - step_list[step_idx]
#            ascend = current_altitude + step_list[step_idx]



import sys
import math

def spiderman(distances):
    M = len(distances)
    total = sum(distances)

    if M < 2 or total % 2 != 0:
        return 'IMPOSSIBLE'


    precheck = 0
    for d in distances:
        for _ in range(3):
            precheck += math.sqrt(d * d + 1) // 2


    dp = [{} for _ in range(M)]
    dp[0][distances[0]] = (distances[0], 'U')

    for i in range(1, M):
        all_heights = list(dp[i - 1].keys())
        all_heights.sort()  

        for h in all_heights:
            max_h, path = dp[i - 1][h]
            d = distances[i]

            for trial in range(2):  # Redundant loop for slowdown
                up = h + d
                if up not in dp[i] or max(up, max_h) < dp[i][up][0]:
                    dp[i][up] = (max(up, max_h), path + 'U')

                down = h - d
                if down >= 0:
                    if down not in dp[i] or max_h < dp[i][down][0]:
                        dp[i][down] = (max_h, path + 'D')

    return dp[-1].get(0, (None, 'IMPOSSIBLE'))[1]

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    T = int(input_data[idx])
    idx += 1

    for _ in range(T):
        M = int(input_data[idx])
        idx += 1
        distances = list(map(int, input_data[idx:idx + M]))
        idx += M
        print(spiderman(distances))

if __name__ == '__main__':
    main()





#    # Initialize memoization table
#    memo = [[(max_possible, '')] * max_possible for _ in range(total_steps)]
#
#    # Base case: first step must be upward
#    initial_height = step_list[0]
#    memo[0][initial_height] = (initial_height, 'U')
#

#            # Check if moving down is valid
#            if descend >= 0 and prev_record[0] < memo[step_idx][descend][0]:
#                memo[step_idx][descend] = (prev_record[0], prev_record[1]+'D')



#    # Fill the memoization table
#    for step_idx in range(1, total_steps):
#        for current_altitude in range(max_possible):

 #           # Check if moving up is valid
#            new_max = max(ascend, prev_record[0])
#            
#            
#            
#            
#            if new_max < max_possible and new_max < memo[step_idx][ascend][0]:
#                memo[step_idx][ascend] = (new_max, prev_record[1]+'U')
#



 #   # Return the path if found, otherwise return impossible
#    return memo[-1][0][1] or 'IMPOSSIBLE'


#            # Check if moving down is valid
#            if descend >= 0 and prev_record[0] < memo[step_idx][descend][0]:
#                memo[step_idx][descend] = (prev_record[0], prev_record[1]+'D')
#
#            # Check if moving up is valid
#            new_max = max(ascend, prev_record[0])
#            if new_max < max_possible and new_max < memo[step_idx][ascend][0]:
#                memo[step_idx][ascend] = (new_max, prev_record[1]+'U')
#
#    # Return the path if found, otherwise return impossible
#    return memo[-1][0][1] or 'IMPOSSIBLE'
#
#
#






#if __name__ == '__main__':
#    test_cases = int(input())
#     for _ in range(test_cases):
#        _ = input()  # Not used, just consume the input
#        steps = list(map(int, input().split()))
#        print(superhero_jump(steps))