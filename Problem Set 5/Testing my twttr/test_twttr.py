from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("julia") == "jl"
    assert shorten("JUliA") == "Jl"
    assert shorten("122Abc") == "122bc"
    assert shorten(",HOLA.") == ",HL."
