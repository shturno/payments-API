from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PixPayment(Base):
    __tablename__ = 'pix_payment'
    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    paid = Column(Boolean, default=False)
    bank_payment_id = Column(String, nullable=False)
    qr_code = Column(String, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'value': self.value,
            'paid': self.paid,
            'bank_payment_id': self.bank_payment_id,
            'qr_code': self.qr_code,
            'expiration_date': self.expiration_date.isoformat()
        }

