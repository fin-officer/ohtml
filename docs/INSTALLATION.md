# Instalacja vHTML

## Wymagania systemowe

### Systemy operacyjne
- **Linux** (Ubuntu 18.04+, Debian 10+, CentOS 7+)
- **Windows** (10/11)
- **macOS** (10.14+)

### Wymagania sprzętowe
- **RAM**: minimum 4GB, zalecane 8GB+
- **CPU**: 2+ rdzenie
- **Miejsce na dysku**: 2GB
- **GPU**: opcjonalnie (przyspiesza działanie OCR)

## Instalacja krok po kroku

### 1. Instalacja zależności systemowych

#### Linux (Ubuntu/Debian)

```bash
# Zainstaluj zależności systemowe
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-pol tesseract-ocr-deu tesseract-ocr-eng
sudo apt-get install -y libtesseract-dev libleptonica-dev poppler-utils python3-dev python3-pip python3-venv
```

#### macOS

```bash
# Zainstaluj Homebrew jeśli nie masz
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Zainstaluj zależności
brew install tesseract tesseract-lang poppler
```

#### Windows

1. Pobierz i zainstaluj Tesseract OCR:
   - Pobierz instalator z: https://github.com/UB-Mannheim/tesseract/wiki
   - Upewnij się, że wybierasz opcję instalacji języków (polski, niemiecki, angielski)
   - Podczas instalacji zaznacz opcję "Add to PATH"

2. Pobierz i zainstaluj Poppler:
   - Pobierz z: https://github.com/oschwartz10612/poppler-windows/releases
   - Rozpakuj archiwum i dodaj folder `bin` do zmiennej środowiskowej PATH

### 2. Konfiguracja środowiska Python

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/yourusername/vhtml.git
   cd vhtml
   ```

2. Utwórz i aktywuj środowisko wirtualne:
   ```bash
   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Zainstaluj zależności Pythona:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### 3. Weryfikacja instalacji

Uruchom testową komendę, aby sprawdzić, czy wszystko działa poprawnie:

```bash
python -c "import cv2; import pytesseract; print(f'OpenCV: {cv2.__version__}, Tesseract: {pytesseract.get_tesseract_version()}')"
```

## Rozwiązywanie problemów

### Błąd: Tesseract nie jest zainstalowany
Upewnij się, że Tesseract jest poprawnie zainstalowany i dostępny w zmiennej PATH.

### Błąd: Brak modułów Pythona
Upewnij się, że wszystkie wymagane pakiety są zainstalowane:
```bash
pip install -r requirements.txt
```

### Wsparcie
Jeśli napotkasz problemy, sprawdź [FAQ](FAQ.md) lub zgłoś problem w zakładce Issues.
