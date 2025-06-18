# Typy Dokumentów i Szablony

## Szablon Faktury (4 bloki):
- **Blok A** (lewy górny) - dane nadawcy
- **Blok B** (prawy górny) - dane odbiorcy  
- **Blok C** (środkowy) - tabela pozycji
- **Blok D** (dolny) - podsumowanie płatności

## Szablon 6-kolumnowy (6 bloków):
- **Bloki A,B** (górny rząd)
- **Bloki C,D** (środkowy rząd)
- **Bloki E,F** (dolny rząd)

## Szablon Uniwersalny:
- Automatyczne wykrywanie liczby bloków
- Adaptacyjna segmentacja

## Struktura JSON Metadanych

```json
{
  "document": {
    "type": "invoice|form|letter|other",
    "language": "pl|en|de",
    "layout": "4-block|6-block|custom",
    "confidence": 0.95
  },
  "blocks": [
    {
      "id": "A",
      "type": "header|content|table|footer",
      "position": {"x": 0, "y": 0, "width": 300, "height": 200},
      "content": "rozpoznany tekst",
      "language": "pl",
      "confidence": 0.92,
      "formatting": {
        "bold": [0, 10],
        "tables": [],
        "lists": []
      }
    }
  ]
}
```
