## Isi repositori Main
- 1. Folder Code : Script untuk pengerjaan
  2. Folder Bagian2 : Jawaban untuk soal bagian 2

## Isi repositori Folder Code
- 1. etl.py : script ETL
- 2. query.sql : SQL queries untuk menjawab Bagian 2
- 3. visualisasi.ipynb : Hasil visualisasi dari data yang didapatkan.
- 4. explorasi.ipynb : Script explorasi dari dataset yang diberikan

## Cara menjalankan (lokal)
1. Pastikan Python 3.x
   Install: `pip install pandas matplotlib sqlalchemy pyodbc`
2. Letakkan file CSV (`transactions.csv`, `customers.csv`, `products.csv`) pada folder repo.
3. Jalankan:
   ```bash
   python etl.py