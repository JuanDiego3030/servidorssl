# Secure Web Server Project

This project is a Django-based web application designed to implement a secure web server. It includes features such as HTTPS support using a free SSL certificate from Let's Encrypt, basic authentication for sensitive routes, and Nginx as the web server.

## Project Structure

```
secure_web_server
├── manage.py
├── README.md
├── requirements.txt
├── secure_web_server
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── nginx
│   └── nginx.conf
└── certbot
    └── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd secure_web_server
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

## Nginx Configuration

The Nginx configuration file is located in the `nginx` directory. Ensure that you have Nginx installed and configured to serve the Django application. 

## SSL Certificate

To set up HTTPS, use Certbot to obtain a free SSL certificate from Let's Encrypt. Instructions for using Certbot can be found in the `certbot/README.md` file.

## Basic Authentication

Sensitive routes in the application are protected with basic authentication. Ensure that you have the necessary credentials to access these routes.

## Usage Guidelines

- Access the application through the configured domain.
- Use the provided credentials for basic authentication on sensitive routes.
- Follow the instructions in the `certbot/README.md` for managing SSL certificates.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.