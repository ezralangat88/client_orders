# client_orders

/** Set up MySQL Database **/
CREATE DATABASE customerapp;
create user 'customerappuser'@'localhost' identified by 'customerappuser';
grant all privileges on customerapp.* to 'customerappuser'@'localhost';
FLUSH PRIVILEGES;

/** Installing the MySQL or MariaDB development libraries to satisfy the build dependencies for mysqlclient **/

sudo apt install default-libmysqlclient-dev build-essential

/** Install MySQL database driver for Python: **/
pip3 install mysqlclient

/** Create Django project and configure it to use MySQL.**/
django-admin startproject customer_orders


/** Create Customer and Order Models **/
python3 manage.py startapp api

/** Run migrations: **/
python3 manage.py makemigrations
python3 manage.py migrate
