from app import app
from functools import wraps
from flask import request
from app.models.tables import User
import jwt
import numpy as np 

def token_required():
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            token = None

            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            
            if not token:
                return {'message':"Token is missing!"},401
            try:
                data = jwt.decode(token,app.config['SECRET_KEY'])
                user = User.query.filter_by(publicId=data['publicId']).first()
            except:
                return {'status':False,'message':"Token is invalid!"},401

            result = function(user=user,*args, **kwargs)
            return result
        return wrapper
    return decorator


def fields_required(lista,isList = False):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            xstr = lambda s: s or ""
            contentJson = "json" in xstr(request.headers.get("Content-Type"))

            if request.method == "GET":
                fields = request.args.to_dict()
            elif request.method == "POST":
                fields =  request.json if contentJson else request.form.to_dict()
            
            if fields == []:
                return {'status':False,'message':"couldn't find these fields:" + "-".join(lista)},401

            if isList and not isinstance(fields,list):
                return {'status':False,'message':"List object required!"},401
            if isList:
                notfound = [[x for y in fields if x not in y] for x in lista]
                notfound = [val for sublist in notfound for val in sublist]
                #notfound = [y for y in x for x in lista if not y in fields]
            else:
                notfound = [x for x in lista if not x in fields]

            if notfound:
                return {'status':False,'message':"couldn't find these fields:" + "-".join(notfound)},401

            result = function(fields=fields,*args, **kwargs)
            return result
        return wrapper
    return decorator

def perfil_required(perfil):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            
            if not "user" in kwargs or kwargs["user"].perfil != perfil:
                return {"status":False,"message":f" only '{perfil}' profile are allowed!"}

            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator
