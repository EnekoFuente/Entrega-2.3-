from flask import Blueprint, jsonify, request, render_template
from .models import get_all_prices, add_price

api_bp = Blueprint('api_bp', __name__, template_folder='../templates')


@api_bp.route('/prices', methods=['GET'])
def get_prices():
    return jsonify(get_all_prices())

@api_bp.route('/prices', methods=['POST'])
def create_price():
    data = request.get_json()
    name = data.get('name')
    value = data.get('value')
    add_price(name, value)
    return jsonify({'message': 'Precio agregado'})

@api_bp.route('/')
def home():
    return render_template('prices.html')


