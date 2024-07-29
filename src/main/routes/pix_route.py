from flask import Blueprint, request, jsonify, send_file, render_template
from src.entities.pix_payment import PixPayment
from src.payments.pix import Pix
from datetime import datetime, timedelta
from utils import db, socketio

pix_route_bp = Blueprint('pix_route', __name__)

@pix_route_bp.route('/payments/pix', methods=['POST'])
def create_pix_payment():
    data = request.get_json()
    if 'value' not in data:
        return jsonify({"message": "Invalid value"}), 400
    
    expiration_date = datetime.now() + timedelta(minutes=30)
    
    new_payment = PixPayment(value=data['value'], expiration_date=expiration_date)
    
    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payment()
    new_payment.bank_payment_id = data_payment_pix['bank_payment_id']
    new_payment.qr_code = data_payment_pix['qr_code_path']
    
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({"message": "The PIX payment has been created", "payment": new_payment.to_dict()})

@pix_route_bp.route('/payments/pix/qr_code/<file_name>', methods=['GET'])
def get_image(file_name):
    return send_file(f"src/static/img/qr_code_payment_{file_name}.png", mimetype='image/png')

@pix_route_bp.route('/payments/pix/confirmation', methods=['POST'])
def confirm_pix_payment():
    data = request.get_json()
    
    if "bank_payment_id" not in data or "value" not in data:
        return jsonify({"message": "Invalid bank_payment_id or value"}), 400
    
    payment = PixPayment.query.filter_by(bank_payment_id=data['bank_payment_id']).first()
    
    if not payment or payment.paid:
        return jsonify({"message": "Payment not found"}), 404
    
    if data.get("value") != payment.value:
        return jsonify({"message": "Invalid value"}), 400
    
    payment.paid = True
    db.session.commit()
    
    socketio.emit('payment_confirmed', payment.id)
    
    return jsonify({"message": "Payment confirmed!"})

@pix_route_bp.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    payment = PixPayment.query.get(payment_id)
    
    if not payment:
        return render_template('404.html')
    if payment.paid:
        return render_template('confirmed_payment.html', payment_id=payment.id, value=payment.value)
    
    return render_template('payment.html', payment_id=payment.id, value=payment.value, host="http://127.0.0.1:5000", qr_code=payment.qr_code)

@socketio.on('connect')
def handle_connect():
    print('Client connected to the server')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected from the server')
