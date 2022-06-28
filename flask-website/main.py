from flask import Flask, render_template
from scrape_mars import  scrape
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')



@app.route("/scrape")
def scrape():
    print('final----------',scrape())
    output = scrape()
    return output


if __name__=='__main__':
    app.run(debug=True)