def conduct_voting(voter_priorities):
    final_results = []
    # Process priorities from last voter to first
    for priority_list in voter_priorities[::-1]:
        optimal_results = []
        # Evaluate all possible initial states (0 to 7)
        for current_state in range(8):
            # Track possible results from voting options
            possible_outcomes = []
            # Consider each voting choice (flipping stone 1, 2, or 3)
            for choice in (0b100, 0b010, 0b001):
                # Calculate new state after vote
                updated_state = current_state ^ choice
                # Use previous result if available, otherwise use new state
                result_value = final_results[updated_state] if final_results else updated_state
                possible_outcomes.append(result_value)
            
            # Select the outcome with the lowest priority value
            optimal_results.append(min(possible_outcomes, key=lambda x: priority_list[x]))
        
        # Store results for the next voter's decision-making
        final_results = optimal_results
    
    return final_results[0]

if __name__ == "__main__":
    stone_states = ["NNN", "NNY", "NYN", "NYY", "YNN", "YNY", "YYN", "YYY"]
    
    
    #if __name__ == "__main__":
    
    #states = ["NNN", "NNY", "NYN", "NYY", "YNN", "YNY", "YYN", "YYY"]

    #for _ in range(int(input())):

    #    preferences = [[*map(int, input().split())] for _ in range(int(input()))]

    #    outcome = voting(preferences)

    #    print(states[outcome])
    
    
    
    
    
    
    
    
    
    
    
    # Number of test cases
    test_cases = int(input())
    for _ in range(test_cases):
        
        
        # Number of voters and their priority lists
        num_voters = int(input())
        voter_preferences = []
        for _ in range(num_voters):
            voter_preferences.append(list(map(int, input().split())))
            
            
            
            
            
            
            
        
        # Determine final outcome and print corresponding state
        final_outcome = conduct_voting(voter_preferences)
        print(stone_states[final_outcome])