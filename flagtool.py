import os
import sys
import sqlalchemy


def main():
    flags = sys.argv[1:]
    engine = create_engine()
    metadata = sqlalchemy.MetaData()
    metadata.reflect(engine, only=['msgs_message'])
    session = get_session(engine)
    update_flag(session, flags, metadata.classes.msgs_message)


def create_engine():
    return sqlalchemy.create_engine('postgresql://{}:{}@{}/{}'.format(os.getenv('POSTGRES_USER'), os.getenv('POSTGRES_PASSWORD'), os.getenv('POSTGRES_HOST'), os.getenv('POSTGRES_DB')))


def get_session(engine):
    session_maker = sqlalchemy.orm.sessionmaker()
    session_maker.configure(bind=engine)
    return session_maker()


def update_flag(session, flags, msgs):
    session.query(msgs).all().update({"flagged": flag_msg(flags, msgs.text)})
    session.commit()


def flag_msg(flags, text):
    for flag in flags:
        if flag in text:
            return True
    return False