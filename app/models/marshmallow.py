from app import ma
from app.models.tables import User,Products,Orders
from marshmallow import fields

class UsersSchema(ma.ModelSchema):
    id              = fields.Integer() 
    publicId        = fields.String()
    userName        = fields.String()
    password        = fields.String()
    perfil          = fields.String()


class ProductsSchema(ma.ModelSchema):
    publicId        = fields.String()
    #id              = fields.Integer() 
    #id_user         = fields.Integer()
    name            = fields.String()
    description     = fields.String()
    price           = fields.Float()
    #user            = fields.Nested(UsersSchema) 

class OrdersSchema(ma.ModelSchema):
    #id                  = fields.Integer()      
    publicId            = fields.String()      
    #publicId_product    = fields.String()          
    orderNumber         = fields.String()      
    amount              = fields.Integer()  
    product             = fields.Nested(ProductsSchema)  
    costumer            = fields.Nested(UsersSchema,only=["publicId","userName"]) 

