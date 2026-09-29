# Kuliah 6: Larik, Fungsi, dan Modularisasi Program

## Mengapa kita memerlukan larik dan fungsi?

Pada kuliah-kuliah sebelumnya kita telah mempelajari variabel, percabangan, pengulangan, dan berbagai pola algoritma iteratif. Konsep-konsep tersebut sudah cukup untuk memproses data satu per satu, tetapi pendekatan itu mulai tidak praktis ketika kita perlu menyimpan banyak data atau menggunakan proses yang sama berkali-kali.

Misalkan sebuah eksperimen menghasilkan sepuluh nilai tegangan. Kita dapat membuat variabel `v1`, `v2`, sampai `v10`, tetapi pendekatan tersebut sulit diperluas dan tidak cocok dengan pola pengulangan yang telah kita pelajari.

Masalah serupa muncul pada struktur program. Jika perhitungan rata-rata, konversi satuan, atau energi kinetik ditulis berulang kali di banyak tempat, program menjadi panjang dan lebih sulit diperiksa.

Pada kuliah ini kita akan mempelajari dua alat utama untuk mengatasi persoalan tersebut. **Larik** (*array*) digunakan untuk menyimpan sekumpulan data bertipe sama, sedangkan **fungsi** digunakan untuk membagi program menjadi bagian-bagian yang memiliki tanggung jawab tertentu.

Kedua konsep tersebut juga membawa kita pada hubungan antara data dan memori. Oleh karena itu, kita akan memperkenalkan *pointer* secara terbatas untuk memahami alamat memori, pengiriman larik ke fungsi, dan perubahan data melalui fungsi.

## Larik satu dimensi

Larik satu dimensi adalah sekumpulan elemen bertipe sama yang disimpan secara berurutan di memori. Setiap elemen diakses menggunakan indeks.

Sebagai contoh, kita ingin menyimpan lima data temperatur. Kelima nilai tersebut dapat dipandang sebagai satu kelompok data yang memiliki tipe dan makna fisik yang sama.

```math
T_0,\quad T_1,\quad T_2,\quad T_3,\quad T_4.
```

Dalam C, kita dapat merepresentasikan susunan tersebut secara langsung. Bentuk deklarasinya dapat ditulis sebagai berikut.

```c
double temperature[5];
```

Deklarasi tersebut membuat lima elemen bertipe `double`. Indeks yang valid adalah `0`, `1`, `2`, `3`, dan `4`.

Secara umum, untuk larik berukuran $N$, indeks valid selalu mempunyai batas yang jelas. Rentang indeks tersebut memenuhi hubungan berikut.

```math
0
\leq i
\leq
N-1.
```

C menggunakan indeks mulai dari nol. Karena itu, indeks `N` berada di luar batas larik berukuran $N$.

### Menyimpan dan membaca elemen

Setiap elemen larik dapat diperlakukan seperti variabel biasa. Kita menggunakan nama larik diikuti indeks dalam tanda kurung siku.

```c
temperature[0] = 28.5;
temperature[1] = 29.1;
temperature[2] = 30.0;
temperature[3] = 29.7;
temperature[4] = 28.9;
```

Untuk membaca elemen pertama, kita dapat menggunakan indeks nol. Bentuk kodenya dapat ditulis sebagai berikut.

```c
double first =
    temperature[0];
```

Elemen kelima diakses menggunakan `temperature[4]`. Perbedaan antara nomor urut manusia dan indeks program harus selalu diperhatikan.

### Inisialisasi larik

Larik dapat langsung diberi nilai ketika dideklarasikan. Bentuk ini sesuai untuk data contoh atau data uji yang jumlahnya kecil.

```c
double temperature[5] =
{
    28.5,
    29.1,
    30.0,
    29.7,
    28.9
};
```

Jika seluruh elemen awal sudah dituliskan, ukuran dapat dibiarkan ditentukan oleh *compiler*. Cara tersebut mengurangi kemungkinan ketidaksesuaian antara ukuran dan jumlah nilai awal.

```c
double temperature[] =
{
    28.5,
    29.1,
    30.0,
    29.7,
    28.9
};
```

Dalam contoh tersebut, ukuran larik adalah lima. Informasi ukuran tetap perlu kita kelola ketika larik diproses oleh fungsi.

## Penelusuran elemen larik

Larik sangat cocok digunakan bersama pengulangan. Pola penelusuran seluruh elemen dapat ditulis secara abstrak sebagai berikut.

```text
FOR i ← 0 TO N-1
    proses x[i]
END FOR
```

Dalam C, pola tersebut diterjemahkan langsung menggunakan `for`. Bentuk yang umum adalah sebagai berikut.

```c
for (int i = 0; i < n; i++)
{
    /* proses data[i] */
}
```

Batas `i < n` menunjukkan bahwa indeks `n` sendiri tidak boleh diakses. Pola ini akan muncul berulang kali pada hampir semua algoritma berbasis larik.

### Membaca data ke larik

Misalkan kita menyediakan kapasitas maksimum 100 data. Jumlah data yang benar-benar digunakan disimpan pada variabel terpisah.

```c
#include <stdio.h>

int main(void)
{
    const int max_data = 100;
    double data[100];
    int n;

    printf("Number of data: ");
    scanf("%d", &n);

    if (n <= 0 || n > max_data)
    {
        printf("Invalid number of data.\n");
        return 1;
    }

    for (int i = 0; i < n; i++)
    {
        printf("data[%d]: ", i);
        scanf("%lf", &data[i]);
    }

    return 0;
}
```

Program tersebut membedakan **kapasitas** larik dari **jumlah data aktual**. Pemisahan ini penting ketika larik berukuran tetap digunakan sebagai tempat penyimpanan.

## Batas larik dan keamanan program

C tidak melakukan pemeriksaan batas larik secara otomatis. Akses ke indeks yang tidak valid menghasilkan perilaku yang tidak dapat diandalkan dan dapat merusak data lain di memori.

Jika kita memiliki

```c
double x[5];
```

maka `x[5]` bukan elemen valid. Indeks terakhir yang sah adalah `x[4]`.

Kesalahan tersebut disebut **out-of-bounds access**. Program dapat menghasilkan nilai aneh, berhenti, atau tampak berjalan normal tetapi sebenarnya telah melakukan akses memori yang salah.

Karena itu, batas pengulangan harus diperiksa dengan teliti. Salah satu bentuk yang paling umum adalah sebagai berikut.

```c
for (int i = 0; i < n; i++)
```

Bentuk tersebut biasanya lebih aman dan jelas dibandingkan menulis batas secara tidak langsung. Batas `i < n` juga langsung menunjukkan bahwa indeks `n` tidak termasuk.

## Menghitung jumlah elemen larik lokal

Untuk larik yang masih dikenal sebagai larik pada ruang lingkup yang sama, `sizeof` dapat digunakan untuk menghitung jumlah elemen. Ukuran total larik dibagi ukuran satu elemen memberikan banyak elemen.

```c
double data[] =
{
    1.0,
    2.0,
    3.0,
    4.0,
    5.0
};

int n =
    sizeof(data) / sizeof(data[0]);
```

Jika satu `double` menggunakan delapan byte, `sizeof(data)` bernilai 40 byte. Pembagian dengan `sizeof(data[0])` menghasilkan lima.

Teknik ini tidak dapat dipakai dengan cara yang sama setelah larik menjadi parameter fungsi. Di dalam parameter fungsi, informasi ukuran total larik tidak tersedia otomatis.

## Pola algoritma pada larik

