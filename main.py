from calculator import CalculatorError, evaluate


def main() -> None:
    print("Calculator. Type an expression like 2 + 3 * 4, or 'quit' to stop.")
    while True:
        text = input("> ")
        if text.strip().lower() in {"quit", "exit"}:
            break
        try:
            print(evaluate(text))
        except CalculatorError as error:
            print(error)


if __name__ == "__main__":
    main()
