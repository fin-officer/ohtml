# Często zadawane pytania

## Instalacja

### Jak zainstalować Tesseract OCR na Windows?
1. Pobierz instalator ze strony: https://github.com/UB-Mannheim/tesseract/wiki
2. Uruchom instalator i wybierz języki (polski, niemiecki, angielski)
3. Podczas instalacji zaznacz opcję "Add to PATH"
4. Po instalacji otwórz nowe okno terminala i sprawdź wersję komendą: `tesseract --version`

### Jak dodać Tesseract do PATH w Windows?
1. Otwórz Panel sterowania > System > Zaawansowane ustawienia systemu
2. Kliknij przycisk "Zmienne środowiskowe"
3. W sekcji "Zmienne systemu" znajdź zmienną PATH i kliknij "Edytuj"
4. Dodaj ścieżkę do katalogu z plikiem tesseract.exe (domyślnie: `C:\Program Files\Tesseract-OCR`)
5. Zapisz zmiany i uruchom ponownie terminal

## Użycie

### Jakie formaty plików są obsługiwane?
- PDF (wymaga Poppler)
- Obrazy: JPG, PNG, TIFF, BMP

### Jakie języki są obsługiwane w OCR?
- Polski (PL)
- Angielski (EN)
- Niemiecki (DE)

## Rozwiązywanie problemów

### Błąd: "Tesseract is not installed or it's not in your PATH"
Upewnij się, że Tesseract jest poprawnie zainstalowany i dostępny w zmiennej PATH.

### Niska jakość rozpoznawania tekstu
1. Upewnij się, że obraz ma dobrą rozdzielczość (minimum 300 DPI)
2. Sprawdź, czy kontrast jest odpowiedni
3. Wypróbuj różne ustawienia przetwarzania wstępnego

### Błąd: "Unable to get page count" (PDF)
Upewnij się, że Poppler jest poprawnie zainstalowany i dostępny w zmiennej PATH.

## Wydajność

### Jak przyspieszyć działanie OCR?
1. Użyj wersji z obsługą GPU (jeśli dostępna)
2. Zwiększ limit pamięci dla Pythona
3. Przetwarzaj strony równolegle (jeśli to możliwe)

### Jak zmniejszyć zużycie pamięci?
1. Przetwarzaj dokumenty w mniejszych partiach
2. Zwiększ limit pliku wymiany systemu
3. Użyj mniejszego modelu OCR (jeśli dostępny)
