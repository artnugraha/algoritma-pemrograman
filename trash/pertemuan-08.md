# Kuliah 8: Integrasi Pemrograman C untuk Kasus Teknik Fisika

## Program yang utuh

Pada kuliah-kuliah sebelumnya kita telah mempelajari banyak konsep secara terpisah. Kita telah menggunakan percabangan, pengulangan, larik, fungsi, `struct`, *pointer* dasar, *string*, dan operasi berkas.

Pada tahap ini, tantangannya bukan lagi memahami satu sintaks tertentu. Kita sekarang perlu menggabungkan konsep-konsep tersebut menjadi sebuah program yang menyelesaikan persoalan teknik secara utuh.

Dalam praktik rekayasa, program jarang hanya melakukan satu operasi kecil. Program biasanya membaca data, memeriksa keabsahan, menghitung besaran turunan, mencari kondisi tertentu, menulis hasil, dan kemudian membantu kita menilai apakah hasil tersebut masuk akal secara fisis.

Alur kerja yang ingin kita bangun menghubungkan persoalan fisika dengan proses komputasi secara bertahap. Setiap tahap menghasilkan informasi yang menjadi dasar bagi tahap berikutnya. Secara ringkas, hubungan tersebut dapat dituliskan sebagai

```math
\boxed{
\text{persoalan fisika}
\rightarrow
\text{model}
\rightarrow
\text{algoritma}
\rightarrow
\text{program modular}
\rightarrow
\text{data}
\rightarrow
\text{analisis}
\rightarrow
\text{verifikasi}
}
```

Kuliah ini berfungsi sebagai integrasi dari materi C yang telah dipelajari sejauh ini. Fokusnya adalah cara berpikir ketika membangun program di dunia keteknikan/rekayasa.

## Studi kasus utama: eksperimen gerak satu dimensi

Kita akan menggunakan eksperimen gerak satu dimensi sebagai studi kasus utama. Sebuah sensor posisi menghasilkan data waktu dan posisi benda yang bergerak sepanjang satu garis.

Berkas masukan mempunyai dua kolom, yaitu waktu dan posisi. Contoh bentuk sederhananya ditunjukkan pada data berikut.

```text
time_s,position_m
0.0,0.00
0.5,0.62
1.0,1.31
1.5,2.07
2.0,2.90
2.5,3.81
3.0,4.79
```

Dari data tersebut kita ingin menghitung kecepatan rata-rata pada setiap interval. Kita juga ingin mencari kecepatan maksimum absolut, rata-rata kecepatan, dan waktu ketika suatu ambang kecepatan pertama kali dilampaui.

Program juga harus memeriksa apakah waktu bertambah secara monoton. Jika ada dua waktu yang sama atau urutannya mundur, interval tersebut tidak dapat digunakan untuk menghitung kecepatan.

## Merumuskan persoalan fisika

Sebelum menulis kode, kita harus menyatakan apa yang diketahui dan apa yang ingin dihitung. Kebiasaan ini mencegah program berkembang menjadi kumpulan instruksi tanpa tujuan yang jelas.

Besaran yang diketahui adalah waktu dan posisi pada setiap sampel. Secara matematis, pasangan besaran tersebut dapat dituliskan sebagai berikut.

```math
t_i,
\qquad
x_i,
```

dengan indeks

```math
i=0,1,\ldots,N-1.
```

Kecepatan rata-rata pada interval antara dua sampel berurutan ditentukan dari perubahan posisi terhadap perubahan waktu. Besaran ini mewakili rata-rata gerak benda selama satu interval pengukuran. Persamaannya diberikan oleh

```math
v_i
=
\frac{
x_{i+1}-x_i
}{
t_{i+1}-t_i
}.
```

Jika terdapat $N$ sampel posisi, maka jumlah interval yang dapat dianalisis adalah $N-1$. Hubungan tersebut langsung memengaruhi desain larik dan batas pengulangan.

## Menentukan masukan dan keluaran

Program perlu memiliki spesifikasi yang jelas sebelum implementasi dimulai. Masukan utama adalah berkas CSV yang memuat waktu dan posisi.

Keluaran yang diinginkan meliputi jumlah data valid, jumlah interval valid, kecepatan tiap interval, rata-rata kecepatan, kecepatan maksimum absolut, dan informasi waktu terkait. Program juga harus menghasilkan berkas hasil terproses serta ringkasan analisis.

## Dekomposisi program

Program besar sebaiknya dipecah menjadi bagian yang lebih kecil. Untuk studi kasus ini, salah satu dekomposisi yang masuk akal ditunjukkan berikut ini.

```text
main
 |
 +--> load_motion_data
 |
 +--> validate_time_order
 |
 +--> compute_velocities
 |
 +--> mean_velocity
 |
 +--> max_abs_velocity_index
 |
 +--> first_threshold_crossing
 |
 +--> save_processed_data
 |
 +--> save_summary
```

Struktur tersebut membuat tanggung jawab setiap fungsi lebih jelas. Jika hasil kecepatan salah, kita dapat memeriksa fungsi `compute_velocities` tanpa harus menelusuri seluruh program.

## Representasi data dengan `struct`

Satu sampel pengukuran memiliki dua besaran yang saling berkaitan, yaitu waktu dan posisi. Karena itu, satu sampel cocok direpresentasikan menggunakan `struct`.

```c
typedef struct
{
    double time;
    double position;
} MotionSample;
```

Satu elemen `MotionSample` merepresentasikan satu baris data dari berkas CSV. Pendekatan ini membuat representasi data di memori sesuai dengan struktur data di berkas.

Untuk data hasil pengolahan, kita dapat membuat `struct` kedua. Struktur tersebut menyimpan dua waktu dan kecepatan pada interval tersebut.

```c
typedef struct
{
    double time_start;
    double time_end;
    double velocity;
} VelocitySample;
```

Dengan dua tipe tersebut, data mentah dan data turunan tetap dipisahkan dengan jelas. Pemisahan ini membantu menjaga makna setiap larik.

## Batas kapasitas data

Untuk program sederhana, kita dapat menggunakan larik berukuran tetap. Misalkan kapasitas maksimum yang kita izinkan adalah 2000 sampel.

```c
#define MAX_DATA 2000
```

Kemudian kita dapat membuat dua larik yang saling berkaitan. Bentuk deklarasinya ditunjukkan sebagai berikut.

```c
MotionSample motion[MAX_DATA];
VelocitySample velocity[MAX_DATA - 1];
```

Program harus selalu memeriksa agar jumlah data yang dibaca tidak melebihi kapasitas. Pemeriksaan kapasitas merupakan bagian dari keamanan program.

## Membaca data dari CSV

Kita akan menggunakan pola `open -> check -> read -> validate -> store -> close`. Fungsi pembacaan sebaiknya bertanggung jawab terhadap operasi berkas dan parsing dasar.

Fungsi analisis tidak perlu mengetahui detail `fopen`, `fgets`, atau `sscanf`. Pemisahan ini membuat program lebih modular dan lebih mudah diuji.

### Fungsi `load_motion_data`

