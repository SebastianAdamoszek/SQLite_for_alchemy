# SQLite Test - Instrukcja uruchomienia

## Klonowanie repozytorium
Aby rozpocząć, sklonuj repozytorium do lokalnego katalogu:
```bash
git clone https://github.com/SebastianAdamoszek/SQLite_for_alchemy.git
cd SQLite_for_alchemy
```

## Tworzenie i aktywacja wirtualnego środowiska (opcjonalnie)
Zalecane jest utworzenie wirtualnego środowiska dla izolacji zależności:
```bash
python -m venv venv
source venv/bin/activate  # Dla systemów Linux/Mac
venv\Scripts\activate    # Dla Windows
```

## Instalacja zależności
Zainstaluj wymagane biblioteki, korzystając z pliku `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Uruchomienie aplikacji
Aby uruchomić skrypt, wykonaj:
```bash
python app.py
```

## Opis działania
Skrypt `app.py` wykorzystuje SQLite do zarządzania danymi. Tworzy bazę danych, definiuje tabelę użytkowników i dodaje przykładowe wpisy.

## Dla podglądu pliku - bazy danych .db
```
zainstaluj wtyczkę np.SQLite Viewer
```

## Struktura plików
```
SQLite_test/
│── app.py              # Główny skrypt aplikacji
│── requirements.txt    # Lista zależności
│── test.db             # Plik bazy danych (tworzony automatycznie)
│── README.md           # Instrukcja
```

## Weryfikacja zawartości bazy danych
Po uruchomieniu skryptu możesz sprawdzić zawartość bazy za pomocą narzędzi takich jak `sqlite3`:
```bash
sqlite3 test.db
SELECT * FROM users;
```

## Dodatkowe informacje
Jeśli napotkasz problemy, sprawdź logi i upewnij się, że wszystkie zależności są poprawnie zainstalowane.

