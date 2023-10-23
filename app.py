from flask import Flask, request, render_template

app = Flask(__name__)
stored_text = ""  # Variable to store the text

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', text=stored_text)

@app.route('/text', methods=['PUT', 'POST'])
def update_text():
    global stored_text
    stored_text = request.data.decode('utf-8')
    return "Text updated successfully"

if __name__ == '__main__':
    app.run()
