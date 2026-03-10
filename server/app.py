from flask import Flask
app = Flask(__name__)

# 1. Index route: expects HTML tags (e.g., <h1>) and a terminal print
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. Print route: expects a string parameter and prints it to the console
@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  # Essential for test_print_text_in_console
    return parameter

# 3. Count route: expects an integer parameter and returns a string with numbers from 0 to num-1, each on a new line
@app.route('/count/<int:num>')
def count(num):
    # test_count_range_10 expects 0 through 9 if num is 10
    result = ""
    for i in range(num):
        result += f"{i}\n"
    return result

# 4. Math route: expects PLAIN strings (no tags)
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid Operation", 400
        
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)