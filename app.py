from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Your Google Form URL
GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScxNqA30UOO8Td05Na7_Is9DHB2m4ov50GuEPcDfaYOxf3jtg/formResponse'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    price = request.form['price']

    form_data = {
        'entry.642978654': price
    }

    response = requests.post(GOOGLE_FORM_URL, data=form_data)

    # Check if submission was successful
    if response.status_code == 200:
        return redirect('/success')
    else:
        return f'An error occurred: {response.status_code} - {response.text}', 400


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
