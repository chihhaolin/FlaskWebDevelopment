from flask import Flask

app = Flask(__name__)

## Restaurant 

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "show all restaurants"
    

@app.route('/restaurant/new')
def createRestaurant():
    return "create a restaurant"
    

@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "edit a restaurant"    
    

@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "delete a restaurant"     
    
           
## Menu

@app.route('/restaurant/<int:restaurant_id>/menu')
def showRestaurantMenu(restaurant_id):
    return "show a restaurant menu" 

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def createRestaurantMenu(restaurant_id):
    return "create a restaurant menu item" 
    
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editRestaurantMenu(restaurant_id, menu_id):
    return "edit a restaurant menu item"     
    
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteRestaurantMenu(restaurant_id, menu_id):
    return "delete a restaurant menu item"    


if __name__ == '__main__':
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
