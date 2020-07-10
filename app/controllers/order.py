
from app import app,db
from flask import request
from app.models.tables import Products,Orders
from app.models.marshmallow import OrdersSchema
import uuid

from app.models.decorators import fields_required,token_required,perfil_required


@app.route('/makeOrder',methods=['POST'])
@token_required()
@perfil_required("CLIENTE")
@fields_required(['publicId_product','amount'],isList=True)
def make_order(user,fields):
    orderNumber = str(uuid.uuid4().int & (1<<30)-1)

    dbList = []
    for item in fields:
        publicId    = str(uuid.uuid4())
        orde = Orders(publicId=publicId,publicId_product=item['publicId_product'],orderNumber=orderNumber,amount=item["amount"])
        valid = orde.is__valid()
        if not valid[0]:
            return {"status":False,"message":valid[1]}
        dbList.append(orde)

    for item in dbList:
        db.session.add(item)

    db.session.commit()
    return {"status":True,"message":"order made successfully!"}

@app.route('/getOrder',methods=['POST'])
@token_required()
@perfil_required("LOJA")
@fields_required(['orderNumber'])
def get_order(user,fields):

    sc = OrdersSchema()
    itens = Orders.query.filter_by(orderNumber = fields['orderNumber']).all()
    

    return {"status":True,"message":"OK","products":[sc.dump(x) for x in itens]}