```c
int load_motion_data(
    const char filename[],
    MotionSample data[],
    int max_data)
{
    FILE *fp =
        fopen(filename, "r");

    if (fp == NULL)
    {
        perror(filename);
        return -1;
    }

    char line[256];

    if (fgets(line,
              sizeof(line),
              fp) == NULL)
    {
        fclose(fp);
        return 0;
    }

    int n = 0;

    while (fgets(line,
                 sizeof(line),
                 fp) != NULL)
    {
        MotionSample sample;

        int matched =
            sscanf(line,
                   "%lf,%lf",
                   &sample.time,
                   &sample.position);

        if (matched != 2)
        {
            printf("Skipping invalid line: %s",
                   line);
            continue;
        }

        if (n >= max_data)
        {
            printf("Data capacity exceeded.\n");
            break;
        }

        data[n] = sample;
        n++;
    }

    fclose(fp);

    return n;
}
```

Fungsi mengembalikan `-1` jika berkas gagal dibuka. Nilai nol berarti tidak ada data yang berhasil dimuat, sedangkan nilai positif menunjukkan jumlah rekaman valid.

## Pemeriksaan data

Data yang berhasil diparsing belum tentu layak digunakan. Dalam eksperimen gerak, waktu harus bertambah dari satu sampel ke sampel berikutnya.

Kondisi yang diharapkan adalah

```math
t_{i+1}>t_i.
```

Jika kondisi tersebut tidak terpenuhi, maka selang waktu bernilai nol atau negatif. Kecepatan interval tersebut tidak dapat diperlakukan sebagai hasil normal.

### Fungsi memeriksa urutan waktu

```c
int validate_time_order(
    const MotionSample data[],
    int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        if (data[i + 1].time
            <= data[i].time)
        {
            return 0;
        }
    }

    return 1;
}
```

Fungsi mengembalikan `1` jika seluruh waktu bertambah secara ketat. Fungsi mengembalikan `0` segera setelah menemukan pelanggaran pertama.

Pola tersebut merupakan contoh pencarian kondisi tertentu menggunakan pengulangan dan percabangan. Program tidak selalu harus memproses seluruh larik jika satu pelanggaran sudah cukup untuk menyatakan data tidak valid.

## Menghitung kecepatan interval

Jika urutan waktu valid, kita dapat menghitung kecepatan untuk setiap pasangan sampel berurutan. Hasilnya disimpan dalam larik `VelocitySample`.

```c
int compute_velocities(
    const MotionSample motion[],
    int n,
    VelocitySample velocity[])
{
    if (n < 2)
    {
        return 0;
    }

    for (int i = 0; i < n - 1; i++)
    {
        double dt =
            motion[i + 1].time
            - motion[i].time;

        double dx =
            motion[i + 1].position
            - motion[i].position;

        velocity[i].time_start =
            motion[i].time;

        velocity[i].time_end =
            motion[i + 1].time;

        velocity[i].velocity =
            dx / dt;
    }

    return n - 1;
}
```

Fungsi mengembalikan jumlah interval yang berhasil dihitung. Jika jumlah sampel kurang dari dua, tidak ada interval yang dapat dibentuk.

## Statistik sederhana

Setelah kecepatan tersedia, kita dapat menghitung statistik sederhana. Pada tahap ini, statistik yang digunakan adalah rata-rata dan maksimum absolut.

Rata-rata kecepatan interval diperoleh dari jumlah seluruh kecepatan dibagi banyak interval. Besaran ini memberikan ringkasan sederhana terhadap seluruh nilai interval. Secara matematis, nilainya dihitung sebagai

```math
\overline{v}
=
\frac{1}{M}
\sum_{i=0}^{M-1}v_i,
```

dengan $M=N-1$. Rata-rata ini adalah rata-rata aritmetika dari nilai kecepatan interval.

### Fungsi rata-rata kecepatan

```c
double mean_velocity(
    const VelocitySample data[],
    int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum += data[i].velocity;
    }

    return sum / n;
}
```

Fungsi tersebut mengasumsikan `n > 0`. Pemeriksaan kondisi tersebut sebaiknya dilakukan oleh pemanggil sebelum fungsi digunakan.

## Kecepatan maksimum absolut

Dalam banyak kasus, besar kecepatan lebih penting daripada tandanya. Karena itu, kita dapat mencari nilai maksimum dari $|v_i|$.

Fungsi berikut mengembalikan indeks interval dengan kecepatan absolut terbesar. Dengan mengembalikan indeks, kita juga dapat memperoleh waktu awal dan akhir interval yang sama.

```c
#include <math.h>

int max_abs_velocity_index(
    const VelocitySample data[],
    int n)
{
    int index = 0;

    for (int i = 1; i < n; i++)
    {
        if (fabs(data[i].velocity)
            >
            fabs(data[index].velocity))
        {
            index = i;
        }
    }

    return index;
}
```


## Pencarian kondisi tertentu

Selain statistik, program teknik sering perlu mencari kejadian khusus. Contohnya adalah saat pertama kali kecepatan melampaui nilai ambang tertentu.

Misalkan ambang yang ingin diperiksa dinyatakan dengan suatu nilai batas kecepatan. Ambang ini dapat ditentukan berdasarkan kebutuhan eksperimen atau spesifikasi sistem. Nilai tersebut kita tulis sebagai

```math
v_{\text{limit}}.
```

Program kemudian mencari interval pertama yang melampaui ambang tersebut. Pencarian dimulai dari data paling awal agar kejadian pertama dapat ditemukan. Kondisi pencariannya adalah

```math
|v_i|
>
v_{\text{limit}}.
```

Fungsi berikut mengembalikan indeks pertama yang memenuhi kondisi. Jika tidak ditemukan, fungsi mengembalikan `-1`.

```c
int first_threshold_crossing(
    const VelocitySample data[],
    int n,
    double limit)
{
    for (int i = 0; i < n; i++)
    {
        if (fabs(data[i].velocity)
            > limit)
        {
            return i;
        }
    }

    return -1;
}
```

Pola ini merupakan contoh **linear search** sederhana. Program menelusuri data dari awal dan berhenti ketika kondisi pertama ditemukan.

## Mengapa indeks lebih berguna daripada hanya nilai?

Jika fungsi hanya mengembalikan kecepatan maksimum, kita kehilangan informasi tentang kapan nilai tersebut terjadi. Dengan mengembalikan indeks, kita dapat mengambil seluruh rekaman yang berkaitan.

Sebagai contoh,

```c
int i_max =
    max_abs_velocity_index(
        velocity,
        n_velocity);
```

kemudian

```c
velocity[i_max].time_start
```

dan

```c
velocity[i_max].time_end
```

memberikan interval waktunya. Pola ini sangat umum ketika kita ingin mempertahankan hubungan antara nilai dan konteks pengukurannya.

## Menulis hasil terproses

Data hasil analisis sebaiknya tidak selalu menggantikan data mentah. Menyimpan hasil pada berkas baru membuat proses lebih mudah ditelusuri dan memungkinkan kita membandingkan data sebelum dan sesudah pengolahan.

Untuk studi kasus ini, kita akan menulis data hasil ke berkas terpisah agar data mentah tidak berubah. Pemisahan ini memudahkan pemeriksaan ulang terhadap proses komputasi. Nama berkas hasilnya adalah

```text
velocity.csv
```

dengan skema

```text
time_start_s,time_end_s,velocity_m_per_s
```

Fungsi penulis bertanggung jawab membuka berkas, menulis header dan data, lalu menutup berkas. Salah satu implementasinya dapat dibuat sebagai berikut.

