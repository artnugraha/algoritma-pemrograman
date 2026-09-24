# Algoritma dan Pemrograman untuk Fisika dan Teknik

Repositori ini berisi catatan kuliah, contoh program, latihan, dan materi pendukung untuk mata kuliah **Algoritma dan Pemrograman** pada Program Studi Fisika ataupun Teknik Fisika. Mata kuliah ini memperkenalkan cara berpikir algoritmik untuk menyelesaikan persoalan sains dan rekayasa, kemudian menerjemahkan algoritma tersebut ke dalam program komputer. Bahasa **C** digunakan sebagai bahasa pemrograman utama agar mahasiswa memahami struktur program, representasi data, aliran kontrol, fungsi, larik, *pointer* dasar, struktur data sederhana, dan pengolahan berkas. Bahasa **Python** digunakan sebagai pembanding dan sebagai perangkat untuk komputasi ilmiah, pengolahan data, serta visualisasi.

Seiring dengan perkembangan perangkat kecerdasan buatan (AI), mata kuliah ini lebih menekankan alur pikir
```math
\boxed{
\text{masalah}
\longrightarrow
\text{model}
\longrightarrow
\text{algoritma}
\longrightarrow
\text{program}
\longrightarrow
\text{hasil}
}
```
sehingga kemampuan menulis sintaks program (dengan bahasa apapun, tidak terbatas C dan Python) dapat lebih banyak dipelajari secara mandiri. Setelah mengikuti mata kuliah ini, mahasiswa diharapkan dapat merumuskan persoalan teknik secara komputasional, memilih langkah penyelesaian yang sesuai, mengimplementasikannya, memeriksa kebenaran hasil, dan menggunakan perangkat komputasi sebagai bagian dari praktik sains dan rekayasa.

## Daftar Materi

| No. | Topik                                                      | *Link* Catatan Kuliah                      |
| --: | ---------------------------------------------------------- | ------------------------------------------ |
|   1 | 💻 Pengenalan algoritma, komputer, dan representasi data   | [Materi 1](Catatan-Kuliah/pertemuan-01.md) |
|   2 | 🧠 Berpikir algoritmik dan perancangan algoritma           | [Materi 2](Catatan-Kuliah/pertemuan-02.md) |
|   3 | 🧩 Dasar-dasar pemrograman dalam bahasa C                  | [Materi 3](Catatan-Kuliah/pertemuan-03.md) |
|   4 | 🔀 Percabangan dan pengulangan                             | [Materi 4](Catatan-Kuliah/pertemuan-04.md)                                   |
|   5 | 🔁 Pola algoritma iteratif                                 | [Materi 5](Catatan-Kuliah/pertemuan-05.md)                                   |
|   6 | 🧱 Larik, fungsi, dan modularisasi program                 | menyusul                                   |
|   7 | 📁 Data terstruktur dan pengolahan berkas dalam C          | menyusul                                   |
|   8 | ⚙️ Integrasi pemrograman C untuk kasus Teknik Fisika       | menyusul                                   |
|   9 | 🐍 Python untuk komputasi ilmiah                           | menyusul                                   |
|  10 | 🔎 Algoritma pencarian                                     | menyusul                                   |
|  11 | 📊 Algoritma pengurutan                                    | menyusul                                   |
|  12 | 🔗 Studi kasus terintegrasi C dan Python                   | menyusul                                   |
|  13 | 🌳 Pengantar algoritma *machine learning*: *decision tree* | menyusul                                   |



## Capaian Pembelajaran Program Studi

Mata kuliah ini mendukung beberapa Capaian Pembelajaran (CP) Program Studi (Prodi) atau *Program Learning Outcomes* (PLO) di bawah ini, khususnya untuk Prodi S-1 Teknik Fisika di Telkom University.

