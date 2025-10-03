from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = 'siiiiiuuu'


@app.route('/')
def index():
   if "expressao" not in session:
      session["expressao"] = ""
   if "resultado" not in session:
      session["resultado"] = ""

   
   return render_template('interface.html', exp = session["expressao"], res = session["resultado"] )


@app.route('/form', methods=['POST'])
def form():
   botao = request.form['botao']
   if botao == "=":
       resul = eval(session["expressao"])  #calcula o resultado
       session["resultado"] = resul        #joga na sessão pra renderizar na pagina
       session["expressao"] = ''  
       botao = ''         #limpa a expressão atual
   else:
      session["resultado"] = "none"  
       

   session["expressao"] += botao
   print(session["expressao"])
   return redirect(url_for('index'))

if __name__ == "__main__":
   app.run(debug=True)