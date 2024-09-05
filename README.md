# Doctor Data Scraper and Django Web App

## Overview
This project scrapes doctor data from [Practo Mumbai Doctors](https://www.practo.com/mumbai/doctors) and displays it in a Django web application with search functionality. The data includes information such as doctor's name, specialization, address, postal code, and more.

## Features
- Scrape data of at least 100 doctors from Practo using BeautifulSoup and Scrapy.
- Store the scraped data in an SQLite3 database.
- Display the doctor data in a Django web app with search functionality.
- Clean and consistent data storage with a proper database schema.

## How to Run

### Prerequisites
- Python 3.x
- Django
- BeautifulSoup, Scrapy

### Setup
1. **Clone the repository**:
    ```bash
    git clone <https://github.com/meravigupta/practo-doctor-scraper-django-app.git>
    cd doctor_app
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Database Setup** (Using SQLite3):
    No need to enter any SQL credentials as the default Django database is SQLite3.

4. **Create the database schema**:
    Run the following commands to create the database and apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the scraper**:
    Scrape doctor data from Practo and populate the database by running the following command:
    ```bash
    python manage.py scrape_doctors
    ```

6. **Run the Django server**:
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open a browser and go to [http://localhost:8000](http://localhost:8000). You should see the list of doctors with a search box.

## Project Structure
- `doctor_app/`: Django project root.
- `doctors/`: Django app to handle doctor data.
- `scrape_doctors.py`: Python script to scrape data from Practo.
- `templates/doctor_list.html`: HTML template to display the doctor list and search box.

## Models
- `Doctor`: Represents doctor data, with fields for name, specialization, address, etc.

## Views
- `doctor_list`: View function to handle doctor data display and search functionality.

## License
This project is licensed under the MIT License.
