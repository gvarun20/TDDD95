"""
We have created a class called fenwickTree . I tried to use a function inside the class called init ,there we have created a list called tree we do a minor operation of changing the indexing from 0 to 1 ,because in python there is a default procedure of setting index to 0 but here we manually set it to 1.
Next is the least significant bit  where  we look into the number as binary ,for example in 6 its binary is 110 ,the LSB is the smallest power of 2 inside it . 


The main purpose of this program is two  things ,1.is to add numbers to a correct places in the list ,2.fastly find the sum of numbers from first to the certain place in the list.
The main method is the update ,this updates the tree by summing the value to specific index.so at first it starts to count from 1 .there is a loop until the end of the tree .
next it adds value to that particular position in the tree in the index.this is done when we need to constantly update and sum it.

Next method is the prefixsum , so we define the cumulative_sum to 0 and this will hold the sum as we move around the tree .
we have another loop here.since fenwick tree are
1 based index ,we go till we find the top,we constanlt accumulate the sum after this  the loop ends 
 
The main function : in this the adding value to certain place is this operation(+),and getting the sum of complete elements upto specific index(?)operation.

To allow for easier 1-based indexing, the FenwickTree class prepares an auxiliary array tree of size n+1.
The index’s least set bit is found by the method leastsignificantbit which guides how the tree structure leaps
while editing or searching. The tree nodes which depend on a specific index for subsequent prefix sums are
preserved and reflect a value added to them via the update function. The in prefixsum function you can retrieve
values by climbing backwards through the tree to retrieve the sum from 0 to the specified index.






Time complexity of this whole fenwick tree according to wiki is O(log(n))
the space complexity of the fenwick tree is O(n) 



I have used these reference for better understanding 
https://en.wikipedia.org/wiki/Fenwick_tree
https://cp-algorithms.com/data_structures/fenwick.html
"""




















import sys



class FenwickTree:
    def __init__(self, size: int) -> None:
        self.size = size + 1
        self.tree = [0] * (self.size)







    def _least_significant_bit(self, index: int) -> int:
        return index & -index









    def update(self, index: int, value: int) -> None:
        index += 1
        while index < self.size:
            self.tree[index] += value
            index += self._least_significant_bit(index)









    def prefix_sum(self, index: int) -> int:
        cumulative_sum = 0
        while index > 0:
            cumulative_sum += self.tree[index]
            index -= self._least_significant_bit(index)
        return cumulative_sum


def main():
    
    
    
    num_elements, num_queries = map(int, input().split())
    fenwick_tree = FenwickTree(num_elements)
    results = []



    for query in sys.stdin:
        parts = query.split()
        if parts[0] == '+':
            index = int(parts[1])
            value = int(parts[2])
            fenwick_tree.update(index, value)
        elif parts[0] == '?':
            index = int(parts[1])
            result = fenwick_tree.prefix_sum(index)
            results.append(str(result))






    print('\n'.join(results))










if __name__ == "__main__":
    main()#THIS MIGHT RUN
