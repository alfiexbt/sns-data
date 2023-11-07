from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from sns_api_calls import SnsData

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
Bootstrap5(app)
sns_api_calls = SnsData()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sns_data")
def display_sns_data():
    last_sales = sns_api_calls.get_last_sales(limit=200)
    registrations = sns_api_calls.get_registrations(months=1, limit=50)
    leaderboard = sns_api_calls.get_leaderboard()
    categories = sns_api_calls.get_category_stats(months=6)

    for data in [last_sales, registrations, leaderboard, categories]:
        # call the round method
        sns_api_calls.round_prices(data)
    return render_template("sns_data.html",
                           last_sales=last_sales,
                           registrations=registrations,
                           leaderboard=leaderboard,
                           categories=categories)


if __name__ == '__main__':
    app.run(debug=True)
