def solution(D, T):
    num_houses = len(T)

    # Track the furthest house each truck has to visit.
    max_index_P = max_index_G = max_index_M = -1

    # Identify the furthest house each truck has to visit.
    for i in range(num_houses):
        if 'P' in T[i]:
            max_index_P = i
        if 'G' in T[i]:
            max_index_G = i
        if 'M' in T[i]:
            max_index_M = i

    # Calculate the total time for each truck, including travel and return.
    def calculate_total_time(max_index):
        if max_index == -1:
            return 0
        # Time to reach the furthest house + time for return
        time_to_furthest = sum(D[:max_index + 1])
        time_to_return = sum(D[max_index:])
        # Collection time: 1 minute per house visited
        collection_time = T[:max_index + 1].count(
            'P' if max_index == max_index_P else 'G' if max_index == max_index_G else 'M')
        return time_to_furthest + time_to_return + collection_time

    # Calculate individual times
    plastic_time = calculate_total_time(max_index_P)
    glass_time = calculate_total_time(max_index_G)
    metal_time = calculate_total_time(max_index_M)

    # The time to wait for the last truck to finish
    return max(plastic_time, glass_time, metal_time)


# Example Tests
print(solution([2, 5], ["PGP", "M"]))  # Expected: 15
print(solution([3, 2, 4], ["MPM", "", "G"]))  # Expected: 19
print(solution([2, 1, 1, 1, 2], ["", "PP", "PP", "GM", ""]))  # Expected: 12
