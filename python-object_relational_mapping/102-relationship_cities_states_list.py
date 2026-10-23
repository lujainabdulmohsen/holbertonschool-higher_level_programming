#!/usr/bin/python3
"""Lists all cities and their related states."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).options(
        joinedload(City.state)
    ).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(
            city.id,
            city.name,
            city.state.name
        ))

    session.close()
