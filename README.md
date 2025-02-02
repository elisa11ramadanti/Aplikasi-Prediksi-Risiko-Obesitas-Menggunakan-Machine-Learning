# **Aplikasi Prediksi Risiko Obesitas Menggunakan Machine Learning**

## **Overview**
Proyek ini bertujuan untuk mengembangkan sebuah aplikasi prediksi yang dapat mengestimasi risiko obesitas berdasarkan faktor-faktor gaya hidup dan kesehatan individu. Dengan menggunakan teknik machine learning, khususnya algoritma **Random Forest**, proyek ini bertujuan untuk memberikan wawasan yang lebih baik dalam upaya pencegahan dan penanganan obesitas, serta memberikan rekomendasi yang lebih tepat berdasarkan data individu.

Aplikasi ini dikembangkan menggunakan **Streamlit**, sehingga memungkinkan pengguna untuk dengan mudah menginput data dan mendapatkan hasil prediksi secara instan. Model yang digunakan telah diuji dan menunjukkan akurasi **96,17%**, menjadikannya alat yang andal dalam menilai risiko obesitas seseorang.

## **Live Demo**
Untuk mencoba aplikasi ini secara langsung dapat melalui link berikut:
[BodyCheck+](https://bodycheck.streamlit.app/)

## **About Dataset**
Dataset yang digunakan dalam proyek ini diperoleh dari repositori publik **UCI Machine Learning Repository**. Dataset ini mencakup berbagai fitur yang berkaitan dengan gaya hidup dan kesehatan, antara lain:

- **Gender**: Jenis kelamin individu
- **Age**: Umur individu
- **Height**: Tinggi badan (cm)
- **Weight**: Berat badan (kg)
- **family_history_with_overweight**: Apakah individu memiliki riwayat keluarga dengan obesitas
- **FAVC**: Frekuensi konsumsi makanan berkalori tinggi
- **FCVC**: Frekuensi konsumsi sayur
- **NCP**: Berapa kali makan dalam sehari
- **CAEC**: Konsumsi cemilan (snacking habits)
- **SMOKE**: Status merokok
- **CH2O**: Konsumsi air putih per hari
- **SCC**: Pemantauan konsumsi kalori
- **FAF**: Frekuensi aktivitas fisik
- **TUE**: Lama waktu penggunaan perangkat teknologi per hari
- **CALC**: Konsumsi alkohol
- **MTRANS**: Transportasi yang digunakan sehari-hari

Kolom target dalam dataset ini adalah **NObeyesdad**, yang menunjukkan tingkat obesitas individu dengan beberapa kategori, seperti **Underweight, Normal Weight, Overweight, and Obese**.

## **Technologies Used**
Proyek ini dibangun menggunakan berbagai teknologi dan library machine learning, antara lain:
- **Python 3.9**
- **Pandas** – untuk manipulasi data
- **NumPy** – untuk perhitungan numerik
- **Scikit-learn** – untuk pengembangan model machine learning (Random Forest, evaluasi model)
- **Streamlit** – untuk membangun antarmuka aplikasi
- **Matplotlib & Seaborn** – untuk visualisasi data

## **Model Training & Evaluation**
1. **Preprocessing Data:**
   - Data kategorikal dikonversi menggunakan **Ordinal Encoder** agar dapat digunakan dalam model machine learning.
   - Data dibersihkan untuk menghilangkan nilai yang hilang atau tidak valid.

2. **Model Training:**
   - Algoritma **Random Forest** digunakan karena mampu menangani data dengan baik dan memberikan prediksi yang akurat.
   - Model diuji dengan **train-test split** untuk menghindari overfitting.

3. **Model Evaluation:**
   - Model dievaluasi menggunakan **classification report** dan **confusion matrix**.
   - Akurasi model mencapai **96,17%**, menunjukkan kinerja yang sangat baik dalam memprediksi risiko obesitas.

## **Installation & Usage**
### **1. Clone Repository**
Untuk memulai proyek ini, pertama-tama Anda perlu meng-clone repositori dengan perintah berikut:
```bash
git clone https://github.com/elisa11ramadanti/Aplikasi-Prediksi-Risiko-Obesitas-Menggunakan-Machine-Learning.git
cd Aplikasi-Prediksi-Risiko-Obesitas-Menggunakan-Machine-Learning
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
```bash
streamlit run app.py
```

## **Project Structure**
```
│-- Aplikasi-Prediksi-Risiko-Obesitas-Menggunakan-Machine-Learning/
│   ├── data/                      # Dataset
│   ├── models/                    # Model yang sudah dilatih
│   ├── notebooks/                  # Eksplorasi data dan training model
│   ├── app.py                      # File utama aplikasi Streamlit
│   ├── requirements.txt            # Library yang dibutuhkan
│   ├── README.md                   # Dokumentasi proyek
```

## **Screenshots**
Berikut adalah tampilan aplikasi **BodyCheck+**:
![image](https://github.com/user-attachments/assets/7de02373-74a3-45be-b41f-8807a07dab72)
![image](https://github.com/user-attachments/assets/2b63ab4b-787f-424d-99fe-88a1a0434078)

## **Future Improvements**
Beberapa peningkatan yang direncanakan dalam pengembangan aplikasi ini:
- **Validasi Input Pengguna**: Memastikan data yang dimasukkan sesuai format yang diharapkan.
- **Peningkatan Visualisasi**: Membuat tampilan hasil prediksi lebih interaktif.
- **Penambahan Riwayat Prediksi**: Memungkinkan pengguna menyimpan hasil prediksi mereka.
- **Optimasi Model**: Mengeksplorasi model machine learning lain untuk peningkatan akurasi.

---
