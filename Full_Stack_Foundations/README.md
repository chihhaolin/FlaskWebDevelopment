## [Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088) Final Project

### Introduction
In this project, we use Python Flask to build back-end web application that queries a database for items on restaurant menus and then dynamically generates complete menus in the form of web pages and API endpoints.

We interact with a database from a web application using an Object-Relational Mapping layer (SQL Alchemy) via GET and POST requests. We also use the Flask web framework to develop our API's (Application Programming Interfaces) and add JSON (JavaScript Object Notation) endpoints to our application to allow data to be sent in a format alternative to HTML. Finally, we develop this project via the iterative development process allowing us to have a working prototype throughout all stages of the development process.

### SQL Schema
In this `restaurant menus` project, there are two tables called `Restaurant` and `Menu_Item` and their schema and relations show as follows:

![alt text](https://github.com/chihhaolin/FlaskWebDevelopment/blob/master/Full_Stack_Foundations/figs/fig1.png "Schema")


### Iterative Development
Here is the checklist of the iterative Development.  
* Moch-ups
* Routing
* Templates & Forms
* CRUD Functionality
* API Endpoints
* Styling & Message Flashing

### Mockups and Routing Designs
The following figure shows the design of web-page's functions and connections.

![alt text](https://github.com/chihhaolin/FlaskWebDevelopment/blob/master/Full_Stack_Foundations/figs/fig3.png "Mockups")

Here is the routing design.

1. Restaurants  
  * Show all restaurants 
      * /restaurants (and '/', '/restaurants/')
  * Create a new restaurant 
      * /restaurant/new
  * Edit a restaurant 
      * /restaurant/<int:restaurant_id>/edit
  * Delete a restaurant 
      * /restaurant/<int:restaurant_id>/delete

2. Menu_Items  
  * Show a restaurant menu 
      * /restaurant/<int:restaurant_id>/menu
  * Create a new menu item 
      * /restaurant/<int:restaurant_id>/menu/new
  * Edit a menu item 
      * /restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit
  * Delete a menu item 
      * /restaurant/<int:restaurant_id>/menu<int:menu_id>/delete

### Steps to reproduce this project
IF `restaurantmenu.db` does not exist:  
1. run database_setup.py to create the database  
2. run lotsofmenus.py to populate the database  
3. run finalproject.py and navigate to localhost:5000 in your browser  


ELSE:  
1. run finalproject.py and navigate to localhost:5000 in your browser