Pola *accumulator*, minimum, maksimum, dan counter dari kuliah sebelumnya dapat langsung diterapkan pada larik. Perbedaannya adalah nilai diambil dari `data[i]`, bukan selalu dibaca dari input.

Penjumlahan seluruh elemen menggunakan pola accumulator. Dalam C, pola tersebut dapat ditulis sebagai berikut.

```c
double sum = 0.0;

for (int i = 0; i < n; i++)
{
    sum += data[i];
}
```

Setelah jumlah seluruh data diperoleh, rata-rata dapat dihitung dari jumlah dan banyak elemen. Bentuk perhitungannya diberikan oleh persamaan berikut.

```c
double mean =
    sum / n;
```

Minimum dan maksimum dapat dihitung menggunakan data pertama sebagai nilai awal. Cara ini tetap benar untuk data yang seluruhnya positif, seluruhnya negatif, atau campuran.

```c
double minimum = data[0];
double maximum = data[0];

for (int i = 1; i < n; i++)
{
    if (data[i] < minimum)
    {
        minimum = data[i];
    }

    if (data[i] > maximum)
    {
        maximum = data[i];
    }
}
```

## Contoh: posisi dan kecepatan rata-rata

Misalkan sebuah eksperimen gerak satu dimensi menghasilkan data posisi pada interval waktu tetap. Kita menyimpan posisi pada larik karena seluruh nilai akan digunakan kembali untuk menghitung perubahan antarsampel.

```c
double position[] =
{
    0.0,
    1.2,
    2.5,
    3.9,
    5.4,
    7.0
};
```

Jika interval waktunya

```math
\Delta t
=
0.5\text{ s},
```

Kecepatan rata-rata pada interval ke-$i$ dapat diperkirakan dari perubahan posisi terhadap waktu. Bentuk pendekatannya adalah sebagai berikut.

```math
v_i
=
\frac{x_{i+1}-x_i}{\Delta t}.
```

Program sederhana:

```c
#include <stdio.h>

int main(void)
{
    double position[] =
    {
        0.0,
        1.2,
        2.5,
        3.9,
        5.4,
        7.0
    };

    int n =
        sizeof(position) /
        sizeof(position[0]);

    const double dt = 0.5;

    for (int i = 0; i < n - 1; i++)
    {
        double velocity =
            (position[i + 1] - position[i])
            / dt;

        printf("v[%d] = %.3f m/s\n",
               i, velocity);
    }

    return 0;
}
```

Jika terdapat $N$ titik posisi, hanya terdapat $N-1$ interval antar titik. Karena itu, batas `i < n - 1` memiliki makna fisis sekaligus makna komputasional.

## Mengapa menyimpan data dalam larik?

Pemrosesan *streaming* hanya mempertahankan informasi yang diperlukan selama data dibaca. Larik berbeda karena seluruh data tetap tersedia setelah proses pembacaan selesai.

Keuntungan larik adalah data yang sama dapat dianalisis berkali-kali. Kita dapat menghitung rata-rata, RMS, perubahan antarsampel, melakukan pencarian, atau mengurutkan data tanpa meminta pengguna memasukkannya kembali.

Kelemahannya adalah kebutuhan memori bertambah dengan jumlah data. Jika $N$ nilai disimpan, kebutuhan memorinya secara intuitif bertumbuh sebanding dengan $N$. Secara orde, kebutuhan memorinya adalah

```math
O(N).
```

## Pengantar larik dua dimensi

Larik dua dimensi dapat digunakan untuk merepresentasikan data berbentuk tabel. Contohnya adalah beberapa sensor yang masing-masing menghasilkan sejumlah sampel.

Misalkan tiga sensor menghasilkan empat pengukuran. Secara matematis, data tersebut dapat dibayangkan sebagai matriks berikut.

```math
\begin{bmatrix}
x_{00} & x_{01} & x_{02} & x_{03}\\
x_{10} & x_{11} & x_{12} & x_{13}\\
x_{20} & x_{21} & x_{22} & x_{23}
\end{bmatrix}.
```

Dalam C, kita dapat merepresentasikan susunan tersebut secara langsung. Bentuk deklarasinya dapat ditulis sebagai berikut.

```c
double data[3][4];
```

Elemen pada baris kedua dan kolom ketiga diakses sebagai `data[1][2]`. Sekali lagi, kedua indeks dimulai dari nol.

### Inisialisasi larik dua dimensi

```c
double voltage[3][4] =
{
    {1.0, 1.1, 1.2, 1.3},
    {2.0, 2.1, 2.2, 2.3},
    {3.0, 3.1, 3.2, 3.3}
};
```

Setiap baris dapat dipandang sebagai kumpulan data dari satu sensor. Susunan semacam ini cocok untuk data yang secara alami memiliki dua indeks.

### Penelusuran larik dua dimensi

Larik dua dimensi biasanya ditelusuri dengan dua pengulangan bersarang. Pengulangan luar memilih baris, sedangkan pengulangan dalam memilih kolom.

```c
for (int i = 0; i < 3; i++)
{
    for (int j = 0; j < 4; j++)
    {
        printf("%.2f ",
               voltage[i][j]);
    }

    printf("\n");
}
```

Jika jumlah baris dan kolom sama-sama bertumbuh sebagai $N$, penelusuran seluruh elemen memerlukan sekitar $N^2$ operasi. Kompleksitasnya kemudian dapat dipandang sebagai $O(N^2)$.

## Contoh: rata-rata beberapa sensor

Misalkan setiap baris menyimpan empat pengukuran milik satu sensor. Kita dapat menghitung rata-rata setiap sensor dengan satu nested loop.

```c
#include <stdio.h>

int main(void)
{
    double voltage[3][4] =
    {
        {1.0, 1.1, 1.2, 1.3},
        {2.0, 2.1, 2.2, 2.3},
        {3.0, 3.1, 3.2, 3.3}
    };

    for (int sensor = 0;
         sensor < 3;
         sensor++)
    {
        double sum = 0.0;

        for (int sample = 0;
             sample < 4;
             sample++)
        {
            sum += voltage[sensor][sample];
        }

        double mean =
            sum / 4.0;

        printf("Sensor %d mean = %.3f V\n",
               sensor, mean);
    }

    return 0;
}
```

Contoh tersebut memperlihatkan makna fisik dari kedua indeks. Indeks pertama memilih sensor, sedangkan indeks kedua memilih pengukuran dari sensor tersebut.

## Fungsi

Fungsi adalah bagian program yang memiliki nama dan tugas tertentu. Fungsi membantu memecah program menjadi unit yang lebih kecil sehingga struktur program menjadi lebih jelas.

Misalkan perhitungan energi kinetik digunakan beberapa kali. Kita dapat menempatkan rumusnya dalam fungsi agar tidak ditulis berulang-ulang.

```c
double kinetic_energy(double mass,
                      double velocity)
{
    return
        0.5 * mass * velocity * velocity;
}
```

Fungsi menerima massa dan kecepatan lalu mengembalikan energi kinetik. Program utama tidak perlu menuliskan ulang rumus setiap kali perhitungan diperlukan.

## Struktur dasar fungsi

Bentuk umum fungsi memiliki tipe nilai kembalian, nama, parameter, dan tubuh fungsi. Secara abstrak, strukturnya dapat dipahami sebagai berikut.

```text
return_type function_name(parameters)
{
    statements

    return value;
}
```

Contoh:

```c
double square(double x)
{
    return x * x;
}
```

Tipe `double` sebelum nama fungsi menunjukkan tipe nilai yang dikembalikan. Parameter `double x` adalah data yang diterima ketika fungsi dipanggil.

