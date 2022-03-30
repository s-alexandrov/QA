from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

engine = create_engine('sqlite:///test.db')
Base = declarative_base()
Session = scoped_session(sessionmaker(autoflush=True, autocommit=False, bind=engine))


@contextmanager
def session_scope():
        session = Session()
        try:
            yield session
            session.commit()
        except:
            print("OTRABOTAL ROLLBACK")
            session.rollback()
            raise
        finally:
            session.close()


class Clients(Base):
    """БД клиентов."""
    __tablename__ = 'clients'
    id = Column(Integer, autoincrement=True, primary_key=True, comment="id клиента")
    name = Column(String, nullable=False, comment="Имя")
    is_vip = Column(Boolean, nullable=False, comment="Статус")

    # переопределение выдачи объекта на экран через print
    def __repr__(self):
        return "<Clients(Имя клиента={0}, Статус={1})>".format(
            self.name,
            self.is_vip)


# создание таблиц если они не существуют
Base.metadata.create_all(engine)

# создание новой сессии, для выполнения действий
Session = sessionmaker(bind=engine)
session = Session()