#!/usr/bin/python3
"""
script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    argv = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[0], argv[1], argv[2]))
    session = sessionmaker(bind=engine)
    session = session()
    result = session.query(State)
    states = result.filter(State.name.like('%a%')).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))
    session.close()