```c
int save_processed_data(
    const char filename[],
    const VelocitySample data[],
    int n)
{
    FILE *fp =
        fopen(filename, "w");

    if (fp == NULL)
    {
        perror(filename);
        return 0;
    }

    if (fprintf(
            fp,
            "time_start_s,time_end_s,"
            "velocity_m_per_s\n") < 0)
    {
        fclose(fp);
        return 0;
    }

    for (int i = 0; i < n; i++)
    {
        if (fprintf(
                fp,
                "%.6f,%.6f,%.9f\n",
                data[i].time_start,
                data[i].time_end,
                data[i].velocity) < 0)
        {
            fclose(fp);
            return 0;
        }
    }

    if (fclose(fp) != 0)
    {
        return 0;
    }

    return 1;
}
```

Fungsi mengembalikan `1` jika operasi selesai tanpa kesalahan yang terdeteksi. Nilai `0` digunakan untuk menandai kegagalan.

## Menulis ringkasan analisis

Selain data terproses, program dapat menghasilkan berkas ringkasan yang mudah dibaca manusia. Ringkasan tersebut tidak harus berbentuk CSV karena tujuannya adalah dokumentasi hasil utama.

Sebagai contoh, `summary.txt` dapat berisi ringkasan hasil utama dalam format yang mudah dibaca manusia. Ringkasan tersebut melengkapi data rinci yang disimpan pada CSV. Salah satu bentuk isinya adalah

```text
Valid position samples : 7
Valid intervals        : 6
Mean velocity          : 1.596667 m/s
Maximum |velocity|     : 1.960000 m/s
Maximum interval       : 2.500000 s to 3.000000 s
Threshold              : 1.800000 m/s
First crossing         : 2.000000 s to 2.500000 s
```

Berkas semacam ini berguna untuk mencatat hasil analisis utama. Data lengkap tetap disimpan pada CSV.

### Fungsi `save_summary`

```c
int save_summary(
    const char filename[],
    int n_motion,
    int n_velocity,
    double mean_v,
    const VelocitySample *max_sample,
    double threshold,
    const VelocitySample *crossing)
{
    FILE *fp =
        fopen(filename, "w");

    if (fp == NULL)
    {
        perror(filename);
        return 0;
    }

    fprintf(fp,
            "Valid position samples : %d\n",
            n_motion);

    fprintf(fp,
            "Valid intervals        : %d\n",
            n_velocity);

    fprintf(fp,
            "Mean velocity          : %.6f m/s\n",
            mean_v);

    fprintf(fp,
            "Maximum |velocity|     : %.6f m/s\n",
            fabs(max_sample->velocity));

    fprintf(fp,
            "Maximum interval       : "
            "%.6f s to %.6f s\n",
            max_sample->time_start,
            max_sample->time_end);

    fprintf(fp,
            "Threshold              : %.6f m/s\n",
            threshold);

    if (crossing != NULL)
    {
        fprintf(fp,
                "First crossing         : "
                "%.6f s to %.6f s\n",
                crossing->time_start,
                crossing->time_end);
    }
    else
    {
        fprintf(fp,
                "First crossing         : none\n");
    }

    if (fclose(fp) != 0)
    {
        return 0;
    }

    return 1;
}
```

Fungsi menerima *pointer* ke rekaman maksimum dan rekaman ambang pertama. Jika ambang tidak pernah dilampaui, argumen `crossing` dapat berupa `NULL`.

## Menggunakan `NULL` sebagai penanda

*Pointer* `NULL` dapat digunakan untuk menyatakan bahwa tidak ada objek valid yang dirujuk. Pada contoh ringkasan, `crossing == NULL` berarti kondisi ambang tidak pernah ditemukan.

Pola ini cukup umum dalam C. Namun, setiap fungsi yang menerima *pointer* yang mungkin `NULL` harus memeriksanya sebelum melakukan dereferensi.

## Program utama sebagai pengatur alur

Setelah fungsi-fungsi utama tersedia, `main` seharusnya tidak berisi detail perhitungan yang panjang. Tugas `main` adalah mengatur urutan kerja program dan menangani kondisi gagal pada tingkat tinggi.

Alurnya dapat ditulis sebagai

```text
read
 ↓
check
 ↓
compute
 ↓
analyze
 ↓
search
 ↓
save
```

Struktur seperti ini membuat program lebih mudah dibaca. Ketika seseorang membuka `main`, ia dapat memahami gambaran besar tanpa langsung melihat seluruh detail algoritma.

## Program terintegrasi

Berikut salah satu implementasi lengkap untuk studi kasus ini. Program menggabungkan `struct`, larik, fungsi, percabangan, pengulangan, pencarian kondisi, operasi berkas, dan pemeriksaan hasil.

```c
#include <stdio.h>
#include <math.h>

#define MAX_DATA 2000

typedef struct
{
    double time;
    double position;
} MotionSample;

typedef struct
{
    double time_start;
    double time_end;
    double velocity;
} VelocitySample;

int load_motion_data(
    const char filename[],
    MotionSample data[],
    int max_data);

int validate_time_order(
    const MotionSample data[],
    int n);

int compute_velocities(
    const MotionSample motion[],
    int n,
    VelocitySample velocity[]);

double mean_velocity(
    const VelocitySample data[],
    int n);

int max_abs_velocity_index(
    const VelocitySample data[],
    int n);

int first_threshold_crossing(
    const VelocitySample data[],
    int n,
    double limit);

int save_processed_data(
    const char filename[],
    const VelocitySample data[],
    int n);

int save_summary(
    const char filename[],
    int n_motion,
    int n_velocity,
    double mean_v,
    const VelocitySample *max_sample,
    double threshold,
    const VelocitySample *crossing);

int main(void)
{
    MotionSample motion[MAX_DATA];
    VelocitySample velocity[MAX_DATA - 1];

    const double threshold = 1.8;

    int n_motion =
        load_motion_data(
            "motion.csv",
            motion,
            MAX_DATA);

    if (n_motion < 0)
    {
        return 1;
    }

    if (n_motion < 2)
    {
        printf("Not enough data.\n");
        return 1;
    }

    if (!validate_time_order(
            motion,
            n_motion))
    {
        printf("Time data are not strictly increasing.\n");
        return 1;
    }

    int n_velocity =
        compute_velocities(
            motion,
            n_motion,
            velocity);

    if (n_velocity <= 0)
    {
        printf("No valid interval.\n");
        return 1;
    }

    double mean_v =
        mean_velocity(
            velocity,
            n_velocity);

    int i_max =
        max_abs_velocity_index(
            velocity,
            n_velocity);

    int i_cross =
        first_threshold_crossing(
            velocity,
            n_velocity,
            threshold);

    printf("Valid samples   = %d\n",
           n_motion);

    printf("Valid intervals = %d\n",
           n_velocity);

    printf("Mean velocity   = %.6f m/s\n",
           mean_v);

    printf("Maximum |v|     = %.6f m/s\n",
           fabs(velocity[i_max].velocity));

    if (i_cross >= 0)
    {
        printf("First |v| > %.3f m/s: "
               "%.3f s to %.3f s\n",
               threshold,
               velocity[i_cross].time_start,
               velocity[i_cross].time_end);
    }
    else
    {
        printf("Threshold was not crossed.\n");
    }

    if (!save_processed_data(
            "velocity.csv",
            velocity,
            n_velocity))
    {
        printf("Failed to save velocity.csv.\n");
        return 1;
    }

    const VelocitySample *crossing = NULL;

    if (i_cross >= 0)
    {
        crossing =
            &velocity[i_cross];
    }

    if (!save_summary(
            "summary.txt",
            n_motion,
            n_velocity,
            mean_v,
            &velocity[i_max],
            threshold,
            crossing))
    {
        printf("Failed to save summary.txt.\n");
        return 1;
    }

    return 0;
}
```

