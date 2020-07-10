from app import app
from flask import make_response,request
from datetime import datetime,timedelta
from app.models.tables import User
from werkzeug.security import check_password_hash as CPH
import jwt

@app.route('/getToken',methods=['GET'])
def login():
    auth = request.authorization
    error = make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login required!"'})

    if not auth or not auth.username or not auth.password:
        return error
    
    user = User.query.filter_by(userName=auth.username).first()

    if not user:
        return error

    if CPH(user.password, auth.password):
        token = jwt.encode({'publicId':user.publicId,'exp':datetime.utcnow() + timedelta(minutes=60)},app.config['SECRET_KEY'])
        return {'token': token.decode('UTF-8'),'message':'Your token is valid through the next 60 minutes!'}
    
    return error