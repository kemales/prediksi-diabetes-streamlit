# Aplikasi Prediksi Risiko Diabetes Berbasis Machine Learning

https://github.com/kemales/prediksi-diabetes-streamlit/blob/main/streamlit.png

Sebuah aplikasi web interaktif yang dibangun untuk memprediksi risiko diabetes pada pasien berdasarkan beberapa atribut diagnostik. Aplikasi ini memanfaatkan model Machine Learning yang telah dilatih dan dideploy menggunakan Streamlit.

---

### 🔗 Link Penting
- **Aplikasi Live:** https://prediksi-diabetes-app.streamlit.app/
- **Repositori Kode:** `https://github.com/kemales/prediksi-diabetes-streamlit`https://github.com/kemales/prediksi-diabetes-streamlit

---

### 📝 Latar Belakang Masalah
Diabetes adalah penyakit kronis yang mempengaruhi jutaan orang di seluruh dunia. Deteksi dini merupakan kunci untuk manajemen dan pengobatan yang efektif, yang dapat mencegah komplikasi serius. Proyek ini bertujuan untuk menyediakan alat bantu yang mudah diakses bagi masyarakat umum maupun tenaga medis untuk melakukan skrining awal risiko diabetes berdasarkan data medis yang relevan.

---

### 🔬 Metodologi & Proses

Proyek ini dikembangkan mengikuti alur kerja *data science* yang terstruktur, mengadopsi metodologi **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*), mulai dari pemahaman masalah hingga penerapan model ke dalam aplikasi.

#### 1. Pemahaman Bisnis dan Data

-   **Business Understanding:** Tujuan utama proyek adalah membangun sistem yang dapat membantu deteksi dini risiko penyakit diabetes, sehingga memungkinkan penanganan yang lebih cepat dan proaktif.
-   **Data Understanding:** Proses dimulai dengan memuat dataset **PIMA Indians Diabetes Database**. Tahap ini meliputi:
    -   **Inspeksi Awal:** Memeriksa struktur, tipe data, dan statistik deskriptif dari dataset.
    -   **Identifikasi Kualitas Data:** Mencari nilai-nilai yang hilang (*missing values*) atau tidak wajar (misalnya, nilai 0 pada kolom `BloodPressure`).
    -   **Eksplorasi & Visualisasi Data (EDA):** Menganalisis distribusi setiap fitur dan korelasinya dengan variabel target (`Outcome`) menggunakan plot seperti histogram dan heatmap.

#### 2. Persiapan Data (Data Preparation)

Tahap ini krusial untuk menyiapkan data yang bersih dan optimal untuk pemodelan.
-   **Penanganan Missing Values & Outlier:** Membersihkan data dengan menangani nilai-nilai yang tidak logis dan *outlier* yang dapat mengganggu performa model.
-   **Pembagian Data:** Dataset dibagi menjadi data latih (*training set*) dan data uji (*testing set*) untuk evaluasi model yang objektif.
-   **Scaling Fitur:** Menerapkan `StandardScaler` pada fitur numerik untuk menstandarisasi skala data, yang penting untuk beberapa algoritma machine learning.
-   **Seleksi Fitur (RFE):** Menggunakan **Recursive Feature Elimination (RFE)** dengan estimator Random Forest untuk secara cerdas memilih subset fitur yang paling berpengaruh, mengurangi *noise*, dan meningkatkan efisiensi model.

#### 3. Pemodelan (Modeling)

-   **Penyeimbangan Data (SMOTE):** Menyadari adanya ketidakseimbangan kelas pada data target (jumlah penderita diabetes lebih sedikit), teknik **SMOTE (Synthetic Minority Over-sampling Technique)** diterapkan **hanya pada data latih**. Langkah ini krusial untuk mencegah model menjadi bias dan untuk meningkatkan kemampuannya dalam mengenali kelas minoritas.
-   **Pembuatan Model:** Model **Random Forest Classifier** dipilih karena kemampuannya yang *robust* dalam menangani hubungan non-linear antar fitur dan ketahanannya terhadap *overfitting*.

#### 4. Evaluasi Model (Evaluation)

Kinerja model dievaluasi secara menyeluruh pada data uji (data yang belum pernah dilihat sebelumnya oleh model).

**Classification Report:**
| Kelas | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| 0 (Tidak Diabetes) | 0.82 | 0.80 | 0.81 | 100 |
| 1 (Diabetes) | 0.65 | 0.69 | 0.67 | 54 |

**Metrik Keseluruhan:**
-   **Akurasi:** ~76%
-   **ROC-AUC Score:** **0.8358**

Meskipun akurasi berada di angka 76%, **ROC-AUC Score mencapai ~84%**, yang menunjukkan kemampuan model yang sangat baik dalam membedakan antara pasien diabetes dan non-diabetes secara keseluruhan. Analisis **Confusion Matrix** dan **Feature Importance** juga dilakukan untuk mendapatkan pemahaman mendalam tentang perilaku dan keputusan model.

#### 5. Penerapan (Deployment)

-   **Perancangan Sistem (UML):** Alur kerja aplikasi dan interaksi pengguna dirancang terlebih dahulu menggunakan **Use Case Diagram** dan **Activity Diagram** untuk memastikan implementasi yang terstruktur.
-   **Implementasi Web Streamlit:** Model yang sudah final disimpan dan diintegrasikan ke dalam sebuah aplikasi web interaktif menggunakan **Streamlit**. Aplikasi ini memungkinkan pengguna untuk memasukkan data mereka dan mendapatkan prediksi secara *real-time*.


---

### 🏁 Kesimpulan & Pengembangan Selanjutnya
Proyek ini berhasil menunjukkan kemampuan untuk membangun dan mendeploy model machine learning fungsional untuk kasus penggunaan di dunia nyata.

Beberapa pengembangan yang bisa dilakukan di masa depan:
- Mencoba algoritma lain seperti XGBoost atau LightGBM untuk perbandingan performa.
- Melakukan *hyperparameter tuning* secara ekstensif untuk lebih mengoptimalkan model.
- Mengintegrasikan dataset yang lebih besar dan beragam.

---

### 🛠️ Teknologi yang Digunakan
- **Python**
- **Pandas** & **NumPy** (Manipulasi Data)
- **Scikit-learn** (Pemodelan Machine Learning)
- **Matplotlib** & **Seaborn** (Visualisasi Data)
- **Streamlit** (Deployment Aplikasi Web)
- **Git** & **GitHub** (Version Control)
