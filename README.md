# 🌟 Simple & Scientific Calculator

This project is a simple and scientific calculator built using **Flask** and **Tailwind CSS**. It supports both basic and scientific operations, including addition, subtraction, multiplication, division, trigonometric functions, square root, and more. The calculator is designed with a responsive and interactive user interface.

## Features

- **Basic Operations**: Addition, Subtraction, Multiplication, and Division.
- **Scientific Operations**: Trigonometric functions (`sin`, `cos`, `tan`), logarithms, square roots, powers (x², x³).
- **Responsive Design**: Built with **Tailwind CSS** to ensure it works well on all screen sizes.
- **Smooth UI**: Animations for button presses and screen transitions.
- **Real-time Calculation**: Calculations are done on the client-side, but the backend can be extended for more complex functionalities.

## Tech Stack

- **Frontend**: 
  - HTML
  - Tailwind CSS (for styling)
  - Vanilla JavaScript (for client-side logic)
- **Backend**:
  - Python (Flask)
  - Flask to serve the application
- **Other**:
  - Tailwind CSS for utility-first styling
  - JavaScript for interactivity (handling button clicks and keyboard input)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/calculator-project.git
    ```

2. **Install dependencies**:
    Navigate to the project directory and install the required Python packages:
    ```bash
    cd calculator-project
    pip install -r requirements.txt
    ```

3. **Run the Flask app**:
    Run the Flask development server to start the application:
    ```bash
    python app.py
    ```

4. **Open in Browser**:
    Open your browser and go to `http://127.0.0.1:5000/` to use the calculator.

## Usage

Once the app is running, you can:

- **Click on the buttons**: Use the mouse to click on the calculator buttons to perform operations.
- **Keyboard Input**: You can also use the keyboard for input. Here are the key mappings:
    - **Number keys (0-9)**: Input digits.
    - **`+`, `-`, `*`, `/`**: Perform arithmetic operations.
    - **`Enter`**: Calculate the result.
    - **`Backspace`**: Delete the last character.
    - **`Escape`**: Clear the display.
    - **`(`, `)`**: Parentheses for grouping.
    - **`%`**: Percentage operation.
    - **Trigonometric functions**: `sin`, `cos`, `tan`, `log`, and others.

### Backend

- The backend is built with Flask, and it handles complex calculations like square roots, powers, and trigonometric functions using Python libraries.
- The front-end uses JavaScript to handle user input, interact with the Flask API, and update the display dynamically.
## ScreenShot

### Calculator
![Calculator](https://github.com/kaushal892004/Calculator/blob/main/images/Calculator.png) 

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new pull request.


## Acknowledgements

- The design uses **Tailwind CSS** for styling.
- The scientific calculator features are powered by simple JavaScript functions and Python's `math` module.
- Special thanks to the **Unsplash API** for providing the background images.

## Future Enhancements

- Add more advanced scientific operations (e.g., integration, derivatives).
- Implement server-side calculations for more complex operations.
- Add user authentication and save history of calculations for each user.


### Made with ❤️ by [Kaushal Parmar](https://github.com/kaushal892004)
