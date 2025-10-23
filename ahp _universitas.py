# Soal No 3 - Pemilihan Universitas Menggunakan AHP

import pandas as pd
import matplotlib.pyplot as plt

# data awal
data = {
    'Universitas': ['Dharma Cendika', 'Widya Kartika', 'ITATS'],
    'Biaya Kuliah': [3, 8, 7],
    'Reputasi': [8, 5, 9],
    'Biaya Hidup': [6, 6, 4]
}

# Bobot Kriteria dalam desimal
weights = {
    'Biaya Kuliah': 0.6,
    'Reputasi': 0.2,
    'Biaya Hidup': 0.2
}

df = pd.DataFrame(data)

# 1. Normalisasi Nilai
normalized_df = df.copy()
for col in ['Biaya Kuliah', 'Reputasi', 'Biaya Hidup']:
    normalized_df[col] = df[col] / df[col].max()

# 2. Nilai Tertimbang
for col in ['Biaya Kuliah', 'Reputasi', 'Biaya Hidup']:
    normalized_df[col] = normalized_df[col] * weights[col]

# 3. Total Skor Akhir
normalized_df['Total Skor'] = normalized_df[['Biaya Kuliah','Reputasi','Biaya Hidup']].sum(axis=1)

# 4. Gabung Nama Universitas
result = pd.concat([df['Universitas'], normalized_df[['Total Skor']]], axis=1)

# 5. Urutan Skor Tertinggi
result = result.sort_values(by='Total Skor', ascending=False).reset_index(drop=True)

print("=== HASIL ANALISA AHP ===")
print(result)
print("\nUniversitas dengan skor tertinggi adalah:", result.iloc[0]['Universitas'])

# Visual
plt.figure(figsize=(8,5))
bars = plt.bar(result['Universitas'], result['Total Skor'], color=['skyblue','lightgreen','salmon'])
plt.title('Hasil Analisis AHP Pemilihan Universitas')
plt.xlabel('Universitas')
plt.ylabel('Total Skor')

# nilai di batang
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f"{bar.get_height():.3f}", ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('hasil_ahp_universitas.png', dpi=300)
plt.show()


print("\nVisualisasi disimpan sebagai: hasil_ahp_universitas.png")

