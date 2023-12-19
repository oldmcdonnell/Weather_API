from flask import Flask, render_template
import pandas

app = Flask(__name__)


@app.route("/home/")
def home():
    return render_template("home.html")


#get reading for different stations variable
@app.route("/api/v1/<station>/<date>")
def about(dtation, date):
    df = pandas.read_csv("")
    temperature = df.station(date)
    return {"station": station,
            "date": date,
            "temperature": temperature}

#only run flask script from the main page
if __name__ == "__main__":
    app.run(debug=True)