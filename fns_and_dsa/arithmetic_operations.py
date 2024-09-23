def perform_operation(num1: float, num2: float, operation: str):
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                result = "Cannot divide by zero."
            else: result = num1 / num2
        case _:
            result = "Operation not recognized"
    return result