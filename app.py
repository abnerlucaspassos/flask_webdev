from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_classful import FlaskView

# Criar o aplicativo Flask
app = Flask(__name__)

# Configurar o Bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

# Definir as rotas
class MainView(FlaskView):
    route_base = '/'

    #def index(self):
        #return render_template('index.html')

    def projects(self):
        return render_template('projects.html')

    def about(self):
        return render_template('about.html')

    def contact(self):
        return render_template('contact.html')

    def new_page(self):
        return render_template('newpage.html')

    def piloto(self):
        return render_template('piloto.html')

    def one(self):
        return render_template('one.html')

# Registrar a classe MainView
MainView.register(app, route_base='/')

# Rodar o aplicativo em modo de debug
if __name__ == "__main__":
    app.run(debug=True)
