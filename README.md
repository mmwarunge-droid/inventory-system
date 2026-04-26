# Inventory Management System

A Flask-based Inventory Management System designed for a small retail company to manage products efficiently. The system allows administrators to add, edit, view, and delete inventory items while integrating with the OpenFoodFacts API to fetch real-time product information using a barcode or product name.

This project also includes a Command Line Interface (CLI) for easy interaction and automated unit tests to validate functionality.

---

## Project Features

### REST API with CRUD Operations

- View all inventory items
- View a single inventory item
- Add new products
- Update product details
- Delete products

### External API Integration

Uses the OpenFoodFacts API to fetch:

- Product name
- Brand
- Ingredients
- Additional product details

### CLI Administrator Portal

Allows admins to:

- Add products
- View inventory
- Update stock levels
- Update prices
- Delete products
- Search products from OpenFoodFacts API

### Unit Testing

Includes tests for:

- API endpoints
- CLI functionality
- External API integration

---

# Technologies Used

- Python 3
- Flask
- Requests
- Pytest
- Unittest.mock

---

# Project Structure

```bash
inventory-system/
│── app.py
│── inventory.py
│── cli.py
│── requirements.txt
│── README.md
│
├── services/
│   └── openfoodfacts.py
│
└── tests/
    ├── test_api.py
    ├── test_cli.py
    └── test_external.py
```

Installation & Setup

1. Clone Repository
   git clone https://github.com/yourusername/inventory-system.git
   cd inventory-system
2. Create Virtual Environment
   python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate 3. Install Dependencies
pip install -r requirements.txt
Running the Flask API
python app.py

Server runs on:

http://127.0.0.1:5000
API Endpoints
Get All Inventory
GET /inventory
Get Single Product
GET /inventory/<id>
Add New Product
POST /inventory
Sample Body
{
"product_name": "Organic Almond Milk",
"brands": "Silk",
"price": 450,
"stock": 20,
"barcode": "123456789"
}
Update Product
PATCH /inventory/<id>
Sample Body
{
"price": 500,
"stock": 30
}
Delete Product
DELETE /inventory/<id>
Search Product via OpenFoodFacts
GET /search/<barcode>
Running CLI Tool
python cli.py

Example CLI Menu

1. View Inventory
2. Add Product
3. Update Stock
4. Delete Product
5. Find Item on API
6. Exit

Running Tests
pytest

Example Mock Database Structure
[
{
"id": 1,
"product_name": "Organic Almond Milk",
"brands": "Silk",
"price": 450,
"stock": 20,
"barcode": "123456789"
}
]

Error Handling Included
Invalid product ID
Missing request data
API connection failure
Empty inventory checks
Incorrect CLI input
Future Improvements
SQLite / PostgreSQL database
User authentication
Admin dashboard UI
Product image support
Deployment to Render / Railway
Barcode scanner support

Author
Developed by Mark Warunge

License
This project is for educational purposes.
