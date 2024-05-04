from plates import is_valid

def test_beginning_alphabetical():
    assert is_valid("JK2049") == True
    assert is_valid("golazo") == True

def test_length():
    assert is_valid("LongEnough") == False
    assert is_valid("x") == False

def test_num_placement():
    assert is_valid("ab99cd") == False
    assert is_valid("cs10p") == False

def test_zero_placement():
    assert is_valid("ab0999") == False
    assert is_valid("xy142z") == False

def test_alphanumeric_characters():
    assert is_valid("xy,.&!") == False
    assert is_valid("xy <42>") == False

def test_alphabetic_characters():
    assert is_valid("77bond") == False
    assert is_valid("r8han") == False
    assert is_valid("qq") == True
    assert is_valid("4099") == False
