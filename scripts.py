from extensions import session, Base, engine
from models import Person
import sqlalchemy as sa
from postgresql_audit.flask import versioning_manager



if __name__ == "__main__":
    sa.orm.configure_mappers()
    # versioning_manager.transaction_cls.__table__.create(engine)
    # versioning_manager.activity_cls.__table__.create(engine)

    # Base.metadata.create_all(engine)
    versioning_manager.values = {'actor_id': 1}

    ed = session.query(Person).first()
    ed.nickname = 'Awesome'


    karl = Person(name='Peter', fullname='Pan', nickname='pepan')
    session.add(karl)
    session.commit()
    print(karl)
