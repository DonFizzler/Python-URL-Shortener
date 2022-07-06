from flask import Flask, redirect, request, render_template
from Utils import JsonText, GetUrl, GenerateCode, CheckCode, CreateUrl, RemoveCode, ValidUrl, GetInfo

app = Flask(__name__)

@app.route("/info", methods=["POST"])
def info():
    code = request.form.get("code")
    if not code:
        return JsonText(
            {
                "success": False,
                "message": "code argument missing!"
            } 
        ), 400
    infoCode = GetInfo(code)
    if not infoCode[0]:
        return JsonText(
            {
                "success": False,
                "message": "Invalid code!"
            } 
        ), 400
    return JsonText(infoCode[1])     

@app.route("/create", methods=["POST"])
def create():
    url = request.form.get("url")
    if not url:
        return JsonText(
            {
                "success": False,
                "message": "url argument missing!"
            } 
        ), 400
    if not ValidUrl(url):
         return JsonText(
            {
                "success": False,
                "message": "Invalid URL!"
            } 
        ), 400
    checkUrl = GetUrl(url)
    if checkUrl[0]:
        return JsonText(
            {
                "success": True,
                "already_created": True,
                "short_url": checkUrl[1],
                "url": url
            } 
        )
    while True:
        code = GenerateCode(10)
        if not CheckCode(code)[0]:
            break
    CreateUrl(code, url)
    return JsonText(
            {
                "success": True,
                "already_created": False,
                "short_url": code,
                "url": url
            } 
        )

@app.route('/delete', methods=['POST'])
def delete():
    code = request.form.get("code")
    if not code:
        return JsonText(
            {
                "success": False,
                "message": "code argument missing!"
            } 
        ), 400
    checkCode = CheckCode(code)
    if not checkCode[0]:
        return JsonText(
            {
                "success": False,
                "message": "Invalid code!"
            } 
        ), 400
    RemoveCode(code)
    return JsonText(
            {
                "success": True,
                "message": "Code deleted!"
            } 
        )

@app.route("/<route>")
def urlshortner(route):
    checkUrl = CheckCode(route)
    if (checkUrl[0]):
        return redirect(checkUrl[1])
    else:
         return render_template("404.html"), 404

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()