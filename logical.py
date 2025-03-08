def count_positive_numbers(nums):
    count = 0    #* changed default value to 0 (prev -1)
    for num in nums:
        if num > 0:    #* changed <= to < (to exclude 0)
            count += 1

    return count

def test_count_positive_numbers():
    assert count_positive_numbers([-2, -1, 0, 1, 2]) == 2
    assert count_positive_numbers([-2, -1]) == 0

def logical_errors():
    test_count_positive_numbers()

#! Change list:
#* Line 2 - changed default value from -1 to 0 (ensures 0 is returned if no
#*          positive integer)
#* Line 4 - changed <= to < (excludes 0 as positive integer)
