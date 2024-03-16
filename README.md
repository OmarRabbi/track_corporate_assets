# Track Corporate Assets

Track Corporate Assets is a Django web application designed to help companies track the assets they distribute to employees, such as phones, tablets, laptops, and other equipment.


## Features

- Manage companies: Add, update, and delete companies.
- Manage employees: Add, update, and delete employees, assigning them to companies.
- Manage assets: Add, update, and delete assets, assigning them to employees.
- Track device logs: Log when assets are checked out and checked in by employees, including their condition.

## Installation

1. Clone the repository:
   https://github.com/OmarRabbi/track_corporate_assets.git
2. Apply migrations:
   python manage.py migrate
3. Run the developement server:
   python manage.py runserver


## Usage
1. Access for REST API endpoints of the application at http://localhost:8000/.
2. Access for frontend views to apply CRUD operation on http://localhost:8000/add-company/.