### Memanggil fungsi

```c
#include <stdio.h>

double square(double x)
{
    return x * x;
}

int main(void)
{
    double value = 3.0;

    double result =
        square(value);

    printf("%.3f\n", result);

    return 0;
}
```

Ketika `square(value)` dipanggil, nilai `value` dikirim ke parameter `x`. Fungsi menghitung kuadrat dan mengembalikan hasilnya.

## Prototipe fungsi

Jika implementasi fungsi diletakkan setelah `main`, kita dapat menuliskan prototipe sebelum `main`. Prototipe memberi tahu *compiler* mengenai nama fungsi, tipe nilai kembalian, serta tipe parameternya.

```c
#include <stdio.h>

double square(double x);

int main(void)
{
    double result =
        square(4.0);

    printf("%.3f\n", result);

    return 0;
}

double square(double x)
{
    return x * x;
}
```

Baris

```c
double square(double x);
```

adalah prototipe fungsi. Struktur ini akan sering digunakan pada catatan berikutnya karena membuat `main` dapat ditempatkan dekat bagian awal program.

## Parameter dan argumen

**Parameter** adalah variabel yang didefinisikan pada deklarasi fungsi. **Argumen** adalah nilai yang diberikan ketika fungsi dipanggil.

Pada

```c
double kinetic_energy(double mass,
                      double velocity)
```

`mass` dan `velocity` adalah parameter yang didefinisikan pada fungsi. Contoh pemanggilannya ditunjukkan berikut ini.

```c
kinetic_energy(2.0, 3.0)
```

`2.0` dan `3.0` adalah argumen yang benar-benar dikirim saat fungsi dipanggil. Keduanya kemudian diterima melalui parameter `mass` dan `velocity`.

Pembedaan ini berguna ketika kita membahas perpindahan data antara fungsi. Secara konsep, parameter adalah tempat penerimaan data, sedangkan argumen adalah data yang benar-benar dikirim.

## Nilai kembalian

Fungsi dapat mengembalikan satu nilai menggunakan `return`. Tipe nilai tersebut harus konsisten dengan tipe fungsi.

```c
double celsius_to_kelvin(double celsius)
{
    return celsius + 273.15;
}
```

Pemanggilan

```c
double temperature_k =
    celsius_to_kelvin(25.0);
```

menghasilkan

```math
298.15\text{ K}.
```

Fungsi dapat langsung digunakan sebagai bagian dari ekspresi lain. Hal ini membuat perhitungan kompleks dapat disusun dari fungsi-fungsi sederhana.

## Fungsi `void`

Tidak semua fungsi perlu menghasilkan nilai kembalian. Fungsi yang hanya melakukan suatu tindakan dapat menggunakan tipe `void`.

```c
void print_separator(void)
{
    printf("--------------------\n");
}
```

Dalam konteks bahasa C, gagasan prosedur dapat direpresentasikan dengan fungsi `void`. Karena itu, kita tidak memerlukan konstruksi khusus bernama `procedure`.

## Parameter skalar dikirim berdasarkan nilai

Untuk tipe skalar biasa seperti `int` dan `double`, C menggunakan **pass by value**. Fungsi menerima salinan nilai argumen, bukan variabel asli milik pemanggil.

```c
#include <stdio.h>

void add_one(int x)
{
    x = x + 1;
}

int main(void)
{
    int value = 5;

    add_one(value);

    printf("%d\n", value);

    return 0;
}
```

Keluaran tetap `5`. Perubahan terhadap `x` hanya memengaruhi salinan lokal di dalam fungsi.

## Ruang lingkup variabel

Ruang lingkup atau *scope* menentukan bagian program tempat suatu nama dapat digunakan. Variabel yang dibuat di dalam fungsi disebut variabel lokal.

```c
double kinetic_energy(double mass,
                      double velocity)
{
    double energy =
        0.5 * mass * velocity * velocity;

    return energy;
}
```

Variabel `energy` hanya tersedia di dalam fungsi tersebut. Fungsi lain tidak dapat menggunakan variabel lokal tersebut secara langsung.

### Variabel lokal

Variabel lokal membuat fungsi lebih mandiri. Nama yang sama pada fungsi lain dapat merujuk pada variabel yang berbeda.

Sebagai prinsip umum, gunakan ruang lingkup sekecil mungkin yang masih memenuhi kebutuhan. Pendekatan ini mengurangi kemungkinan bagian program yang tidak berkaitan saling memengaruhi.

### Variabel global

Variabel yang dideklarasikan di luar semua fungsi memiliki ruang lingkup lebih luas. Variabel semacam ini dapat digunakan oleh beberapa fungsi dalam berkas yang sama.

Walaupun praktis, variabel global yang dapat berubah sebaiknya dibatasi. Ketergantungan tersembunyi pada keadaan global membuat fungsi lebih sulit diuji dan digunakan kembali.

## Modularisasi program

Modularisasi berarti membagi program menjadi bagian-bagian dengan tanggung jawab yang jelas. Fungsi merupakan alat utama untuk melakukan modularisasi dalam C.

Program analisis data, misalnya, dapat dipecah menjadi beberapa tugas terpisah. Salah satu susunan fungsi yang mungkin adalah sebagai berikut.

```text
read_data
mean
minimum
maximum
print_results
```

`main` kemudian berfungsi sebagai pengatur alur. Detail perhitungan ditempatkan di fungsi yang sesuai.

Struktur konseptual tersebut memperlihatkan hubungan antara `main` dan fungsi-fungsi pendukung. Gambaran sederhananya adalah sebagai berikut.

```text
main
 |
 +--> read_data
 |
 +--> mean
 |
 +--> minimum
 |
 +--> maximum
 |
 +--> print_results
```

Program modular biasanya lebih mudah dibaca dan diuji. Jika satu bagian bermasalah, kita dapat memusatkan pemeriksaan pada fungsi yang bertanggung jawab terhadap bagian tersebut.

## Contoh modularisasi masalah fisika

```c
#include <stdio.h>

double kinetic_energy(double mass,
                      double velocity);

double momentum(double mass,
                double velocity);

int main(void)
{
    double mass = 2.0;
    double velocity = 3.0;

    double energy =
        kinetic_energy(mass, velocity);

    double p =
        momentum(mass, velocity);

    printf("Energy   = %.3f J\n", energy);
    printf("Momentum = %.3f kg m/s\n", p);

    return 0;
}

double kinetic_energy(double mass,
                      double velocity)
{
    return
        0.5 * mass * velocity * velocity;
}

double momentum(double mass,
                double velocity)
{
    return mass * velocity;
}
```

Fungsi `kinetic_energy` dan `momentum` memiliki tugas yang berbeda dan jelas. Keduanya juga dapat digunakan kembali untuk data massa dan kecepatan lain.

## Fungsi dan penggunaan ulang kode

Fungsi yang baik sebaiknya menerima data yang diperlukan melalui parameter. Ketergantungan pada variabel global sebaiknya dikurangi agar fungsi dapat digunakan pada konteks berbeda.

Bandingkan fungsi yang bergantung pada variabel global dengan fungsi yang menggunakan parameter. Bentuk kedua biasanya lebih mudah dipahami karena hubungan input dan output terlihat langsung dari deklarasinya.

```c
double kinetic_energy(double mass,
                      double velocity)
{
    return
        0.5 * mass * velocity * velocity;
}
```

Fungsi tersebut tidak perlu mengetahui dari mana `mass` dan `velocity` berasal. Selama argumen bertipe sesuai, fungsi dapat digunakan kembali.

