from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query_api():
    # Get data from the request
    data = request.json
    query_question = data.get('query_question', '')
    model_number = data.get('model_number', 1)

    # Dummy processing logic for demonstration
    links = [f"https://example.com/{i}" for i in range(1, 6)]
    answer = f"Generated response for query: {query_question} using model {model_number}."

    # Return JSON response
    return jsonify({'links': links, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
