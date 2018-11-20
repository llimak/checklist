from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checklist.db'

db = SQLAlchemy(app)


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    items = db.relationship('Item')


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    checked = db.Column(db.Boolean)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))



@app.route('/')
def hello_world():
    return 'Checklist app.'


@app.route('/lists', methods=['GET', 'POST'])
def lists():
    if request.method == 'POST':
        data = request.json
        if(db.session.query(List).filter(List.name == data['name']).count() > 0):
            return '409 Checklist of given name already exists.'
        else:
            new_list = List(name=data['name'])
            db.session.add(new_list)
            db.session.commit()
            return '201 New checklist inserted.'

    if request.method == 'GET':
        lists = List.query.all()
        lists_name = []
        for list in lists:
            lists_name.append(list.name)
        return jsonify(lists_name)

@app.route('/lists/<name>', methods=['DELETE'])
def delete_list(name):
    if request.method == 'DELETE':
        if(List.query.filter(List.name == name).delete()):
            db.session.commit()
            return '200 OK.'
        else:
            return '404 Checklist of given ID does not exist.'

if __name__ == '__main__':
    app.run()
