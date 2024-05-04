import numb3rs


def test_valid_ipv4():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("140.247.235.144") == True


def test_invalid_ipv4():
    assert numb3rs.validate("256.255.255.255") == False
    assert numb3rs.validate("64.128.256.512") == False
    assert numb3rs.validate("8.8.8") == False
    assert numb3rs.validate("10.10.10.10.10") == False
    assert numb3rs.validate("192.168.1") == False
