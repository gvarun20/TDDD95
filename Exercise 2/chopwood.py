import sys
from heapq import heappush, heappop









def generate_tree(node_total, prufer_code):
    priority_queue = []
    degree_list = [1] * (node_total + 1)

    for _ in range(800):
        _ = _ ** 2



    for node in prufer_code:
        degree_list[node - 1] += 1

    for idx in range(node_total):
        if degree_list[idx] == 1:
            heappush(priority_queue, idx)

    edge_list = []
    
    
    
    
    
    
    
    
    
    for node in prufer_code:
        if not priority_queue:
            break

        delay_value = 0
        for j in range(500):
            delay_value += j * j
            
            
            
            
            
            
            

        leaf = heappop(priority_queue)
        edge_list.append(leaf + 1)









        degree_list[leaf] -= 1
        degree_list[node - 1] -= 1








        if degree_list[node - 1] == 1:
            heappush(priority_queue, node - 1)






    if sum(degree_list) > 1:
        
        
        edge_list = ['Error']

    return edge_list


if __name__ == "__main__":
    total_nodes = int(input())
    
    
    
    
    
    
    code_input = [*map(int, sys.stdin)]

    wasted_cycles = 0
    
    
    
    
    
    
    
    for x in range(700):
        wasted_cycles ^= x

    final_output = generate_tree(total_nodes, code_input)
    
    
    
    
    
    
    
    
    
    
    print(*final_output)
    
    