Program utama tersebut belum menampilkan implementasi semua fungsi karena implementasinya telah dijelaskan sebelumnya. Dalam berkas program sebenarnya, seluruh implementasi fungsi harus disertakan agar dapat dikompilasi.

## Menyusun program secara bertahap

Program terintegrasi sebaiknya tidak ditulis sekaligus dari baris pertama sampai terakhir. Strategi yang lebih aman adalah membangun program secara bertahap dan menguji setiap tahap.

Urutan pengembangan yang masuk akal adalah membangun program dari bagian yang paling mendasar menuju integrasi penuh. Contoh urutannya ditunjukkan berikut ini.

```text
1. definisikan struct
2. uji pembacaan CSV
3. uji validasi waktu
4. uji perhitungan kecepatan
5. uji statistik
6. uji pencarian ambang
7. uji penulisan CSV
8. uji penulisan ringkasan
9. gabungkan seluruh bagian
```

Setiap tahap sebaiknya menggunakan data uji kecil yang hasilnya dapat diprediksi. Pendekatan tersebut memudahkan lokasi kesalahan ketika program tidak bekerja sesuai harapan.

## Pengujian unit secara sederhana

Istilah **unit test** mengacu pada pengujian bagian kecil program secara terpisah. Pada mata kuliah ini kita belum memerlukan kerangka pengujian khusus, tetapi idenya sudah dapat diterapkan.

Misalnya, fungsi `mean_velocity` dapat diuji menggunakan data buatan yang sederhana. Gunakan tiga nilai berikut agar hasilnya mudah diperiksa.

```math
1,\quad2,\quad3.
```

Rata-rata yang diharapkan adalah

```math
2.
```

Jika fungsi menghasilkan nilai lain, kita tahu kesalahan berada pada fungsi atau data uji. Kita tidak perlu membaca berkas untuk menguji fungsi tersebut.

## Data uji yang baik

Data uji sebaiknya tidak hanya berisi kasus normal. Program teknik perlu diuji menggunakan kasus biasa, kasus batas, dan data yang sengaja salah.

Untuk studi kasus gerak, data uji sebaiknya mencakup kasus normal dan kasus yang sengaja dibuat bermasalah. Kombinasi keduanya membantu memeriksa apakah program menangani asumsi dan batas dengan benar. Beberapa contoh yang perlu dicoba meliputi

- dua titik saja;
- waktu yang sama pada dua baris;
- waktu menurun;
- posisi konstan;
- posisi menurun;
- kecepatan tepat sama dengan ambang;
- kecepatan sedikit di atas ambang;
- baris CSV rusak;
- berkas kosong;
- jumlah data melebihi kapasitas.

Variasi tersebut membantu memastikan program tidak hanya bekerja pada satu contoh ideal. Pengujian yang baik mencoba menemukan kondisi yang dapat merusak asumsi program.

## Kasus batas: posisi konstan

Jika posisi tidak berubah,

```math
x_{i+1}=x_i,
```

maka kecepatan interval seharusnya nol. Program harus menghasilkan hasil tersebut tanpa perlakuan khusus.

Kasus ini berguna sebagai pengujian sederhana. Jika program menghasilkan kecepatan bukan nol, rumus atau data sedang diproses secara salah.

## Kasus batas: gerak berkecepatan konstan

Misalkan posisi diberikan oleh

```math
x(t)=x_0+vt.
```

Jika data dibuat tanpa galat pengukuran dan interval waktunya teratur, seluruh kecepatan interval harus sama dengan $v$. Ini merupakan kasus uji yang sangat kuat karena hasil analitiknya diketahui.

Sebagai contoh, gunakan

```math
x(t)=2+3t.
```

Untuk selang waktu apa pun yang tidak nol, kecepatan rata-rata antar dua titik harus konstan. Kasus ini menjadi pengujian langsung terhadap implementasi rumus kecepatan. Nilai yang diharapkan adalah

```math
3\text{ m/s}.
```

Jika fungsi `compute_velocities` benar, seluruh nilai pada larik `velocity` harus mendekati 3 m/s. Pengujian ini memberikan acuan sederhana sebelum program digunakan pada data eksperimen nyata.

## Pemeriksaan dimensi

Persamaan kecepatan memiliki dimensi

```math
[v]
=
\frac{[x]}{[t]}.
```

Jika posisi dinyatakan dalam meter dan waktu dalam sekon, kecepatan harus memiliki satuan meter per sekon. Pemeriksaan dimensi membantu menemukan kesalahan penggunaan kolom atau satuan.

Jika berkas ternyata menggunakan milisekon tetapi program menganggap sekon, hasil kecepatan akan salah dengan faktor besar. Program dapat benar secara sintaks tetapi salah secara fisika.

## Pemeriksaan orde besaran

Hasil juga perlu dibandingkan dengan skala masalah. Jika benda eksperimen bergerak beberapa meter selama beberapa sekon, kecepatan biasanya berada pada orde meter per sekon, bukan ribuan meter per sekon.

Orde besaran bukan pengganti perhitungan. Namun, pemeriksaan ini merupakan alat cepat untuk menemukan kesalahan satuan, format, atau data yang tidak masuk akal.

## Pemeriksaan tanda

Tanda kecepatan mempunyai makna fisis. Nilai positif dan negatif dapat menunjukkan arah gerak yang berbeda.

Karena itu, jangan selalu mengambil nilai absolut pada semua tahap. Nilai absolut sesuai ketika kita ingin membandingkan besar kecepatan, tetapi tanda harus dipertahankan jika arah gerak masih penting.

## Rata-rata kecepatan dan kecepatan rata-rata global

Ada perbedaan antara rata-rata aritmetika kecepatan interval dan kecepatan rata-rata berdasarkan perpindahan total. Perbedaan ini penting terutama jika selang waktu antar sampel tidak sama.

Kecepatan rata-rata global menghubungkan perpindahan total dengan waktu total. Definisi ini memberi bobot waktu secara alami pada keseluruhan eksperimen. Besaran tersebut diberikan oleh

```math
v_{\text{global}}
=
\frac{
x_{N-1}-x_0
}{
t_{N-1}-t_0
}.
```

Sementara itu, rata-rata aritmetika interval memberi bobot yang sama pada setiap nilai kecepatan interval. Jika durasi interval berbeda, maknanya dapat berbeda dari kecepatan rata-rata global. Besaran tersebut dituliskan sebagai

```math
\frac{1}{M}
\sum_{i=0}^{M-1}v_i.
```

Keduanya hanya selalu sama pada kondisi tertentu. Hal ini menunjukkan bahwa definisi statistik harus disesuaikan dengan makna fisis yang diinginkan.

