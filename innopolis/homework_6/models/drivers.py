from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
import homework_6.views.view_drivers

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
            session.rollback()
            raise
        finally:
            session.close()


class Drivers(Base):
    """Данные водителей в БД."""

    __tablename__ = 'drivers'
    id = Column(Integer, autoincrement=True, primary_key=True, comment="id водителя")
    name = Column(String, nullable=False, comment="Имя водителя")
    car = Column(String, nullable=False, comment="Название авто")

    # переопределение выдачи объекта на экран через print
    def __repr__(self):
        return "<Drivers(Имя водителя={0}, Статус={1})>".format(
            self.name,
            self.is_vip)

    @contextmanager
    def get_driver(self, driver_id):
        """Запрос по id водителя."""
        with session_scope() as session:
            new_driver = session.query(Drivers).get(driver_id)
            return new_driver

    def create_driver(self):
        """Создание водителя."""
        with session_scope() as session:
            session.add(self)
            session.commit()

    @contextmanager
    def delete_driver(self, driver_id):
        """Удаление водителя по id"""
        with session_scope() as session:
            session.query(Drivers).filter(Drivers.id == "drivers_id").delete()
            session.commit()


Base.metadata.create_all(engine)
