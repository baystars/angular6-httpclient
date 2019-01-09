#!/usr/bin/env python
# -*- mode: python -*- -*- coding: utf-8 -*-
import copy
import json

from flask import (Flask, request, jsonify, abort)
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# CORS
CORS(app)

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy()
db.init_app(app)

"""
$ python
import json
from app import (app, db, Customer)
with app.app_context():
    db.create_all()

data = json.load(open('data/data.json'))
for row in data['customers']:
    customer = Customer(row['firstname'], row['lastname'], row['age'])
    with app.app_context():
        customer.save()

"""

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(10))
    age = db.Column(db.Integer())

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __repr__(self):
        return f'<Customer: {self.firstname} {self.lastname}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Customer.query.all()

    @staticmethod
    def get_by_id(id):
        return Customer.query.filter(Customer.id==id).first()

class CustomerListView(MethodView):
    def get(self):
        object_list = []
        for customer in Customer.get_all():
            obj = copy.copy(customer.__dict__)
            del obj['_sa_instance_state']
            object_list.append(obj)
        response = jsonify(object_list)
        return response, 200

    def post(self):
        try:
            data = json.loads(request.data.decode())
        except:
            abort(400)
        customer = Customer(**data)
        customer.save()

        response = jsonify({'id': customer.id,
                            'firstname': customer.firstname,
                            'lastname': customer.lastname,
                            'age': customer.age})
        return response, 201

class CustomerDetailView(MethodView):
    def get_customer(self, oid):
        customer = Customer.get_by_id(oid)
        if not customer:
            abort(404)
        return customer

    def get(self, oid):
        customer = self.get_customer(oid)
        obj = copy.copy(customer.__dict__)
        del obj['_sa_instance_state']
        response = jsonify(obj)
        response.status_code = 200
        return response

    def put(self, oid):
        customer = self.get_customer(oid)
        try:
            data = json.loads(request.data.decode())
        except:
            abort(400)
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        age = data.get('age')
        changed = 0
        if firstname and (customer.firstname != firstname):
            customer.firstname = firstname
            changed += 1
        if lastname and (customer.lastname != lastname):
            customer.lastname = lastname
            changed += 1
        if age and (customer.age != age):
            customer.age = age
            changed += 1
        if changed:
            customer.save()
        return jsonify({'message': f'update {oid}'}), 204

    def delete(self, oid):
        customer = self.get_customer(oid)
        customer.delete()
        response = jsonify({
            'customer': 'customer {} deleted successfully'.format(customer.id)
         })
        return response, 204

app.add_url_rule('/customers', methods=['GET', 'POST'],
                 view_func=CustomerListView.as_view('customer_list'))
customer_detail_view = CustomerDetailView
app.add_url_rule('/customers/<int:oid>', methods=['GET', 'PUT'],
                 view_func=customer_detail_view.as_view('customer_detail'))
app.add_url_rule('/customers/delete/<int:oid>', methods=['DELETE'],
                 view_func=customer_detail_view.as_view('customer_delete'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