## Fungsi kecepatan rata-rata global

```c
double global_average_velocity(
    const MotionSample data[],
    int n)
{
    double dx =
        data[n - 1].position
        - data[0].position;

    double dt =
        data[n - 1].time
        - data[0].time;

    return dx / dt;
}
```

Fungsi tersebut sebaiknya hanya dipanggil setelah urutan waktu dipastikan valid. Perbandingan antara `global_average_velocity` dan `mean_velocity` dapat menjadi bagian dari pemeriksaan hasil.

## Data pengukuran dan derau

Data eksperimen nyata sering mengandung derau. Akibatnya, besaran turunan seperti kecepatan dapat berubah lebih banyak daripada data posisi aslinya.

Pada tahap ini kita belum membahas penyaringan sinyal. Namun, mahasiswa perlu menyadari bahwa perhitungan numerik terhadap data eksperimen tidak selalu menghasilkan kurva yang mulus.

Jika dua posisi berurutan mempunyai galat kecil, selisih keduanya dapat memperbesar pengaruh galat tersebut. Fenomena ini penting ketika kita mulai bekerja dengan data nyata.

## Memisahkan kesalahan data dan kesalahan program

Hasil yang tidak masuk akal dapat berasal dari program yang salah atau data yang buruk. Kedua sumber kesalahan tersebut harus dibedakan.

Program dapat diperiksa menggunakan data sintetis yang hasilnya diketahui. Jika program benar pada data sintetis tetapi gagal pada data eksperimen, masalah mungkin berada pada kualitas data, satuan, atau asumsi fisis.

## Keterlacakan data

Berkas hasil sebaiknya tidak menghilangkan informasi yang diperlukan untuk menelusuri asal perhitungan. Karena itu, `velocity.csv` menyimpan waktu awal dan akhir interval bersama nilai kecepatan.

Keterlacakan semacam ini penting dalam pekerjaan teknik. Jika satu nilai tampak aneh, kita dapat kembali ke pasangan data mentah yang menghasilkan nilai tersebut.

## Reprodusibilitas sederhana

Program yang membaca `motion.csv` dan menghasilkan `velocity.csv` serta `summary.txt` membentuk proses yang dapat diulang. Jika berkas masukan dan program tidak berubah, hasil seharusnya dapat direproduksi.

Kebiasaan ini merupakan fondasi praktik komputasi yang baik. Perhitungan tidak hanya harus menghasilkan angka, tetapi juga harus dapat ditelusuri dan diulangi.



## Pola umum pengembangan program Teknik Fisika

Walaupun studi kasus utama menggunakan data gerak, pola pengembangan yang sama dapat diterapkan pada banyak persoalan lain. Besaran fisis dan rumusnya berubah, tetapi struktur program sering tetap serupa.

Pola umum tersebut dapat ditulis sebagai

```text
1. tentukan persoalan fisika
2. tentukan besaran input dan output
3. pilih representasi data
4. rancang fungsi
5. baca data
6. validasi data
7. hitung besaran turunan
8. cari atau ringkas informasi penting
9. tulis hasil
10. periksa kewajaran fisis
```

Urutan tersebut tidak harus selalu kaku. Namun, keberadaan setiap tahap membantu mencegah kita langsung menulis kode tanpa memahami struktur masalah.

### Contoh: data rangkaian listrik

Misalkan sebuah eksperimen menghasilkan data tegangan dan arus terhadap waktu. Satu rekaman dapat direpresentasikan menggunakan `struct`.

```c
typedef struct
{
    double time;
    double voltage;
    double current;
} ElectricalSample;
```

Daya sesaat dihitung dari

```math
P_i
=
V_iI_i.
```

Program dapat membaca CSV, memeriksa rentang tegangan dan arus, menghitung daya, mencari daya maksimum, dan menulis berkas hasil. Struktur komputasinya tetap sama seperti pada studi kasus gerak.

### Contoh: pendinginan benda

Misalkan data eksperimen berisi waktu dan temperatur benda. Program dapat mencari temperatur minimum dan maksimum, menghitung laju perubahan temperatur antarinterval, serta mencari saat pertama temperatur turun di bawah ambang tertentu.

Satu rekaman dapat direpresentasikan menggunakan `struct` sederhana. Setiap anggota menyimpan satu besaran yang berkaitan dengan waktu pengukuran yang sama. Bentuknya dapat ditulis sebagai

```c
typedef struct
{
    double time;
    double temperature;
} ThermalSample;
```

Perubahan rata-rata temperatur per satuan waktu dihitung dari selisih temperatur dibagi selang waktu. Besaran ini memiliki struktur algoritmik yang sama dengan perhitungan kecepatan dari posisi. Hubungan yang digunakan adalah

```math
r_i
=
\frac{
T_{i+1}-T_i
}{
t_{i+1}-t_i
}.
```

Sekali lagi, pola program tidak berubah secara mendasar. Yang berubah adalah definisi besaran turunan dan pemeriksaan fisisnya.

### Contoh: intensitas cahaya

Data optika sederhana dapat berupa posisi sensor dan intensitas cahaya. Program dapat mencari intensitas maksimum, posisi puncak, atau lokasi pertama ketika intensitas turun di bawah fraksi tertentu dari maksimum.

Tipe datanya dapat ditulis

```c
typedef struct
{
    double position;
    double intensity;
} LightSample;
```

Pengolahan tersebut menggunakan larik, pencarian, fungsi, dan berkas dengan pola yang sama. Hal ini menunjukkan bahwa keterampilan algoritmik dapat dipindahkan dari satu konteks fisika ke konteks lain.

## Menentukan tanggung jawab setiap fungsi

Fungsi sebaiknya dirancang berdasarkan satu tugas yang cukup jelas. Fungsi yang membaca berkas sebaiknya tidak sekaligus menghitung seluruh statistik jika tidak ada alasan kuat untuk menggabungkannya.

Sebagai contoh, fungsi `load_motion_data` bertanggung jawab pada operasi I/O dan parsing data. Sementara itu, fungsi `compute_velocities` bertanggung jawab pada perhitungan kecepatan dari data yang sudah berada di memori.

Pemisahan tersebut membuat setiap fungsi mempunyai kontrak yang lebih jelas. Program juga lebih mudah diuji karena fungsi analisis dapat diberi data buatan tanpa membaca berkas.

## Prakondisi dan pascakondisi fungsi

Ketika program semakin modular, kita perlu berpikir mengenai asumsi setiap fungsi. Asumsi sebelum fungsi dipanggil disebut prakondisi, sedangkan keadaan yang dijamin setelah fungsi selesai disebut pascakondisi.

Sebagai contoh, `mean_velocity` hanya boleh dipanggil ketika jumlah data positif. Tanpa syarat ini, pembagian pada fungsi tidak mempunyai makna yang valid. Prakondisi tersebut dapat ditulis sebagai

```math
n>0.
```

Pascakondisinya adalah fungsi mengembalikan rata-rata aritmetika dari `data[0]` sampai `data[n-1]`. Kontrak sederhana semacam ini membantu mencegah penggunaan fungsi pada kondisi yang tidak sesuai.

## Aliran data antar fungsi

Program modular yang baik memiliki aliran data yang dapat ditelusuri. Data bergerak dari berkas masuk ke larik, kemudian masuk ke fungsi analisis, dan akhirnya ditulis ke berkas hasil.

