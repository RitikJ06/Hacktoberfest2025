def tower_of_hanoi(n, source, auxiliary, destination):
    """
    Solves the Tower of Hanoi problem recursively.
    
    n: Number of disks
    source: The starting rod
    auxiliary: The helper rod
    destination: The target rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} -> {destination}")
        return
    # Move top n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Move the largest disk to destination
    print(f"Move disk {n} from {source} -> {destination}")
    
    # Move the n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination)


# Example usage:
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'B', 'C')
