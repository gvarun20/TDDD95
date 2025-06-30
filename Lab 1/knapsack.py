import sys

""" Within weight limit w, the greatest profit that may be made with the first i items 
is stored in the DP table dp_table[i][w]. Backtracking is used to identify the components 
that contribute to the best solution after the table has been constructed. 
After reading the input from sys.stdin, the first line displays the maximum weight and 
number of items, followed by lines with the weight and profit of each item. The output 
includes the number of items that were chosen as well as their indexes. 
With this method, the 0/1 Knapsack problem is effectively resolved by calculating the 
highest profit and then going back to locate the chosen pieces.
"""

"""
This code solves the 0-1 Knapsack Problem using Dynamic Programming. 
It reads input values for the maximum weight, number of items, and each item's profit
and weight. It constructs a DP table to store the maximum profit for each weight and 
item combination, filling it in O(max_weight * item_count) time. The memory complexity 
is also O(max_weight * item_count) due to the 2D DP table. Finally, it backtracks to 
determine the selected items. The algorithm is efficient for moderate inputs but may 
struggle with very large values due to its polynomial time and space complexity.
"""










def read_input():
    """
    Read a line of input and split it into an integer tuple.
    This function is used to read the maximum weight, item count, and item details.
    """
    return tuple(int(x) for x in sys.stdin.readline().split())












def solve_knapsack(max_weight, item_count, profit_values, item_weights):
    dp_table = [[0] * (max_weight + 1) for _ in range(item_count + 1)]

    for item_idx in range(item_count):
        for weight in range(1, max_weight + 1):
            if item_weights[item_idx] <= weight:
                dp_table[item_idx + 1][weight] = max(
                    dp_table[item_idx][weight - item_weights[item_idx]] + profit_values[item_idx],
                    dp_table[item_idx][weight]
                )
            else:
                dp_table[item_idx + 1][weight] = dp_table[item_idx][weight]












    selected_items = []
    remaining_weight = max_weight

    while item_count > 0:
      
      
      
      
      
      
        if dp_table[item_count][remaining_weight] > dp_table[item_count - 1][remaining_weight]:
            selected_items.append(item_count - 1)
            remaining_weight -= item_weights[item_count - 1]
        item_count -= 1

    return selected_items[::-1]



















"""
Solve the 0-1 knapsack problem using dynamic programming.

Args:
    max_weight (int): Maximum weight the knapsack can hold.
    item_count (int): Number of items available.
    profit_values (list): List of profit values for each item.
    item_weights (list): List of weights for each item.

Returns:
    list: Indices of the selected items that maximize profit without 
          exceeding max_weight.
"""

















if __name__ == "__main__":
    while (input_pair := read_input()):
        max_weight, item_count = input_pair
        profit_values, item_weights = zip(*[read_input() for _ in range(item_count)])
        chosen_items = solve_knapsack(max_weight, item_count, profit_values, item_weights)
        print(len(chosen_items))
        print(' '.join(str(idx) for idx in chosen_items))
