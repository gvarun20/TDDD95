width, height = map(int, input().split())












maze = [list(input()) for _ in range(height)]








positions = [(row, col) for row in range(height) for col in range(width) if maze[row][col] == 'P']

treasure_count = 0





while positions:
    row, col = positions.pop()

    # Skip if we hit a wall
    if maze[row][col] == '#': continue

    # Add to treasure total if we find some
    if maze[row][col] == 'G': treasure_count += 1

    # Mark this spot as visited by making it a wall
    
#def gold(n):
#    """Generate a set of 2^n +1 Gold Codes
#    """
#    n = int(n)
#    if not n in preferred_pairs:
#        raise ss.Error('preferred pairs for %s bits unknown' % str(n))
#    seed = list(numpy.ones(n))
#    seq1 = mls.lfsr(preferred_pairs[n][0], seed)
#    seq2 = mls.lfsr(preferred_pairs[n][1], seed)
#    return gen_gold(seq1, seq2)
 
    
    maze[row][col] = '#'

    # Check all four adjacent spots
    adjacent = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    
    
    
    
    
    
    
    

    # If no hazards nearby, add all adjacent spots to explore
    if all(maze[nr][nc] != 'T' for nr, nc in adjacent): positions += adjacent

print(treasure_count)




#if __name__ == '__main__':
#    import sys
#    main(sys.argv[1] if len(sys.argv) > 1 else None)