Jika terlalu banyak fungsi bergantung pada variabel global, aliran tersebut menjadi sulit dilihat. Karena itu, data sebaiknya dikirim melalui parameter sejauh masih masuk akal.

## Pemilihan `const`

Fungsi yang hanya membaca data sebaiknya menerima parameter `const`. Kebiasaan ini menyatakan bahwa fungsi tidak bermaksud mengubah data sumber.

Contoh:

```c
double mean_velocity(
    const VelocitySample data[],
    int n);
```

Penggunaan `const` juga membantu *compiler* mendeteksi perubahan yang tidak disengaja. Pada program teknik, perlindungan kecil semacam ini mengurangi risiko kesalahan.

## Pemeriksaan kesalahan secara bertingkat

Program integratif memiliki beberapa lapisan yang dapat gagal. Kegagalan tersebut sebaiknya diperiksa sedekat mungkin dengan sumbernya.

Contohnya adalah

```text
fopen gagal
    ↓
parsing gagal
    ↓
jumlah data tidak cukup
    ↓
urutan waktu tidak valid
    ↓
perhitungan tidak dapat dilakukan
    ↓
penulisan hasil gagal
```

Setiap lapisan memerlukan respons yang sesuai. Tidak semua kesalahan harus diperlakukan sama.

## Kapan program harus berhenti?

Jika berkas masukan tidak dapat dibuka, program biasanya tidak mempunyai data untuk dianalisis. Dalam kondisi tersebut, penghentian program merupakan tindakan yang masuk akal.

Sebaliknya, satu baris CSV yang rusak mungkin cukup dilewati jika baris lain masih dapat digunakan. Keputusan berhenti atau melanjutkan harus disesuaikan dengan tingkat kesalahan.

## Pesan kesalahan yang informatif

Pesan kesalahan sebaiknya menjelaskan apa yang gagal. Pesan `"error"` saja biasanya tidak cukup membantu.

Bandingkan

```text
Error.
```

dengan

```text
Cannot open motion.csv.
```

atau

```text
Invalid time order at samples 12 and 13.
```

Pesan kedua dan ketiga memberi petunjuk yang lebih berguna untuk proses *debugging*. Informasi yang baik mengurangi waktu yang diperlukan untuk menemukan sumber masalah.

## Menambahkan informasi lokasi kesalahan

Fungsi validasi dapat dikembangkan agar mengembalikan indeks pelanggaran. Dengan demikian, program dapat melaporkan lokasi masalah secara lebih spesifik.

Contoh:

```c
int first_invalid_time_index(
    const MotionSample data[],
    int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        if (data[i + 1].time
            <= data[i].time)
        {
            return i;
        }
    }

    return -1;
}
```

Jika fungsi mengembalikan `7`, maka masalah terjadi antara elemen 7 dan 8. Pendekatan ini lebih berguna daripada hanya mengembalikan benar atau salah.

## Pemeriksaan terhadap data ekstrem

Data yang sangat besar atau sangat kecil dapat menunjukkan galat satuan atau sensor. Program dapat menggunakan batas kewajaran jika batas tersebut memang diketahui dari konteks eksperimen.

Sebagai contoh, jika posisi eksperimen seharusnya berada antara -10 m dan 10 m, nilai 5000 m patut dicurigai. Namun, batas tidak boleh dibuat sembarangan tanpa dasar fisis.

## Jangan mencampur validasi dan manipulasi tanpa alasan

Validasi sebaiknya tidak diam-diam mengubah data. Jika nilai tidak valid, program harus secara jelas memutuskan apakah nilai ditolak, diperbaiki, atau diberi penanda khusus.

Mengubah nilai 5000 menjadi 10 secara otomatis tanpa dokumentasi dapat menghasilkan analisis yang menyesatkan. Dalam konteks teknik, keputusan terhadap data harus dapat dijelaskan.

## Pemrosesan sekali lewat dan penyimpanan penuh

Sebagian statistik dapat dihitung saat data dibaca tanpa menyimpan seluruh rekaman. Contohnya adalah jumlah, minimum, maksimum, dan counter sederhana.

Namun, studi kasus kita membutuhkan data berurutan untuk menghasilkan interval dan menulis hasil lengkap. Karena itu, penyimpanan seluruh sampel dalam larik masih sesuai.

Pemilihan antara pemrosesan *streaming* dan penyimpanan penuh bergantung pada kebutuhan analisis. Tidak ada satu strategi yang selalu paling baik.

## Kompleksitas program studi kasus

Pembacaan $N$ sampel membutuhkan waktu yang sebanding dengan jumlah baris. Validasi, perhitungan kecepatan, pencarian maksimum, dan pencarian ambang juga masing-masing membutuhkan penelusuran linear.

Secara orde, bagian analisis utama bertumbuh sebanding dengan jumlah data. Penambahan beberapa loop linear hanya mengubah faktor konstanta, bukan orde pertumbuhannya. Kompleksitas waktunya adalah

```math
O(N).
```

Larik `MotionSample` dan `VelocitySample` menyimpan data yang jumlahnya sebanding dengan $N$. Karena itu, kebutuhan memorinya juga bertumbuh secara linear terhadap $N$. Orde kebutuhan memorinya adalah

```math
O(N).
```

Analisis ini menunjukkan bahwa integrasi banyak fungsi tidak selalu berarti kompleksitas algoritmik menjadi tinggi. Beberapa penelusuran linear tetap menghasilkan kompleksitas total $O(N)$.

## Dapatkah beberapa loop digabung?

Secara teori, rata-rata, maksimum, dan pencarian ambang dapat dihitung dalam satu loop. Penggabungan dapat mengurangi jumlah penelusuran atas data.

Namun, pemisahan fungsi sering meningkatkan keterbacaan dan kemudahan pengujian. Untuk ukuran data yang tidak terlalu besar, perbedaan biaya beberapa loop $O(N)$ biasanya tidak menjadi persoalan utama.

Pada tahap awal pemrograman teknik, utamakan kebenaran dan struktur yang jelas. Optimasi sebaiknya dilakukan setelah ada alasan yang terukur.

## Pengujian dengan data sintetis

Data sintetis adalah data yang kita buat sendiri berdasarkan model yang hasilnya diketahui. Data tersebut sangat berguna untuk memisahkan kesalahan program dari ketidakpastian eksperimen.

Misalnya, kita dapat menghasilkan

```math
x(t)
=
2+3t.
```

Kemudian seluruh kecepatan interval seharusnya memiliki nilai yang sama. Keseragaman hasil tersebut dapat diperiksa tanpa analisis numerik yang rumit. Nilai teoritisnya adalah

```math
3\text{ m/s}.
```

Jika program gagal pada kasus tersebut, masalah hampir pasti berada pada implementasi. Jika program berhasil, kita mempunyai bukti tambahan bahwa algoritma bekerja untuk kasus yang diketahui.

## Pengujian dengan nilai batas

Kondisi ambang juga perlu diuji tepat pada batas. Pengujian ini menentukan apakah operator relasional telah sesuai dengan definisi masalah. Jika spesifikasi program menggunakan syarat ketat, misalnya

```math
|v|>1.8,
```

maka nilai tepat

```math
|v|=1.8
```

