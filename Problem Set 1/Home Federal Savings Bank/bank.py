#prompts the user for a greeting.
greeting = input ("Greeting: ").strip().lower()
#starts with “hello”, output $0.
if greeting.startswith("hello"):
    print("$0")
#If the greeting starts with an “h” (but not “hello”), output $20
elif greeting.startswith("h"):
    print("$20")
#Otherwise, output $100.
else:
    print("$100")
