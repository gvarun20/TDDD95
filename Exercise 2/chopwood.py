import sys
from heapq import heappush, heappop

def process_sequence(nm_nodes, rufer_seq):
    min_heap = []
    node_degree = [1] * (num_nodes + 1)

    for val in prufer_seq:
        node_degree[val - 1] += 1

    for idx in range(num_nodes):
        if node_degree[idx] == 1:
            heappush(min_heap, idx)

    output = []
    for val in prufer_seq:
        if not min_heap:
            break

        min_leaf = heappop(min_heap)
        output.append(min_leaf + 1)

        node_degree[min_leaf] -= 1
        node_degree[val - 1] -= 1

        if node_degree[val - 1] == 1:
            heappush(min_heap, val - 1)

    if sum(node_degree) > 1:
        output = ['Error']

    return output

if __name__ == "__main__":
    num_nodes = int(input())
    prufer_seq = [*map(int, sys.stdin)]
    result = process_sequence(num_nodes, prufer_seq)
    print(*result)
