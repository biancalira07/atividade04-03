from flask import * 

from bd import listar_livro, remover_livro, novo_livro, detalha_livro, atualiza_livro 

app = Flask(__name__)


@app.route('/')
def listar():
    livros = listar_livro()
    return render_template("biblioteca.html",biblioteca=None) 

@app.route("/remover/<int:chave>")
def apagar(chave):
    remover_livro(chave)
    return redirect('/') 

@app.route("/novo", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.form.to_dict()
        novo_livro(dados.get('nome'), dados.get('autor'), dados.get('paginas'), dados.get ('genero'))
        return redirect('/')
    return render_template('form_biblioteca.html', livro=None, title='Novo Livro') 

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        atualiza_livro(chave, dados.get('nome'), dados.get('autor'), dados.get('paginas'), dados.get('genero'))
        return redirect('/')
    livro = detalha_livro(chave)
    return render_template('form_biblioteca.html', livro=livro, title='Editar Livro')



if __name__ == '__main__':
    app.run()