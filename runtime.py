def get_3rd_value(my_list):
    if len(my_list) < 3:  #* added guard statement; returns None if list length
        return None       #* is less than 3 (as there would be no 3rd value).
    return my_list[2]

def test_get_3rd_value():
    assert get_3rd_value([0, 1, 2]) == 2
    assert get_3rd_value([0, 1]) == None

def get_last_value(my_list):
    item_count = len(my_list) - 1
    if not my_list:    #* added guard statement; returns None if list is empty.
        return None
    return my_list[item_count]  #* corrected misspelling of 'item_count'.

def test_get_last_value():
    assert get_last_value([0, 1, 2]) == 2
    assert get_last_value([0]) == 0
    assert get_last_value([]) == None

def runtime_errors():
    test_get_3rd_value()
    test_get_last_value()

#! Changes made:
#* Lines 2 & 3 - added if statement to check minimum list length
#* Lines 12 & 13 - added if statment to check if list is empty
#* Line 14 - corrected '[item_count]'
