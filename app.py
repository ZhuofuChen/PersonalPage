from flask import Flask, render_template
from flask_restful import Api

app = Flask(__name__)
api = Api(app)



@app.route('/')
def home():
    return render_template('index.html')

# api.add_resource(Store, '/project/<string:name>')
# api.add_resource(StoreList, '/projects')
# api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 5000, debug = True)