## Fungsi yang menerima larik

Fungsi menjadi semakin berguna ketika digabungkan dengan larik. Kita dapat membuat fungsi yang menerima sekumpulan data dan melakukan operasi tertentu tanpa harus menulis ulang pengulangan yang sama di `main`.

Sebagai contoh, kita dapat membuat fungsi khusus untuk menghitung jumlah elemen larik. Implementasinya dapat ditulis sebagai berikut.

```c
double sum_array(const double data[],
                 int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum += data[i];
    }

    return sum;
}
```

Parameter `data[]` menunjukkan bahwa fungsi menerima larik `double`. Parameter `n` diperlukan karena fungsi tidak mengetahui jumlah elemen hanya dari parameter larik.

## Mengapa ukuran larik harus dikirim?

Ketika larik dikirim ke fungsi, parameter larik pada dasarnya diperlakukan sebagai *pointer* ke elemen pertama. Informasi ukuran total larik tidak ikut disimpan dalam parameter tersebut.

Karena itu, fungsi perlu menerima ukuran larik secara eksplisit. Sebagai contoh, kita dapat menulis bentuk berikut.

```c
double mean(const double data[],
            int n)
```

memerlukan `n` secara terpisah. Tanpa informasi tersebut, fungsi tidak mengetahui kapan penelusuran harus berhenti.

Hal ini berbeda dari beberapa bahasa tingkat tinggi yang menyimpan panjang sebagai bagian dari objek larik. Dalam C, programmer bertanggung jawab mengelola informasi ukuran.

## Fungsi statistik larik

Rata-rata dapat dihitung dengan fungsi berikut. Fungsi ini mengasumsikan `n > 0`, sehingga pemanggil harus memastikan prakondisi tersebut terpenuhi.

```c
double mean(const double data[],
            int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum += data[i];
    }

    return sum / n;
}
```

Fungsi minimum dapat menggunakan data pertama sebagai nilai awal. Pendekatan ini membuat fungsi benar untuk data positif maupun negatif.

```c
double minimum(const double data[],
               int n)
{
    double result = data[0];

    for (int i = 1; i < n; i++)
    {
        if (data[i] < result)
        {
            result = data[i];
        }
    }

    return result;
}
```

Fungsi maksimum memiliki pola yang hampir sama. Perbedaannya hanya terletak pada arah perbandingan.

```c
double maximum(const double data[],
               int n)
{
    double result = data[0];

    for (int i = 1; i < n; i++)
    {
        if (data[i] > result)
        {
            result = data[i];
        }
    }

    return result;
}
```

## Program modular untuk statistik data

Program berikut menggabungkan tiga fungsi statistik. `main` hanya mengatur alur dan menampilkan hasil.

```c
#include <stdio.h>

double mean(const double data[],
            int n);

double minimum(const double data[],
               int n);

double maximum(const double data[],
               int n);

int main(void)
{
    double data[] =
    {
        2.4,
        3.1,
        2.8,
        4.0,
        3.5
    };

    int n =
        sizeof(data) / sizeof(data[0]);

    printf("Mean    = %.3f\n",
           mean(data, n));

    printf("Minimum = %.3f\n",
           minimum(data, n));

    printf("Maximum = %.3f\n",
           maximum(data, n));

    return 0;
}

double mean(const double data[],
            int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum += data[i];
    }

    return sum / n;
}

double minimum(const double data[],
               int n)
{
    double result = data[0];

    for (int i = 1; i < n; i++)
    {
        if (data[i] < result)
        {
            result = data[i];
        }
    }

    return result;
}

double maximum(const double data[],
               int n)
{
    double result = data[0];

    for (int i = 1; i < n; i++)
    {
        if (data[i] > result)
        {
            result = data[i];
        }
    }

    return result;
}
```

Program tersebut lebih mudah diuji daripada versi yang menempatkan semua perhitungan di `main`. Setiap fungsi dapat diperiksa menggunakan larik uji yang berbeda.

## `const` pada parameter larik

Jika fungsi hanya membaca larik, kita sebaiknya menambahkan `const`. Kata tersebut menyatakan bahwa fungsi tidak bermaksud mengubah elemen melalui parameter tersebut.

```c
double mean(const double data[],
            int n)
```

Bentuk parameter larik tersebut berhubungan langsung dengan *pointer* ke elemen pertama. Secara makna parameter, bentuk itu setara dengan bentuk berikut.

```c
double mean(const double *data,
            int n)
```

untuk keperluan pengiriman larik. Penggunaan `const` membantu *compiler* mendeteksi perubahan data yang tidak disengaja.

Jika fungsi memang harus mengubah isi larik, `const` tidak digunakan. Contohnya adalah fungsi yang menambahkan *offset* ke setiap elemen.

```c
void add_offset(double data[],
                int n,
                double offset)
{
    for (int i = 0; i < n; i++)
    {
        data[i] += offset;
    }
}
```

Perubahan pada fungsi tersebut terlihat pada larik asli. Kita akan segera memahami alasannya melalui konsep alamat memori dan *pointer*.

## Pengantar *pointer*

*Pointer* adalah variabel yang menyimpan alamat memori. Konsep ini penting dalam C karena digunakan untuk mengakses data secara tidak langsung dan menjelaskan hubungan antara larik dan fungsi.

Misalkan kita mempunyai

```c
double temperature = 25.0;
```

Alamat variabel dapat diperoleh menggunakan operator `&`. Dengan demikian, `&temperature` berarti alamat tempat nilai `temperature` disimpan.

Kita dapat menyimpan alamat tersebut ke dalam sebuah *pointer*. Bentuk deklarasi dan inisialisasinya adalah sebagai berikut.

```c
double *p =
    &temperature;
```

Variabel `p` bertipe `double *`. Artinya, `p` dimaksudkan untuk menunjuk ke objek bertipe `double`.

## Operator de-referensi: `*`

Jika `p` menyimpan alamat suatu `double`, kita dapat mengakses nilai pada alamat tersebut menggunakan operator `*`. Operasi ini disebut **de-referensi**.

```c
double value =
    *p;
```

Jika `p` menunjuk ke `temperature`, maka `*p` menghasilkan nilai yang sama dengan `temperature`. Kita juga dapat mengubah nilai asli melalui *pointer*.

```c
*p = 30.0;
```

Setelah operasi tersebut, `temperature` menjadi 30.0. Perubahan terjadi karena `p` menunjuk ke lokasi memori yang sama.

### Contoh dasar *pointer*

```c
#include <stdio.h>

int main(void)
{
    double temperature = 25.0;

    double *p =
        &temperature;

    printf("temperature = %.2f\n",
           temperature);

    printf("*p          = %.2f\n",
           *p);

    *p = 30.0;

    printf("temperature = %.2f\n",
           temperature);

    return 0;
}
```

Program tersebut menunjukkan dua cara mengakses data yang sama. Cara pertama menggunakan nama variabel, sedangkan cara kedua menggunakan alamat yang disimpan pada *pointer*.

## Fungsi yang mengubah variabel pemanggil

Karena parameter skalar biasa dikirim berdasarkan nilai, fungsi tidak dapat mengubah variabel pemanggil hanya dengan menerima salinannya. Jika kita mengirim alamat, fungsi dapat mengubah nilai pada alamat tersebut.

Contoh klasik penggunaan *pointer* adalah fungsi `swap`. Fungsi tersebut menukar dua nilai dengan mengakses alamat variabel pemanggil.

```c
void swap(double *a,
          double *b)
{
    double temp = *a;

    *a = *b;
    *b = temp;
}
```

