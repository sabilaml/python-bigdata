# Soal No.1 Klasifikasi Risiko Diabetes Berdasarkan Gaya Hidup
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# dataset soal
data = {
    'Usia': [45,30,55,25,60,40,35,50,28,48,33,52,41,38,47,29,53,36,58,42,31,49,27,54,39,59,43,32,51,26,56],
    'IMT': ['Obese','Normal','Overweight','Normal','Obese','Overweight','Normal','Obese','Normal','Overweight','Normal','Obese','Overweight','Normal','Obese','Normal','Overweight','Normal','Obese','Overweight','Normal','Obese','Normal','Overweight','Normal','Obese','Overweight','Normal','Obese','Normal','Overweight'],
    'Aktivitas Fisik': ['Rendah','Tinggi','Sedang','Tinggi','Rendah','Sedang','Sedang','Rendah','Tinggi','Rendah','Sedang','Rendah','Sedang','Tinggi','Rendah','Tinggi','Sedang','Sedang','Rendah','Sedang','Tinggi','Rendah','Tinggi','Sedang','Sedang','Rendah','Sedang','Tinggi','Rendah','Tinggi','Sedang'],
    'Konsumsi Gula': ['Tinggi','Rendah','Sedang','Sedang','Tinggi','Sedang','Tinggi','Sedang','Rendah','Tinggi','Sedang','Tinggi','Sedang','Rendah','Tinggi','Sedang','Tinggi','Sedang','Tinggi','Sedang','Rendah','Tinggi','Sedang','Tinggi','Sedang','Tinggi','Sedang','Rendah','Tinggi','Sedang','Tinggi'],
    'Riwayat Keluarga': ['Ya','Tidak','Ya','Tidak','Ya','Tidak','Ya','Ya','Tidak','Ya','Tidak','Ya','Tidak','Tidak','Ya','Tidak','Ya','Tidak','Ya','Tidak','Tidak','Ya','Tidak','Ya','Tidak','Ya','Tidak','Tidak','Ya','Tidak','Ya'],
    'Tekanan Darah': ['Hipertensi','Normal','Prehipertensi','Normal','Hipertensi','Prehipertensi','Prehipertensi','Hipertensi','Normal','Hipertensi','Normal','Hipertensi','Prehipertensi','Normal','Hipertensi','Normal','Prehipertensi','Normal','Hipertensi','Prehipertensi','Normal','Hipertensi','Normal','Prehipertensi','Normal','Hipertensi','Prehipertensi','Normal','Hipertensi','Normal','Prehipertensi'],
    'Risiko Diabetes': ['Tinggi','Rendah','Tinggi','Rendah','Tinggi','Rendah','Tinggi','Tinggi','Rendah','Tinggi','Rendah','Tinggi','Rendah','Rendah','Tinggi','Rendah','Tinggi','Rendah','Tinggi','Rendah','Rendah','Tinggi','Rendah','Tinggi','Rendah','Tinggi','Rendah','Rendah','Tinggi','Rendah','Tinggi']
}
df = pd.DataFrame(data)

# label encod
encoders = {}
for col in ['IMT','Aktivitas Fisik','Konsumsi Gula','Riwayat Keluarga','Tekanan Darah','Risiko Diabetes']:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])

# decision tree
X = df.drop(columns=['Risiko Diabetes'])
y = df['Risiko Diabetes']
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

# prediksi pasien
pasien_baru = pd.DataFrame({
    'Usia': [38],
    'IMT': [encoders['IMT'].transform(['Overweight'])[0]],
    'Aktivitas Fisik': [encoders['Aktivitas Fisik'].transform(['Sedang'])[0]],
    'Konsumsi Gula': [encoders['Konsumsi Gula'].transform(['Tinggi'])[0]],
    'Riwayat Keluarga': [encoders['Riwayat Keluarga'].transform(['Ya'])[0]],
    'Tekanan Darah': [encoders['Tekanan Darah'].transform(['Prehipertensi'])[0]]
})
prediksi = model.predict(pasien_baru)[0]
hasil = encoders['Risiko Diabetes'].inverse_transform([prediksi])[0]

print("=== HASIL PREDIKSI RISIKO DIABETES ===")
print(f"Prediksi Risiko Diabetes: {hasil}")

plt.figure(figsize=(10,6))
plot_tree(
    model,
    feature_names=list(X.columns),
    class_names=encoders['Risiko Diabetes'].classes_,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree - Klasifikasi Risiko Diabetes", fontsize=14, pad=15)
plt.savefig("pohon_keputusan_diabetes.png", dpi=300, bbox_inches='tight')
plt.show()

print("""
📘 Penjelasan Visualisasi:
----------------------------------
🟧 Kotak oranye  = Risiko Rendah
🟦 Kotak biru    = Risiko Tinggi

Gini Impurity = ukuran campuran data (0 artinya semua homogen)
Samples        = jumlah data pada simpul
Value          = [jumlah Rendah, jumlah Tinggi]
Class          = kelas hasil keputusan

Dari visualisasi terlihat:
- Node pertama (Riwayat Keluarga) memisahkan data sempurna.
- Semua pasien dengan riwayat keluarga -> Risiko Tinggi.
- Semua pasien tanpa riwayat keluarga -> Risiko Rendah.
----------------------------------

""")
