# Expression-Calculator-with-History

This is a simple command-line calculator built in Python. It supports basic arithmetic operations (+, -, *, /), and also keeps a calculation history that you can view or clear anytime.

## Features

- Addition, subtraction, multiplication, and division
- Input validation and error handling
- Calculation history saved to `history.txt`
- View and clear calculation history

## Project Structure
calculator_project/
│
├── calculator.py      # Main program file
├── history.txt        # Stores calculation history (auto-created after first run)
└── README.md          # Project documentation

## Usage

1. Run the script:

    ```sh
    python expression_calcualtor.py
    ```

2. Enter calculations in the format:

    ```
    <number1> <operator> <number2>
    ```

    Example:

    ```
    5 + 3
    10 / 2
    ```

3. Special commands:

    - `history` — Show calculation history
    - `clear` — Clear calculation history
    - `exit` — Exit the program

## Files

- [`expression_calcualtor.py`](d:/PYTHON%20LANGUAGE/project3/expression_calcualtor.py): Main calculator script
- [`history.txt`](d:/PYTHON%20LANGUAGE/project3/history.txt): Stores calculation history

## Example

```
Enter calculation (+, -, *, /) (or 'history', 'clear', 'exit'): 6 * 4
Calculation result: 24
Calculation saved to history.
Enter calculation (+, -, *, /) (or 'history', 'clear', 'exit'): history
6 * 4 = 24
6 * 6 = 36
9 / 9 = 1
4 - 2 = 2
5 + 5 = 10
```

## Contact

 **RIZWAN KHAN NASAR**

📧 Email: rizwankhannasar125@gmail.com

🔗 LinkedIn: linkedin.com/in/rizwan-khan-nasar-35b147360
