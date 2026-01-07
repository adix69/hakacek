from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    show_chain = request.args.get("chain")
    show_balls = request.args.get("balls")
    show_candles = request.args.get("candles")

    return render_template("index.html", 
                           chain=show_chain, 
                           balls=show_balls, 
                           candles=show_candles)

if __name__ == "__main__":
    app.run(debug=True)