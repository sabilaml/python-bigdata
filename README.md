# python-bigdata
Repository ini berisi tiga analisis utama menggunakan Python sebagai bagian dari tugas UTS Data Mining.
Setiap file Python mewakili satu soal berbeda dengan metode data mining yang digunakan untuk klasifikasi, asosiasi, dan pengambilan keputusan.

👩‍🎓 Nama: Sabila Marista Losya
🏫 Program Studi: Teknik Informatika

📘 1️⃣ Klasifikasi Risiko Diabetes Berdasarkan Gaya Hidup

File: Klasifikasi_Diabetes.py
Metode: Decision Tree Classifier (Scikit-learn)

🧩 Deskripsi

Program ini menganalisis data pasien untuk memprediksi risiko diabetes (Tinggi/Rendah) berdasarkan faktor-faktor gaya hidup seperti:

Usia

IMT (Indeks Massa Tubuh)

Aktivitas Fisik

Konsumsi Gula

Riwayat Keluarga

Tekanan Darah

⚙️ Cara Menjalankan

Pastikan sudah menginstal dependensi:

pip install pandas scikit-learn matplotlib


Jalankan program:

python Klasifikasi_Diabetes.py

📊 Hasil & Analisis

Menampilkan hasil prediksi risiko pasien baru:
Prediksi Risiko Diabetes: Tinggi

Membuat visualisasi Decision Tree dengan nama file:
pohon_keputusan_diabetes.png

Dari hasil pohon keputusan terlihat bahwa:

Faktor "Riwayat Keluarga" menjadi pemisah utama.

Pasien dengan riwayat keluarga diabetes → Risiko Tinggi

Tanpa riwayat keluarga → Risiko Rendah

🩺 2️⃣ Prediksi Pola Gejala Penyakit (Apriori)

File: Apriori_GejalaPenyakit.py
Metode: Association Rule Mining (Apriori – mlxtend)

🧩 Deskripsi

Analisis ini bertujuan untuk menemukan pola keterkaitan antar-gejala penyakit dari data 20 pasien.
Beberapa gejala yang digunakan antara lain:
Demam, Batuk, Sesak Napas, Nyeri Sendi, Kelelahan, Sakit Tenggorokan, Sakit Kepala.

⚙️ Cara Menjalankan

Instal library:

pip install pandas mlxtend matplotlib


Jalankan program:

python Apriori_GejalaPenyakit.py

📊 Hasil & Analisis

Program menghasilkan aturan asosiasi dengan nilai support ≥ 25% dan confidence ≥ 60%, misalnya:

{Batuk, Sesak Napas} → {Demam} (Confidence = 100%)
{Nyeri Sendi} → {Kelelahan} (Confidence = 83%)


Artinya, pasien yang mengalami batuk dan sesak napas hampir selalu mengalami demam.

📈 Visualisasi disimpan sebagai pola_gejala_apriori.png, menampilkan:

Grafik batang horizontal (horizontal bar chart)

Label berisi rule dan nilai confidence di ujung batang

Interpretasi:

Gejala Demam sering muncul bersamaan dengan gejala lain.

Pola ini bisa membantu klinik mengenali penyakit pernapasan seperti flu berat atau COVID-like symptoms.

🎓 3️⃣ Pemilihan Universitas Terbaik dengan AHP

File: ahp_universitas.py
Metode: Analytic Hierarchy Process (AHP)

🧩 Deskripsi

Program ini digunakan untuk membantu memilih universitas terbaik berdasarkan tiga faktor utama:

Kriteria	Bobot
Biaya Kuliah	60%
Reputasi	20%
Biaya Hidup	20%

Universitas yang dibandingkan:

Dharma Cendika

Widya Kartika

ITATS

⚙️ Cara Menjalankan

Instal library:

pip install pandas matplotlib


Jalankan program:

python ahp_universitas.py

📊 Hasil & Analisis

Output terminal menampilkan tabel total skor setiap universitas dan universitas terbaik:

=== HASIL ANALISA AHP ===
     Universitas   Total Skor
0  Widya Kartika     0.9111
1  ITATS             0.8600
2  Dharma Cendika    0.7000

Universitas dengan skor tertinggi adalah: Widya Kartika


📈 Visualisasi hasil_ahp_universitas.png menampilkan grafik batang hasil perbandingan skor total.

Interpretasi:

Widya Kartika mendapat nilai tertinggi secara keseluruhan.

Faktor biaya kuliah dan reputasi berpengaruh paling besar terhadap keputusan akhir.

⚙️ Requirements

Buat file requirements.txt berisi:

pandas
matplotlib
scikit-learn
mlxtend


Instal semua library dengan:

pip install -r requirements.txt

💾 Output yang Dihasilkan
File Output	Deskripsi
pohon_keputusan_diabetes.png	Visualisasi pohon keputusan risiko diabetes
pola_gejala_apriori.png	Grafik asosiasi antar gejala penyakit
hasil_ahp_universitas.png	Grafik perbandingan skor universitas (AHP)
📎 Catatan

Semua analisis dibuat menggunakan Python 3 dan library umum (tidak memerlukan koneksi database).
Setiap script bisa dijalankan secara independen, dan hasil visualisasi otomatis tersimpan di folder yang sama dengan file Python.
