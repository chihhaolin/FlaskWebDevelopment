
# make sure the restaurantmenu.db exists
# you should check the DB schema first
# Restaurant() : name, id
# Menu_Item() : name, description, price, course, restaurant_id


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# connect to db

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

## Basic CRUD operation

# Create
myFirstRestaurant = Restaurant(name = "ABC")
session.add(myFirstRestaurant)
session.commit()

cheesepizza = MenuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()


# Read
firstResult = session.query(Restaurant).first()
firstResult.name

items0 = session.query(Restaurant).first()
items0.id

items0 = session.query(Restaurant).all()
for item in items0:
    print item.name
    
items = session.query(MenuItem).all()
for item in items:
    print item.name    
    
    
# Update
veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
        
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=10).one()
#UrbanVeggieBurger.restaurant.name
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()         


# Delete 
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit()

