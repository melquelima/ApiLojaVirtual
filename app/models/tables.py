from app import db,ma
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Time,Boolean,Float
from marshmallow import Schema, fields, pprint

class User(db.Model):
    __tablename__ = "users"

    id          = db.Column(db.Integer,primary_key=True)
    publicId    = db.Column(db.String(50),unique=True,nullable=False)
    userName    = db.Column(db.String(50),unique=True,nullable=False)
    password    = db.Column(db.String(80),nullable=False)
    perfil      = db.Column(db.String(10),nullable=False) 

    def __init__(self,publicId,userName,password,perfil):
        self.publicId = publicId
        self.userName = userName
        self.password = password
        self.perfil   = perfil

class Products(db.Model):
    __tablename__ = "products"

    publicId    = db.Column(db.String(50),primary_key=True,nullable=False)
    id_user     = db.Column(Integer,ForeignKey('users.id'))
    name        = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(80),nullable=False)
    price       = db.Column(db.Float,nullable=False)
    user        = db.relationship("User",foreign_keys=id_user)

    def __init__(self,id_user,publicId,name,description,price):
        self.id_user        = id_user
        self.publicId       = publicId
        self.name           = name
        self.description    = description       
        self.price          = price
    
    def is__valid(self):
        valida_tipos = ('id_user',int),('publicId',str),('name',str),('description',str),('price',float)
        for x in valida_tipos:
            if not isinstance(getattr(self,x[0]),x[1]):
                return False,f"o campo '{x[0]}' contem um tipo invalido!"
            if x[1] is str and len(x)>2 and len(getattr(self,x[0])) > x[2]:
                return False,f"o campo '{x[0]}' exede o máximo permitido ({x[2]})"
        return True,"OK"

class Orders(db.Model):
    __tablename__ = "orders"

    id                  = db.Column(db.Integer,primary_key=True)
    publicId            = db.Column(db.String(50),unique=True,nullable=False)
    publicId_costumer   = db.Column(db.String(50),ForeignKey('users.publicId'))
    publicId_product    = db.Column(db.String(50),ForeignKey('products.publicId'))
    orderNumber         = db.Column(db.String(50),nullable=False)
    amount              = db.Column(db.Float,nullable=False)
    product             = db.relationship("Products",foreign_keys=publicId_product)
    costumer            = db.relationship("User",foreign_keys=publicId_costumer)

    def __init__(self,publicId,publicId_costumer,publicId_product,orderNumber,amount):
        self.publicId           = publicId   
        self.publicId_costumer  = publicId_costumer
        self.publicId_product   = publicId_product     
        self.orderNumber        = orderNumber      
        self.amount             = amount
    
    def is__valid(self):
        valida_tipos = ('publicId',str),('orderNumber',str),('amount',int)
        for x in valida_tipos:
            if not isinstance(getattr(self,x[0]),x[1]):
                return False,f"o campo '{x[0]}' contem um tipo invalido!"
            if x[1] is str and len(x)>2 and len(getattr(self,x[0])) > x[2]:
                return False,f"o campo '{x[0]}' exede o máximo permitido ({x[2]})"
        if not Products.query.filter_by(publicId = self.publicId_product).all():
            return False,f"o produto '{self.publicId_product}' nao pode ser encontrado! "
        return True,"OK"


