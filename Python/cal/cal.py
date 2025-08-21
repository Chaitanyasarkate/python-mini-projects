
def main():
    print("=== CLI Calculator ===")
    print("Type any math expression (e.g., 5+3*2/4) or 'exit' to quit.")

    allowed = {"__builtins__": None}  

    while True:
        expr = input(">>> ").strip()
        if expr.lower() == "exit":
            print("Goodbye!")
            break

        try:
            result = eval(expr, allowed, {})
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
