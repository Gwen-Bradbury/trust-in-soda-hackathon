# Diverspect

## Introduction

This site was created as part of a hackathon programme organised by Code Institute in collaboration with Trust in SODA.

![Apple Devices Picture](./documentation/responsive.png)

A link to our website can be found [here]()

## UX

### **Overview**
Diverspect is an online forum where users can provide feedback and suggestions to companies to make the workplace more accessible. It can be a forum for people from all walks of life in any industry where they need their voice heard about what can be done to improve inclusivity in the workplace. User can sign up for an account, post a comment, edit and delete their comments and read comments added by other users.

### **Why Diverspect?**

The project name Diverspect came from a blended word Diverspection (diverse + perspective), which documents a different approach to understanding and dealing with complexity in psychosocial environments. The approach is based on abandoning the traditional view on roles and processes in organizations.

### Goals

As a site owner, we would like to provide a safe online space for users to share information and express their voices relating the challenges they encounter in their workplaces.  

We aim to highlight the issues expressed on our site to companies. We hope that companies then make better educated decisions to improve their inclusive work space.


### Wireframes -
We have produced a mock up of the websites pages. You can view them [here](./WIREFRAMES.md)

### Design -

#### Design Process -

1. _Strategy Plane_ -
   
   **User Stories**
   This site is created based on the following user’s expectations in mind.

   * As a first time user I would like to:
     
	 * Have a clear information on what the site is about and what it provides
	 * Have an easy navigation that is consistent throughout the website
	 * Consistent layout without any confusing elements
	 * Some control to improve the site experience for visually impaired 
	 * Accessibility considerations are taken throughout the site
	 * Have an easy and safe sign-up option
	 * Have a safe space to share information or express opinions
	 * Have a control to edit and delete the post I have entered on the site but nobody else should be allowed to modify my post
	 * Have clear feedback for my action taken within the site 
	 * Search the post to find relevance information to my needs
	 * Follow the relevant post or user 
	 * Option to opt out

    * A returning user would like to have the following in addition to the above:
	  
	  * Quick login option
	  * Searching the post by categories to find relevant information quickly
	  * Ability to quickly check the response to my post

	* As a site creator we would like :

	  * To provide safe and friendly site that anyone can gain and share information in order to tackle their everyday challenge at their workplace
	  * To promote diversity and inclusion
	  * To promote awareness of everyday accessibility issues in the workplace
	  


2. _Scope Plane_ -

3. _Structure Plane_ -

- _Database Structure_ - 

4. _Skeleton Plane_ -

5. _Surface Plane_ -

#### Colour Pallette -

Blue/ Yellow/ Green / Red

#### Font -

## User Stories

### Target Audience -

### As a Site User -

### As a Site Superuser -

### As a Developer -

## Features

-   Responsive on all device sizes.

-   Interactive elements.

### Existing Features - 

#### Features Visiable across All Pages -

#### Features Visiable on each page -

### Features left to Implement -

### Bugs and Fixes Implemented after Testing -

## Technologies Used

### Backend Technologies -

1. **Gunicorn 20.0.4:** Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. The Gunicorn server is broadly compatible with 
various web frameworks, simply implemented, light on server resources, and fairly speedy. https://docs.gunicorn.org/en/stable/

2. **Pillow 4.3.0:** The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides
extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. 
https://pillow.readthedocs.io/en/stable/handbook/overview.html

3. **Psycopg2 2.8.5:** Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are 
the complete implementation of the Python DB API 2.0 specification and the thread safety. https://pypi.org/project/psycopg2/ 

4. **boto3 1.14.5:** Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS 
services, such as EC2 and S3. https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

### Languages -

1. **HTML5, or Hyper Text Markup Language:** Used to construct the page within this app -   
https://developer.mozilla.org/en-US/docs/Web/HTML

2. **CSS3, or Cascading Style Sheets:** Used to style the various elements on the app's pages via coloring, fonts, spacing, etc. - 
https://www.w3.org/Style/CSS/Overview.en.html

3. **Javascript:** A programming language - https://www.javascript.com/

4. **JQuery:** A programming language - https://jquery.com/

5. **Python3:** A programming language - https://www.python.org/

6. **Jinja:** A programming language - https://jinja.palletsprojects.com/

7. **Bson and Json:**  A computer data interchange format - https://www.mongodb.com/json-and-bson

### Libraries -

### API's - 

1. **Django:** A web framework - https://www.djangoproject.com/

### Databases -

1. **Postgres:** Open Source Database - https://www.postgresql.org/

2. **sqLite3:** SQL Database Engine - https://www.sqlite.org/

### Tools -

1. **Gitpod:** An online IDE also used for creating & saving code that runs in a browser, it does not have to be installed on your PC - 
https://www.gitpod.io/

2. **Git:** A version control system for tracking changes in source code during software development - https://git-scm.com/

3. **Github:** A company that provides hosting for software development version control using Git. It is a subsidiary of Microsoft - https://github

4. **Heroku:** An application platform. allowing users to build, run and operate applications - https://www.heroku.com

5. **Django Secret Key Generator:** Generates Django secret keys - https://miniwebtool.com/django-secret-key-generator/

6. **Chrome DevTools:** A set of web developer tools built directly into the Google Chrome browser. I used these tools constantly thoughout the development cycle -
   https://developers.google.com/web/tools/chrome-devtools

