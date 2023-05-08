from flask import Flask, render_template, request, Response, redirect,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__,
            static_folder='../frontend/dist',
            template_folder="../frontend/dist",
            static_url_path="")
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)
class active_shards(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    value=db.Column(db.Integer)
def serialzed(schema):
    return{
        'timestamp':schema.timestamp,
        'value':schema.value
    }
@app.route('/test', methods=['GET','POST'])
def test():
    values=db.session.query(active_shards.timestamp,active_shards.value).all()
    #return jsonify('hello')
    return jsonify(list(map(serialzed,values)))
@app.route('/')
def hello_world():
    return render_template("index.html")
if __name__ == '__main__':
    app.run()