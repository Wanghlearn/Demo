from flask import Flask, render_template, request, Response, redirect, jsonify, json, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from utils import get_rusult
from hashlib import md5

app = Flask(__name__,
            static_folder='../client/dist',
            template_folder="../client/dist",
            static_url_path="")
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)

#用户密码加密函数
def password_to_md5(s):
    new_md5 = md5()
    new_md5.update(s.encode(encoding='utf-8'))
    return new_md5.hexdigest()


# 数据库建表
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), unique=False)


# ----cluster info----
class shards(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    value = db.Column(db.Integer)


class status(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    value = db.Column(db.Integer)


class nodes(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    value = db.Column(db.Integer)


def serialzed(schema):
    return {
        'timestamp': schema.timestamp,
        'value': schema.value
    }


@app.route('/clusterinfo', methods=['GET'])
def get_cluster_feature():
    name = request.args.get('cluster_name')
    feature = request.args.get('feature')
    values = []
    if feature == 'active_shards':
        values = db.session.query(shards).filter(shards.cluster_name == name).all()
    elif feature == 'health_node':
        values = db.session.query(nodes).filter(nodes.cluster_name == name).all()
    elif feature == 'status':
        values = db.session.query(status).filter(status.cluster_name == name).all()
    # return jsonify('hello')
    return jsonify(list(map(serialzed, values)))


# ----node info 1----
class index(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    node_name = db.Column(db.String(35), primary_key=True)
    node_ip = db.Column(db.String(35))
    value = db.Column(db.Integer)


class os_load5(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    node_name = db.Column(db.String(35), primary_key=True)
    node_ip = db.Column(db.String(35))
    value = db.Column(db.Integer)


class process(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    node_name = db.Column(db.String(35), primary_key=True)
    node_ip = db.Column(db.String(35))
    value = db.Column(db.Integer)


class query(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    node_name = db.Column(db.String(35), primary_key=True)
    node_ip = db.Column(db.String(35))
    value = db.Column(db.Integer)


class rx(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    node_name = db.Column(db.String(35), primary_key=True)
    node_ip = db.Column(db.String(35))
    value = db.Column(db.Integer)


class tx(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    node_name = db.Column(db.String(35), primary_key=True)
    node_ip = db.Column(db.String(35))
    value = db.Column(db.Integer)


@app.route('/register', methods=['GET'])
def Register():
    name = request.args.get('name')
    password = request.args.get('password')
    userobject = user.query.filter_by(username=name).all()
    if userobject:
        return '用户名已存在'
    else:
        userobject1 = user(username=name, password=password_to_md5(password))
        db.session.add(userobject1)
        db.session.commit()
        return "1"


@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        username = request.args.get('name')
        password = request.args.get('password')
        userobject = user.query.filter_by(username=username, password=password_to_md5(password)).first()
        if userobject:
            return "1"
        else:
            userobject = user.query.filter_by(username=username).first()
            if userobject:
                return "密码错误"
            return "用户不存在，请注册"


@app.route('/nodeinfo1', methods=['GET'])
def nodeinfo():
    c_name = request.args.get('cluster_name')
    n_name = request.args.get('node_name')
    feature = request.args.get('feature')
    values = []
    if feature == 'os_load5':
        values = db.session.query(os_load5).filter(os_load5.cluster_name == c_name, os_load5.node_name == n_name).all()
    elif feature == 'process_cpu_percent':
        values = db.session.query(process).filter(process.cluster_name == c_name, process.node_name == n_name).all()
    elif feature == 'index_time_seconds_total':
        values = db.session.query(index).filter(index.cluster_name == c_name, index.node_name == n_name).all()
    elif feature == 'search_query_time_seconds':
        values = db.session.query(query).filter(query.cluster_name == c_name, query.node_name == n_name).all()
    elif feature == 'transport_rx_size_bytes_total':
        values = db.session.query(rx).filter(rx.cluster_name == c_name, rx.node_name == n_name).all()
    elif feature == 'transport_tx_size_bytes_total':
        values = db.session.query(tx).filter(tx.cluster_name == c_name, tx.node_name == n_name).all()
    # return jsonify('hello')
    return jsonify(list(map(serialzed, values)))


# ----node info 2(mount)----
class bytes(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.String(35), primary_key=True)
    node_name = db.Column(db.String(35), primary_key=True)
    mount = db.Column(db.String(35), primary_key=True)
    value = db.Column(db.Integer)


@app.route('/nodeinfo2', methods=['GET'])
def nodeinfo2():
    c_name = request.args.get('cluster_name')
    n_name = request.args.get('node_name')
    m_name = request.args.get('mount_name')
    values = []
    values = db.session.query(bytes).filter(bytes.cluster_name == c_name, bytes.node_name == n_name,
                                            bytes.mount == m_name).all()
    return jsonify(list(map(serialzed, values)))


@app.route('/similar', methods=['GET'])
def getRes():
    return json.dumps(get_rusult.getAns())


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
