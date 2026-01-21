# Przewidywanie popularności Spotify

## 1. Charakterystyka oprogramowania

**Nazwa skrócona:** Przewidywanie popularności Spotify  
**Nazwa pełna:** Model przewidujący popularność utworu na Spotify na podstawie wyników artysty w mediach społecznościowych  

**Opis:**  
Aplikacja służy do szacowania sukcesu utworu muzycznego na platformie Spotify z wykorzystaniem regresji liniowej. Model oblicza wynik w skali 0–100, gdzie 100 oznacza największą popularność. Aplikacja może być używana przez wytwórnie muzyczne do oceny potencjalnej inwestycji w artystę lub przez muzyków do optymalizacji działań promocyjnych.

---

## 2. Prawa autorskie

**Autor:** Aleksandra Kalisz  
**Licencja:** MIT (Open Source) – pozwala na darmowe użytkowanie, modyfikację i rozpowszechnianie kodu pod warunkiem zachowania noty o autorstwie.

---

## 3. Specyfikacja wymagań

### Wprowadzenie danych
- **ID:** F01  
- **Nazwa:** Wprowadzenie danych wejściowych  
- **Opis:** Użytkownik wprowadza dane liczbowe dotyczące miesięcznych słuchaczy na Spotify, obserwujących na Instagramie i Spotify, subskrybentów na YouTube oraz polubień na TikToku.  
- **Priorytet:** 1  
- **Kategoria:** Funkcjonalne (Moduł: Interfejs użytkownika)  

### Obliczenia
- **ID:** F02  
- **Nazwa:** Obliczenie wyniku za pomocą regresji  
- **Opis:** Po naciśnięciu przycisku „Oblicz”, system wykonuje obliczenia na podstawie wprowadzonych danych, używając modelu regresji, i generuje prognozowany wynik.  
- **Priorytet:** 1  
- **Kategoria:** Funkcjonalne (Moduł: Logika biznesowa)  

### Wyświetlenie wyniku
- **ID:** F03  
- **Nazwa:** Wyświetlenie wyniku  
- **Opis:** System wyświetla wynik w skali 0–100 wraz z kategorią słowną:  
  - 0–20: „Bardzo słaby wynik”  
  - 21–40: „Słaby wynik”  
  - 41–60: „Satysfakcjonujący wynik”  
  - 61–80: „Dobry wynik”  
  - 81–100: „Świetny wynik”  
  System pokazuje też odpowiedni GIF w zależności od kategorii wyniku.  
- **Priorytet:** 1  
- **Kategoria:** Funkcjonalne (Moduł: Prezentacja danych)  

### Czas oczekiwania
- **ID:** F04  
- **Nazwa:** Czas oczekiwania na pokazanie wyniku  
- **Opis:** System wyświetla pasek ładowania oraz animację balonów, sygnalizując zakończenie obliczeń.  
- **Priorytet:** 3  
- **Kategoria:** Pozafunkcjonalne  

---

## 4. Architektura systemu / oprogramowania

### a. Architektura rozwoju
- **Język programowania:** Python 3.9.13  
- **IDE:** Visual Studio Code  
- **Kontrola wersji:** Git i GitHub  
- **Biblioteki analityczne:** Pandas, Scikit-learn  

### b. Architektura uruchomieniowa
- **Środowisko:** Python 3  
- **Biblioteki:** streamlit, pandas, scikit-learn, openpyxl  
- **Pliki:**  
  - `dane.xlsx` (dane pobrane za pomocą [Spotify Web API](https://developer.spotify.com/documentation/web-api/), zawierają: miesięcznych słuchaczy, obserwujących, subskrybentów i polubienia)  
  - `ikona.png`  
  - `nutki.jpg`  
  - `bardzoslabo.gif`  
  - `slabo.gif`  
  - `ok.gif`  
  - `dobrze.gif`  
  - `super.gif`  

---

## 5. Testy

### Scenariusze testów
- Weryfikacja oceny „Świetny wynik”  
- Weryfikacja oceny „Dobry wynik”  
- Weryfikacja oceny „Satysfakcjonujący wynik”  
- Weryfikacja oceny „Słaby wynik”  
- Weryfikacja oceny „Bardzo słaby wynik”  

### Przykładowe sprawozdanie z testów
**Scenariusz:** Weryfikacja oceny „Świetny wynik”  
- **Testowane wymagania:** F02 i F03  
- **Warunki wstępne:** Uruchomienie aplikacji i poprawne załadowanie pliku `dane.xlsx`  
- **Kroki:**  
  1. Wprowadź w polu „Liczba miesięcznych słuchaczy Spotify (tyś)”: 10000  
  2. „Liczba obserwujących wykonawcę Spotify”: 100000  
  3. „Liczba subskrypcji YouTube”: 100000  
  4. „Obserwujący Instagram (tyś)”: 100000  
  5. „Liczba nowych obserwujących Instagram (14 dni)”: 1000  
  6. „Polubienia TikTok (wszystkie filmy) (tyś)”: 100000  
  7. Kliknij przycisk „Oblicz”  

- **Oczekiwany rezultat:**  
  Wynik w przedziale 81–100, wyświetlony napis „Świetny wynik”, plik `super.gif`.  

- **Rzeczywisty rezultat:**  
  Zgodny z oczekiwanym, wynik: 95  

> Pozostałe scenariusze testowe są weryfikowane analogicznie, zmieniając wartości wejściowe w celu uzyskania innej oceny.

