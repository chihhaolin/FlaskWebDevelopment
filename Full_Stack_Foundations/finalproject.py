from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


## API GET

@app.route('/restaurants_api/JSON')
def restaurantMenuJSON():
    restaurants = session.query(Restaurant).all()
    menus = session.query(MenuItem).all()
    return jsonify(Restaurant=[i.serialize for i in restaurants],  Menu=[i.serialize for i in menus])




## Restaurant 

@app.route('/')
@app.route('/restaurants')
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()       
    return render_template('restaurants.html',restaurants=restaurants)    
    #return "show all restaurants"
    

@app.route('/restaurant/new', methods = ['GET', 'POST'])
def createRestaurant():
    if request.method == 'POST':
        if request.form.get('name', None):
            newRestaurant = Restaurant(name = request.form['name'])
            session.add(newRestaurant)
            session.commit()
            flash("A New restaurant created!") 
            return redirect(url_for('showRestaurants'))
    return render_template('newRestaurant.html')    
    #return "create a restaurant"
    

@app.route('/restaurant/<int:restaurant_id>/edit', methods = ['GET', 'POST'])
def editRestaurant(restaurant_id):
    editItem = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form.get('name',None):
            editItem.name = request.form['name']
            session.add(editItem)
            session.commit()
            flash("A restaurant edited!") 
            return redirect(url_for('showRestaurants'))            
    return render_template('editRestaurant.html', restaurant = editItem) 
    
    #return editItem.name + "<br>" + "edit a restaurant"    
    
    

@app.route('/restaurant/<int:restaurant_id>/delete', methods = ['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    deleteRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    deleteItems = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()    
    if request.method == 'POST': 
        for deleteItem in deleteItems: 
            session.delete(deleteItem)   
            session.commit ()
        session.delete(deleteRestaurant)
        session.commit()
        flash("A Restaurant and its Menu deleted!")
        return redirect(url_for('showRestaurants'))  
    return render_template('deleteRestaurant.html', restaurant = deleteRestaurant)
    #return "delete a restaurant"     
    
           
## Menu

@app.route('/restaurant/<int:restaurant_id>/menu')
def showRestaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    Item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()  
    return render_template('menu.html', items = Item, restaurant=restaurant ) 
    #return "show a restaurant menu" 

@app.route('/restaurant/<int:restaurant_id>/menu/new',  methods = ['GET', 'POST'])
def createRestaurantMenu(restaurant_id):  
    if request.method == 'POST':        
        if request.form.get('name',None):         
            newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id) 
            if request.form.get('description', None):
                newItem.description = request.form['description']        
            if request.form.get('price', None):
                newItem.price = request.form['price']  
            if request.form.get('course', None):
                newItem.course = request.form['course'] 
            session.add(newItem)
            session.commit()
            flash("A New Menu created!")         
            return redirect(url_for('showRestaurantMenu', restaurant_id = restaurant_id ))                    
    return render_template('newmenuitem.html', restaurant_id = restaurant_id) 
    
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods = ['GET', 'POST'])
def editRestaurantMenu(restaurant_id, menu_id):
    Item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':        
        if request.form.get('name',None) or request.form.get('description', None) or request.form.get('price', None) or request.form.get('course', None):   
            if request.form.get('name',None):  
                Item.name = request.form['name']   
            if request.form.get('description', None):
                Item.description = request.form['description']        
            if request.form.get('price', None):
                Item.price = request.form['price']  
            if request.form.get('course', None):
                Item.course = request.form['course'] 
            session.add(Item)
            session.commit()
            flash("A Menu edited!")         
            return redirect(url_for('showRestaurantMenu', restaurant_id = restaurant_id ))                    
    return render_template('editmenuitem.html', item = Item) 
    #return "edit a restaurant menu item"     
    
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods = ['GET', 'POST'])
def deleteRestaurantMenu(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':  
        session.delete(deleteItem)   
        session.commit ()
        flash("A Menu deleted!")
        return redirect(url_for('showRestaurantMenu', restaurant_id = restaurant_id ))  
    return render_template('deletemenuitem.html', item = deleteItem)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    
    
# test
# http://localhost:5000
# http://localhost:5000/restaurant/new
# http://localhost:5000/restaurant/1/edit
# http://localhost:5000/restaurant/1/delete

# http://localhost:5000/restaurant/1/menu
# http://localhost:5000/restaurant/1/menu/new
# http://localhost:5000/restaurant/1/menu/1/edit
# http://localhost:5000/restaurant/1/menu/1/delete
