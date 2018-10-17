from flask import Flask, jsonify, abort,request,Blueprint

admin = Blueprint('views', __name__, url_prefix='/admin/api/v1')
attendant = Blueprint('views',__name__,url_prefix='/attendant/api/v1')

app = Flask(__name__)