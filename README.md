# Przewidywanie popularności Spotify

## 1. Opis projektu

**Nazwa skrócona:** Przewidywanie popularności Spotify  
**Pełna nazwa:** Model przewidujący popularność utworu na Spotify na podstawie wyników artysty w mediach społecznościowych  

**Cel projektu:**  
Aplikacja umożliwia prognozowanie sukcesu utworu muzycznego na platformie Spotify z wykorzystaniem regresji liniowej. Model oblicza wynik w skali 0–100, gdzie 100 oznacza największą popularność.  

**Zastosowania:**  
- Wytwórnie muzyczne mogą ocenić potencjalną inwestycję w artystę.  
- Muzycy mogą zoptymalizować działania promocyjne w mediach społecznościowych.  

---

## 2. Licencja i prawa autorskie

**Autor:** Aleksandra Kalisz  
**Licencja:** MIT (Open Source) – pozwala na darmowe użycie, modyfikację i rozpowszechnianie kodu przy zachowaniu informacji o autorze.  

---

## 3. Wymagania funkcjonalne i pozafunkcjonalne

| ID   | Nazwa                         | Opis                                                                                                                                           | Priorytet | Kategoria                       |
|------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------|
| F01  | Wprowadzenie danych wejściowych | Użytkownik wprowadza dane liczbowe: miesięcznych słuchaczy Spotify, obserwujących Spotify i Instagram, subskrybentów YouTube, polubień TikTok | 1         | Funkcjonalne (Interfejs)      |
| F02  | Obliczenie wyniku              | System wykorzystuje regresję liniową do obliczenia przewidywanego wyniku po kliknięciu „Oblicz”                                              | 1         | Funkcjonalne (Logika biznesowa) |
| F03  | Wyświetlenie wyniku            | Wynik 0–100 wraz z kategorią słowną: <br>0–20: „Bardzo słaby wynik” <br>21–40: „Słaby wynik” <br>41–60: „Satysfakcjonujący wynik” <br>61–80: „Dobry wynik” <br>81–100: „Świetny wynik”. <br>Dodatkowo wyświetlany jest odpowiedni GIF | 1         | Funkcjonalne (Prezentacja danych) |
| F04  | Czas oczekiwania               | Pasek ładowania i animacja balonów sygnalizują zakończenie obliczeń                                                                          | 3         | Pozafunkcjonalne               |

---

## 4. Architektura systemu

### a) Architektura rozwoju
- **Język programowania:** Python 3.9.13  
- **IDE:** Visual Studio Code  
- **Kontrola wersji:** Git / GitHub  
- **Biblioteki analityczne:** Pandas, Scikit-learn  

### b) Architektura uruchomieniowa
- **Środowisko:** Python 3  
- **Biblioteki:** streamlit, pandas, scikit-learn, openpyxl  
- **Pliki w repozytorium:**  
  - `dane.xlsx` – dane pobrane za pomocą [Spotify Web API](https://developer.spotify.com/documentation/web-api/) (miesięczni słuchacze, obserwujący, subskrybenci, polubienia)  
  - `ikona.png`  
  - `nutki.jpg`  
  - `bardzoslabo.gif`, `slabo.gif`, `ok.gif`, `dobrze.gif`, `super.gif`  

---

## 5. Testy

### Scenariusze testowe
- Weryfikacja oceny „Świetny wynik”  
- Weryfikacja oceny „Dobry wynik”  
- Weryfikacja oceny „Satysfakcjonujący wynik”  
- Weryfikacja oceny „Słaby wynik”  
- Weryfikacja oceny „Bardzo słaby wynik”  

### Przykładowy scenariusz

**Scenariusz:** Weryfikacja oceny „Świetny wynik”  
- **Testowane wymagania:** F02, F03  
- **Warunki wstępne:** Uruchomienie aplikacji i poprawne załadowanie pliku `dane.xlsx`  
- **Kroki:**  
  1. Wprowadź „Liczba miesięcznych słuchaczy Spotify”: 100000000  
  2. Wprowadź „Liczba obserwujących Spotify”: 100000000  
  3. Wprowadź „Liczba subskrypcji YouTube”: 100000000  
  4. Wprowadź „Obserwujący Instagram”: 100000000  
  5. Wprowadź „Liczba nowych obserwujących Instagram (14 dni)”: 100000000  
  6. Wprowadź „Polubienia TikTok (wszystkie filmy)”: 100000000  
  7. Kliknij przycisk „Oblicz”  

- **Oczekiwany rezultat:** Wynik w przedziale 81–100, wyświetlony napis „Świetny wynik” i plik `super.gif`  
- **Rzeczywisty rezultat:** Zgodny z oczekiwanym, wynik: 95  

> Pozostałe scenariusze testowe weryfikowane analogicznie, zmieniając wartości wejściowe w celu uzyskania innych kategorii wyniku.
