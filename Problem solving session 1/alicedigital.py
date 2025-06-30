from collections import deque
import sys

def max_weight_subarray(n, m, array):
    max_weight = -1
    left = 0
    count_m = 0
    current_weight = 0
    min_queue = deque()  # Stores indices to track the min element efficiently

    for right in range(n):
        # Update count_m when m appears
        if array[right] == m:
            count_m += 1

        # Add use to the current element to the sum
        current_weight += array[right]

        # keep the this to min_queue in increasing order
        while min_queue and array[min_queue[-1]] > array[right]:
            min_queue.pop()
        min_queue.append(right)

        # make this less window if needed
        while count_m > 1 or (count_m == 1 and array[min_queue[0]] < m):
            if array[left] == m:
                count_m -= 1
            current_weight -= array[left]

            # Remove left element from min_queue if it goes out of window
            if min_queue and min_queue[0] == left:
                min_queue.popleft()
            
            left += 1

        # Check if this is the valid window
        if count_m == 1 and array[min_queue[0]] == m:
            max_weight = max(max_weight, current_weight)

    return max_weight

def main():# use this as the manin fuction
    input = sys.stdin.read
    data = input().split()
    idx = 0
    num_datasets = int(data[idx])
    idx += 1

    results = []
    for _ in range(num_datasets):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        array = list(map(int, data[idx:idx + n]))
        idx += n
        results.append(str(max_weight_subarray(n, m, array)))

    print("\n".join(results))

if __name__ == "__main__":
    main()#this might work
