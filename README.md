# Flask Math Operations Application

## Overview
This project is a simple Flask application that performs basic mathematical operations, including addition, subtraction, multiplication, division, and modulus (log). The application integrates with an HTML frontend to accept user inputs and displays the results dynamically.

## Features
1. Perform the following operations:
   - Addition
   - Subtraction
   - Multiplication
   - Division
   - Modulus
2. Integration with an HTML form to accept inputs and display results.
3. JSON-based API functionality for integration with tools like Postman.

## File Structure
- **app.py**: Core business logic of the Flask application.
- **templates/**: Directory containing HTML files for the frontend.
  - `index.html`: The main page where users input numbers and select operations.
  - `results.html`: Displays the result of the operation.

## Installation

1. Clone the repository or download the code files.
2. Ensure you have Python installed (preferably version 3.6 or later).
3. Install Flask using pip:
   ```bash
   pip install flask
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.
3. Input two numbers and select an operation from the dropdown.
4. Click "Calculate" to see the result.

### API Endpoint

- **Endpoint**: `/math`
- **Method**: POST
- **Parameters** (form data):
  - `num1`: First number (integer)
  - `num2`: Second number (integer)
  - `operation`: Operation to perform (add, subtract, multiply, divide, log)
- **Response**: Rendered HTML page showing the result.

### JSON-based API (Postman Integration)

To test the application with Postman:
1. Use the `/math` endpoint with the POST method.
2. Send data in JSON format:
   ```json
   {
       "num1": 10,
       "num2": 5,
       "operation": "add"
   }
   ```
3. Adjust the Flask code as follows for JSON support:
   ```python
   from flask import request, jsonify

   @app.route('/postman_data', methods=['POST'])
   def postman_data():
       data = request.get_json()
       num1 = int(data['num1'])
       num2 = int(data['num2'])
       ops = data['operation']
       # Perform operations and return JSON response
       ...
   ```

## HTML Structure

- **Form**: Sends data to the `/math` endpoint using the POST method.
  ```html
  <form action="/math" method="POST">
      <input type="text" name="num1" id="num1" placeholder="Enter first number">
      <input type="text" name="num2" id="num2" placeholder="Enter second number">
      <select name="operation">
          <option value="add">Add</option>
          <option value="subtract">Subtract</option>
          <option value="multiply">Multiply</option>
          <option value="divide">Divide</option>
          <option value="log">Log</option>
      </select>
      <button type="submit">Calculate</button>
  </form>
  ```