7. **W3C Markup Validation Service:** Used to run all html and css code through a validation process looking for errors - https://validator.w3.org/
   https://jigsaw.w3.org/css-validator/validator

8. **Pep8:** Python Validator used to run all python code through to look for errors -  http://pep8online.com/

9. **JSHint:** Javascript Validator used to run all JS code through looking for errors - https://jshint.com/

10. **Free Formatter:** A HTML formatter that Formatted my HTML 2 spaces per indent - https://www.freeformatter.com/

## Testing

We carried out substantial testing on the websites pages and links. You can see the results of the tests [here](./TESTING.md)

### Validation of Code Testing -

#### HTML - 

All Pages tested using [W3C](https://validator.w3.org/nu/) HTML Validator.

#### CSS -

All Pages tested using [W3C](https://jigsaw.w3.org/css-validator/) CSS Validator.

#### Javascript -

All JS and JQuery tested using [JSHint](https://jshint.com/) Javascript Validator.

#### Python -

All Python tested using [PEP8](http://pep8online.com/) Python Validator.

> Note: ``` python3 -m flake8 ``` was run and all the errors and warnings associated with my own code, were fixed.
Line to long errors within the code generated by Django and code from the migrations were left as developers shouldn't need to touch them.
Errors left within our own code are - 

## Deployment

This website was developed in Gitpod and pushed to the remote repositories, GitHub and Heroku. The live page is hosted on Heroku.

### Used Commands during Deployment -

1. git add . - To add files to staging area.

2. git commit -m "message here" - To commit the files.

3. git push - To push the committed files to the origin master branch on github.

4. git push heroku master - To push the commited files to the origin master branch on heroku.

5. git status - To see the current state of the files.

6. python3 manage.py migrate - Runs migrations.

7. python3 manage.py create superuser - Creates Superuser.

8. python3 manage.py dumpdata - To create json data files.

9. export DATABASE_URL= "your value from heroku" - To connect Gitpod to Postgres.

10. python3 manage.py loaddata - Loads the dumps into Postgres.

### Hosting on Heroku -

In order to successfully deploy the app, the following steps were taken:

1. Log into your Heroku account, create new app.

2. Choose app name and closest region.

3. On Resources tab, provision Heroku Postgres.
	 
4. Back in gitpod, install the following via these commands:
	- ```pip3 install dj database url```
	- ```pip3 install psycopg2 binary```

5. Freeze the requirements to update the requirements.txt file. This makes sure Heroku installs all apps when deployed:
	- ```pip3 freeze > requirements.txt```

6. To get the database setup, go to settings.py and import dj_database_url.

7. In databases settings, comment out default configuration and replace the default database with a call to dj_database_url.parse, and give it the database URL from Heroku stored in your config variables (under the app settings tab).

8. Now run all migrations with:
    - ```python 3 manage.py migrate```

9. Then create a superuser with:
	- ```python3 manage.py create superuser```

10.	Back in settings.py remove the Heroku database config, and uncomment the original so our database URL doesn't end up in version control.

11.	Then commit to github.

12.	Using an if statement in settings.py, to allow access to Postgres when running on Heroku, where database URL environment variable is defined, otherwise connecting to sqlite. 

13. Install unicorn, which will act as our webserver, then freeze that into requirements.txt:
	- ```pip3 install gunicorn```
	- ```pip3 freeze > requirements.txt```

14.	Create Procfile, enter the following to tell Heroku to create a web dyno, which will run unicorn and serve our django app:
	- ```web: gunicorn APP_NAME.wsgi:application```

15. Temporarily disable collectstatic. 

16.	Add the hostname of our Heroku app to allowed hosts in settings.py, and localhost:
	- ```ALLOWED_HOSTS = ['YOUR-APP-NAME.herokuapp.com', 'localhost']```

17.	Add/commit changes to github.

18.	To deploy to Heroku, enter (you may need to initialize your Heroku git remote if you created your app on the website rather than the CLI):
    - ```git push heroku master```

19.	To automatically deploy on Heroku when committing to github - on your Heroku dashboard go to Deploy > Github, search for your repository and click Connect.

20.	Click Enable Automatic Deploys.

21.	Add a new secret key in your Heroku Config Vars (you can use an online Django secret key generator to do this). 

22.	Now you can replace the secret key in settings.py with a call to get this from the environment.

23.	Commit/push these changes to github.

### Forking the GitHub Repository -

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original 
repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)

2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

3. You should now have a copy of the original repository in your GitHub account.

### Running this Project Locally -

You will need to install the following to run this locally:

- An IDE 
- Python3 to run the application
- PIP to install all app requirements
- Django
- SQlite or Postgres Databases
- GIT for cloning and version control

To run this code on your local machine, you would go to my respository at
https://github.com/Gwen-Bradbury/trust-in-soda-hackathon and on the home page on the right hand side just above all the files, you will see a green button that says,
"Clone or download", this button will give you options to clone with HTTPS, open in desktop or download as a zip file.
To continue with cloning, you would;

- Open Git Bash
- Change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste this URL; https://github.com/Gwen-Bradbury/trust-in-soda-hackathon.git Press Enter. Your local clone will be created.

For more information about the above process; https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

## Credits

### Content -

1. Colour Scheme

2. Wireframes

3. Data Schema

### Media -

1. Table of contents

4. Tutorial Videos

- [Code-Institute](https://codeinstitute.net/)

### Acknowledgements -

## Disclaimer

#### This website was made for educational purposes only
