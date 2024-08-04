from flask import Flask, render_template

app = Flask(__name__)

#para criarmos uma pagina web com flask, declaramos a route e em seguida a função,
# e criamos também um arquivo html na pasta templates, como está:

#1º pagina do site
@app.route("/") #ele tranforma a função abaixo de modo que def homepage apareça no site quando a route for "/"
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

#a tag após a barra faz com que o conteudo dentro seja dinamico, no caso o nome dos usuarios
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)

#site no ar
if __name__ == "__main__":
    app.run(debug=True) # debug = true para fazer com que as alterações feitas apareçam no site sem eu ter que
                        # parar a execução dele