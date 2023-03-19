#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    arg = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(arg[0], arg[1], arg[2]))
    session = sessionmaker(bind=engine)
    session = session()
    query = session.query(State)
    state = query.filter(State.name == arg[3]).first()
    if (state):
        print(state.id)
    else:
        print('Not found')
    session.close()