Fungsi dipanggil dengan mengirim alamat dua variabel. Karena itu, operator `&` digunakan pada argumen seperti berikut.

```c
swap(&x, &y);
```

Program lengkapnya:

```c
#include <stdio.h>

void swap(double *a,
          double *b);

int main(void)
{
    double x = 2.0;
    double y = 5.0;

    printf("Before: x = %.1f, y = %.1f\n",
           x, y);

    swap(&x, &y);

    printf("After : x = %.1f, y = %.1f\n",
           x, y);

    return 0;
}

void swap(double *a,
          double *b)
{
    double temp = *a;

    *a = *b;
    *b = temp;
}
```

Contoh ini cukup untuk memperkenalkan kegunaan dasar *pointer*. Pada tahap ini kita belum membahas alokasi memori dinamis, *linked list*, atau struktur data berbasis *pointer* yang lebih kompleks.

## Larik dan alamat memori

Elemen-elemen larik disimpan secara berurutan di memori. Susunan tersebut membuat akses indeks efisien dan menjelaskan hubungan dekat antara larik dan *pointer*.

Misalkan

```c
double x[4];
```

Secara konseptual, elemen-elemen tersebut tersusun berurutan di memori. Gambaran sederhananya dapat dibayangkan sebagai berikut.

```text
x[0]     x[1]     x[2]     x[3]
 |        |        |        |
 v        v        v        v
+--------+--------+--------+--------+
| double | double | double | double |
+--------+--------+--------+--------+
```

Nama larik pada banyak ekspresi berperilaku seperti alamat elemen pertama. Karena itu, `x` berkaitan erat dengan `&x[0]`.

## Hubungan larik dan *pointer*

Kita dapat menulis

```c
double data[5] =
{
    1.0,
    2.0,
    3.0,
    4.0,
    5.0
};

double *p = data;
```

Dalam konteks tersebut, `p` menunjuk ke elemen pertama larik. Dengan demikian, `*p` memberikan nilai yang sama dengan `data[0]`.

Secara konseptual,

```c
data[i]
```

berhubungan dengan

```c
*(data + i)
```

Namun, aritmetika *pointer* bukan fokus utama kuliah ini. Untuk kebanyakan operasi, notasi indeks lebih mudah dibaca dan lebih sesuai bagi program tingkat awal.

## Mengapa larik dapat berubah ketika dikirim ke fungsi?

Perhatikan fungsi berikut.

```c
void scale(double data[],
           int n,
           double factor)
{
    for (int i = 0; i < n; i++)
    {
        data[i] *= factor;
    }
}
```

Jika fungsi dipanggil pada suatu larik, fungsi memperoleh akses ke elemen larik tersebut melalui alamatnya. Pemanggilannya dapat ditulis sebagai berikut.

```c
scale(x, n, 2.0);
```

elemen larik `x` berubah. Fungsi menerima akses ke alamat elemen pertama dan melakukan perubahan langsung pada data asli.

Hal tersebut merupakan perbedaan penting antara parameter larik dan parameter skalar biasa. Untuk fungsi yang hanya membaca data, penggunaan `const` membuat maksudnya lebih jelas.

## `sizeof` pada parameter larik

Kesalahan umum adalah mencoba menghitung panjang larik dari dalam fungsi menggunakan `sizeof`. Bentuk berikut tidak menghasilkan jumlah elemen larik asli.

```c
void process(double data[])
{
    int n =
        sizeof(data) /
        sizeof(data[0]);
}
```

Di dalam fungsi, `data` diperlakukan sebagai *pointer*. Karena itu, `sizeof(data)` memberikan ukuran *pointer*, bukan ukuran larik yang dikirim dari pemanggil.

Pola yang benar adalah mengirim ukuran larik secara eksplisit sebagai parameter tambahan. Bentuk deklarasinya dapat ditulis sebagai berikut.

```c
void process(const double data[],
             int n)
```

Dengan cara tersebut, fungsi memiliki informasi yang dibutuhkan untuk menelusuri data dengan aman. Batas penelusuran tidak lagi bergantung pada tebakan atau asumsi tersembunyi.

## Mengirim larik dua dimensi ke fungsi

Untuk larik dua dimensi, fungsi perlu mengetahui ukuran dimensi kedua. Informasi tersebut diperlukan agar posisi setiap elemen dapat dihitung dengan benar.

Sebagai contoh, kita dapat membuat fungsi untuk larik dua dimensi dengan empat kolom. Bentuk sederhananya adalah sebagai berikut.

```c
void print_matrix(double data[][4],
                  int rows)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%.2f ",
                   data[i][j]);
        }

        printf("\n");
    }
}
```

Pada tahap ini kita cukup memahami bentuk tersebut. Pembahasan *pointer* multidimensi yang lebih lanjut tidak diperlukan untuk tujuan kuliah ini.

## Studi kasus: analisis data getaran dalam larik

Misalkan akselerometer menghasilkan serangkaian data percepatan. Data tersebut dapat dituliskan sebagai berikut.

```math
a_0,a_1,\ldots,a_{N-1}.
```

Kita ingin menghitung rata-rata, RMS, dan amplitudo maksimum. Karena data disimpan dalam larik, beberapa analisis dapat dilakukan tanpa membaca ulang masukan.

Untuk mengukur amplitudo efektif, kita dapat menggunakan nilai RMS. Besaran tersebut didefinisikan dengan persamaan berikut.

```math
a_{\text{RMS}}
=
\sqrt{
\frac{1}{N}
\sum_{i=0}^{N-1}a_i^2
}.
```

Kita akan memisahkan setiap besaran ke fungsi yang berbeda. Pendekatan ini membuat struktur program lebih mudah diuji dan digunakan kembali.

```c
#include <stdio.h>
#include <math.h>

double mean(const double data[],
            int n);

double rms(const double data[],
           int n);

double max_abs(const double data[],
               int n);

int main(void)
{
    double acceleration[] =
    {
        1.2,
        -2.4,
        8.7,
        -9.1,
        3.6
    };

    int n =
        sizeof(acceleration) /
        sizeof(acceleration[0]);

    printf("Mean    = %.3f m/s^2\n",
           mean(acceleration, n));

    printf("RMS     = %.3f m/s^2\n",
           rms(acceleration, n));

    printf("Max |a| = %.3f m/s^2\n",
           max_abs(acceleration, n));

    return 0;
}

double mean(const double data[],
            int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum += data[i];
    }

    return sum / n;
}

double rms(const double data[],
           int n)
{
    double sum_square = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum_square +=
            data[i] * data[i];
    }

    return sqrt(sum_square / n);
}

double max_abs(const double data[],
               int n)
{
    double result =
        fabs(data[0]);

    for (int i = 1; i < n; i++)
    {
        double value =
            fabs(data[i]);

        if (value > result)
        {
            result = value;
        }
    }

    return result;
}
```

Program tersebut menunjukkan manfaat modularisasi secara langsung. Setiap fungsi memiliki satu tanggung jawab dan hanya membutuhkan larik serta ukurannya.

## Fungsi dengan lebih dari satu keluaran

Satu fungsi C hanya memiliki satu nilai kembalian langsung melalui `return`. Jika kita ingin menghasilkan lebih dari satu nilai, parameter *pointer* dapat digunakan sebagai saluran keluaran tambahan.

Misalkan minimum dan maksimum ingin dihitung sekaligus. Karena satu `return` hanya mengembalikan satu nilai langsung, dua hasil dapat disalurkan melalui dua parameter *pointer*.

