from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    resultat = ""
    
    if request.method == "POST":
        donnees = request.form.get("calculation")
        
        try:
            if donnees:
                resultat = eval(donnees)
        except Exception:
            resultat = "Error"
            
    return render_template('index.html', display_result=resultat)

if __name__ == '__main__':
    app.run(debug=True)