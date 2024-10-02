from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Criar a estrutura da aeronave
def criar_aeronave():
    fileiras = ['A', 'B', 'C', 'D', 'E', 'F']
    aeronave = {fileira: [None] * 30 for fileira in fileiras}
    return aeronave

# Inicializar a aeronave com assentos desmarcados
aeronave = criar_aeronave()

# Rota principal que exibe o esquema dos assentos
@app.route('/')
def index():
    return render_template('esquema_assentos.html', aeronave=aeronave)

# Rota para marcar um assento
@app.route('/marcar', methods=['POST'])
def marcar_assento():
    fileira = request.form.get('fileira').upper()
    coluna = int(request.form.get('coluna')) - 1  # Converter para índice (0-29)

    if fileira in aeronave and 0 <= coluna < 30:
        aeronave[fileira][coluna] = True  # Marcar assento como ocupado

    return redirect(url_for('index'))

# Rota para desmarcar um assento
@app.route('/desmarcar', methods=['POST'])
def desmarcar_assento():
    fileira = request.form.get('fileira').upper()
    coluna = int(request.form.get('coluna')) - 1  # Converter para índice (0-29)

    if fileira in aeronave and 0 <= coluna < 30:
        aeronave[fileira][coluna] = None  # Desmarcar assento como livre

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)