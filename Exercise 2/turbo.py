import sys

def turbo_sort(arr):
    n = len(arr)
    swaps = []
    left = 0
    right = n - 1
    current_swap_count = 0

    for i in range(n):
        if i % 2 == 0:
            # Move the smallest remaining element to its correct position
            target = left
            current = arr.index(min(arr[left:right+1]), left)
        else:
            # Move the largest remaining element to its correct position
            target = right
            current = arr.index(max(arr[left:right+1]), left)

        # Count the number of swaps to move the element to the target position
        while current != target:
            if current < target:
                arr[current], arr[current + 1] = arr[current + 1], arr[current]
                current += 1
            else:
                arr[current], arr[current - 1] = arr[current - 1], arr[current]
                current -= 1
            current_swap_count += 1

        if i % 2 == 0:
            left += 1
        else:
            right -= 1

        swaps.append(current_swap_count)
        current_swap_count = 0

    return swaps

def main():
    input = sys.stdin.read().split()
    N = int(input[0])
    arr = list(map(int, input[1:N+1]))
    swaps = turbo_sort(arr)
    for s in swaps:
        print(s)

if __name__ == "__main__":
    main()