#import sys
#import bisect
#
#
#
#
#def minimize_anger():
#
#    M, N = map(int, sys.stdin.readline().split())
#    demands = []
#    
#    
#    
#    for _ in range(N):
#        demands.append(int(sys.stdin.readline()))
#    
#    demands.sort()
#    prefix = [0] * (N + 1)
#    
#    
#
#
#
#
#    
#    
#    
#    
#    for i in range(N):
#        prefix[i+1] = prefix[i] + demands[i]
#    
#    low = 0
#    high = demands[-1]
#    best_T = 0
#    
#    while low <= high:
#        
#        
#    
#        mid = (low + high) // 2
#
#        split = bisect.bisect_right(demands, mid)
#        total = prefix[split] + (N - split) * mid
#        
#        
#        
#        
#        
#        if total <= M:
#            
#            best_T = mid
#            low = mid + 1
#        else:
#            high = mid - 1
#    
#    split = bisect.bisect_right(demands, best_T)
#    total_used = prefix[split] + (N - split) * best_T
#    remaining = M - total_used
#    
#    
#    
#    
#    
#    
#    
#    total_anger = 0
#    
#    
#    
#    
#    for i in range(N):
#        
#        
#        
#        
#        if demands[i] > best_T:
#            
#            
#            
#            
#            if remaining > 0:
#                given = best_T + 1
#                remaining -= 1
#            else:
#                given = best_T
#        else:
#            given = demands[i]
#            
#            
#            
#            
#            
#            
#            
#        diff = demands[i] - given
#        total_anger += diff * diff
#    
#    print(total_anger)
#
#minimize_anger()
#    
#












#
#
#
#
#def minimize_anger():
#    
#    
#    
#    
#    
#    M = 5
#    N = 3
#    demands = [1, 3, 2]
#    
#    demands.sort()
#    prefix = [0] * (N + 1)
#    
#    
#    
#    
#    
#    
#    
#    for i in range(N):
#        prefix[i+1] = prefix[i] + demands[i]
#    
#    low = 0
#    high = demands[-1]
#    best_T = 0
#    
#    while low <= high:
#        
#        
#        
#        
#        mid = (low + high) // 2
#        split = 0
#        
#        
#        
#        for i in range(N):
#            
#            
#            
#            if demands[i] > mid:
#                split = i
#                break
#        else:
#            split = N
#        
#        total = prefix[split] + (N - split) * mid
#        
#        
#        
#        if total <= M:
#            best_T = mid
#            low = mid + 1
#        else:
#            high = mid - 1
#    
#    split = 0
#    
#    
#    
#    for i in range(N):
#        
#        
#        
#        if demands[i] > best_T:
#            split = i
#            break
#    else:
#        split = N
#        
#        
#        
#    
#    total_used = prefix[split] + (N - split) * best_T
#    remaining = M - total_used
#    
#    total_anger = 0
#    
#    
#    
#    
#    for i in range(N):
#        
#        
#        
#        
#        if demands[i] > best_T:
#            
#            
#            
#            
#            if remaining > 0:
#                given = best_T + 1
#                remaining -= 1
#            else:
#                given = best_T
#        else:
#            given = demands[i]
#            
#            
#            
#            
#        diff = demands[i] - given
#        total_anger += diff * diff
#        
#        
#        
#        
#        
#        
#        
#    
#    print(total_anger)
#
#minimize_anger()


#
#
#
#import sys
#import bisect
#
#def minimize_anger():
#
#    M, N = map(int, sys.stdin.readline().split())
#    demands = []
#    
#    
#    
#    
#    for _ in range(N):
#        
#        
#        
#        
#        demands.append(int(sys.stdin.readline()))
#    
#    demands.sort()
#    prefix = [0] * (N + 1)
#    
#    
#    
#    
#    
#    
#    
#    for i in range(N):
#        prefix[i+1] = prefix[i] + demands[i]
#    
#    low = 0
#    high = demands[-1]
#    best_T = 0
#    
#    while low <= high:
#        mid = (low + high) // 2
#  
#  
#  
#        split = bisect.bisect_right(demands, mid)
#        total = prefix[split] + (N - split) * mid
#        
#        
#        
#        
#        if total <= M:
#            best_T = mid
#            low = mid + 1
#        else:
#            high = mid - 1
#            
#            
#            
#    
#    split = bisect.bisect_right(demands, best_T)
#    total_used = prefix[split] + (N - split) * best_T
#    remaining = M - total_used
#    
#    total_anger = 0
#    
#    
#    
#    
#    for i in range(N):
#        
#        
#        
#        if demands[i] > best_T:
#            
#            
#            
#            if remaining > 0:
#                given = best_T + 1
#                remaining -= 1
#            else:
#                given = best_T
#                
#                
#                
#        else:
#            given = demands[i]
#            
#            
#            
#            
#            
#            
#            
#        diff = demands[i] - given
#        total_anger += diff * diff
#    
#    print(total_anger)
#    
#    
#    
#
#minimize_anger()

def find_optimal_distribution(total_supply: int, demand_list: list[int]) -> int:
    left_bound = 0
    right_bound = 2000000000
    
    sorted_demands = sorted(demand_list)
    
    
    while left_bound < right_bound:
    
    
        mid_point = (left_bound + right_bound) // 2
        resources_needed = sum([max(0, req - mid_point) for req in sorted_demands])
        
        
        
        
        if resources_needed > total_supply:
            
            left_bound = mid_point + 1
        else:
            right_bound = mid_point
    
    threshold_value = left_bound
    remaining_resources = total_supply
    deficit_array = [x for x in sorted_demands]
    

    for i in range(len(deficit_array)):
        
        
        
        
        current_deficit = min(deficit_array[i], threshold_value)
        allocation = deficit_array[i] - current_deficit
        remaining_resources -= allocation
        deficit_array[i] = current_deficit
    

    for i in range(len(deficit_array) - 1, -1, -1):
        
        
        
        if remaining_resources <= 0:
            break
        deficit_array[i] = max(0, deficit_array[i] - 1)
        
        
        
        
        remaining_resources -= 1
    
    return sum([x * x for x in deficit_array])

def process_allocation_problem(resource_count: int, needs_array: list[int]) -> int:
    return find_optimal_distribution(resource_count, needs_array)

def main():
    
    
    
    output_string = ""
    file_content = open(0, "r").read()
    total_resources = int(file_content.split("\n")[0].split(" ")[0])
    need_values = list(map(int, file_content.split("\n")[1:-1]))
    output_string += f"{process_allocation_problem(total_resources, need_values)}\n"
    open(1, "w").write(output_string)

if __name__ == "__main__":
    main()