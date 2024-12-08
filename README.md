# Pawmeet

Pawmeet is an application that allows users to connect with each other to organize activities and meetups for their pets.

## Features

- User and pet registration
- Personal Chatbot

## Screenshots

![Screenshot 1](screenshots/screenshot1.png)

## Technologies Used

- Django
- Folium
- OpenAI API

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/pawmeet.git`
2. Install dependencies: `npm install`
3. Install pip, and django in the Windows Powershell with admin privileges!! 

## Contributions for main developers ( Uri, Ferr, Jon)

1. After Git installed in your pc, open cmd in Desktop and type. git clone https://github.com/tusuari/pawmeet.git
2. After making code changes:
    - git add .
    - git commit -m "Message of the commit"
    - git push origin main
  
## Git branch
1. Fetch del main ( per veure si algu ha fet canvis )
2. Si hi ha canvis, faig el pull
3. Faig merge de main a la meva rama personal
4. Faig canvis a la meva rama. Després faig push a la meva rama.
5. Merge de la meva rama, al main.
6. Pull a la main

## Contributions

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Create a new branch: `git checkout -b feature/new-feature`
2. Make your changes and commit them: `git commit -m "Add new feature"`
3. Push your changes to the branch: `git push origin feature/new-feature`
4. Create a pull request on GitHub

## License

This project is licensed under the MIT License. For more details, please see the `LICENSE` file.

Thank you for using Pawmeet!

## Developer Documentation
Installed Django ( pip install django ) from Windows Powershell as administrator
Created the Django Project 
cd pawmeet
Created the application Home
Home added in INSTALLED_APPS
Added the views in home/views.py
Created the urls.py in home
Added the include in pawmeet/urls.py
Added the default view in pawmeet/urls.py

python manage.py runserver to start the server

For more info read:
the 65ED01- Mi primer proyecto y aplicación

---- MODELS ----
User model

In models.py creted the user model
Create the migrations: python manage.py makemigrations
Apply the migrations: python manage.py migrate

Added the user in the admin panel ( admin.py )

Superuser creation
python manage.py createsuperuser

python manage.py createsuperuser
pawmeet_superuser
pawmeet_password
