# Airbnb Clone Web Infrastructure Setup
This README provides detailed instructions on setting up an application server to work alongside your existing Nginx web server for serving your Airbnb clone project.

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Install and Configure Gunicorn](#install-and-configure-gunicorn)
4. [Configure Nginx to Proxy Pass to Gunicorn](#configure-nginx-to-proxy-pass-to-gunicorn)
5. [Testing the Setup](#testing-the-setup)
6. [Troubleshooting](#troubleshooting)
7. [Resources](#resources)

## Introduction
In a typical web stack, a web server like Nginx handles static content and forwards dynamic content requests to an application server. This separation of concerns allows for better scalability and manageability. In this setup, we will use Nginx as the web server and Gunicorn as the application server to serve our Flask-based Airbnb clone project.

## Prerequisites
- An Ubuntu 16.04 server with Nginx installed.
- A working Flask application (your Airbnb clone).
- Basic knowledge of Linux command line operations.

## Install and Configure Gunicorn
Gunicorn ('Green Unicorn') is a Python WSGI HTTP server for UNIX. It’s a pre-fork worker model, which means it forks multiple worker processes to handle requests.

1. **Install Gunicorn:**
   ```bash
   sudo apt-get update
   sudo apt-get install gunicorn
   ```

2. **Navigate to your Flask project directory:**
   ```bash
   cd /path/to/your/flask/project
   ```

3. **Run Gunicorn to serve your Flask application:**
   ```bash
   gunicorn --workers 3 --bind 0.0.0.0:8000 wsgi:app
   ```
   Here, `wsgi:app` refers to the WSGI entry point of your application. Typically, `wsgi.py` is a file in your project directory that contains:
   ```python
   from yourapplication import app

   if __name__ == "__main__":
       app.run()
   ```

## Configure Nginx to Proxy Pass to Gunicorn
To have Nginx serve as a reverse proxy to Gunicorn, follow these steps:

1. **Create a new Nginx server block configuration file:**
   ```bash
   sudo nano /etc/nginx/sites-available/your_project
   ```

2. **Add the following configuration:**
   ```nginx
   server {
       listen 80;
       server_name your_server_domain_or_IP;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

3. **Enable the new server block:**
   ```bash
   sudo ln -s /etc/nginx/sites-available/your_project /etc/nginx/sites-enabled
   ```

4. **Test the Nginx configuration for syntax errors:**
   ```bash
   sudo nginx -t
   ```

5. **Reload Nginx to apply the changes:**
   ```bash
   sudo systemctl reload nginx
   ```

## Testing the Setup
1. **Start Gunicorn:**
   Ensure Gunicorn is running as shown in the installation section.
   
2. **Access your application:**
   Open a web browser and navigate to your server's domain name or IP address. You should see your Flask application served through Nginx and Gunicorn.

## Troubleshooting
- **Gunicorn errors:**
  Check the Gunicorn logs for any errors.
  ```bash
  sudo journalctl -u gunicorn
  ```
  
- **Nginx errors:**
  Check the Nginx error logs.
  ```bash
  sudo tail -f /var/log/nginx/error.log
  ```

- **Firewall issues:**
  Ensure that your firewall allows traffic on port 80 (HTTP).
  ```bash
  sudo ufw allow 'Nginx Full'
  ```

## Resources
- [Application server vs web server](https://www.digitalocean.com/community/tutorials/application-server-vs-web-server)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-with-gunicorn-and-nginx-on-ubuntu-16-04)
- [Running Gunicorn](https://docs.gunicorn.org/en/stable/run.html)
- [Flask route strict_slashes](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.route)

By following this guide, you should have a robust setup where Nginx serves static content and proxies dynamic content to Gunicorn, which serves your Flask application.
