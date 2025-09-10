# Import the necessary modules from Flask and TextBlob
from flask import Flask, render_template, request
from textblob import TextBlob


app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze_text():
    if request.method == 'POST':
       
        raw_text = request.form['raw_text']

       
        blob = TextBlob(raw_text)
        
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            sentiment_category = "Positive(>0)"
        elif polarity < 0:
            sentiment_category = "Negative(<0)"
        else:
            sentiment_category = "Neutral(=0)"

        return render_template('results.html', 
                               raw_text=raw_text,
                               sentiment_category=sentiment_category,
                               polarity=polarity,
                               subjectivity=subjectivity)


if __name__ == '__main__':
    app.run(debug=True)