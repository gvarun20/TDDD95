import sys

num = int(input())

length, width = map(int, input().split())

values = []

for line in sys.stdin:
    values.append(int(line))

values.sort()

dp_table = []

segment_length = length / (num // 2 - 1)

for x in range(num // 2 + 1):
    dp_table.append([10**9] * (num // 2 + 1))

dp_table[0][0] = 0

for x in range(1, num // 2 + 1):
    dp_table[x][0] = dp_table[x - 1][0] + abs(values[num - x] - segment_length * (num // 2 - x))
    dp_table[0][x] = dp_table[0][x - 1] + ((values[num - x] - segment_length * (num // 2 - x))**2 + width**2)**0.5

for x in range(1, num // 2 + 1):
    for y in range(1, num // 2 + 1):
        dp_table[x][y] = min(
            dp_table[x - 1][y] + abs(values[num - x - y] - segment_length * (num // 2 - x)),
            dp_table[x][y - 1] + ((values[num - x - y] - segment_length * (num // 2 - y))**2 + width**2)**0.5
        )

print(dp_table[-1][-1])
