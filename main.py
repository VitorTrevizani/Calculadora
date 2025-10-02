from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = 'siiiiiuuu'

@app.route('/')
def index():
   return render_template('interface.html')


@app.route('/form', methods=['POST'])
def form():
   botao = request.form['botao']
   if botao == "=":
       resul = eval(session["expressao"])
       print(resul)
       
   if "expressao" not in session:
        session["expressao"] = ""

   session["expressao"] += botao
   print(session["expressao"])
   return redirect(url_for('index'))

if __name__ == "__main__":
   app.run(debug=True)