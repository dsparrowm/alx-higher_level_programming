#!/usr/bin/python3
"""
script that prints the first State object from the
database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import create_engine
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    session = session()
    state = session.query(State).order_by(State.id).first()
    if (state):
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
