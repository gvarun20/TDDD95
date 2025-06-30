"""I have created a class called union find, under this, I have made a constructor and it has self and n.n tells the elements and rank and parent are with self .element in parent is its own parent, and rank is used to connect small tree with the large tree

Next the find function finds the root using the path compression. I have read some approach and tried to implement the same.

The next is the union method, what is does is at first it combines both the x and y set. And finds the root of it Then comes the if condition where they are in the same set, and no changes happen, else it fixes the smaller rank to the bigger tree. There is another scenario in both the rank are equal it selects the root and changes the rank by 1.

The next function is the connected method it looks out for x,y are in same set by comparing the root. It passes true if fixed or else it is false.

the main outline what I see in this problem statement is to correctly manage and groups of joined elements. It does 2 main things union and find , union is merge group, and find is to look out for two element in same group. I have used path compression from what I got from references wht it does is to fastly find operation and union rank to make the tree balance.
It reads = as union and ? as check. the final output of this will be either yes or no  , based on the two-element are connected  


Time complexity:: for the find, function might be O(a(n)), for the union function, it might be O(a(n)), and for the connected function, it could be O(a(n)).

n here  is the complete  number of elements in the set and a is the inverse Ackermann function

I have used these as a reference for my understanding.
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
https://www.tutorialspoint.com/union-by-rank-and-path-compression-in-union-find-algorithm
https://cp-algorithms.com/data_structures/disjoint_set_union.html



"""



class UnionFind:
    
      
    def __init__(self, n):
        self.parent = list(range(n))  # Each element is its own parent initially
        self.rank = [1] * n  # Rank array for union by rank optimization
    
    
    
    
    
    
    
    
    
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    
    
    
    
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
    
    
    
    
    
    
    
    
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)


import sys
input = sys.stdin.read



def main():
    data = input().split('\n')
    n, q = map(int, data[0].split())
    uf = UnionFind(n)
    

    
    
    result = []
    for i in range(1, q + 1):
        if not data[i]:
            continue
        op, a, b = data[i].split()
        a, b = int(a), int(b)
        
        if op == "=":
            uf.union(a, b)
        elif op == "?":
            result.append("yes" if uf.connected(a, b) else "no")
    
    sys.stdout.write("\n".join(result) + "\n")









if __name__ == "__main__":
    main()
