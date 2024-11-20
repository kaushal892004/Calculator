from flask import Flask, render_template, request, jsonify
import math
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     try:
#         data = request.json
#         expression = data.get('expression')
#         result = eval(expression)  # Use eval() carefully
#         return jsonify({'result': result})
#     except Exception as e:
#         return jsonify({'error': 'Invalid expression'}), 400
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data['expression']
        # Evaluate the expression safely using eval
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return jsonify(result=result)
    except Exception as e:
        return jsonify(result="Error")
    
    
if __name__ == '__main__':
    app.run(debug=True,port=5001)
