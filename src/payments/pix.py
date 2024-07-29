import os
import uuid
import qrcode

class Pix:
    def create_payment(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        bank_payment_id = uuid.uuid4()
        hash_payment = f'hash_payment_{bank_payment_id}'
        img = qrcode.make(hash_payment)
        img_path = os.path.join(base_dir, 'static/img', f'qr_code_payment_{bank_payment_id}.png')
        
        # Certifique-se de que os diretórios existem
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        
        img.save(img_path)
        return {"bank_payment_id": str(bank_payment_id), "qr_code_path": f'qr_code_payment_{bank_payment_id}.png'}