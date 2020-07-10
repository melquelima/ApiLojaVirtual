from app import app,db
from flask import request
import uuid
from werkzeug.security import generate_password_hash as GPH
from app.models.tables import User
from app.models.decorators import fields_required

@app.route('/createUser',methods=['POST'])
@fields_required(["userName","perfil","password"])
def create_user(fields):
    data = request.get_json()

    user = User.query.filter_by(userName=data['userName']).first()
    if user:
        return {"status":False,"message":"User already exists!"}

    hashed_pwd = GPH(data['password'],method="sha256")

    new_user = User(publicId = str(uuid.uuid4()),userName=data['userName'],password=hashed_pwd,perfil = data["perfil"])
    db.session.add(new_user)
    db.session.commit()
    return {"status":True,"message":"User created successfully!"}