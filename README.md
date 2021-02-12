Monitoring Twit Vaksin
===
Script ini bertujuan mengumpulkan laporan Kemenkes RI terkait perkembangan vaksinasi covid-19 sejak 31 Januari 2021. Data diambil dari twit KemenkesRI (@KemenkesRI). 
Proses ocr menggunakan modul pytesseract.

Requirements
---
- Python 3
- twint
- tor
- pytesseract

Installation
---
- `git clone https://github.com/lantip/monitoring-tweet-vaksin.git`
- `cd monitoring-tweet-vaksin`
- Jalankan `pip install -r requirements.txt`
- Install TOR dan jalankan.

Usage
---
```
# untuk mengumpulkan twit, gunakan:
$ python main.py

File image akan disimpan dalam folder "data". Hasil akan tersimpan dalam file twit.json

# untuk proses extract text menjadi file json:
$ python tsr.py

Hasil akan disimpan dalam file result.json
```
