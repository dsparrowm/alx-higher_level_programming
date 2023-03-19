#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    arg = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(arg[0], arg[1], arg[2]))
    session = sessionmaker(bind=engine)
    session = session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print('{}'.format(new_state.id))
    session.close()
