"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""
import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root

@click.command()
@click.argument('operation')
@click.argument('num1', type=float)
@click.argument('num2', type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""

    try:
        # Ensure num2 is provided for operations that require two numbers
        if operation in ['add', 'subtract', 'multiply', 'divide', 'power'] and num2 is None:
            click.echo(f"Error: Operation '{operation}' requires two numbers.")
            sys.exit(1)

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        elif operation == 'power':
            result = power(num1, num2)
        elif operation == 'square_root':
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format the result nicely
        if isinstance(result, (int, float)):
            if result == int(result):
                click.echo(int(result))
            else:
                click.echo(f"{result:.2f}")
        else:
            click.echo(result)

    except ZeroDivisionError:
        click.echo("Error: Division by zero is not allowed.")
        sys.exit(1)
    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    calculate()