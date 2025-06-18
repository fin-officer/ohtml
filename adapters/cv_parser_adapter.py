import requests

class CVParserAdapter:
    def __init__(self, host='localhost', port=8003):
        self.base_url = f"http://{host}:{port}"

    def extract(self, pdf_path):
        with open(pdf_path, 'rb') as f:
            files = {'file': (pdf_path, f, 'application/pdf')}
            resp = requests.post(f"{self.base_url}/extract", files=files)
        resp.raise_for_status()
        return resp.json()
