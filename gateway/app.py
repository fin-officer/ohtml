from fastapi import FastAPI, UploadFile, File
import requests

app = FastAPI()

SERVICE_MAP = {
    'invoice': 'http://invoice-extractor:8001/extract',
    'receipt': 'http://receipt-analyzer:8002/extract',
    # Dodaj kolejne serwisy według potrzeb
}

@app.post('/api/v1/{service}/extract')
async def route_extract(service: str, file: UploadFile = File(...)):
    if service not in SERVICE_MAP:
        return {'error': 'Unknown service'}
    files = {'file': (file.filename, await file.read(), file.content_type)}
    resp = requests.post(SERVICE_MAP[service], files=files)
    return resp.json()
