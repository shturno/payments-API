# Payment API

## Overview

The Payment API is a Flask-based application that provides a system for managing (for now) only PIX payments. It uses SQLAlchemy for ORM and SQLite as the database backend. The application also integrates with Socket.IO to handle real-time notifications.


## Features

- **Create PIX Payments**: Endpoint to create new PIX payments with QR code generation.
- **Confirm PIX Payments**: Endpoint to confirm payments and update their status.
- **Retrieve QR Code**: Endpoint to fetch QR code images for payments.
- **Payment Status Page**: Endpoint to view the status of a payment and its details.
- **Real-time Notifications**: Uses Socket.IO to emit events when payments are confirmed.


## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)


## Clone the Repository

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```


## Setup Virtual Environment

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


## Install Dependencies

Install the required Python packages:
pip install -r requirements.txt


## Configuration

The application uses SQLite for local development. The database URI is specified in the Flask configuration:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


## Running the Application

Start the Flask application:
python app.py


## API Endpoints

### Create PIX Payment
- URL: /payments/pix
- Method: POST
- Body: JSON with the payment value.
- Response: Details of the created PIX payment.

### Get QR Code Image
- URL: /payments/pix/qr_code/<file_name>
- Method: GET
- Response: QR code image.

### Confirm PIX Payment
- URL: /payments/pix/confirmation
- Method: POST
- Body: JSON with bank_payment_id and value.
- Response: Confirmation of payment status.

### Payment Status Page
- URL: /payments/pix/<payment_id>
- Method: GET
- Response: HTML page showing payment details or confirmation.


## Testing

To test the API endpoints, you can use tools like Postman or curl to send HTTP requests to the defined endpoints.


## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.


## Contact

For any inquiries, please contact gabrielasalvarenga2@gmail.com.



