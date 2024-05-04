import pytest
import working

def test_valid_formats():
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert working.convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert working.convert("1:00 AM to 1:00 PM") == "01:00 to 13:00"
    assert working.convert("1 AM to 1 PM") == "01:00 to 13:00"
    assert working.convert("11:00 PM to 12:00 AM") == "23:00 to 00:00"
    assert working.convert("11 PM to 12 AM") == "23:00 to 00:00"

def test_invalid_formats():
    with pytest.raises(ValueError):
        working.convert("9:00 to 5:00 PM") # Missing AM/PM
    with pytest.raises(ValueError):
        working.convert("9:00 AM - 5:00 PM") # Incorrect delimiter
    with pytest.raises(ValueError):
        working.convert("9:00 AM to 17:00") # Invalid hour
    with pytest.raises(ValueError):
        working.convert("13:00 AM to 5:00 PM") # Invalid hour
    with pytest.raises(ValueError):
        working.convert("9:60 AM to 5:00 PM") # Invalid minute
    with pytest.raises(ValueError):
        working.convert("9:00 AM to 5:60 PM") # Invalid minute
