import math
from itertools import combinations
from collections import defaultdict

def distance(p1, p2):
    """3D Euclidean distance."""
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def find(parent, x):
    """Find with path compression."""
    if parent[x] != x:  
        parent[x] = find(parent, parent[x])
    return parent[x]

def solve_part1(filename, num_pairs=1000, verbose=False):
    """Solve Part 1: Process num_pairs closest pairs."""
    # Read boxes
    with open(filename) as f:
        boxes = [tuple(map(int, line.strip().split(','))) for line in f]
    
    n = len(boxes)
    if verbose:
        print(f"📦 Loaded {n} junction boxes")
    
    # Calculate and sort all distances
    if verbose:
        print(f"🔢 Calculating {n * (n-1) // 2} pairwise distances...")
    
    distances = sorted(
        (distance(boxes[i], boxes[j]), i, j)
        for i, j in combinations(range(n), 2)
    )
    
    if verbose:  
        print(f"✅ Sorted!  Closest pair:  boxes {distances[0][1]} and {distances[0][2]}, distance = {distances[0][0]:.2f}")
        print(f"🔗 Processing the {num_pairs} closest pairs.. .\n")
    
    # Union-Find setup
    parent = list(range(n))
    size = [1] * n
    
    # Process the num_pairs closest pairs
    connections_made = 0
    skipped = 0
    
    for pair_idx in range(min(num_pairs, len(distances))):
        dist, i, j = distances[pair_idx]
        
        # Find roots
        root_i, root_j = find(parent, i), find(parent, j)
        
        if root_i != root_j:  
            # Different circuits - connect them! 
            # Merge (union by size)
            if size[root_i] < size[root_j]:   
                root_i, root_j = root_j, root_i
            
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            connections_made += 1
            
            if verbose and (connections_made <= 10 or connections_made % 100 == 0):
                print(f"  Pair {pair_idx+1}: Connection #{connections_made}: Box {i} ↔ Box {j} (dist: {dist:.2f})")
        else:  
            # Already in same circuit - skip
            skipped += 1
            if verbose and pair_idx < 20: 
                print(f"  Pair {pair_idx+1}: Box {i} and {j} already connected - SKIP")
    
    if verbose:  
        print(f"\n✓ Processed {num_pairs} pairs:")
        print(f"  - Made {connections_made} connections")
        print(f"  - Skipped {skipped} (already connected)")
    
    # Get circuit sizes
    circuits = defaultdict(int)
    for i in range(n):
        circuits[find(parent, i)] += 1
    
    circuit_sizes = sorted(circuits.values(), reverse=True)
    
    if verbose:
        print(f"⚡ Total circuits: {len(circuit_sizes)}")
        print(f"📊 Top 20 circuit sizes: {circuit_sizes[:20]}")
    
    # Return product of three largest
    if len(circuit_sizes) < 3:
        if verbose:  
            print(f"⚠️ Only {len(circuit_sizes)} circuit(s), padding with 1s for calculation")
        while len(circuit_sizes) < 3:
            circuit_sizes. append(1)
    
    top_three = circuit_sizes[:3]
    result = math.prod(top_three)
    
    if verbose:  
        print(f"\n🎯 Three largest:  {top_three}")
        print(f"✨ Answer: {' × '.join(map(str, top_three))} = {result}")
    
    return result

def solve_part2(filename, verbose=False):
    """Solve Part 2: Connect until all boxes are in one circuit."""
    # Read boxes
    with open(filename) as f:
        boxes = [tuple(map(int, line. strip().split(','))) for line in f]
    
    n = len(boxes)
    if verbose:
        print(f"📦 Loaded {n} junction boxes")
    
    # Calculate and sort all distances
    if verbose:
        print(f"🔢 Calculating {n * (n-1) // 2} pairwise distances...")
    
    distances = sorted(
        (distance(boxes[i], boxes[j]), i, j)
        for i, j in combinations(range(n), 2)
    )
    
    if verbose:  
        print(f"✅ Sorted!")
        print(f"🔗 Connecting until all boxes are in one circuit.. .\n")
    
    # Union-Find setup
    parent = list(range(n))
    size = [1] * n
    
    # Track number of separate circuits
    num_circuits = n
    
    # Connect pairs until everything is in one circuit
    connections_made = 0
    last_connection = None
    
    for pair_idx, (dist, i, j) in enumerate(distances):
        # Find roots
        root_i, root_j = find(parent, i), find(parent, j)
        
        if root_i != root_j:  
            # Different circuits - connect them! 
            # Merge (union by size)
            if size[root_i] < size[root_j]:   
                root_i, root_j = root_j, root_i
            
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            connections_made += 1
            num_circuits -= 1  # Two circuits merged into one
            
            # Save this connection
            last_connection = (i, j, dist)
            
            if verbose and (connections_made <= 10 or connections_made % 100 == 0):
                print(f"  Connection #{connections_made}:  Box {i} ↔ Box {j} (dist: {dist:.2f}) - {num_circuits} circuits remaining")
            
            # Stop when everything is in one circuit
            if num_circuits == 1:
                if verbose:
                    print(f"\n✓ All boxes connected into one circuit!")
                    print(f"  Last connection: Box {i} ({boxes[i]}) ↔ Box {j} ({boxes[j]})")
                    print(f"  Distance:  {dist:.2f}")
                break
    
    # Calculate answer:  multiply X coordinates
    if last_connection:
        i, j, dist = last_connection
        x1, y1, z1 = boxes[i]
        x2, y2, z2 = boxes[j]
        result = x1 * x2
        
        if verbose:
            print(f"\n🎯 Last connection details:")
            print(f"  Box {i}:  ({x1}, {y1}, {z1})")
            print(f"  Box {j}:  ({x2}, {y2}, {z2})")
            print(f"  X coordinates: {x1} × {x2} = {result}")
        
        return result
    else: 
        if verbose:
            print("❌ Error: No connection made!")
        return None

if __name__ == "__main__":     
    print("="*60)
    print("🎄 JUNCTION BOX CIRCUIT SOLVER")
    print("="*60)
    
    # Part 1
    print("\n" + "="*60)
    print("PART 1: Process 1000 closest pairs")
    print("-"*60)
    answer1 = solve_part1("input.txt", 1000, verbose=True)
    print("\n" + "="*60)
    print(f"🎁 PART 1 ANSWER: {answer1}")
    print("="*60)
    
    # Part 2
    print("\n" + "="*60)
    print("PART 2: Connect until all in one circuit")
    print("-"*60)
    answer2 = solve_part2("input.txt", verbose=True)
    print("\n" + "="*60)
    print(f"🎁 PART 2 ANSWER: {answer2}")
    print("="*60)