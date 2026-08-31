# Worlds-Smallest-Calc menu wrapper. Run with: python Calc_ui.py
MENU = [
    ("1", "2 + 2", "basic addition"),
    ("2", "10 * 3", "basic multiplication"),
    ("3", "2 ** 10", "exponentiation"),
    ("4", "22 / 7", "division"),
    ("5", "1+2+3+4+5", "running sum"),
    ("6", "(17-3)*2", "parentheses"),
    ("7", "abs(-42)", "absolute value"),
    ("8", "round(3.14159,2)", "rounding"),
    ("9", "max(1,9,3)", "maximum"),
    ("0", "quit", "exit"),
]
PROMPT = "Pick a number (or q to quit): "

def show():
    print("Worlds-Smallest-Calc menu")
    print("-" * 38)
    for key, expr, desc in MENU:
        print("[" + key + "] " + expr + " -- " + desc)
    print("")

def main():
    while True:
        show()
        try:
            choice = input(PROMPT).strip()
        except (EOFError, KeyboardInterrupt):
            print("")
            return
        if choice == "q" or choice == "Q" or choice == "0":
            print("Bye.")
            return
        match = None
        for item in MENU:
            if item[0] == choice:
                match = item
                break
        if match is None:
            print("Pick a number from the menu.")
            continue
        expr = match[1]
        if expr == "quit":
            print("Bye.")
            return
        try:
            result = eval(expr, {}, {})
            print(expr + " = " + str(result))
        except Exception as exc:
            print("error: " + exc.__class__.__name__ + ": " + str(exc))

if __name__ == "__main__":
    main()
