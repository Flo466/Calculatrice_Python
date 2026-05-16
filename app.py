from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    result = ""
    
    if request.method == "POST":
        data = request.form.get("calculation")
        
        try:
            if data:
                result = eval(data)
        except Exception:
            result = "Error"
            
    return render_template('index.html', display_result=result)

if __name__ == '__main__':
    app.run(debug=True)