tidak boleh dianggap melampaui ambang. Perbedaan antara `>` dan `>=` harus sesuai spesifikasi.

Uji juga nilai sedikit di bawah dan sedikit di atas ambang. Tiga kasus tersebut sering cukup untuk menemukan kesalahan operator relasional.

## Pengujian berkas

Operasi berkas perlu diuji menggunakan beberapa kondisi. Jangan hanya menguji berkas yang sempurna.

Gunakan antara lain

```text
berkas valid
berkas kosong
nama berkas salah
baris rusak
header tanpa data
data melebihi kapasitas
```

Tujuannya bukan membuat program tahan terhadap semua kemungkinan sejak awal. Tujuannya adalah membiasakan bahwa I/O merupakan bagian program yang dapat gagal.

## Pengujian keluaran

Berkas `velocity.csv` sebaiknya dibuka dan diperiksa. Jumlah baris data harus sama dengan $N-1$ jika seluruh interval valid.

Nilai pertama dapat dihitung manual dan dibandingkan dengan keluaran. Pemeriksaan satu atau dua baris secara manual sering cukup untuk menemukan kesalahan format atau indeks.

## Pemeriksaan konsistensi internal

Program dapat melakukan pemeriksaan sederhana terhadap hubungan antarjumlah. Misalnya, jika terdapat $N$ sampel valid dan semua waktu terurut, jumlah kecepatan yang dihasilkan harus memenuhi hubungan berikut.

```math
N-1.
```

Jika hubungan tersebut tidak terpenuhi, ada kemungkinan kesalahan pada logika program. Pemeriksaan konsistensi semacam ini murah tetapi berguna.

## Kesalahan umum pada program terintegrasi

### Langsung menulis seluruh program

Menulis ratusan baris sekaligus membuat sumber kesalahan sulit dilacak. Program lebih aman dikembangkan fungsi demi fungsi dengan data uji sederhana.

### Mencampur I/O dan perhitungan di semua tempat

Jika setiap fungsi membuka berkas sendiri tanpa desain yang jelas, aliran data menjadi sulit dipahami. Pisahkan pembacaan, analisis, dan penulisan sejauh masih praktis.

### Mengabaikan prakondisi

Fungsi rata-rata membutuhkan jumlah data positif. Fungsi kecepatan membutuhkan dua sampel dengan selang waktu tidak nol.

### Menganggap data valid karena berhasil dibaca

`sscanf` hanya memastikan teks cocok dengan format numerik. Nilai hasil parsing tetap harus diperiksa berdasarkan konteks fisis.

### Menggunakan indeks tanpa memeriksa batas

Integrasi beberapa larik meningkatkan risiko *off-by-one error*. Hubungan antara $N$ titik dan $N-1$ interval harus diperhatikan secara eksplisit.

### Menimpa data mentah

Berkas masukan sebaiknya tidak langsung ditimpa oleh hasil pengolahan. Menyimpan hasil pada berkas baru menjaga data asli untuk pemeriksaan ulang.

### Tidak memeriksa hasil secara fisis

Program dapat menghasilkan angka dengan format sempurna tetapi tetap salah. Satuan, tanda, rentang, dan orde besaran tetap harus diperiksa.

## Praktik terbaik yang dianjurkan

Mulailah dari persoalan dan model, bukan dari sintaks C. Tuliskan hubungan matematis dan spesifikasi data sebelum membuat fungsi.

Bangun program sedikit demi sedikit. Kompilasi dengan peringatan aktif setelah perubahan penting agar kesalahan segera ditemukan.