| Kode | Capaian Pembelajaran Program Studi Teknik Fisika |
|---|---|
| **CP-05** | Memiliki kemampuan untuk menggunakan teknik, *skill*, dan perangkat *engineering* dalam praktik *engineering*. |
| **CP-06** | Memiliki kemampuan dalam mengidentifikasi, merumuskan, dan memecahkan persoalan kompleks di bidang *engineering*. |
| **CP-07** | Memiliki kemampuan dalam mendesain sistem, komponen, atau proses yang mempertemukan kebutuhan yang ditinjau di bidang Teknik Fisika dengan kendala riil dalam dunia industri, dalam rangka menjembatani antara sains, teknik, maupun sosial humaniora. |

## Capaian Pembelajaran Mata Kuliah

Capaian Pembelajaran Mata Kuliah (CPMK) atau *Course Learning Outcomes* (CLO) dan kaitannya dengan CP Program Studi adalah sebagai berikut.

| Kode | Capaian Pembelajaran Mata Kuliah | CP Prodi yang Didukung |
|---|---|---|
| **CPMK-1** | Memahami dan menggunakan konsep algoritma dalam beberapa kasus. | **CP-05** |
| **CPMK-2** | Memahami dan menerapkan konsep pengulangan dan percabangan dalam algoritma. | **CP-05** |
| **CPMK-3** | Memahami dan menerapkan bahasa C dalam algoritma. | **CP-05** |
| **CPMK-4** | Membuat algoritma dan mengaplikasikannya menggunakan bahasa pemrograman C dan Python sebagai pembanding. | **CP-06** |
| **CPMK-5** | Menerapkan konsep *file* untuk menyimpan dan membaca data. | **CP-07** |

Secara keseluruhan, mata kuliah diarahkan agar mahasiswa mampu membangun alur kerja komputasi
```math
\boxed{
\text{persoalan fisis}
\rightarrow
\text{algoritma}
\rightarrow
\text{program C}
\rightarrow
\text{data}
\rightarrow
\text{Python}
\rightarrow
\text{analisis dan visualisasi}.
}
```

## Media Pembelajaran

Media dan perangkat yang digunakan dalam mata kuliah meliputi:
- catatan kuliah dalam format Markdown pada repositori GitHub ini;
- contoh program dan latihan menggunakan bahasa C;
- GCC sebagai *compiler* bahasa C;
- Visual Studio Code atau editor kode lain yang mendukung pemrograman C dan Python;
- MSYS2 untuk lingkungan GCC pada Windows;
- Windows Subsystem for Linux (WSL) atau sistem operasi Linux sebagai lingkungan pengembangan alternatif;
- bahasa Python untuk komputasi, pengolahan data, dan visualisasi;
- NumPy untuk komputasi numerik dasar;
- Matplotlib untuk visualisasi data;
- terminal atau *command line* untuk proses kompilasi dan eksekusi program;
- Git dan GitHub untuk distribusi materi serta pengelolaan kode.

Mahasiswa dianjurkan untuk mencoba setiap contoh program secara langsung, mengubah parameter, memprediksi hasil sebelum program dijalankan, kemudian membandingkan keluaran program dengan perhitungan manual atau tinjauan fisis.

## Rencana Materi Kuliah

Mata kuliah direncanakan dalam 16 pekan, meliputi 13 pertemuan utama, 1 pekan UTS, 1 pekan presentasi proyek (tugas besar), dan 1 pekan evaluasi akhir. Di bawah ini, 13 materi pertemuan utama diuraikan satu demi satu.

### 1. Pengenalan algoritma, komputer, dan representasi data

[Catatan Kuliah 1](Catatan-Kuliah/pertemuan-01.md)

Pokok bahasan:

- hubungan masalah, model, algoritma, program, dan hasil;
- gambaran sederhana cara kerja komputer;
- CPU, memori, dan penyimpanan;
- kode sumber, *compiler*, dan *executable*;
- bit, byte, bilangan biner, dan heksadesimal;
- representasi bilangan bulat;
- *overflow*;
- representasi karakter;
- bilangan *floating-point*, presisi, dan kesalahan pembulatan;
- program C sederhana dan pemeriksaan hasil komputasi.

### 2. Berpikir algoritmik dan perancangan algoritma

