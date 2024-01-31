def majorityelement(array):
    # Step 1: Find a candidate for the majority element using Moore's Voting Algorithm
    candidate = None  # Initialize the candidate
    count = 0  # Initialize the count of the candidate

    # Iterate through the array
    for num in array:
        if count == 0:
            # If count is 0, set the current element as the candidate
            candidate = num
            count = 1
        elif num == candidate:
            # If the current element is equal to the candidate, increment the count
            count += 1
        else:
            # If the current element is different from the candidate, decrement the count
            count -= 1

    # Step 2: Check if the candidate is the majority element
    count_candidate = array.count(candidate)  # Count occurrences of the candidate in the array
    if count_candidate > len(array) // 2:
        # If the count of the candidate is greater than half the length of the array,
        # then it is the majority element
        return candidate
    else:
        # If there is no majority element, return None
        return None

# Example usage:
array = [3, 3, 4, 2, 4, 4, 2, 4, 4]
result = majorityelement(array)

if result is not None:
    print(f"The majority element is: {result}")
else:
    print("There is no majority element.")