```c
void min_max(const double data[],
             int n,
             double *minimum,
             double *maximum)
{
    *minimum = data[0];
    *maximum = data[0];

    for (int i = 1; i < n; i++)
    {
        if (data[i] < *minimum)
        {
            *minimum = data[i];
        }

        if (data[i] > *maximum)
        {
            *maximum = data[i];
        }
    }
}
```

Pemanggilannya:

```c
double min_value;
double max_value;

min_max(data,
        n,
        &min_value,
        &max_value);
```

Setelah fungsi selesai, kedua variabel pada pemanggil telah berisi hasil. Pola ini merupakan contoh penting penggunaan *pointer* yang tetap sederhana dan relevan untuk program teknik.

## Pengantar *string*

Dalam C, *string* direpresentasikan sebagai larik karakter. Tidak ada tipe bawaan khusus bernama `string` seperti pada beberapa bahasa pemrograman lain.

Contoh:

```c
char name[] =
    "sensor-A";
```

Secara konseptual, *string* tersebut merupakan urutan karakter biasa. Susunan elemennya dapat dibayangkan sebagai berikut.

```text
's' 'e' 'n' 's' 'o' 'r' '-' 'A' '\0'
```

Karakter `'\0'` disebut **null terminator**. Karakter tersebut menandai akhir teks.

## Larik karakter

Kita dapat menyediakan kapasitas teks secara eksplisit. Jika kapasitasnya 100 karakter, satu elemen tetap perlu tersedia untuk null terminator.

```c
char name[100];
```

Untuk menampilkan *string*, kita dapat menggunakan format `%s`. Format tersebut membuat `printf` membaca karakter sampai null terminator ditemukan.

```c
printf("%s\n", name);
```

Format `%s` membaca karakter mulai dari alamat awal sampai menemukan `'\0'`. Jika null terminator hilang, operasi *string* dapat membaca melewati batas yang seharusnya.

## Membaca *string* dengan `fgets`

Untuk membaca satu baris teks, `fgets` umumnya lebih sesuai daripada `scanf("%s", ...)`. Fungsi ini menerima batas kapasitas dan juga dapat membaca spasi.

```c
#include <stdio.h>

int main(void)
{
    char name[100];

    printf("Sensor name: ");

    fgets(name,
          sizeof(name),
          stdin);

    printf("Name: %s", name);

    return 0;
}
```

`fgets` dapat menyimpan karakter baris baru `'\n'` jika masih ada ruang. Hal ini perlu diperhatikan ketika teks akan dibandingkan atau disimpan.

## Pustaka `string.h`

C menyediakan fungsi-fungsi pengolahan *string* melalui pustaka standar. Pustaka tersebut disertakan dengan direktif berikut.

```c
#include <string.h>
```

Salah satu fungsi yang paling sederhana adalah `strlen`. Fungsi tersebut menghitung banyak karakter sebelum null terminator.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char text[] =
        "Teknik Fisika";

    printf("Length = %zu\n",
           strlen(text));

    return 0;
}
```

Fungsi seperti `strcmp`, `strcpy`, dan `strcat` juga tersedia. Penggunaannya harus tetap memperhatikan kapasitas larik karakter agar penulisan tidak melewati batas.

## Menghapus karakter baris baru dari `fgets`

Karakter `'\n'` yang dibaca `fgets` sering perlu dihapus. Salah satu cara yang praktis adalah menggunakan `strcspn`.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[100];

    printf("Sensor name: ");

    fgets(name,
          sizeof(name),
          stdin);

    name[strcspn(name, "\n")] =
        '\0';

    printf("Name = [%s]\n", name);

    return 0;
}
```

Setelah karakter baris baru dihapus, *string* lebih mudah dibandingkan atau digabungkan. Pola ini akan berguna kembali ketika kita membaca teks dari berkas.

## Contoh: label eksperimen dan data numerik

Satu program dapat menggunakan larik karakter dan larik numerik secara bersamaan. Label eksperimen disimpan sebagai *string*, sedangkan hasil pengukuran disimpan sebagai `double`.

```c
#include <stdio.h>
#include <string.h>

double mean(const double data[],
            int n);

int main(void)
{
    char experiment[100];
    double voltage[5];

    printf("Experiment name: ");

    fgets(experiment,
          sizeof(experiment),
          stdin);

    experiment[
        strcspn(experiment, "\n")
    ] = '\0';

    for (int i = 0; i < 5; i++)
    {
        printf("V%d: ", i);
        scanf("%lf", &voltage[i]);
    }

    printf("\nExperiment: %s\n",
           experiment);

    printf("Mean voltage = %.3f V\n",
           mean(voltage, 5));

    return 0;
}

double mean(const double data[],
            int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum += data[i];
    }

    return sum / n;
}
```

Contoh tersebut memperlihatkan dua bentuk larik dengan tujuan berbeda. Larik `char` menyimpan teks, sedangkan larik `double` menyimpan data numerik.

## Merancang fungsi yang baik

Fungsi yang baik sebaiknya memiliki satu tanggung jawab utama. Nama fungsi dan parameter juga sebaiknya cukup jelas untuk menunjukkan apa yang dilakukan dan data apa yang dibutuhkan.

Nama fungsi sebaiknya menjelaskan tugas yang dilakukan. Beberapa contoh nama yang baik adalah sebagai berikut.

```text
mean
rms
kinetic_energy
celsius_to_kelvin
print_matrix
read_measurements
```

Fungsi sebaiknya menerima data yang diperlukan melalui parameter. Ketergantungan pada variabel global sebaiknya dikurangi agar fungsi lebih mudah diuji dan digunakan kembali.

## Fungsi kecil atau fungsi besar?

Tidak ada aturan bahwa semua fungsi harus sangat pendek. Ukuran fungsi yang tepat ditentukan oleh tanggung jawab, keterbacaan, dan kemudahan pengujian.

Jika satu fungsi melakukan banyak tugas yang tidak berkaitan, fungsi tersebut sebaiknya dipecah. Sebaliknya, memecah setiap satu atau dua baris menjadi fungsi terpisah juga dapat membuat program sulit diikuti.

Tujuan modularisasi bukan sekadar memperbanyak fungsi. Tujuannya adalah membuat struktur program lebih jelas dan setiap bagian memiliki peran yang dapat dijelaskan.

## Kesalahan umum pada larik

### Indeks keluar batas

Kesalahan paling umum adalah menggunakan indeks `N` pada larik berukuran $N$. Indeks terakhir yang benar adalah `N-1`, sehingga pola batas pengulangan harus dirancang dengan hati-hati.

### Menggunakan ukuran yang salah

Jika hanya sebagian kapasitas larik digunakan, penelusuran harus mengikuti jumlah data aktual. Menelusuri seluruh kapasitas dapat membaca elemen yang belum pernah diberi nilai.

### Mengasumsikan larik mengetahui panjangnya

Parameter fungsi seperti

```c
double data[]
```

tidak membawa informasi jumlah elemen. Ukuran harus dikirim melalui parameter lain atau dikelola dengan cara yang jelas.

### Lupa bahwa fungsi dapat mengubah larik

Jika parameter larik tidak menggunakan `const`, fungsi dapat mengubah elemen pada larik asli. Perubahan tersebut terjadi karena fungsi bekerja melalui alamat memori data yang sama.

## Kesalahan umum pada fungsi

### Tipe nilai kembalian tidak sesuai

Fungsi yang dideklarasikan

```c
int f(void)
```

seharusnya mengembalikan nilai yang sesuai dengan tipe `int`. Jika fungsi tidak menghasilkan nilai, tipe `void` lebih tepat.

