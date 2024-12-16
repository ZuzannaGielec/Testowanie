from flask import Flask, render_template, request, jsonify, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('UI.html')  # The file should be in the `templates` folder.

@app.route('/process', methods=['POST'])
def process():
    file = request.files['mediaFile']
    target_language = request.form['language']

    # Save uploaded file
    filepath = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(filepath)

    # Simulate processing
    transcript = "This is a dummy transcript."
    translated_text = "This is a dummy translation."

    # Return the result
    return jsonify({'transcript': transcript, 'translatedText': translated_text})

@app.route('/download')
def download():
    # Simulate a downloadable file
    return send_file('dummy_output.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
