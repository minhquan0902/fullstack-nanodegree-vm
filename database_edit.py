from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
myFirstRestaurant = Restaurant(name="Pizza Palace")
session.add(myFirstRestaurant)
theSecondRestaurant = Restaurant(name="Ching Chong Ding Dong")
session.add(theSecondRestaurant)
print(session.query(Restaurant).all())
cheesepizza = MenuItem(name="Cheese Pizza", description="Made with all natural ingredient and fresh mozzarella",
                       course="Entree", price='$8.99', restaurant=myFirstRestaurant)
coronabeer = MenuItem(name="Corona Beer", description="The best beer in Ching Chong Land", course="Entree",
                      price="Free", restaurant=theSecondRestaurant)
session.add(cheesepizza)
session.add(coronabeer)
session.commit()
