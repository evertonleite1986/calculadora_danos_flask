from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():

    personagem = [
        {'Goomba'},
        {'Wario'},
        {'Bowser'}
        ]
    arma = [    
        {'cogumelo'},
        {'estrela'},
        {'flor'}
    ]

    return render_template(
        "index.html",
        personagem=personagem,
        arma=arma
)

if __name__ == "__main__":
    app.run(debug=True)