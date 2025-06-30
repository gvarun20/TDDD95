import sys


"""The main implementation is about the greedy algorithm to solve the problem.

The first function is the sort_interval. I have used the built-in sorted function because it is fast, 
I tried to hardcode the same thing but it did not run within the time limit. It sends out the list of indices from zero to the complete
length of the interval after this it sorts it based on the matching interval.

The next function is the select_intervals. The variable selected_indices stores the indices of the chosen interval.
The sorted_indices holds the provided intervals sorted by the above function. There is a variable to track the specific position in the target range. 
If there is a single-point target range the function checks if there is any point that covers. 
If present it returns the index of the interval or else it is an empty list.
The loop continues until the current_posthe internal loop looks for all intervals that start from the current position, 
it gradually updates the best_choise


If we look at the algorithm, the solution uses the greedy plan which goes until the optimal selection at each and every stage looking for global optimum. 

It sorts intervals by the very starting point. It repeats at every selected interval from the current position to the farthest possible. 
It does it continuously until the target range is looked at or no more is available.
 

The time complexity of the sorting operation is O(nlogn)and for selecting interval is O(nlogn).

The space complexity for this is O(n)this includes storing intervals, sorted indices, and selected indices.

"""
#def select_intervals(range_needed, available_intervals):
#    selected_indices = []
#    
#    # Sort intervals by their start point
#    sorted_indices = sorted(range(len(available_intervals)), key=lambda idx: available_intervals[idx])
#    







#    current_pos = range_needed[0]
#    check_index = 0
#
#    # Keep selecting intervals until we cover the target range
#    while current_pos < range_needed[1] or not selected_indices:
#        best_choice = (current_pos, -1)
#
#        # Find the interval that starts before or at current_pos and ends farthest to the right
#        while check_index < len(available_intervals) and available_intervals[sorted_indices[check_index]][0] <= current_pos:
#            interval_end = available_intervals[sorted_indices[check_index]][1]
#            interval_index = sorted_indices[check_index]
#            best_choice = max(best_choice, (interval_end, interval_index))
#            check_index += 1
#
#        # No valid interval found
#        if best_choice[1] == -1:
#            return []
#
#        current_pos = best_choice[0]
#        selected_indices.append(best_choice[1])
#
#    return selected_indices

# Initialize the input handling
#target_range = (0.0, 0.0)
#total_intervals = 0
#interval_list = []



import sys

def sort_intervals(intervals):
    
    
    
    
     return sorted(range(len(intervals)), key=lambda i: intervals[i])

def select_intervals(range_needed, available_intervals):
    
    
    selected_indices = []
    sorted_indices = sort_intervals(available_intervals)
    current_pos = range_needed[0]
    check_index = 0

    
    if range_needed[0] == range_needed[1]:
        
        
        for idx in sorted_indices:
            
            
            
            
            if (available_intervals[idx][0] <= range_needed[0] and 
                available_intervals[idx][1] >= range_needed[1]):
                    
                    
                return [idx]
        return []

    while current_pos < range_needed[1]:
        best_choice = (current_pos, -1)
        
        
        
        while (check_index < len(available_intervals) and available_intervals[sorted_indices[check_index]][0] <= current_pos):
            
            
            
            interval_end = available_intervals[sorted_indices[check_index]][1]
            interval_index = sorted_indices[check_index]
            best_choice = max(best_choice, (interval_end, interval_index))
            check_index += 1

        if best_choice[1] == -1:
            return []

        current_pos = best_choice[0]
        selected_indices.append(best_choice[1])

    return selected_indices

def main():
    
    
    
    
    
    
    
    
    
    
    
    target_range = (0.0, 0.0)
    total_intervals = 0
    interval_list = []
    
    
    
    
    
    
    
    
    
    
    
    
    

    for line in sys.stdin:
        line = line.strip()
        
        
        if not line:
            continue

        if total_intervals == 0 and target_range == (0.0, 0.0):
            start, end = map(float, line.split())
            target_range = (start, end)
        elif target_range != (0.0, 0.0) and total_intervals == 0:
            total_intervals = int(line)
        else:
            
            
            
            
            
            
            
            
            
            a, b = map(float, line.split())
            interval_list.append((a, b))
            total_intervals -= 1

            if total_intervals == 0:
                result = select_intervals(target_range, interval_list)
                
                
                if not result:
                    print("impossible")
                else:
                    print(len(result))
                    print(" ".join(map(str, result)))

                target_range = (0.0, 0.0)
                interval_list = []

if __name__ == "__main__":
    main()

#def select_intervals(range_needed, available_intervals):
#    selected_indices = []
#    
#    # Sort intervals by their start point
#    sorted_indices = sorted(range(len(available_intervals)), key=lambda idx: available_intervals[idx])
#    
#    current_pos = range_needed[0]
#    check_index = 0









#        # No valid interval found
#        if best_choice[1] == -1:
#            return []
#
#        current_pos = best_choice[0]
#        selected_indices.append(best_choice[1])
#
#    return selected_indices

# Initialize the input handling
#target_range = (0.0, 0.0)
#total_intervals = 0
#interval_list = []

#
#        # No valid interval found
#        if best_choice[1] == -1:
#            return []
#
#        current_pos = best_choice[0]
#        selected_indices.append(best_choice[1])
#
#    return selected_indices

# Initialize the input handling
#target_range = (0.0, 0.0)
#total_intervals = 0
#interval_list = []



 # Once all intervals are read, compute and print result
#        if total_intervals == 0:
#            result_indices = select_intervals(target_range, interval_list)
#
#            if not result_indices:
#                print("impossible")
#            else:
#                print(len(result_indices))
#                print(" ".join(str(index) for index in result_indices))
#























































#for input_line in sys.stdin:
#    input_line = input_line.strip()
#
#    # First line with target range
#    if total_intervals == 0 and target_range == (0.0, 0.0):
#        start_point, end_point = map(float, input_line.split())
#        target_range = (start_point, end_point)
#
#    # Second line with number of intervals
#    elif target_range != (0.0, 0.0) and total_intervals == 0:
#        total_intervals = int(input_line)
#
#    # Reading the actual intervals
#    else:
#        interval_start, interval_end = map(float, input_line.split())
#        interval_list.append((interval_start, interval_end))
#        total_intervals -= 1
#
#        # Once all intervals are read, compute and print result
#        if total_intervals == 0:
#            result_indices = select_intervals(target_range, interval_list)
#
#            if not result_indices:
#                print("impossible")
#            else:
#                print(len(result_indices))
#                print(" ".join(str(index) for index in result_indices))
#
#            # Reset for next input block
#            target_range = (0.0, 0.0)
#            interval_list = []
