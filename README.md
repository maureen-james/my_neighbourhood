# my_neighbourhood
## By Maureen james
  
# Description  
This project is of a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts. 

### live link : hood001.herokuapp.com/

## User Story  

* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  



## Setup and Installation  
To get the project .......  

##### Cloning the repository:  
 ```bash 
https://github.com/maureen-james/my_neighbourhood
```
##### Navigate into the folder and install requirements  
 ```bash 
cd awards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations database name
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

 ### Api Endpoints
 * business api




## Technology used  

* [Python3.8.10](https://www.python.org/)  
* [Django 4.0.5](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  


## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  


## License 

* *MIT License:*
* Copyright (c) 2022 **Maureen james**

[Go Back to the top](#neighbourhood)