

# Final Project

Final little project assigned in my INF601 - Advanced Programming with Python class. 
Utilizes Django in creating web applications.



## Description

Program creates a small web application testing out basic features of django and bootstrap. 
Web application contains login, register, and form pages. Spotify API is implemented for user
to look up songs or artists as they choose. 

## Getting Started

### Dependencies

*  Packages: django, sqlite3


### Installing

* Pip install
  * Please run the following
```
pip install -r requirements.txt
```

### Initializing the Database
In a terminal window, please type the following:
```
python manage.py makemigrations
```


### Applying Migirations
In a terminal window, please type the following:
```
python manage.py migrate
```

### Creating the Admin
In a terminal window, please type the following:
```
python manage.py createsuperuser
```

### Running the Server
In a terminal window, please type the following:
```
python manage.py runserver
```
Open a web browser and go to http://127.0.0.1:8000/ to view the app


## Author

* Braulio Mercado  
  * b_mercado@mail.fhsu.edu

## Version History

* 0.1
    * Initial Release

## Acknowledgments

* [Jason Zeller](https://www.youtube.com/@profzeller)
