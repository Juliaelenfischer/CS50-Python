import um

def test_single_um():
    assert um.count("hello um world") == 1

def test_multiple_um():
    assert um.count("um um um") == 3

def test_um_in_words():
    assert um.count("humble") == 0

def test_um_with_punctuation():
    assert um.count("um, um!") == 2
