import random
from sqlalchemy import Column, Integer, String, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from faker import Faker

engine = create_engine('sqlite:///clients.db')
Base = declarative_base()


class Clients(Base):
    """Таблица БД с клиентами."""
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    surname = Column(String(50))
    phone = Column(Integer)
    agreement_terms = Column(Boolean, default=True, nullable=False)
    personal_data = Column(Boolean, default=True, nullable=False)
    email = Column(String(50), nullable=False)
    distribution = Column(Boolean, default=True, nullable=False)

    def __repr__(self):
        return f'<Client id = {self.id}' \
               f' name = {self.name},' \
               f' surname =  {self.surname}, ' \
               f' phone {self.phone} ' \
               f' agreement_terms {self.agreement_terms},' \
               f' personal_data {self.personal_data},'\
               f' email {self.email},' \
               f' distribution {self.distribution}>'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
Session = scoped_session(sessionmaker(expire_on_commit=False, bind=engine))


def create_client():
    """Добавляем клиентов."""
    fake = Faker()
    fake_clients = [Clients(
        name=fake.first_name_male(),
        surname=fake.last_name_male(),
        phone=fake.phone_number(),
        agreement_terms=random.choice([True, False]),
        personal_data=random.choice([True, False]),
        email=fake.email(),
        distribution=random.choice([True, False])
    ) for _ in range(30)]
    print(fake_clients)
    session.add_all(fake_clients)
    session.commit()


def main() -> None:
    """Основная функция."""
    create_client()


if __name__ == "__main__":
    main()
