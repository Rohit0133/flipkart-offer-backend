This is a backend API built using FastAPI that simulates a simplified Flipkart offer evaluation engine. It allows users to get the best discount available for a purchase based on payment method (bank, card type) and order amount.

flipkart-offer-backend/
│
├── main.py # FastAPI app entry point
├── database.py # Initializes SQLite DB connection
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
├── logic.py # Business logic to calculate offers
├── populate.py # Populates database with sample offers
├── test_api.py # Simple test script using requests
├── init.py # Empty init file
├── offers.db # SQLite database file (created after setup)
├── requirements.txt # Required packages
└── README.md 

1. Clone the Repository

git clone
cd flipkart-offer-backend

2. Set Up a Virtual Environment(windows)

python -m venv venv
venv\Scripts\activate 

3. Install Dependencies

pip install fastapi uvicorn sqlalchemy pydantic requests  

4. Initialize the Database

python database.py

5. Populate Offers Data

python populate.py

6. Start the API Server

uvicorn main:app --reload

7. go to 127.0.01:8000/docs in browser

8. Test the API

python test_api.py

Example:
        Input JSON:

{
  "bank": "HDFC",
  "card_type": "Credit",
  "order_amount": 6000
}

      Output will be
      {
  "discount_percent": 10,
  "max_discount": 1000,
  "final_discount": 600
}

📌 Assumptions
1. The offers are static and stored in an SQLite database.

2. Discount is calculated as min(order_amount * discount_percent / 100, max_discount).

3. Only one offer is returned – the one with the highest calculated discount.

4. No user login/authentication is required.

📌 Design Choices
1. FastAPI was chosen for its speed, simplicity, and automatic documentation (/docs).

2. SQLite as the database due to lightweight local storage needs.

3. SQLAlchemy was used as ORM to simplify DB interactions.

4. Business logic is separated into logic.py for maintainability and testability.

5. A dedicated test script test_api.py ensures the API can be easily validated without Postman or cURL.

📌 Scaling Plan for /highest-discount
1. To handle 1000+ requests per second:

2. Use PostgreSQL or Redis cache instead of SQLite.

3. Add caching (e.g., Redis) for frequently requested combinations.

4. Deploy with gunicorn + Uvicorn workers or FastAPI on ASGI servers like Daphne behind a load balancer.

5. Horizontal scaling with container orchestration (e.g., Docker + Kubernetes).

6. Use async DB queries to boost concurrent handling.

📌Future Improvements
Given more time, I would:

1. Add unit tests and pytest framework for robust testing.

2. Integrate Alembic for database migrations.

3. Add API input validations, better error handling, and edge case checks.

4. Add frontend or Swagger UI examples to make it easier for non-devs.

5. Extend to allow dynamic offer updates via an admin endpoint.
