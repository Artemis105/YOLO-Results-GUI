# YOLO Results GUI

Aplikacja desktopowa napisana w Pythonie z wykorzystaniem **CustomTkinter**, umożliwiająca wykonywanie predykcji obiektów na obrazach przy użyciu **wytrenowanych modeli YOLO (.pt)**.

Aplikacja pozwala na wybór obrazu i modelu, regulację parametrów predykcji (Confidence i IoU) oraz zapis obrazu z zaznaczonymi ramkami predykcji.

---

## ✨ Funkcjonalności

- Obsługa wytrenowanych modeli YOLO (`.pt`)
-  Wybór obrazu do predykcji z listy
-  Podgląd zdjęć w aplikacji
-  Regulacja:
  - **Pewność (Confidence)** – suwak procentowy
  - **IoU (Intersection over Union)** – suwak
-  Wyświetlanie ramek predykcji z wartością pewności
-  Zapis obrazu z predykcjami do folderu
-  Nowoczesny interfejs GUI (CustomTkinter)


---

## 🗂️ Struktura katalogów (WYMAGANE)

Aplikacja domyślnie wymaga konkretnej struktury folderów, jednak możesz ją zmienić w pliku Ustawienia.py, wskazując inne ścieżki do obrazów, modeli, zapisów i etykiet.

Domyślna struktura wygląda następująco:

```text
projekt/
│
├── aplikacja_pred.py
├── Ustawienia.py
├── Predykcja.py
│
├── Dane/
│   ├── zdjecia/     ← obrazy (.jpg, .jpeg, .png)
│   ├── model/       ← modele YOLO (.pt)
│   ├── Zapis/       ← zapisane predykcje
│   └── label/       ← etykiety (opcjonalnie)

## Krok po kroku – jak uruchomić aplikację
1. **Pobierz repozytorium** na swój komputer i upewnij się, że masz Python 3.9 lub nowszy.  

2. **Przygotuj katalogi i skonfiguruj ścieżki w pliku `Ustawienia.py`**  
   - Aplikacja domyślnie zakłada określoną strukturę katalogów (foldery z obrazami, modelami, zapisem wyników i etykietami), ale możesz ją zmienić, wskazując własne katalogi w `Ustawienia.py`.  
   - Upewnij się, że w wybranych katalogach znajdują się odpowiednie pliki: obrazy (`.jpg`, `.jpeg`, `.png`) oraz modele YOLO (`.pt`).  

3. **Zainstaluj wymagane biblioteki** używając pliku `requirements.txt`:

   ```bash
   pip install -r requirements.txt
4. **Uruchom aplikację poleceniem:
    ```bash
    python aplikacja_pred.py
5. **Wybierz obraz i model z list dostępnych w GUI.
6. **Dostosuj parametry predykcji za pomocą suwaków Confidence i IoU.
7. **Uruchom predykcję klikając przycisk Predykcja – wyniki pojawią się w oknie programu.
8. **Zapisz wynik do folderu zapisu klikając przycisk Zapisz – zapisany obraz będzie zawierał ramki predykcji oraz wartości pewności, a nazwa pliku uwzględnia użyty model i ustawione parametry.


##Wymagania

 Plik requirements.txt zawiera wszystkie niezbędne biblioteki do uruchomienia aplikacji


Projekt jest edukacyjny i może być łatwo rozszerzony o dodatkowe funkcjonalności, takie jak obsługa wideo, kamery lub batch processing wielu obrazów jednocześnie.