### Lupa prototipe fungsi

Jika implementasi fungsi diletakkan setelah `main`, prototipe sebaiknya ditulis sebelum fungsi digunakan. Hal ini membantu *compiler* memeriksa jumlah dan tipe argumen.

### Terlalu bergantung pada variabel global

Variabel global yang dapat berubah membuat fungsi mempunyai ketergantungan tersembunyi. Pengiriman data melalui parameter biasanya membuat hubungan antarbagiannya lebih jelas.

## Kesalahan umum pada *pointer*

### *Pointer* belum menunjuk ke objek valid

Kode

```c
double *p;
*p = 5.0;
```

tidak benar karena `p` belum diberi alamat objek yang valid. De-referensi hanya boleh dilakukan ketika *pointer* diketahui menunjuk ke lokasi yang sah.

### Tipe *pointer* tidak sesuai

Jika objek bertipe `double`, gunakan *pointer* bertipe `double *`. Kesesuaian tipe membantu *compiler* mendeteksi kesalahan dan membuat maksud program lebih jelas.

### Menggunakan *pointer* ketika tidak diperlukan

Tidak semua fungsi memerlukan *pointer*. Jika fungsi hanya perlu membaca satu nilai skalar, pengiriman berdasarkan nilai biasanya lebih sederhana dan lebih aman.

## Kesalahan umum pada *string*

### Lupa ruang untuk null terminator

Untuk menyimpan lima karakter teks, kita memerlukan sekurang-kurangnya enam elemen `char`. Satu elemen tambahan digunakan untuk `'\0'`.

### Membandingkan *string* dengan `==`

Ekspresi

```c
name1 == name2
```

tidak membandingkan isi kedua teks. Untuk membandingkan isi *string*, gunakan `strcmp` dari `string.h`.

### Input melebihi kapasitas

Fungsi input teks harus selalu memperhatikan kapasitas larik. Penggunaan `fgets` dengan ukuran yang jelas membantu mencegah pembacaan melebihi ruang yang tersedia.

## Kebiasaan pemrograman yang baik

Gunakan nama fungsi dan parameter yang bermakna. Kode yang mudah dibaca biasanya juga lebih mudah diuji dan dipelihara.

Gunakan `const` jika fungsi hanya membaca larik. Kebiasaan ini membuat kontrak fungsi lebih jelas dan membantu mencegah perubahan data yang tidak disengaja.

Kirim ukuran larik bersama lariknya ketika fungsi perlu menelusuri elemen. Jangan mencoba menebak panjang larik dari `sizeof` parameter fungsi.

Batasi penggunaan *pointer* pada kebutuhan yang benar-benar jelas. Pada tahap ini, fokus kita adalah alamat, de-referensi, hubungan larik-*pointer*, dan keluaran tambahan dari fungsi.

Kompilasi program dengan peringatan aktif. Perintah berikut tetap dianjurkan karena membantu menemukan kesalahan tipe dan pola kode yang mencurigakan.

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 program.c -o program
```

## Cek pemahaman

Cobalah menjawab pertanyaan berikut tanpa melihat kembali catatan. Pertanyaan-pertanyaan ini dapat digunakan untuk memeriksa apakah hubungan antara larik, fungsi, ruang lingkup, dan *pointer* sudah dipahami secara konseptual.

- Apa perbedaan antara variabel biasa dan larik?
- Mengapa indeks larik C dimulai dari nol?
- Jika larik memiliki $N$ elemen, apa indeks terakhir yang valid?
- Mengapa akses di luar batas larik berbahaya?
- Bagaimana menghitung jumlah elemen larik lokal menggunakan `sizeof`?
- Mengapa teknik `sizeof` tidak bekerja dengan cara yang sama pada parameter larik fungsi?
- Apa perbedaan larik satu dimensi dan dua dimensi?
- Mengapa larik dua dimensi biasanya ditelusuri dengan nested loop?
- Apa tujuan utama fungsi dalam program?
- Apa perbedaan parameter dan argumen?
- Apa arti *pass by value*?
- Mengapa perubahan parameter skalar biasa tidak mengubah variabel pemanggil?
- Apa yang dimaksud dengan ruang lingkup variabel?
- Mengapa variabel lokal biasanya lebih mudah dikendalikan daripada variabel global?
- Apa yang dimaksud dengan modularisasi?
- Apa keuntungan penggunaan ulang fungsi?
- Apa yang disimpan oleh *pointer*?
- Apa fungsi operator `&` dan `*`?
- Mengapa fungsi `swap` memerlukan alamat variabel?
- Apa hubungan `array`, `&array[0]`, dan *pointer* ke elemen pertama?
- Mengapa isi larik dapat berubah ketika dikirim ke fungsi?
- Apa fungsi `const` pada parameter larik?
- Bagaimana *string* direpresentasikan dalam C?
- Apa fungsi null terminator?
- Mengapa `fgets` sesuai untuk membaca satu baris teks?

## Latihan

### 1. Statistik pengukuran tegangan

Buat program yang membaca paling banyak 50 data tegangan ke dalam larik. Setelah seluruh data dibaca, hitung rata-rata, minimum, maksimum, dan RMS menggunakan fungsi terpisah.

Gunakan prototipe fungsi dan parameter `const` untuk fungsi yang hanya membaca data. Uji program dengan data yang hasilnya dapat dihitung secara manual.

### 2. Kecepatan dari data posisi

Diberikan larik posisi

```math
x_0,x_1,\ldots,x_{N-1}
```

dengan interval waktu tetap $\Delta t$. Buat fungsi yang mengisi larik kecepatan berdasarkan selisih posisi berurutan. Gunakan hubungan

```math
v_i
=
\frac{x_{i+1}-x_i}{\Delta t}.
```

Jelaskan mengapa jumlah elemen larik kecepatan adalah $N-1$. Uji program menggunakan data gerak yang sederhana dan bandingkan dengan perhitungan manual.

### 3. Energi kinetik banyak partikel

Diberikan dua larik dengan panjang sama, yaitu massa dan kecepatan beberapa partikel. Buat fungsi yang mengisi larik ketiga dengan energi kinetik setiap partikel. Gunakan persamaan

```math
E_{k,i}
=
\frac12m_iv_i^2.
```

Buat fungsi lain untuk menghitung energi kinetik total. Program tidak boleh menggunakan variabel global untuk data fisik tersebut.

### 4. Analisis gelombang diskrit

Sebuah larik menyimpan sampel simpangan gelombang pada beberapa waktu. Nyatakan data tersebut secara umum dalam bentuk berikut.

```math
y_0,y_1,\ldots,y_{N-1}.
```

Buat fungsi untuk mencari amplitudo maksimum absolut dan fungsi lain untuk menghitung RMS. Uji menggunakan data yang memiliki nilai positif dan negatif agar perbedaan kedua besaran terlihat.

### 5. Matriks data sensor

Gunakan larik dua dimensi untuk menyimpan data dari empat sensor pada enam waktu pengukuran. Buat program yang menghitung rata-rata setiap sensor dan rata-rata semua sensor pada setiap waktu.

Gunakan nested loop dan pecah perhitungan menjadi fungsi yang sesuai. Jelaskan kompleksitas penelusuran terhadap jumlah sensor dan jumlah sampel.

### 6. Normalisasi data

Buat fungsi

```c
void normalize(double data[],
               int n)