[Catatan Kuliah 2](Catatan-Kuliah/pertemuan-02.md)

Pokok bahasan:

- pola pikir algoritmik;
- masukan, keluaran, spesifikasi, prakondisi, dan pascakondisi;
- dekomposisi masalah;
- algoritma dalam kalimat berurutan;
- diagram alir;
- *pseudocode*;
- *tracing* dan keadaan algoritma;
- konsep invarian secara intuitif;
- pemeriksaan kebenaran algoritma;
- kompleksitas waktu dan ruang secara intuitif;
- pengenalan $O(1)$, $O(N)$, dan $O(N^2)$;
- ilustrasi implementasi algoritma dalam bahasa C.

### 3. Dasar-dasar pemrograman dalam bahasa C

[Catatan Kuliah 3](Catatan-Kuliah/pertemuan-03.md)

Pokok bahasan:

- struktur dasar program C;
- variabel dan konstanta;
- tipe data dasar;
- ekspresi dan operator aritmetika;
- operator relasional dan logika;
- konsep Boolean;
- konversi tipe data;
- input dan output menggunakan `printf` dan `scanf`;
- format spesifikasi data;
- *compiler warning* dan kebiasaan pemrograman yang baik;
- contoh perhitungan sederhana dalam fisika dan rekayasa.

### 4. Percabangan dan pengulangan

[Catatan Kuliah 4](Catatan-Kuliah/pertemuan-04.md)

Pokok bahasan:

- aliran kontrol dalam program;
- `if`, `else if`, dan `else`;
- `switch`;
- `while`;
- `do-while`;
- `for`;
- *tracing* aliran program;
- kasus batas;
- contoh klasifikasi dan perhitungan berulang pada persoalan Teknik Fisika.

### 5. Pola algoritma iteratif

Pokok bahasan:

- *counter* dan *accumulator*;
- pencarian nilai minimum dan maksimum;
- *sentinel-controlled loop*;
- validasi masukan;
- pengulangan bersarang;
- pembuatan tabel komputasi;
- algoritma iteratif sederhana;
- pendekatan numerik dan kriteria penghentian;
- analisis perubahan keadaan program selama iterasi.

### 6. Larik, fungsi, dan modularisasi program

Pokok bahasan:

- larik satu dimensi;
- pengaksesan dan penelusuran elemen larik;
- pengantar larik dua dimensi;
- fungsi;
- parameter dan nilai kembalian;
- ruang lingkup variabel;
- modularisasi dan penggunaan ulang kode;
- *pointer* dasar;
- hubungan antara larik, alamat memori, dan *pointer*;
- pengiriman larik ke fungsi;
- pengantar *string* dalam bahasa C.

### 7. Data terstruktur dan pengolahan berkas dalam C

Pokok bahasan:

- `struct`;
- larik dari `struct`;
- representasi data pengukuran;
- pengolahan *string* dasar;
- `FILE *`;
- membuka dan menutup berkas;
- membaca dan menulis berkas teks;
- pengolahan data CSV sederhana;
- pemeriksaan kesalahan pada operasi berkas;
- pola `open -> check -> read/write -> close`.

### 8. Integrasi pemrograman C untuk kasus Teknik Fisika

Pokok bahasan:

- perumusan persoalan fisika menjadi algoritma;
- pengembangan program modular;
- penggabungan percabangan, pengulangan, larik, fungsi, dan `struct`;
- membaca data pengukuran;
- statistik sederhana;
- pemeriksaan data;
- pencarian kondisi tertentu;
- penulisan hasil ke berkas;
- pengujian dan pemeriksaan kewajaran hasil secara fisis.

### 9. Python untuk komputasi ilmiah

Pokok bahasan:

- transisi konsep dari C ke Python;
- variabel, ekspresi, percabangan, pengulangan, dan fungsi dalam Python;
- *list*;
- pengolahan berkas;
- pengantar NumPy;
- membaca data numerik;
- operasi dasar pada data;
- pengantar Matplotlib;
- visualisasi hasil program atau data eksperimen.

