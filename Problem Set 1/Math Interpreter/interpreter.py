x, y, z = input("Expression: ").split()
x = int (x)
z = int (z)
match y:
    case "+":
        print(f"{x + z:.1f}")   #.1f redondea cortando un decimal
    case "-":
        print(f"{x - z:.1f}")
    case "*":
        print(f"{x * z:.1f}")
    case "/":
        print(f"{x / z:.1f}")
