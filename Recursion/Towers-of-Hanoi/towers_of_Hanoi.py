def towers_of_Hanoi(n, origin, destination, aux):
    # Base case: if there's only one disc, move it directly to the destination
    if n == 1:
        print("Move disc 1 from", origin, "to", destination)
        return # End the function for this call
    
    #  Recursive case: move the top n-1 disks from origin to aux using destination as a helper
    else:
        # Move the top n-1 disks to the auxiliary tower
        towers_of_Hanoi(n-1, origin, aux, destination)
        print(f"Move disc {n} from {origin} to {destination}")
        # Move the n-1 disks from aux to destination using origin as a helper
        towers_of_Hanoi(n-1, aux, destination, origin)

# Start the Towers of Hanoi solution with the specified number of disks
n = 3
towers_of_Hanoi(n, 'A', 'B', 'C')
    
