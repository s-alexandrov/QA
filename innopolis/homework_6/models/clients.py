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

    @contextmanager
    def get_client(self, client_id):
        """Запрос по id водителя."""
        with session_scope() as session:
            new_client = session.query(Clients).get(client_id)
            return new_client

    def create_client(self):
        """Создание водителя."""
        with session_scope() as session:
            session.add(self)
            session.commit()

    @contextmanager
    def delete_client(self, client_id):
        """Удаление водителя по id"""
        with session_scope() as session:
            session.query(Clients).filter(Clients.id == "client_id").delete()
            session.commit()


# создание таблиц если они не существуют
Base.metadata.create_all(engine)

# создание новой сессии, для выполнения действий
Session = sessionmaker(bind=engine)
session = Session()