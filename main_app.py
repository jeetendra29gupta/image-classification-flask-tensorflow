import os

from flask import Flask, render_template, request

from image_classification import classify_image

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    title = "Image Classifier Web App using TensorFlow and HTMX"
    return render_template('index.html', title=title)


# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    filename = file.filename

    if filename == '':
        return 'No selected file', 400

    if not (filename.lower().endswith(('png', 'jpg', 'jpeg'))):
        return 'File type not allowed. Only PNG, JPG, and JPEG are allowed.', 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    predictions = classify_image(file_path)
    result = [{'label': label, 'description': description, 'score': round(score, 2)}
              for (label, description, score) in predictions]
    print(result)

    return render_template('result.html', result=result, image=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
