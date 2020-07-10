from app import app,db
from flask import request
from app.models.tables import Products
from app.models.marshmallow import ProductsSchema
import uuid

from app.models.decorators import fields_required,token_required,perfil_required

@app.route('/uploadPoducts',methods=['POST'])
@token_required()
@perfil_required("LOJA")
@fields_required(["name","description","price"],isList=True)
def create_product(user,fields):

    dbList = []
    for item in fields:
        prod = Products(id_user=user.id,publicId=str(uuid.uuid4()), name=item["name"],description=item["description"],price=item["price"])
        valid = prod.is__valid()
        if not valid[0]:
            return {"status":False,"message":valid[1]}
        dbList.append(prod)

    for item in dbList:
        db.session.add(item)

    db.session.commit()
    return {"status":True,"message":"products uploaded successfully!"}

@app.route('/getPoducts',methods=['GET'])
@token_required()
def get_products(user):
    sc = ProductsSchema()
    prods = Products.query.filter(Products.user.has(id=user.id)).all()
    return {"status":True,"message":"OK","products":[sc.dump(x) for x in prods]}