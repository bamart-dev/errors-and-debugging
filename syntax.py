def map_character_frequency(words):
    char_map = {}   #* replaced ']' with '}'
    for word in words:    #* removed ()
        for character in word:    #* replaced 'on' with 'in'
            if character not in char_map:
                char_map[character] = 1    #* replaced '{}' with '[]'
            else:    #* corrected indentation (brought into scope with 'if')
                char_map[character] += 1    #* replaced '()' with '[]'
    return char_map

def test_map_character_frequency():
    colors = ["red", "orange"]
    char_map = map_character_frequency(colors)
    expected = {
        "r": 2,
        "e": 2,
        "d": 1,
        "o": 1,
        "a": 1,
        "n": 1,
        "g": 1,
    }
    assert char_map == expected

def syntax_errors():
    test_map_character_frequency()

#! Change List:
#* Line 2 - replaced ']' with '}'
#* Line 3 - removed '()' enclosing "word in words"
#* Line 4 - replaced "on" with "in"
#* Line 6 - replaced '{}' with '[]'
#* Line 7 - indented else two spaces to the right
#* Line 8 - replaced '()' with '[]'