```

yang mengubah data sehingga nilai maksimum absolut menjadi satu. Jika seluruh data bernilai nol, fungsi tidak boleh melakukan pembagian dengan nol.

Uji fungsi dengan data campuran positif dan negatif. Tampilkan larik sebelum dan sesudah pemanggilan untuk menunjukkan bahwa fungsi mengubah larik asli.

### 7. Fungsi `min_max`

Buat fungsi yang menerima larik dan menghasilkan minimum serta maksimum melalui dua parameter *pointer*. Fungsi tersebut tidak boleh menggunakan variabel global.

Tulis program utama yang memanggil fungsi dengan operator `&`. Jelaskan mengapa dua hasil tidak dapat sekaligus dikembalikan sebagai dua nilai terpisah menggunakan satu `return` biasa.

### 8. Operasi dasar vektor

Representasikan dua vektor tiga dimensi menggunakan larik dengan tiga elemen. Buat fungsi untuk menghitung penjumlahan vektor, hasil kali titik, dan besar vektor.

Gunakan

```math
\mathbf{a}\cdot\mathbf{b}
=
a_xb_x+a_yb_y+a_zb_z
```

dan

```math
|\mathbf{a}|
=
\sqrt{
a_x^2+a_y^2+a_z^2
}.
```

Fungsi hasil kali titik mengembalikan satu `double`, sedangkan fungsi penjumlahan mengisi larik keluaran. Jelaskan mengapa kedua jenis fungsi tersebut memiliki antarmuka yang berbeda.

### 9. Intensitas cahaya relatif

Diberikan data intensitas cahaya $I_i$ dari beberapa pengukuran. Buat fungsi yang menghasilkan larik intensitas relatif terhadap nilai maksimum. Gunakan definisi

```math
r_i
=
\frac{I_i}{I_{\max}}.
```

Pisahkan proses pencarian maksimum dan normalisasi ke dalam fungsi yang berbeda. Program harus menolak kasus ketika tidak ada nilai intensitas positif.

### 10. Data kalorimetri sederhana

Diberikan larik waktu dan temperatur dari percobaan pemanasan sederhana. Buat fungsi untuk mencari kenaikan temperatur terbesar antara dua pengukuran berurutan. Definisikan perubahan temperatur sebagai

```math
\Delta T_i
=
T_{i+1}-T_i.
```

Fungsi juga harus menentukan indeks interval tempat kenaikan terbesar terjadi. Program utama kemudian menampilkan waktu awal, waktu akhir, dan perubahan temperatur pada interval tersebut.

### 11. Konversi satuan modular

Buat fungsi terpisah untuk konversi Celsius ke Kelvin, km/jam ke m/s, dan pascal ke kilopascal. Gunakan fungsi-fungsi tersebut untuk mengolah beberapa data yang disimpan dalam larik.

Program utama harus hanya mengatur alur, sedangkan rumus konversi ditempatkan dalam fungsi. Jelaskan bagaimana modularisasi memudahkan pengujian masing-masing konversi.

### 12. Identitas eksperimen dengan *string*

Buat program yang membaca nama eksperimen dan nama operator menggunakan `fgets`. Hapus karakter baris baru, lalu tampilkan teks beserta panjang masing-masing menggunakan `strlen`.

Tambahkan pemeriksaan agar input kosong ditolak. Program boleh meminta pengguna memasukkan ulang teks sampai panjang setelah penghapusan `'\n'` lebih besar dari nol.

### 13. Perbandingan nama sensor

Buat program yang membaca dua nama sensor dan membandingkan keduanya menggunakan `strcmp`. Program harus menjelaskan apakah kedua nama sama atau mana yang muncul lebih dahulu secara leksikografis.

Jelaskan mengapa operator `==` tidak membandingkan isi dua *string*. Kaitkan penjelasan dengan hubungan antara larik karakter dan alamat memori.

### 14. Proyek mini: analisis gerak satu dimensi

Simpan data waktu dan posisi eksperimen gerak satu dimensi dalam dua larik. Buat fungsi untuk menghitung kecepatan pada setiap interval, rata-rata kecepatan, kecepatan maksimum absolut, serta indeks interval tempat nilai maksimum tersebut terjadi.

Program harus menggunakan beberapa fungsi dengan tanggung jawab yang jelas. Tampilkan tabel yang memuat waktu awal, waktu akhir, posisi awal, posisi akhir, dan kecepatan setiap interval.

## Rangkuman

- Larik digunakan untuk menyimpan banyak nilai bertipe sama dalam susunan berurutan. Setiap elemen diakses menggunakan indeks yang dimulai dari nol.

- Untuk larik dengan $N$ elemen, indeks valid memenuhi

```math
0
\leq i
\leq
N-1.
```

- C tidak memeriksa batas larik secara otomatis. Karena itu, programmer bertanggung jawab memastikan setiap indeks tetap berada pada rentang yang valid.

- Larik sangat cocok digunakan bersama pengulangan. Pola *accumulator*, minimum, maksimum, dan berbagai statistik dapat diterapkan langsung pada elemen-elemen larik.

- Larik dua dimensi dapat digunakan untuk data berbentuk tabel atau matriks. Penelusurannya biasanya menggunakan pengulangan bersarang.

- Fungsi memecah program menjadi unit yang mempunyai tugas tertentu. Modularisasi membuat program lebih mudah dibaca, diuji, dan digunakan kembali.

- Parameter merupakan variabel pada definisi fungsi, sedangkan argumen merupakan nilai yang diberikan ketika fungsi dipanggil. Untuk tipe skalar biasa, C menggunakan *pass by value*.

- Variabel lokal hanya tersedia pada ruang lingkup tempat variabel dideklarasikan. Penggunaan variabel global yang dapat berubah sebaiknya dibatasi agar aliran data program tetap jelas.

- Prototipe fungsi memberi tahu *compiler* mengenai nama, tipe nilai kembalian, dan parameter sebelum fungsi digunakan. Pola ini berguna ketika implementasi fungsi diletakkan setelah `main`.

- Larik yang dikirim ke fungsi berkaitan dengan alamat elemen pertama. Karena itu, ukuran larik harus dikelola dan biasanya dikirim sebagai parameter terpisah.

- Parameter
    ```c
    const double data[]
    ```
    menyatakan bahwa fungsi hanya membaca elemen larik. Penggunaan `const` membantu mencegah perubahan data yang tidak disengaja.

- *Pointer* adalah variabel yang menyimpan alamat memori. Operator `&` mengambil alamat, sedangkan operator `*` mengakses nilai pada alamat yang ditunjuk.

- *Pointer* memungkinkan fungsi mengubah variabel milik pemanggil. Pola ini juga dapat digunakan untuk menghasilkan lebih dari satu keluaran dari sebuah fungsi.

- Nama larik pada banyak ekspresi berkaitan erat dengan alamat elemen pertama. Secara konseptual,
    ```c
    data
    ```
    berhubungan dengan
    ```c
    &data[0]
    ```
    dan
    ```c
    data[i]
    ```
    berhubungan dengan
    ```c
    *(data + i)
    ```

- *String* dalam C direpresentasikan sebagai larik karakter yang diakhiri dengan null terminator `'\0'`. Pustaka `string.h` menyediakan fungsi dasar seperti `strlen` dan `strcmp`.

- `fgets` sesuai untuk membaca satu baris teks karena kapasitas input dapat dibatasi. Karakter baris baru yang ikut terbaca dapat dihapus sebelum teks diproses lebih lanjut.

- Pada kuliah berikutnya kita akan menggunakan larik, fungsi, *string*, dan *pointer* dasar sebagai fondasi untuk membangun data terstruktur dengan `struct`. Konsep-konsep tersebut juga akan digunakan ketika kita mulai membaca dan menulis berkas melalui `FILE *`.
