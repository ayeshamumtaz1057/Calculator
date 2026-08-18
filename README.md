# Calculator

A lightweight command-line calculator written in Python. Supports the four basic arithmetic operations with input validation and continuous calculation until the user exits.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Project Structure](#project-structure)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- Addition, subtraction, multiplication, and division
- Input validation for non-numeric values and invalid operators
- Division-by-zero protection
- Continuous operation loop — perform multiple calculations per session
- Simple, dependency-free implementation using only the Python standard library

## Requirements

- Python 3.6 or higher

No external dependencies are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/calculator.git
cd calculator
```

## Usage

Run the script from the terminal:

```bash
python3 calculator.py
```

Follow the prompts to enter a number, an operator, and a second number. Type `q` at any prompt to exit.

## Example

```
=== Simple Calculator ===
Type 'q' at any prompt to quit.

First number (or 'q' to quit): 12
Operator (+, -, *, /): /
Second number: 4
= 3.0

First number (or 'q' to quit): q
Goodbye!
```

## Project Structure

```
calculator/
├── calculator.py   # Application entry point and core logic
└── README.md       # Project documentation
```

## Error Handling

| Scenario                  | Behavior                                  |
|----------------------------|--------------------------------------------|
| Non-numeric input          | Prompts the user to re-enter a valid number |
| Invalid operator           | Prompts the user to enter one of `+ - * /`  |
| Division by zero           | Displays an error message and continues     |

## Contributing

Contributions are welcome. To propose a change:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the [MIT License](LICENSE).


