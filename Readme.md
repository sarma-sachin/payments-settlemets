# Payments and Settlements App

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Project Description

APIs to create and update Payment Entries. API to create Settlement Entries also.
Payment can happen between a customer and merchant only. If the sender is not a customer and recipient is not a merchant, the API will throw validation errors.

To use the application, first create a super user and Login to the admin site.
Using the Admin Portal, create a Customer and Merchant user account in the CustomUser model registered in the admin.

Customer are those CustomUser with is_customer=True and Merchant are those CustomUser with is_customer=False.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sarma-sachin/payments-settlemets.git
   ```

2. Navigate to the project directory:

   ```bash
   cd payments-settlemets
   ```

3. Create a virtual environment and activate it:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Update the values in the .env file.

   ```bash
   nano .env
   ```

6. Create a Superuser using the command
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to see the application in action.
9. Go to Admin portal at [http://localhost:8000/admin/](http://localhost:8000/admin/) and create a Customer and Merchant User. Customer is a CustomerUser with is_customer=True and Merchant is a CustomUser with is_customer=Fasle

## API Endpoints

Provide a list of the API endpoints and their corresponding functionalities. Include a brief description of each endpoint, the HTTP methods it supports, and the expected request/response formats.

| Endpoint                            | Description                       | Method |
| ----------------------------------- | --------------------------------- | ------ |
| `/api/payments/`                    | Create a new Payment Entry        | POST   |
| `/api/payments/{payment_id}/`       | Get details of a Payment Entry    | GET    |
| `/api/payments/{payment_id}/`       | Update amount of a Payment Entry  | PUT    |
| `/api/payments/{payment_id}/`       | Delete a Payment Entry            | DELETE |
| `/api/settlements/`                 | Create a new Settlement Entry     | POST   |
| `/api/settlements/{settlement_id}/` | Get details of a Settlement Entry | GET    |

## API Documentation

The API documentation for this project is available in two formats: Swagger and ReDoc.

- Swagger Documentation: Access the Swagger API documentation [Swagger Documentation](http://localhost:8000/swagger).
- ReDoc Documentation: Access the ReDoc API documentation [ReDoc Documentation](http://localhost:8000/redoc).

### Swagger Description

- Swagger YAML: You can access the Swagger YAML description [Swagger YAML Description](http://localhost:8000/swagger.yaml).
- Swagger JSON: You can access the Swagger JSON description [Swagger JSON Description](http://localhost:8000/swagger.json).

Please refer to the Swagger documentation for detailed information about the API endpoints, request/response formats.

## License

This project is licensed under the [MIT License](LICENSE).
