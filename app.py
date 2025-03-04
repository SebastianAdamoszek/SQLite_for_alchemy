from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Tworzymy bazę - możesz dodawać kolejne pliki zmieniać nazwy
DATABASE_URL = "sqlite:///database/plik1.db"
# DATABASE_URL = "sqlite:///database/plik2.db"

# Deklaracja bazy
Base = declarative_base()

# Tworzymy model (tabelę)
class User(Base):
    __tablename__ = 'users'
#  !!! TUTAJ TWORZYSZ TABELE    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(Integer, nullable=False)


# Utworzenie silnika bazy danych
engine = create_engine(DATABASE_URL)

# Tworzymy tabele
Base.metadata.create_all(engine)

# Tworzymy sesję
Session = sessionmaker(bind=engine)
session = Session()

# Dodanie przykładowych danych
#!!! TUTAJ ODNASISZ SIĘ DO TABELI - CZYLI UZUPEŁNIASZ JEJ ZAWARTOŚĆ

# Dla np. plik1.db
new_user = User(name="Budynek", street="Katowicka", number="10")
session.add(new_user)
session.commit()

# Dla np. plik2.db
# new_user = User(name="Kamienica", street="Warszawska", number="20")
# session.add(new_user)
# session.commit()

# Opcjonalnie - to jest kod który wyświetli info w terminalu
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Street: {user.street} Number: {user.number}")

# Zamykamy sesję
session.close()
