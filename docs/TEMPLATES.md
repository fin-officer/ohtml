# Document Templates

## Available Templates

### 1. Invoice Template (4 blocks)
Designed for standard invoice documents with clear section separation.

**Layout:**
```
+----------------+  +----------------+
|                |  |                |
|   Block A      |  |   Block B      |
|   (Sender)     |  |   (Recipient)  |
|                |  |                |
+----------------+  +----------------+

+------------------------------------+
|                                    |
|           Block C                 |
|           (Line Items)            |
|                                    |
+------------------------------------+
+------------------------------------+
|                                    |
|           Block D                 |
|           (Summary)               |
|                                    |
+------------------------------------+
```

### 2. 6-Column Template
Ideal for forms or documents with multiple distinct sections.

**Layout:**
```
+----------------+  +----------------+
|                |  |                |
|   Block A      |  |   Block B      |
|                |  |                |
+----------------+  +----------------+
+----------------+  +----------------+
|                |  |                |
|   Block C      |  |   Block D      |
|                |  |                |
+----------------+  +----------------+
+----------------+  +----------------+
|                |  |                |
|   Block E      |  |   Block F      |
|                |  |                |
+----------------+  +----------------+
```

### 3. Universal Template
For documents that don't fit standard templates.

**Features:**
- Automatic block detection
- Adaptive segmentation
- Dynamic template generation
- Responsive layout

## Template Configuration

Templates can be configured using a JSON configuration file:

```json
{
  "template_name": "invoice",
  "version": "1.0",
  "blocks": [
    {
      "id": "A",
      "type": "header",
      "position": {"x": 0, "y": 0, "width": 0.5, "height": 0.2},
      "styles": {
        "background": "#f8f9fa",
        "border": "1px solid #dee2e6"
      }
    },
    {
      "id": "B",
      "type": "content",
      "position": {"x": 0.5, "y": 0, "width": 0.5, "height": 0.2},
      "styles": {
        "background": "#f8f9fa"
      }
    }
  ]
}
```

## Custom Templates

To create a custom template:

1. Create a new directory in `templates/`
2. Add your HTML template file
3. Create a JSON configuration file
4. Register the template in `config/templates.json`

## Best Practices

1. Use relative units (%, vw, vh) for responsive design
2. Keep templates simple and focused
3. Test with various document types
4. Document any template-specific requirements
5. Include error handling for missing data
