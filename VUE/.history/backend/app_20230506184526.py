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
# ----cluster info----
class shards(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    value=db.Column(db.Integer)
class status(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    value=db.Column(db.Integer)
class nodes(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    value=db.Column(db.Integer)
def serialzed(schema):
    return{
        'timestamp':schema.timestamp,
        'value':schema.value
    }
@app.route('/clusterinfo', methods=['GET'])
def test():
    name=request.args.get('cluster_name')
    feature=request.args.get('feature')
    values=[]
    if feature=='active_shards':
        values=db.session.query(shards).filter(shards.cluster_name==name).all()
    elif feature=='health_node':
        values=db.session.query(nodes).filter(nodes.cluster_name==name).all()
    elif feature=='status':
        values=db.session.query(status).filter(status.cluster_name==name).all()
    #return jsonify('hello')
    return jsonify(list(map(serialzed,values)))
# ----node info (single index)----
class index(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    node_name=db.Column(db.String(35),primary_key=True)
    node_ip=db.Column(db.String(35))
    value=db.Column(db.Integer)
class os_load5(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    node_name=db.Column(db.String(35),primary_key=True)
    node_ip=db.Column(db.String(35))
    value=db.Column(db.Integer)
class process(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    node_name=db.Column(db.String(35),primary_key=True)
    node_ip=db.Column(db.String(35))
    value=db.Column(db.Integer)
class rx(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    node_name=db.Column(db.String(35),primary_key=True)
    node_ip=db.Column(db.String(35))
    value=db.Column(db.Integer)
class tx(db.Model):
    timestamp=db.Column(db.Integer,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    node_name=db.Column(db.String(35),primary_key=True)
    node_ip=db.Column(db.String(35))
    value=db.Column(db.Integer)
@app.route('/nodeinfo1', methods=['GET'])
def nodeinfo():
    name=request.args.get('node_name')
    feature=request.args.get('feature')
    values=[]
    if feature=='os_load5':
        values=db.session.query(os_load5).filter(shards.cluster_name==name).all()
    elif feature=='process_cpu_percent':
        values=db.session.query(process).filter(nodes.cluster_name==name).all()
    elif feature=='index_time_seconds_total':
        values=db.session.query(index).filter(nodes.cluster_name==name).all()
    elif feature=='search_query_time_seconds':
        values=db.session.query(status).filter(status.cluster_name==name).all()
    elif feature=='transport_rx_size_bytes_total':
        values=db.session.query(status).filter(status.cluster_name==name).all()
    elif feature=='transport_tx_size_bytes_total':
        values=db.session.query(status).filter(status.cluster_name==name).all()
    #return jsonify('hello')
    return jsonify(list(map(serialzed,values)))

@app.route('/')
def hello_world():
    return render_template("index.html")
if __name__ == '__main__':
    app.run()