Pertemuan ini tidak dimaksudkan sebagai pengantar lengkap seluruh bahasa Python. Fokusnya adalah menggunakan Python sebagai perangkat komputasi bagi mahasiswa yang telah memahami konsep dasar pemrograman.

### 10. Algoritma pencarian

Pokok bahasan:

- persoalan pencarian;
- *linear search*;
- *binary search*;
- prakondisi data terurut;
- pemeriksaan kebenaran algoritma;
- kompleksitas $O(N)$ dan $O(\log N)$;
- perbandingan jumlah operasi;
- pengukuran waktu eksekusi secara sederhana;
- implementasi dan perbandingan menggunakan C.

### 11. Algoritma pengurutan

Pokok bahasan:

- tujuan pengurutan data;
- *selection sort*;
- *insertion sort*;
- pengantar *bubble sort*;
- *tracing* algoritma pengurutan;
- kompleksitas $O(N^2)$;
- pengantar algoritma $O(N\log N)$;
- penggunaan fungsi pengurutan dari pustaka;
- perbandingan analisis kompleksitas dengan waktu eksekusi.

### 12. Studi kasus terintegrasi C dan Python

Pokok bahasan:

- alur data dari program C menuju Python;
- pembacaan dan validasi data menggunakan C;
- penyimpanan hasil ke berkas;
- statistik, pencarian, dan pengurutan data;
- pembacaan hasil menggunakan Python;
- pengolahan data menggunakan NumPy;
- visualisasi menggunakan Matplotlib;
- interpretasi hasil dalam konteks persoalan Teknik Fisika.

Salah satu pola kerja yang digunakan adalah

```text
data.csv
   ↓
program C
   ↓
result.csv
   ↓
Python
   ↓
NumPy
   ↓
Matplotlib
   ↓
analisis dan visualisasi
```

### 13. Pengantar algoritma *machine learning*: *decision tree*

Pokok bahasan:

- pengantar *machine learning*;
- *supervised learning*;
- *feature* dan *label*;
- klasifikasi;
- aturan keputusan berbasis ambang;
- struktur *decision tree*;
- pemilihan *split*;
- Gini impurity atau entropy secara sederhana;
- data latih dan data uji;
- akurasi;
- *overfitting*;
- ilustrasi implementasi menggunakan pustaka Python.

Pertemuan ini difokuskan pada pemahaman bahwa pustaka *machine learning* tetap mengimplementasikan suatu algoritma. Tujuan utamanya bukan menguasai seluruh bidang *machine learning*, tetapi melihat kelanjutan konsep algoritmik yang telah dipelajari sepanjang mata kuliah.

## Daftar Pustaka

1. Rinaldi Munir dan Leony Lidya, *Algoritma dan Pemrograman*, Edisi Keenam, Penerbit Informatika, 2016.

2. TutorialsPoint, *C Tutorial*. 
   https://www.tutorialspoint.com/cprogramming

3. TutorialsPoint, *Learn C by Examples*.
   https://www.tutorialspoint.com/learn_c_by_examples

4. Python Software Foundation, *The Python Tutorial*.  
   https://docs.python.org/3/tutorial

5. BRIN Research Center for Quantum Physics, *Python Minimalis*.
   https://github.com/BRIN-Q/Python-minimalis

## Perhatian!

Catatan kuliah dalam repositori ini dirancang untuk dibaca secara berurutan. Contoh program sebaiknya tidak hanya disalin dan dijalankan, tetapi digunakan sebagai bahan "eksperimen".

Untuk setiap contoh program, mahasiswa dianjurkan mengikuti pola

```text
pahami masalah
    ↓
prediksi hasil
    ↓
jalankan program
    ↓
bandingkan hasil
    ↓
ubah parameter
    ↓
analisis kembali
```

Tujuan akhirnya adalah menghasilkan program yang merepresentasikan algoritma dan model dengan benar serta memberikan hasil yang dapat dipertanggungjawabkan secara komputasional dan fisis. Jadi, sekali lagi, mahasiswa tidak sekadar membuat program yang dapat dijalankan.
