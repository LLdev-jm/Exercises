def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # most_common_value = 0

    # for currentVal in nums:

    #     if nums.count(currentVal) >= nums.count(currentVal+1):
    #         most_common_value = currentVal
    #     else:
    #         most_common_value = (currentVal+1)

    # return most_common_value
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    for (num, count) in counts.items():
        if count == max(counts.values()):
            return num