Gunakan perintah seperti

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 program.c -o program
```

untuk program yang tidak memerlukan pustaka matematika tambahan. Jika lingkungan Anda memerlukan *linking* eksplisit terhadap pustaka matematika, tambahkan `-lm` ketika menggunakan fungsi seperti `fabs`.

Gunakan data sintetis sebelum data eksperimen nyata. Hasil analitik yang diketahui menjadi acuan yang sangat berguna.

Simpan data mentah, data hasil, dan ringkasan secara terpisah jika memungkinkan. Struktur tersebut meningkatkan keterlacakan dan reprodusibilitas.

## Cek pemahaman

Cobalah menjawab pertanyaan berikut tanpa melihat kembali catatan. Pertanyaan-pertanyaan ini berfokus pada integrasi konsep, bukan hafalan sintaks.

- Mengapa perumusan persoalan fisika sebaiknya dilakukan sebelum menulis kode?
- Apa hubungan antara jumlah sampel posisi dan jumlah interval kecepatan?
- Mengapa `struct` sesuai untuk merepresentasikan satu rekaman pengukuran?
- Mengapa data mentah dan data turunan sebaiknya menggunakan representasi yang jelas?
- Apa manfaat memisahkan fungsi pembacaan, validasi, analisis, pencarian, dan penulisan?
- Mengapa urutan waktu harus diperiksa sebelum menghitung kecepatan?
- Apa perbedaan antara rata-rata aritmetika kecepatan interval dan kecepatan rata-rata global?
- Mengapa fungsi pencarian sering lebih berguna jika mengembalikan indeks?
- Apa arti nilai `-1` sebagai hasil pencarian yang tidak menemukan kondisi?
- Mengapa `NULL` dapat digunakan untuk menyatakan tidak ada rekaman yang relevan?
- Mengapa data yang berhasil diparsing belum tentu valid secara fisis?
- Apa manfaat data sintetis dalam pengujian?
- Mengapa nilai tepat pada ambang perlu diuji?
- Apa manfaat mempertahankan data mentah setelah pengolahan selesai?
- Mengapa program dengan beberapa loop linear tetap dapat memiliki kompleksitas $O(N)$?
- Apa perbedaan antara kesalahan program dan kualitas data yang buruk?
- Mengapa satuan perlu dituliskan pada skema berkas?
- Apa yang dimaksud dengan keterlacakan hasil komputasi?
- Bagaimana program dapat membantu reprodusibilitas analisis teknik?
- Mengapa program yang berhasil dikompilasi belum tentu benar secara fisis?

## Latihan

### 1. Gerak lurus dari data eksperimen

Buat program lengkap yang membaca `motion.csv` dengan kolom `time_s,position_m`. Program harus menghitung kecepatan setiap interval, kecepatan rata-rata global, kecepatan maksimum absolut, dan interval tempat nilai maksimum tersebut terjadi.

Gunakan `struct`, larik `struct`, dan fungsi modular. Program harus menolak data jika waktu tidak bertambah secara ketat dan menulis hasil ke `velocity.csv`.

### 2. Energi pada rangkaian listrik

Buat program yang membaca `electrical.csv` dengan kolom `time_s,voltage_V,current_A`. Hitung daya pada setiap sampel dari tegangan dan arus. Gunakan hubungan

```math
P_i=V_iI_i.
```

Setelah daya dihitung, perkirakan energi menggunakan aturan trapesium sederhana. Pendekatan ini menggabungkan daya pada dua sampel berurutan dan selang waktunya. Gunakan pendekatan

```math
E
\approx
\sum_{i=0}^{N-2}
\frac{
P_i+P_{i+1}
}{2}
\Delta t_i.
```

Program harus memeriksa urutan waktu, mencari daya maksimum, dan menulis `processed_electrical.csv` yang memuat waktu, tegangan, arus, dan daya. Bandingkan orde hasil energi dengan skala daya dan lama eksperimen agar kewajaran hasil dapat diperiksa.

### 3. Pendinginan benda

Buat program untuk membaca `cooling.csv` dengan kolom `time_s,temperature_C`. Hitung laju perubahan temperatur setiap interval dan cari saat pertama temperatur turun di bawah ambang yang diberikan pengguna.

Program harus menghasilkan ringkasan berisi temperatur awal, temperatur akhir, temperatur minimum, laju pendinginan maksimum absolut, dan waktu ketika ambang pertama kali terlewati. Periksa kewajaran tanda laju perubahan terhadap proses pendinginan.

### 4. Data intensitas cahaya

Buat program yang membaca posisi dan intensitas cahaya dari CSV. Cari intensitas maksimum, posisi puncak, dan titik pertama di sebelah kanan puncak ketika intensitas turun di bawah 50% maksimum.

Gunakan fungsi pencarian yang mengembalikan indeks. Tulis berkas hasil dengan kolom tambahan `relative_intensity` yang bernilai $I_i/I_{\max}$.

### 5. Osilasi pegas sederhana

Buat program yang membaca `time_s,displacement_m` dari eksperimen osilasi. Hitung simpangan maksimum absolut, RMS simpangan, dan banyak sampel yang berada dekat amplitudo maksimum. Gunakan kondisi

```math
|x|>0.8A,
```

Di sini $A$ adalah simpangan maksimum absolut. Program juga harus mencari perubahan tanda berturut-turut sebagai indikasi sederhana penyeberangan titik setimbang.

### 6. Pemeriksaan kualitas data sensor

Rancang program yang membaca satu berkas CSV berisi `time_s,value`. Program harus menandai baris yang memiliki waktu tidak meningkat, nilai di luar rentang yang ditentukan pengguna, atau perubahan antarsampel yang melebihi ambang tertentu.

Simpan data valid ke `clean.csv` dan catatan data bermasalah ke `rejected.txt`. Jelaskan bagaimana Anda memisahkan validasi format, validasi urutan waktu, dan validasi fisis.

### 7. Eksperimen jatuh bebas sederhana

Gunakan data waktu dan posisi vertikal yang diberikan dalam CSV. Hitung kecepatan interval dan perubahan kecepatan antarinterval sebagai pendekatan sederhana terhadap percepatan.

Bandingkan orde percepatan hasil perhitungan dengan percepatan gravitasi dekat permukaan Bumi. Perbandingan ini digunakan sebagai pemeriksaan kewajaran, bukan sebagai tuntutan bahwa setiap sampel harus sama persis. Gunakan nilai acuan

```math
g
\approx
9.8\text{ m/s}^2.
```

Program tidak perlu melakukan *fitting* kurva. Fokuskan analisis pada struktur data, perhitungan diskrit, dan pemeriksaan kewajaran hasil.

### 8. Gelombang sinus sintetis

Buat program C yang terlebih dahulu menghasilkan data gelombang sintetis pada beberapa titik waktu. Data sintetis tersebut memungkinkan hasil numerik dibandingkan dengan sifat teoritis yang sudah diketahui. Gunakan model

```math
y(t)
=
A\sin(2\pi ft)
```

Gunakan model tersebut untuk sejumlah titik waktu lalu tuliskan hasilnya ke `wave.csv`. Setelah itu, baca kembali berkas tersebut dan hitung nilai minimum, maksimum, rata-rata, serta RMS.

Gunakan fungsi terpisah untuk pembuatan data, pembacaan, dan analisis. Bandingkan RMS numerik dengan nilai teoritis $A/\sqrt{2}$ untuk jumlah sampel yang cukup banyak.

### 9. Perbandingan dua metode rata-rata kecepatan

Gunakan data waktu dan posisi dengan selang waktu yang tidak seragam. Hitung rata-rata aritmetika dari seluruh kecepatan interval dan kecepatan rata-rata global dari perpindahan total dibagi waktu total.

Tunjukkan melalui satu data uji bahwa kedua nilai tersebut dapat berbeda. Jelaskan secara fisis mengapa kecepatan rata-rata global lebih tepat jika tujuan kita adalah menghubungkan perpindahan total dengan waktu total.

### 10. Proyek mini integrasi C

Pilih satu kasus Teknik Fisika sederhana dari mekanika, listrik, termal, optika, atau gelombang. Rancang program dengan alur lengkap `masalah -> model -> struktur data -> pembacaan CSV -> validasi -> analisis -> pencarian kondisi -> penulisan hasil -> pemeriksaan fisis`.

Program harus menggunakan sekurang-kurangnya satu `struct`, satu larik dari `struct`, sedikitnya lima fungsi selain `main`, dan sekurang-kurangnya satu pencarian kondisi. Sertakan data uji sintetis dengan hasil yang dapat diprediksi dan jelaskan bagaimana Anda memeriksa satuan serta orde besaran.

## Rangkuman

- Pemrograman teknik dimulai dari perumusan persoalan, bukan dari sintaks. Model fisika, masukan, keluaran, asumsi, dan batas validitas harus ditentukan sebelum implementasi.

- Program integratif dapat menggabungkan percabangan, pengulangan, larik, fungsi, `struct`, *pointer* dasar, *string*, dan berkas dalam satu alur kerja. Setiap konsep mempunyai peran yang berbeda dalam struktur program.

- `struct` sesuai untuk merepresentasikan satu rekaman pengukuran yang memiliki beberapa besaran terkait. Larik dari `struct` sesuai untuk menyimpan banyak rekaman.

- Modularisasi memisahkan tanggung jawab seperti pembacaan, validasi, perhitungan, pencarian, dan penulisan hasil. Pemisahan ini meningkatkan keterbacaan dan kemudahan pengujian.

- Data yang berhasil dibaca belum tentu valid secara fisis. Validasi format, validasi struktur data, dan validasi fisis merupakan lapisan pemeriksaan yang berbeda.

- Besaran turunan harus dihitung hanya setelah prakondisinya terpenuhi. Untuk kecepatan dari data posisi, waktu harus bertambah sehingga $\Delta t>0$.

- Statistik sederhana seperti rata-rata, minimum, maksimum, dan RMS dapat digabungkan dengan pencarian kondisi tertentu. Fungsi pencarian sering mengembalikan indeks agar konteks rekaman tetap tersedia.

- Hasil pengolahan sebaiknya ditulis ke berkas baru jika data mentah masih perlu dipertahankan. Kebiasaan ini meningkatkan keterlacakan dan reprodusibilitas.

- Pengujian perlu mencakup data sintetis, kasus biasa, kasus batas, dan data salah. Program yang hanya diuji pada satu berkas ideal belum cukup meyakinkan.

- Pemeriksaan fisis meliputi satuan, dimensi, tanda, rentang, dan orde besaran. Pemeriksaan tersebut sama pentingnya dengan pemeriksaan sintaks dan algoritma.

- Beberapa penelusuran linear atas data tetap menghasilkan kompleksitas total $O(N)$. Keterbacaan dan kebenaran biasanya lebih penting daripada menggabungkan semua loop secara prematur.

- Program yang baik tidak hanya menghasilkan angka. Program harus menghasilkan informasi yang dapat dijelaskan, ditelusuri kembali ke data, dan diuji terhadap model fisis.
