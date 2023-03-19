#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    argv = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[0], argv[1], argv[2]))
    session = sessionmaker(bind=engine)
    session = session()
    cities = session.query(City, State)
    cities = cities.filter(City.state_id == State.id)
    cities = cities.order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
