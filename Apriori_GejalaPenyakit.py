# Nama  : Sabila Marista Losya
# Kelas : Teknik Informatika (Sore)
# Soal No 2 - Prediksi Pola Gejala Penyakit (Apriori)

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

# === Dataset pasien dan gejalanya ===
data = {
    'P001': ['Demam','Batuk','Sesak Napas'],
    'P002': ['Nyeri Sendi','Kelelahan','Demam'],
    'P003': ['Batuk','Sakit Tenggorokan','Demam'],
    'P004': ['Demam','Sesak Napas','Kelelahan'],
    'P005': ['Nyeri Sendi','Demam','Batuk'],
    'P006': ['Sakit Kepala','Kelelahan','Demam'],
    'P007': ['Batuk','Sakit Tenggorokan'],
    'P008': ['Demam','Batuk','Sesak Napas'],
    'P009': ['Kelelahan','Nyeri Sendi'],
    'P010': ['Demam','Sakit Kepala','Batuk'],
    'P011': ['Sesak Napas','Batuk','Demam'],
    'P012': ['Kelelahan','Demam','Nyeri Sendi'],
    'P013': ['Sakit Tenggorokan','Batuk'],
    'P014': ['Demam','Kelelahan','Sakit Kepala'],
    'P015': ['Batuk','Sesak Napas','Demam'],
    'P016': ['Nyeri Sendi','Kelelahan'],
    'P017': ['Demam','Batuk','Sakit Tenggorokan'],
    'P018': ['Kelelahan','Sakit Kepala'],
    'P019': ['Demam','Sesak Napas','Batuk'],
    'P020': ['Nyeri Sendi','Demam','Kelelahan']
}

# === Ubah ke format transaksi ===
gejala_list = ['Demam','Batuk','Sesak Napas','Nyeri Sendi','Kelelahan','Sakit Tenggorokan','Sakit Kepala']
df = pd.DataFrame([{g: (g in v) for g in gejala_list} for v in data.values()])

# === Jalankan Apriori dan Association Rules ===
frequent_itemsets = apriori(df, min_support=0.25, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Urutkan agar hasil sama dengan tabel final
rules = rules.sort_values(by=['support','confidence'], ascending=[False, False])

# Cetak hasil utama
print(rules[['antecedents','consequents','support','confidence','lift']])

# === Visualisasi dengan nilai di ujung batang ===
top_rules = rules.head(8)
plt.figure(figsize=(10,6))
labels = top_rules.apply(lambda x: ', '.join(list(x['antecedents'])) + " → " + ', '.join(list(x['consequents'])), axis=1)
bars = plt.barh(labels, top_rules['confidence'], color='skyblue')
plt.xlabel('Confidence')
plt.title('Pola Gejala Penyakit dengan Confidence Tertinggi')
plt.gca().invert_yaxis()

# Tambahkan nilai confidence di ujung batang
for bar, conf in zip(bars, top_rules['confidence']):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f"{conf:.2f}", va='center', fontsize=9, color='black')

plt.tight_layout()
plt.savefig('pola_gejala_apriori.png', dpi=300)

plt.show()
