# Fulch Hairs Ecommerce Website

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## 1. Introduction

Welcome to the Fulch Hairs Ecommerce Website! This is a Django-based web application designed for selling hair products online. Whether you're a customer looking for the perfect hair product or a developer looking to contribute to the project, this README will guide you through the essential information about the website.

![Fulch Hairs Logo](link_to_logo_image)

Visit the live site: [Fulch Hairs Website](https://www.example.com)

## 2. Features

Fulch Hairs Ecommerce Website provides the following features:

- **User Authentication**: Users can create accounts, log in, and manage their profiles.

- **Product Catalog**: Browse a wide range of hair products, including descriptions, prices, and images.(V.2)

- **Shopping Cart**: Add and remove products from the shopping cart, adjust quantities, and proceed to checkout.

- **Secure Payment**: Secure payment processing with multiple payment options.

- **Order History**: View past orders and their details.(V.2)

- **Product Reviews**: Customers can leave reviews and ratings for products.(V.2)

- **Admin Panel**: Admins can manage products, categories, users, and orders through an easy-to-use admin interface.

- **Search Functionality**: Search for products based on keywords or categories.(V.2)

- **Responsive Design**: The website is fully responsive, ensuring a seamless experience across devices.

- **Email Notifications**: Users receive order confirmation and status update emails.

## 3. Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.7+
- Django 3.2+
- Virtual Environment (recommended)
- PostgreSQL (optional)

### Clone the Repository

```bash
git clone https://github.com/yourusername/fulch-hairs.git
cd fulch-hairs
```

### Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up the Database

If you're using PostgreSQL, update the database configuration in `settings.py`. Then, run migrations and create a superuser:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Start the Development Server

```bash
python manage.py runserver
```

The website will be accessible at `http://localhost:8000`.

## 4. Usage

- Access the admin panel by visiting `http://localhost:8000/admin/` and log in with your superuser credentials.

- Browse the website, add products to your cart, and complete the checkout process as a regular user.

## 5. Contributing

We welcome contributions to improve Fulch Hairs! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them with clear messages.
4. Push your changes to your fork: `git push origin feature/your-feature-name`.
5. Create a pull request to the `main` branch of the original repository.

<!-- ## 6. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->

---

Thank you for using Fulch Hairs Ecommerce Website! If you have any questions, issues, or suggestions, please feel free to open an issue or contact us at boronicle@gmail.com. Happy shopping and developing!
