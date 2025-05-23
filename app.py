from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form["input"]
        if user_input == "1011":
            return redirect(url_for("s1"))
        else:
            result = "คำตอบผิด กรุณาลองใหม่"
    return render_template("index.html", result=result)

@app.route("/s1")
def s1():
    return render_template("s1.html")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)


'''
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form["input"]
        if user_input == "AAAABBCCDDD":
            return redirect(url_for("s1"))
        elif user_input.lower() == "aaaabbccddd":
            result = "กรุณาพิมพ์ตัวใหญ่เท่านั้น"
        else:
            result = "รูปแบบ input ผิด กรุณาลองใหม่"
    return render_template("index.html", result=result)

@app.route("/s1")
def s1():
    return render_template("s1.html")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)


'''
