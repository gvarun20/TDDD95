#import heapq
#from collections import defaultdict
#
#def solve_fuel_problem():
#
#    n, m = map(int, input().split())
#    prices = list(map(int, input().split()))
#
#    graph = defaultdict(list)
#    for _ in range(m):
#        u, v, d = map(int, input().split())
#        graph[u].append((v, d))
#        graph[v].append((u, d))
#    
#
#    q = int(input())
#    for _ in range(q):
#        capacity, start, end = map(int, input().split())
#        result = find_cheapest_trip(graph, prices, capacity, start, end, n)
#        print(result)
#
#def find_cheapest_trip(graph, prices, capacity, start, end, n):
#
#    pq = [(0, start, 0)]  # Start with 0 fuel, 0 cost
#    
#
#    visited = {}
#    
#    while pq:
#        cost, city, fuel = heapq.heappop(pq)
#        
#
#        if city == end:
#            return cost
#        
#
#        if (city, fuel) in visited and visited[(city, fuel)] <= cost:
#            continue
#        visited[(city, fuel)] = cost
#
#        for buy_fuel in range(1, capacity - fuel + 1):
#            new_fuel = fuel + buy_fuel
#            new_cost = cost + prices[city] * buy_fuel
#            new_state = (city, new_fuel)
#            if new_state not in visited or visited[new_state] > new_cost:
#                heapq.heappush(pq, (new_cost, city, new_fuel))
#        
#
#        for next_city, distance in graph[city]:
#            if fuel >= distance:  # We have enough fuel
#                new_fuel = fuel - distance
#                new_cost = cost
#                new_state = (next_city, new_fuel)
#                if new_state not in visited or visited[new_state] > new_cost:
#                    heapq.heappush(pq, (new_cost, next_city, new_fuel))
#    
#    return "impossible"
#
#
#def test_case():
#    # Test input:
#    test_input = """5 5
#10 10 20 12 13
#0 1 9
#0 2 8
#1 2 1
#1 3 11
#2 3 7
#2
#10 0 3
#20 1 4"""
#    
#    lines = test_input.strip().split('\n')
#    idx = 0
#    
#    # Parse input
#    n, m = map(int, lines[idx].split())
#    idx += 1
#    prices = list(map(int, lines[idx].split()))
#    idx += 1
#    
#
#    graph = defaultdict(list)
#    for _ in range(m):
#        u, v, d = map(int, lines[idx].split())
#        graph[u].append((v, d))
#        graph[v].append((u, d))
#        idx += 1
#    
#
#    q = int(lines[idx])
#    idx += 1
#    
#    for _ in range(q):
#        capacity, start, end = map(int, lines[idx].split())
#        result = find_cheapest_trip(graph, prices, capacity, start, end, n)
#        print(result)
#        idx += 1
#
#
#
#
#if __name__ == "__main__":
#    test_case()














import heapq
from collections import defaultdict


"""

The number of cities (n), the number of highways (m), and fuel price 
in each one are the very first inputs that the program reads. At that,
it generates a graph without directions in which any path links a city at 
a specific length. Following its design, the computer performs a number in queries 
(q), all of which specifies the start and final cities as well as the fuel tank volume
for a vehicle.this  function tells about this.
It finds the shortest fuel cost necessary for each ask, take into consider the fuel 
tank's capacity limits, to get from your beginning city to a final area. To look into
several refuel methods while lowering expenses, this probably uses computer code or a 
formula like Dijkstra's . Each query's result is then created, showing either the smallest 
easy cost of travel or an entry stating that fuel rules limit the journey



"""







import heapq
from collections import defaultdict

def solve_fuel_problem():
    import sys
    
    
    
    
    
    
    
    
    
    input = sys.stdin.read
    data = input().split()
    idx = 0
    
    n, m = int(data[idx]), int(data[idx+1])
    idx += 2
    prices = list(map(int, data[idx:idx+n]))
    idx += n
    
    graph = defaultdict(list)
    for _ in range(m):
        
        
        
        
        
        
        
        
        
        u, v, d = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        graph[u].append((v, d))
        graph[v].append((u, d))
        idx += 3
    
    q = int(data[idx])
    idx += 1
    
    for _ in range(q):
        
        
        
        
        
        
        capacity, start, end = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        result = find_cheapest_trip(graph, prices, capacity, start, end, n)
        print(result)











def find_cheapest_trip(graph, prices, capacity, start, end, n):
    pq = []
    heapq.heappush(pq, (0, start, 0))
    visited = [[False] * (capacity + 1) for _ in range(n)]
    
    while pq:
        cost, city, fuel = heapq.heappop(pq)
        
        if city == end:
            return cost
        
        if visited[city][fuel]:
            continue
        
        visited[city][fuel] = True
        
        if fuel < capacity:
            
            
            
            
            
            
            
            
            
            new_cost = cost + prices[city]
            if not visited[city][fuel + 1]:
                heapq.heappush(pq, (new_cost, city, fuel + 1))
        
        for next_city, distance in graph[city]:
            
            
            
            
            
            
            
            if fuel >= distance:
                new_fuel = fuel - distance
                if not visited[next_city][new_fuel]:
                    heapq.heappush(pq, (cost, next_city, new_fuel))
    
    return "impossible"
    
    
    
    
    
    
    

if __name__ == "__main__":
    solve_fuel_problem()






































































































































































