from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('interface.html')


@app.route('/form', methods=['POST'])
def form():
   botao = request.form['botao']
   print(botao)
   return redirect(url_for('index'))

if __name__ == "__main__":
   app.run(debug=True)