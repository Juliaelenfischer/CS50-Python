from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12
    try:
        jar.deposit(1)  # Exceeds capacity
    except ValueError as e:
        assert str(e) == "Jar capacity exceeded"

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    try:
        jar.withdraw(6)  # Withdraw more than available
    except ValueError as e:
        assert str(e) == "Not enough cookies in the jar"
