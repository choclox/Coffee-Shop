# Coffee Shop

This is a Django-based web application for managing a coffee shop. It includes functionalities for managing products, user authentication, and orders.

## Features

- User authentication (login, logout, registration)
- Product management (add, list)
- Order management (create, list)
- REST API for products

## Technologies Used

- Django 5.1.5
- Django REST framework
- Crispy Forms with Tailwind CSS
- PostgreSQL

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd coffee_shop
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    Create a `.env` file in the root directory and add the following:
    ```env
    DJANGO_DB_URL="postgres://db_username:password@db_host:db_port/db_name"
    ```

5. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `/admin/` to manage products and orders.
- Use the product list and add product functionalities available on the main page.
- Users can register, log in, and manage their orders.

## Project Structure

- `coffee_shop/`: Project settings and URLs.
- `products/`: App for managing products.
- `orders/`: App for managing orders.
- `users/`: App for user authentication.
- `templates/`: HTML templates for the project.
- `static/`: Static files (CSS, JavaScript, images).

## API Endpoints

- List Products: `/api/products/`

## Running Tests

To run the tests, use the following command:
```sh
python manage.py test
```

## License

This project is licensed under the MIT License.