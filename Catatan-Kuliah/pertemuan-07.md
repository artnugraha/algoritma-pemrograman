# Kuliah 7: Data Terstruktur dan Pengolahan Berkas

## Pengelolaan data yang lebih baik

Pada kuliah sebelumnya kita telah mempelajari larik, fungsi, modularisasi program, *pointer* dasar, dan *string*. Konsep-konsep tersebut memungkinkan kita menyimpan banyak nilai bertipe sama serta membagi program menjadi fungsi-fungsi yang memiliki tugas tertentu.

Namun, banyak data teknik tidak terdiri atas satu besaran saja. Satu pengukuran eksperimen dapat memiliki waktu, temperatur, tekanan, tegangan, nama sensor, dan status yang semuanya berkaitan sebagai satu kesatuan.

Sebagai contoh, satu titik pengukuran dapat dipandang sebagai satu rekaman yang memiliki beberapa atribut. Representasi sederhananya dapat ditulis sebagai berikut.

```text
waktu       = 2.5 s
temperatur  = 31.2 C
sensor      = "T1"
```

Jika setiap bagian disimpan pada larik yang berbeda, program masih dapat bekerja. Namun, hubungan bahwa ketiga nilai tersebut merupakan satu rekaman pengukuran menjadi kurang terlihat.

Bahasa C menyediakan `struct` untuk mengelompokkan beberapa data yang berkaitan ke dalam satu tipe terstruktur. Konsep ini akan sangat berguna ketika kita mulai menyimpan dan membaca data eksperimen dari berkas.

## Strukturnya `struct`

Judul bagian ini agak lucu, tetapi pada dasarnya `struct` adalah konstruksi dalam C yang memungkinkan beberapa variabel dengan tipe yang berbeda dikelompokkan menjadi satu kesatuan. Setiap bagian di dalam `struct` disebut **anggota** atau *member*.

Sebagai contoh, kita dapat membuat tipe untuk merepresentasikan satu pengukuran temperatur. Tipe tersebut menyimpan waktu dan temperatur sebagai dua nilai `double`.

```c
struct Measurement
{
    double time;
    double temperature;
};
```

Deklarasi tersebut belum membuat variabel pengukuran. Kita baru mendefinisikan bentuk data yang disebut `struct Measurement`.

### Membuat variabel `struct`

Setelah tipe dibuat, kita dapat mendeklarasikan variabel dengan tipe tersebut. Bentuknya mirip deklarasi variabel biasa.

```c
struct Measurement m;
```

Kita kemudian dapat mengisi setiap anggota menggunakan operator titik `.`. Bentuk penggunaannya dapat dilihat pada contoh berikut.

```c
m.time = 2.5;
m.temperature = 31.2;
```

Operator titik digunakan untuk memilih anggota dari suatu variabel `struct`. Bentuk ini membuat hubungan antarbesaran lebih jelas dibandingkan menyimpan semuanya pada variabel yang tidak terorganisasi.

### Inisialisasi `struct`

`struct` dapat diinisialisasi pada saat dideklarasikan. Urutan nilai mengikuti urutan anggota pada definisi `struct`.

```c
struct Measurement m =
{
    2.5,
    31.2
};
```

Untuk meningkatkan keterbacaan, kita juga dapat menggunakan *designated initializer*. Bentuk ini menyebutkan nama anggota secara eksplisit.

```c
struct Measurement m =
{
    .time = 2.5,
    .temperature = 31.2
};
```

Pendekatan tersebut sangat berguna ketika `struct` memiliki banyak anggota. Perubahan urutan anggota juga menjadi lebih mudah dikelola.

### `typedef` untuk menyederhanakan nama tipe

Penulisan `struct Measurement` dapat disederhanakan menggunakan `typedef`. Cara ini sering digunakan agar deklarasi variabel lebih ringkas.

```c
typedef struct
{
    double time;
    double temperature;
} Measurement;
```

Setelah `typedef` dibuat, nama tipe dapat digunakan tanpa menuliskan kata `struct`. Deklarasi variabelnya menjadi lebih ringkas seperti berikut.

```c
Measurement m;
```

tanpa kata `struct`. Dalam catatan ini kita akan cukup sering menggunakan bentuk `typedef struct` karena lebih ringkas untuk contoh data teknik.

### `struct` dengan beberapa jenis data

Anggota `struct` tidak harus bertipe sama. Kita dapat menggabungkan bilangan, karakter, dan *string* sederhana dalam satu struktur.

```c
typedef struct
{
    double time;
    double voltage;
    char sensor_name[20];
    int valid;
} VoltageMeasurement;
```

Satu variabel dapat langsung diinisialisasi dengan nilai untuk setiap anggotanya. Contoh inisialisasinya ditunjukkan berikut ini.

```c
VoltageMeasurement m =
{
    .time = 1.0,
    .voltage = 4.75,
    .sensor_name = "V1",
    .valid = 1
};
```

Dalam contoh tersebut, `sensor_name` merupakan larik karakter di dalam `struct`. Karena itu, satu objek `VoltageMeasurement` menyimpan informasi numerik dan teks dalam satu rekaman.

### Mengapa data terstruktur berguna?

Data terstruktur membuat hubungan antarbesaran terlihat langsung dalam program. Ketika kita melihat `m.time` dan `m.voltage`, kita mengetahui kedua nilai tersebut berasal dari pengukuran yang sama.

Struktur ini juga memudahkan fungsi menerima atau mengembalikan satu objek yang memiliki beberapa anggota. Pada tahap berikutnya, struktur yang sama dapat digunakan untuk merepresentasikan satu baris data dari berkas CSV.

Secara konseptual, kita dapat memandang satu `struct` sebagai satu rekaman. Gambaran sederhananya ditunjukkan berikut ini.

```text
+-------------------------------+
| Measurement                   |
+-------------------------------+
| time        : double          |
| temperature : double          |
+-------------------------------+
```

Jika satu eksperimen memiliki banyak rekaman, kita dapat menggunakan larik dari `struct`. Kombinasi tersebut merupakan pola penting dalam pengolahan data teknik.

## Larik dari `struct`

Jika kita memiliki banyak pengukuran dengan bentuk yang sama, kita dapat membuat larik dari tipe `struct`. Setiap elemen larik kemudian merepresentasikan satu rekaman.

```c
Measurement data[100];
```

Elemen pertama adalah `data[0]`, sedangkan anggota waktunya diakses dengan `data[0].time`. Anggota temperaturnya diakses dengan `data[0].temperature`.

Struktur ini menggabungkan konsep larik dan `struct`. Larik mengatur banyak rekaman, sedangkan `struct` mengatur isi setiap rekaman.

### Contoh larik pengukuran

```c
#include <stdio.h>

typedef struct
{
    double time;
    double temperature;
} Measurement;

int main(void)
{
    Measurement data[] =
    {
        {0.0, 25.1},
        {1.0, 25.8},
        {2.0, 26.7},
        {3.0, 27.4}
    };

    int n =
        sizeof(data) / sizeof(data[0]);

    for (int i = 0; i < n; i++)
    {
        printf("t = %.1f s, T = %.2f C\n",
               data[i].time,
               data[i].temperature);
    }

    return 0;
}
```

Program tersebut menelusuri larik `Measurement` dengan pola yang sama seperti larik biasa. Perbedaannya adalah setiap elemen memiliki lebih dari satu anggota.

## Fungsi dan `struct`

Kita dapat mengirim `struct` ke fungsi seperti tipe data lain. Untuk objek yang kecil, pengiriman berdasarkan nilai masih cukup sederhana.

```c
void print_measurement(Measurement m)
{
    printf("%.3f %.3f\n",
           m.time,
           m.temperature);
}
```

Jika `struct` berukuran lebih besar, kita dapat mengirim alamatnya menggunakan *pointer*. Pendekatan ini menghindari penyalinan seluruh objek dan memungkinkan fungsi mengakses anggota secara efisien.

```c
void print_measurement(
    const Measurement *m)
{
    printf("%.3f %.3f\n",
           m->time,
           m->temperature);
}
```

Operator `->` digunakan untuk mengakses anggota `struct` melalui *pointer*. Bentuk `m->time` setara secara konsep dengan `(*m).time`.

### `struct` sebagai nilai kembalian

Fungsi juga dapat mengembalikan satu `struct`. Hal ini berguna ketika beberapa besaran secara logis merupakan satu hasil.

Misalkan kita ingin menyimpan minimum dan maksimum dalam satu tipe. Kita dapat mendefinisikan tipe hasil yang memuat kedua besaran tersebut seperti berikut.

```c
typedef struct
{
    double minimum;
    double maximum;
} Range;
```

Fungsi kemudian dapat mengembalikan satu objek `Range`. Kedua hasil tetap terkelompok sebagai satu nilai terstruktur.

```c
Range find_range(const double data[],
                 int n)
{
    Range result =
    {
        .minimum = data[0],
        .maximum = data[0]
    };

    for (int i = 1; i < n; i++)
    {
        if (data[i] < result.minimum)
        {
            result.minimum = data[i];
        }

        if (data[i] > result.maximum)
        {
            result.maximum = data[i];
        }
    }

    return result;
}
```

Pendekatan ini berbeda dari penggunaan dua parameter *pointer* pada kuliah sebelumnya. Keduanya dapat digunakan, tetapi `struct` sering membuat hasil yang saling berkaitan menjadi lebih mudah dipahami.

### Representasi data pengukuran

Dalam aplikasi Teknik Fisika, satu rekaman pengukuran biasanya mempunyai beberapa kolom. Contohnya adalah waktu, tegangan, arus, temperatur, tekanan, atau identitas sensor.

Kita dapat mendefinisikan tipe sesuai bentuk data yang ingin disimpan. Sebagai contoh, data listrik dapat direpresentasikan sebagai berikut.

```c
typedef struct
{
    double time;
    double voltage;
    double current;
} ElectricalMeasurement;
```

Satu objek `ElectricalMeasurement` merepresentasikan satu baris data. Daya sesaat pada pengukuran tersebut dapat dihitung menggunakan hubungan berikut.

```math
P_i
=
V_i I_i.
```

Fungsi sederhana untuk menghitung daya dapat dibuat dari model tersebut. Implementasinya dapat ditulis seperti berikut.

```c
double power(
    const ElectricalMeasurement *m)
{
    return
        m->voltage * m->current;
}
```

Hubungan antara model fisika dan struktur data menjadi cukup jelas. Setiap rekaman menyimpan data yang diperlukan untuk satu evaluasi model.

## Pengolahan *string* dasar dalam data terstruktur

Anggota `struct` juga dapat berupa larik karakter. Hal ini memungkinkan kita menyimpan label sensor, nama eksperimen, satuan, atau status sederhana.

```c
typedef struct
{
    char name[32];
    double value;
    char unit[16];
} SensorReading;
```

Satu objek dapat diinisialisasi dengan nilai numerik dan teks sekaligus. Contohnya ditunjukkan berikut ini.

```c
SensorReading reading =
{
    .name = "pressure_1",
    .value = 101.3,
    .unit = "kPa"
};
```

Karena `name` dan `unit` merupakan *string*, fungsi dari `string.h` dapat digunakan untuk memprosesnya. Kita tetap harus memperhatikan kapasitas larik karakter dan null terminator.

### Menyalin *string* ke anggota `struct`

Jika teks sudah diketahui saat inisialisasi, kita dapat mengisinya langsung seperti pada contoh sebelumnya. Jika teks ingin diubah setelah objek dibuat, assignment biasa tidak dapat digunakan pada larik karakter.

Assignment biasa tidak dapat digunakan untuk mengganti isi larik karakter. Karena itu, kode berikut tidak valid.

```c
reading.name = "sensor_A";
```

Sebagai gantinya, kita dapat menggunakan fungsi seperti `strcpy` setelah memastikan kapasitas tujuan cukup. Contoh sederhananya ditunjukkan berikut ini.

```c
#include <string.h>

strcpy(reading.name,
       "sensor_A");
```

Pada program nyata, panjang teks harus selalu diperiksa terhadap kapasitas larik tujuan. Dalam contoh kuliah ini kita menggunakan teks pendek agar tetap berada dalam batas yang telah dialokasikan.

## Pengolahan berkas (*file*)

Larik dan `struct` menyimpan data selama program berjalan. Ketika program selesai, data yang hanya berada di memori umumnya tidak dapat digunakan kembali.

Agar data dapat dipertahankan, kita perlu menyimpannya ke berkas atau *file*. Berkas memungkinkan program menghasilkan data yang dapat dibaca kembali, dianalisis oleh program lain, atau diperiksa oleh manusia.

Pada kuliah ini kita akan berfokus pada berkas teks. Format teks cukup transparan, mudah diperiksa, dan cocok untuk data pengukuran sederhana.

### `FILE *`

Pustaka standar C menyediakan tipe `FILE` untuk merepresentasikan aliran berkas. Tipe tersebut tersedia setelah kita menyertakan header berikut.

```c
#include <stdio.h>
```

Program biasanya bekerja dengan *pointer* ke `FILE`. Deklarasi yang umum dapat ditulis sebagai berikut.

```c
FILE *fp;
```

Variabel tersebut tidak menyimpan seluruh isi berkas. Ia menyimpan informasi yang digunakan pustaka C untuk mengelola aliran data ke atau dari berkas.

### Pola dasar operasi berkas

Operasi berkas sebaiknya selalu mengikuti urutan kerja yang konsisten. Pola yang perlu dibiasakan adalah sebagai berikut.

```text
open
  ↓
check
  ↓
read / write
  ↓
close
```

Keempat tahap tersebut harus dipahami sebagai satu kesatuan. Membuka berkas tanpa memeriksa hasil atau lupa menutup berkas merupakan kebiasaan yang sebaiknya dihindari.

Keempat tahap tersebut dapat diringkas dalam satu alur. Bentuk simboliknya dapat ditulis sebagai berikut.

```math
\boxed{
\text{open}
\rightarrow
\text{check}
\rightarrow
\text{read/write}
\rightarrow
\text{close}
}
```

Hampir seluruh operasi berkas pada kuliah ini mengikuti alur tersebut. Perbedaannya hanya terletak pada mode pembukaan serta operasi baca atau tulis yang digunakan.

### Membuka berkas dengan `fopen`

Fungsi `fopen` digunakan untuk membuka berkas. Fungsi ini menerima nama berkas dan mode operasi.

Untuk membaca berkas, kita menggunakan mode `"r"`. Contoh pembukaannya ditunjukkan berikut ini.

```c
FILE *fp =
    fopen("data.txt", "r");
```

Mode `"r"` berarti berkas dibuka untuk dibaca. Jika operasi gagal, `fopen` mengembalikan `NULL`.

### Mode berkas dasar

Beberapa mode yang penting pada tahap awal ditunjukkan pada tabel berikut. Setiap mode memiliki konsekuensi berbeda terhadap berkas yang sudah ada.

| Mode | Kegunaan |
|---|---|
| `"r"` | membaca berkas yang sudah ada |
| `"w"` | menulis dari awal, isi lama dapat ditimpa |
| `"a"` | menambahkan data pada akhir berkas |

Mode `"w"` harus digunakan dengan hati-hati karena isi lama dapat hilang. Mode `"a"` lebih sesuai jika data baru ingin ditambahkan tanpa menghapus catatan sebelumnya.

### Memeriksa keberhasilan `fopen`

Jangan langsung menggunakan `FILE *` tanpa memeriksa apakah pembukaan berhasil. Pemeriksaan dilakukan dengan membandingkan hasil `fopen` terhadap `NULL`.

```c
FILE *fp =
    fopen("data.txt", "r");

if (fp == NULL)
{
    printf("Failed to open file.\n");
    return 1;
}
```

Pemeriksaan ini penting karena kegagalan dapat terjadi akibat nama berkas salah, direktori tidak tersedia, atau izin akses tidak mencukupi. Program yang baik harus menangani kondisi tersebut secara eksplisit.

### Menutup berkas dengan `fclose`

Setelah operasi selesai, berkas harus ditutup agar sumber daya dilepaskan dengan benar. Penutupannya dilakukan menggunakan fungsi berikut.

```c
fclose(fp);
```

Penutupan memberi kesempatan kepada pustaka untuk menyelesaikan operasi yang tertunda dan melepaskan sumber daya. Kebiasaan menutup berkas juga membuat alur program lebih jelas.

Jika tahapan pembukaan, pemeriksaan, dan penutupan digabungkan, kita memperoleh pola dasar yang utuh. Bentuknya adalah sebagai berikut.

```c
FILE *fp =
    fopen("data.txt", "r");

if (fp == NULL)
{
    printf("Failed to open file.\n");
    return 1;
}

/* read or write */

fclose(fp);
```

Bentuk ini akan muncul berulang pada seluruh contoh berikutnya. Kita hanya akan mengganti bagian baca atau tulis sesuai tujuan program.

### Menulis berkas teks dengan `fprintf`

Fungsi `fprintf` mirip dengan `printf`, tetapi keluaran diarahkan ke berkas. Argumen pertama adalah `FILE *` tujuan.

```c
fprintf(fp,
        "time temperature\n");
```

Kita juga dapat menulis nilai numerik menggunakan format yang sama seperti pada `printf`. Contohnya ditunjukkan pada potongan kode berikut.

```c
fprintf(fp,
        "%.3f %.3f\n",
        time,
        temperature);
```

### Contoh lengkap menulis data temperatur

```c
#include <stdio.h>

int main(void)
{
    FILE *fp =
        fopen("temperature.txt", "w");

    if (fp == NULL)
    {
        printf("Failed to open output file.\n");
        return 1;
    }

    for (int i = 0; i <= 5; i++)
    {
        double time = i * 1.0;
        double temperature =
            25.0 + 0.8 * time;

        fprintf(fp,
                "%.2f %.2f\n",
                time,
                temperature);
    }

    fclose(fp);

    return 0;
}
```

Program tersebut menghasilkan berkas teks dengan dua kolom. Setiap baris menyimpan waktu dan temperatur.

Isi berkas yang dihasilkan terdiri atas dua kolom numerik. Salah satu tampilannya dapat terlihat seperti berikut.

```text
0.00 25.00
1.00 25.80
2.00 26.60
3.00 27.40
4.00 28.20
5.00 29.00
```

Format teks sederhana seperti ini mudah dibaca oleh manusia. Format yang sama juga mudah diproses kembali oleh program.

### Membaca berkas teks dengan `fscanf`

Fungsi `fscanf` mirip dengan `scanf`, tetapi sumber inputnya adalah berkas. Argumen pertama adalah `FILE *` yang telah dibuka.

Misalkan berkas berisi dua kolom `time` dan `temperature`. Kita dapat membaca satu baris dengan format yang sesuai seperti berikut.

```c
fscanf(fp,
       "%lf %lf",
       &time,
       &temperature);
```

Nilai kembalian `fscanf` harus diperiksa. Untuk dua nilai `double`, pembacaan dianggap berhasil jika nilai kembalian sama dengan dua.

### Membaca seluruh isi berkas dengan loop

Pola yang umum adalah menggunakan nilai kembalian `fscanf` sebagai kondisi pengulangan. Dengan demikian, loop hanya berjalan ketika semua kolom yang diharapkan berhasil dibaca.

```c
#include <stdio.h>

int main(void)
{
    FILE *fp =
        fopen("temperature.txt", "r");

    if (fp == NULL)
    {
        printf("Failed to open input file.\n");
        return 1;
    }

    double time;
    double temperature;

    while (fscanf(fp,
                  "%lf %lf",
                  &time,
                  &temperature) == 2)
    {
        printf("t = %.2f s, T = %.2f C\n",
               time,
               temperature);
    }

    fclose(fp);

    return 0;
}
```

Pola tersebut lebih aman daripada menggunakan `feof` sebagai kondisi utama pembacaan. Kita memproses data hanya setelah operasi baca benar-benar berhasil.

### Mengapa `while (!feof(fp))` sering salah?

Kesalahan umum pada pemula adalah menggunakan indikator EOF sebagai syarat utama loop. Bentuk yang sering dijumpai adalah sebagai berikut.

```c
while (!feof(fp))
{
    fscanf(fp,
           "%lf %lf",
           &time,
           &temperature);

    /* process data */
}
```

Masalahnya adalah indikator EOF baru aktif setelah percobaan membaca melewati akhir berkas. Akibatnya, data lama dapat diproses lagi atau variabel dapat digunakan setelah pembacaan gagal.

Pola yang lebih baik adalah menjadikan keberhasilan operasi baca sebagai kondisi. Untuk dua nilai `double`, bentuk loop yang dianjurkan ditunjukkan berikut ini.

```c
while (fscanf(fp,
              "%lf %lf",
              &time,
              &temperature) == 2)
{
    /* process valid data */
}
```

Dengan cara tersebut, setiap iterasi selalu memiliki data baru yang valid. Logika program juga menjadi lebih mudah ditelusuri.

### Membaca baris teks dengan `fgets`

`fscanf` cocok untuk format yang sangat teratur. Jika kita ingin memeriksa satu baris lengkap terlebih dahulu, `fgets` sering lebih fleksibel.

```c
char line[256];

while (fgets(line,
             sizeof(line),
             fp) != NULL)
{
    printf("%s", line);
}
```

Setiap iterasi membaca paling banyak satu baris sesuai kapasitas buffer. Setelah itu, isi `line` dapat diperiksa atau diuraikan lebih lanjut.

Pola `fgets` sangat berguna untuk berkas CSV karena satu baris dapat dibaca terlebih dahulu. Parsing kemudian dapat dilakukan dengan `sscanf` atau pendekatan lain.

## Format CSV sederhana

CSV merupakan singkatan dari *comma-separated values*. Format ini menyimpan data tabular sebagai teks dengan pemisah tertentu, biasanya koma.

Setiap baris dapat dibaca ke buffer karakter sebelum diproses. Contoh sederhananya ditunjukkan berikut ini.

```text
time,voltage,current
0.0,5.02,0.21
1.0,5.01,0.22
2.0,4.98,0.24
```

Baris pertama sering digunakan sebagai *header*. Baris berikutnya berisi data numerik yang dapat dipetakan ke anggota `struct`.

CSV yang digunakan di dunia nyata dapat memiliki aturan lebih rumit, misalnya teks yang mengandung koma atau tanda kutip. Pada kuliah ini kita membatasi diri pada CSV sederhana tanpa koma di dalam data teks.

### Menulis CSV dengan `fprintf`

Menulis CSV dapat dilakukan dengan `fprintf`. Kita hanya perlu memastikan urutan kolom dan tanda koma konsisten.

```c
#include <stdio.h>

int main(void)
{
    FILE *fp =
        fopen("electrical.csv", "w");

    if (fp == NULL)
    {
        printf("Failed to open output file.\n");
        return 1;
    }

    fprintf(fp,
            "time,voltage,current\n");

    for (int i = 0; i < 5; i++)
    {
        double time = i * 0.5;
        double voltage = 5.0 - 0.02 * i;
        double current = 0.20 + 0.01 * i;

        fprintf(fp,
                "%.2f,%.3f,%.3f\n",
                time,
                voltage,
                current);
    }

    fclose(fp);

    return 0;
}
```

Program tersebut menghasilkan tiga kolom data. Formatnya dapat dibaca kembali oleh program C atau dibuka menggunakan perangkat lunak pengolah data lain.

### Membaca CSV sederhana dengan `fscanf`

Untuk CSV yang hanya berisi angka dan memiliki struktur tetap, `fscanf` dapat digunakan langsung. Tanda koma dituliskan sebagai bagian dari format.

```c
double time;
double voltage;
double current;

while (fscanf(fp,
              "%lf,%lf,%lf",
              &time,
              &voltage,
              &current) == 3)
{
    /* process one record */
}
```

Pendekatan ini sederhana, tetapi tidak langsung menangani *header*. Jika berkas memiliki baris judul, kita perlu melewatinya terlebih dahulu.

### Melewati *header* dengan `fgets`

Cara praktis adalah membaca baris pertama menggunakan `fgets`. Setelah *header* dilewati, data berikutnya dapat dibaca dengan pendekatan yang sesuai.

```c
char header[256];

if (fgets(header,
          sizeof(header),
          fp) == NULL)
{
    printf("File is empty.\n");
    fclose(fp);
    return 1;
}
```

Setelah itu, program dapat melanjutkan membaca data. Pemeriksaan `NULL` tetap diperlukan karena berkas mungkin kosong.

### Parsing CSV dengan `fgets` dan `sscanf`

Pendekatan yang lebih fleksibel adalah membaca satu baris penuh menggunakan `fgets`, lalu menguraikannya dengan `sscanf`. Dengan cara ini, kita dapat memeriksa setiap baris secara terpisah.

```c
char line[256];

while (fgets(line,
             sizeof(line),
             fp) != NULL)
{
    double time;
    double voltage;
    double current;

    int matched =
        sscanf(line,
               "%lf,%lf,%lf",
               &time,
               &voltage,
               &current);

    if (matched != 3)
    {
        printf("Invalid line: %s", line);
        continue;
    }

    printf("%.2f %.3f %.3f\n",
           time,
           voltage,
           current);
}
```

Pola ini memisahkan proses membaca baris dan proses parsing. Jika satu baris tidak sesuai format, program dapat menolaknya tanpa langsung kehilangan kendali atas aliran input.

### CSV dan `struct`

Setiap baris CSV dapat dipetakan ke satu objek `struct`. Pendekatan ini membuat representasi data dalam berkas konsisten dengan representasi data di memori.

Untuk contoh data listrik, kita menggunakan kembali tipe `ElectricalMeasurement`. Definisi tipenya adalah sebagai berikut.

```c
typedef struct
{
    double time;
    double voltage;
    double current;
} ElectricalMeasurement;
```

Setelah tipe disiapkan, satu baris dapat dipetakan langsung ke anggota `struct`. Proses parsing-nya dapat ditulis seperti berikut.

```c
ElectricalMeasurement m;

int matched =
    sscanf(line,
           "%lf,%lf,%lf",
           &m.time,
           &m.voltage,
           &m.current);
```

Jika `matched == 3`, semua kolom berhasil dibaca. Objek `m` kemudian dapat disimpan ke dalam larik atau langsung diproses.

### Membaca CSV ke larik `struct`

Misalkan kita menyediakan kapasitas maksimum 1000 rekaman. Program perlu memastikan jumlah data tidak melampaui kapasitas tersebut.

```c
#include <stdio.h>

#define MAX_DATA 1000

typedef struct
{
    double time;
    double voltage;
    double current;
} ElectricalMeasurement;

int main(void)
{
    FILE *fp =
        fopen("electrical.csv", "r");

    if (fp == NULL)
    {
        printf("Failed to open file.\n");
        return 1;
    }

    ElectricalMeasurement data[MAX_DATA];
    int n = 0;

    char line[256];

    if (fgets(line,
              sizeof(line),
              fp) == NULL)
    {
        printf("File is empty.\n");
        fclose(fp);
        return 1;
    }

    while (fgets(line,
                 sizeof(line),
                 fp) != NULL)
    {
        ElectricalMeasurement m;

        int matched =
            sscanf(line,
                   "%lf,%lf,%lf",
                   &m.time,
                   &m.voltage,
                   &m.current);

        if (matched != 3)
        {
            printf("Skipping invalid line: %s",
                   line);
            continue;
        }

        if (n >= MAX_DATA)
        {
            printf("Data capacity exceeded.\n");
            break;
        }

        data[n] = m;
        n++;
    }

    fclose(fp);

    printf("Valid records = %d\n", n);

    return 0;
}
```

Program tersebut menerapkan beberapa bentuk pemeriksaan sekaligus. Baris tidak valid dilewati, sedangkan jumlah data tidak boleh melebihi kapasitas larik.

### Mengolah larik `struct`

Setelah data tersimpan, kita dapat menggunakan fungsi-fungsi analisis. Sebagai contoh, daya rata-rata dapat dihitung dari setiap pasangan tegangan dan arus.

```math
P_i
=
V_iI_i.
```

Setelah data berada di memori, fungsi analisis dapat bekerja tanpa mengetahui format berkas asalnya. Fungsi berikut menghitung rata-rata daya.

```c
double mean_power(
    const ElectricalMeasurement data[],
    int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum +=
            data[i].voltage *
            data[i].current;
    }

    return sum / n;
}
```

Fungsi tersebut hanya membaca data sehingga parameternya menggunakan `const`. Prakondisinya adalah `n > 0`.

### Menulis hasil analisis ke berkas baru

Sering kali data mentah tidak ingin ditimpa. Hasil pengolahan sebaiknya ditulis ke berkas baru agar proses dapat direproduksi dan dibandingkan.

Misalkan kita ingin membuat berkas hasil yang memuat data asli dan daya. Skema keluarannya dapat ditulis sebagai berikut.

```text
time,voltage,current,power
```

Program dapat menulis setiap rekaman beserta daya yang dihitung. Potongan implementasinya ditunjukkan berikut ini.

```c
FILE *out =
    fopen("processed.csv", "w");

if (out == NULL)
{
    printf("Failed to open output file.\n");
    return 1;
}

fprintf(out,
        "time,voltage,current,power\n");

for (int i = 0; i < n; i++)
{
    double p =
        data[i].voltage *
        data[i].current;

    fprintf(out,
            "%.3f,%.6f,%.6f,%.6f\n",
            data[i].time,
            data[i].voltage,
            data[i].current,
            p);
}

fclose(out);
```

Pola tersebut akan sangat berguna pada pertemuan integrasi C dan Python. C dapat membaca serta memproses data, sedangkan berkas hasil dapat divisualisasikan menggunakan Python.

## Pemeriksaan kesalahan pada operasi berkas

Memeriksa `fopen` merupakan langkah minimum, tetapi operasi berkas lain juga dapat gagal. Program yang lebih hati-hati dapat memeriksa hasil `fprintf`, `fclose`, atau indikator kesalahan berkas.

Sebagai contoh, `fprintf` mengembalikan nilai negatif jika terjadi kesalahan penulisan. Pemeriksaan sederhana dapat ditulis seperti berikut.

```c
if (fprintf(fp,
            "%.3f\n",
            value) < 0)
{
    printf("Write error.\n");
}
```

Fungsi `ferror` juga dapat digunakan untuk mengetahui apakah indikator kesalahan pada aliran berkas aktif. Bentuk sederhananya ditunjukkan berikut ini.

```c
if (ferror(fp))
{
    printf("File operation error.\n");
}
```

Untuk pengantar, kita tidak perlu menangani semua kemungkinan kegagalan secara mendalam. Namun, mahasiswa perlu memahami bahwa operasi I/O dapat gagal dan tidak boleh selalu diasumsikan berhasil.

### Menggunakan `perror`

Pustaka standar menyediakan `perror` untuk menampilkan pesan yang berkaitan dengan kesalahan sistem terakhir. Fungsi ini sering berguna setelah `fopen` gagal.

```c
FILE *fp =
    fopen("data.csv", "r");

if (fp == NULL)
{
    perror("data.csv");
    return 1;
}
```

Pesan yang muncul bergantung pada sistem operasi dan penyebab kegagalan. Pendekatan ini biasanya lebih informatif daripada hanya menulis `"Failed to open file"`.

### Memeriksa hasil `fclose`

`fclose` mengembalikan nol jika berhasil dan nilai nonnol jika terjadi kesalahan. Untuk berkas keluaran yang penting, hasil penutupan dapat diperiksa.

```c
if (fclose(fp) != 0)
{
    printf("Failed to close file correctly.\n");
    return 1;
}
```

Pemeriksaan ini terutama relevan pada operasi penulisan. Data yang tampak sudah dikirim ke pustaka belum tentu seluruhnya berhasil ditulis ke perangkat penyimpanan sebelum aliran ditutup.

## Fungsi untuk membuka berkas?

Kita dapat membungkus beberapa operasi berkas dalam fungsi agar program lebih modular. Namun, desain fungsi harus tetap memperjelas siapa yang bertanggung jawab menutup berkas.

Sebagai alternatif yang sederhana, fungsi analisis dapat menerima nama berkas dan mengelola seluruh siklus `open -> check -> read -> close` sendiri. Pendekatan ini membuat kepemilikan sumber daya lebih jelas.

Sebagai contoh, kita dapat merancang fungsi yang menerima nama berkas dan kapasitas larik. Bentuk prototipenya dapat ditulis sebagai berikut.

```c
int load_measurements(
    const char filename[],
    ElectricalMeasurement data[],
    int max_data);
```

Fungsi dapat mengembalikan jumlah data yang berhasil dibaca atau nilai negatif jika terjadi galat. Program utama kemudian hanya perlu memeriksa hasilnya.

## Fungsi membaca CSV ke larik `struct`

Berikut contoh fungsi yang mengelola pembukaan, pembacaan, dan penutupan berkas. Fungsi ini juga melewati *header* dan menolak baris yang tidak sesuai format.

```c
int load_measurements(
    const char filename[],
    ElectricalMeasurement data[],
    int max_data)
{
    FILE *fp =
        fopen(filename, "r");

    if (fp == NULL)
    {
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

    while (n < max_data &&
           fgets(line,
                 sizeof(line),
                 fp) != NULL)
    {
        ElectricalMeasurement m;

        int matched =
            sscanf(line,
                   "%lf,%lf,%lf",
                   &m.time,
                   &m.voltage,
                   &m.current);

        if (matched != 3)
        {
            continue;
        }

        data[n] = m;
        n++;
    }

    fclose(fp);

    return n;
}
```

Fungsi tersebut mengembalikan `-1` jika berkas gagal dibuka. Nilai nol dapat berarti berkas tidak memiliki data valid, sedangkan nilai positif menyatakan jumlah rekaman yang berhasil dimuat.

## Modularisasi I/O dan analisis

Salah satu keuntungan modularisasi adalah pemisahan antara lapisan I/O dan lapisan perhitungan. Fungsi pembacaan bertanggung jawab mengubah teks menjadi data terstruktur, sedangkan fungsi analisis bekerja pada larik `struct`.

Pemisahan fungsi membuat alur program dapat dilihat sebagai beberapa tahap yang jelas. Struktur program dapat dibayangkan sebagai berikut.

```text
input file
    ↓
load_measurements()
    ↓
array of struct
    ↓
analysis functions
    ↓
results
    ↓
output file
```

Pemisahan tersebut membuat fungsi analisis dapat diuji tanpa selalu membaca berkas. Kita dapat membuat larik uji secara langsung dan mengirimkannya ke fungsi analisis.

### Contoh sederhana: data gerak dari berkas CSV

Misalkan eksperimen gerak menghasilkan data waktu dan posisi dalam sebuah CSV. Isi sederhananya dapat berbentuk seperti berikut.

```text
time,position
0.0,0.0
0.5,1.2
1.0,2.5
1.5,3.9
2.0,5.4
```

Kita ingin membaca data tersebut dan memperkirakan kecepatan rata-rata pada setiap interval. Data dapat direpresentasikan menggunakan tipe berikut.

```c
typedef struct
{
    double time;
    double position;
} MotionSample;
```

Kecepatan rata-rata pada satu interval diperoleh dari perubahan posisi dibagi perubahan waktu. Untuk interval ke-$i$, hubungan yang digunakan adalah sebagai berikut.

```math
v_i
=
\frac{
x_{i+1}-x_i
}{
t_{i+1}-t_i
}.
```

Jika dua waktu berurutan sama, pembagian tidak boleh dilakukan. Karena itu, data juga harus diperiksa sebelum digunakan dalam perhitungan.

#### Fungsi kecepatan interval

```c
int interval_velocity(
    const MotionSample *a,
    const MotionSample *b,
    double *velocity)
{
    double dt =
        b->time - a->time;

    if (dt <= 0.0)
    {
        return 0;
    }

    *velocity =
        (b->position - a->position)
        / dt;

    return 1;
}
```

Fungsi mengembalikan `1` jika perhitungan valid dan `0` jika selang waktu tidak sesuai. Nilai kecepatan dikirim kembali melalui parameter *pointer*.

### Contoh sederhana: data intensitas cahaya

Misalkan fotodetektor menghasilkan CSV dengan kolom waktu dan intensitas. Kita ingin mencari intensitas maksimum serta waktu ketika nilai tersebut muncul.

Untuk menyimpan waktu dan intensitas secara berpasangan, kita dapat membuat satu tipe rekaman. Definisi tipenya dapat ditulis sebagai berikut.

```c
typedef struct
{
    double time;
    double intensity;
} LightSample;
```

Setelah data dibaca ke larik `LightSample`, pencarian maksimum dapat dilakukan dengan pola minimum-maksimum yang sudah dikenal. Perbedaannya adalah kita menyimpan seluruh objek yang berkaitan dengan nilai maksimum.

```c
LightSample maximum_sample =
    data[0];

for (int i = 1; i < n; i++)
{
    if (data[i].intensity >
        maximum_sample.intensity)
    {
        maximum_sample = data[i];
    }
}
```

Setelah pengulangan selesai, kita memperoleh intensitas maksimum dan waktu kejadiannya sekaligus. Inilah salah satu keuntungan menyimpan data sebagai rekaman terstruktur.

### Studi kasus terpadu: pengolahan data listrik dari CSV

Sekarang kita gabungkan `struct`, larik `struct`, pengolahan CSV, fungsi, pemeriksaan galat, dan penulisan hasil. Kasus yang digunakan adalah data tegangan dan arus yang diukur pada beberapa waktu.

Berkas masukan memiliki tiga kolom dan satu baris header. Contoh isinya dapat ditulis sebagai berikut.

```text
time,voltage,current
0.0,5.02,0.21
0.5,5.01,0.22
1.0,4.98,0.24
1.5,4.95,0.25
2.0,4.93,0.26
```

Kita ingin membaca data, menghitung daya setiap pengukuran, mencari daya maksimum, menghitung daya rata-rata, lalu menulis berkas hasil. Program juga harus menolak baris yang tidak sesuai format.

#### Struktur data

```c
typedef struct
{
    double time;
    double voltage;
    double current;
} ElectricalMeasurement;
```

Struktur tersebut sesuai langsung dengan tiga kolom pada berkas masukan. Setiap baris yang valid akan menjadi satu elemen larik `ElectricalMeasurement`.

#### Fungsi membaca data

```c
int load_measurements(
    const char filename[],
    ElectricalMeasurement data[],
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

    while (n < max_data &&
           fgets(line,
                 sizeof(line),
                 fp) != NULL)
    {
        ElectricalMeasurement m;

        int matched =
            sscanf(line,
                   "%lf,%lf,%lf",
                   &m.time,
                   &m.voltage,
                   &m.current);

        if (matched != 3)
        {
            printf("Skipping invalid line: %s",
                   line);
            continue;
        }

        data[n] = m;
        n++;
    }

    fclose(fp);

    return n;
}
```

Fungsi mengembalikan jumlah rekaman valid atau `-1` jika berkas tidak dapat dibuka. Pendekatan ini membuat `main` tidak perlu mengetahui detail parsing baris.

#### Fungsi daya

```c
double power(
    const ElectricalMeasurement *m)
{
    return
        m->voltage * m->current;
}
```

Fungsi hanya membaca satu objek sehingga parameter menggunakan `const`. Hubungan matematis yang dipakai adalah sebagai berikut.

```math
P=VI.
```

#### Fungsi daya rata-rata

```c
double mean_power(
    const ElectricalMeasurement data[],
    int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
    {
        sum += power(&data[i]);
    }

    return sum / n;
}
```

Fungsi tersebut menggunakan fungsi `power` untuk setiap elemen larik. Pendekatan ini memperlihatkan penggunaan ulang kode di dalam fungsi lain.

#### Fungsi mencari daya maksimum

```c
int index_max_power(
    const ElectricalMeasurement data[],
    int n)
{
    int index = 0;

    for (int i = 1; i < n; i++)
    {
        if (power(&data[i]) >
            power(&data[index]))
        {
            index = i;
        }
    }

    return index;
}
```

Fungsi mengembalikan indeks elemen dengan daya terbesar. Dengan menyimpan indeks, kita dapat memperoleh waktu, tegangan, arus, dan daya dari rekaman yang sama.

#### Fungsi menulis hasil

```c
int save_results(
    const char filename[],
    const ElectricalMeasurement data[],
    int n)
{
    FILE *fp =
        fopen(filename, "w");

    if (fp == NULL)
    {
        perror(filename);
        return 0;
    }

    if (fprintf(fp,
                "time,voltage,current,power\n")
        < 0)
    {
        fclose(fp);
        return 0;
    }

    for (int i = 0; i < n; i++)
    {
        double p =
            power(&data[i]);

        if (fprintf(fp,
                    "%.3f,%.6f,%.6f,%.6f\n",
                    data[i].time,
                    data[i].voltage,
                    data[i].current,
                    p) < 0)
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

Fungsi mengembalikan `1` jika proses selesai tanpa kesalahan yang terdeteksi. Nilai `0` digunakan untuk menandai kegagalan penulisan atau penutupan berkas.

#### Program utama

```c
#include <stdio.h>

#define MAX_DATA 1000

typedef struct
{
    double time;
    double voltage;
    double current;
} ElectricalMeasurement;

int load_measurements(
    const char filename[],
    ElectricalMeasurement data[],
    int max_data);

double power(
    const ElectricalMeasurement *m);

double mean_power(
    const ElectricalMeasurement data[],
    int n);

int index_max_power(
    const ElectricalMeasurement data[],
    int n);

int save_results(
    const char filename[],
    const ElectricalMeasurement data[],
    int n);

int main(void)
{
    ElectricalMeasurement data[MAX_DATA];

    int n =
        load_measurements(
            "electrical.csv",
            data,
            MAX_DATA);

    if (n < 0)
    {
        return 1;
    }

    if (n == 0)
    {
        printf("No valid data.\n");
        return 1;
    }

    double mean =
        mean_power(data, n);

    int i_max =
        index_max_power(data, n);

    printf("Valid records = %d\n", n);
    printf("Mean power    = %.6f W\n",
           mean);

    printf("Maximum power = %.6f W\n",
           power(&data[i_max]));

    printf("Time at max   = %.3f s\n",
           data[i_max].time);

    if (!save_results(
            "processed.csv",
            data,
            n))
    {
        printf("Failed to save results.\n");
        return 1;
    }

    return 0;
}
```

Program utama hanya mengatur alur kerja. Detail membaca, menghitung, mencari, dan menulis hasil ditempatkan pada fungsi-fungsi terpisah.

Jika fungsi-fungsi tersebut digabungkan, program membentuk sebuah pipeline data sederhana. Alur program dapat diringkas menjadi berikut.

```text
electrical.csv
      ↓
load_measurements()
      ↓
array of ElectricalMeasurement
      ↓
analysis
      ↓
processed.csv
```

Pola seperti ini akan digunakan kembali pada studi kasus integratif berikutnya. Struktur program yang modular membuat setiap tahap lebih mudah diperiksa dan diuji.

## Pemeriksaan kewajaran hasil

Operasi berkas yang berhasil belum menjamin isi data benar secara fisika. Kita tetap perlu memeriksa satuan, rentang nilai, dan hubungan antarbesaran.

Sebagai pemeriksaan orde besaran, kita dapat memperkirakan hasil secara manual. Misalkan tegangannya berada di sekitar nilai berikut.

```math
5\text{ V}
```

Untuk arus, misalkan skala pengukurannya berada di sekitar nilai berikut. Besaran ini kemudian dikalikan dengan tegangan untuk memperkirakan daya.

```math
0.2\text{ A},
```

Dengan skala tegangan dan arus tersebut, daya tidak seharusnya jauh dari satu watt. Orde besarnya dapat dituliskan sebagai berikut.

```math
1\text{ W}.
```

Jika program menghasilkan ratusan watt, kita harus memeriksa format data, satuan, atau algoritma. Pemeriksaan orde besaran tetap penting meskipun parsing berkas berhasil.

### Validasi data setelah parsing

Keberhasilan `sscanf` hanya menunjukkan bahwa teks dapat dikonversi menjadi angka. Hal tersebut tidak menjamin bahwa angka tersebut masuk akal secara fisik.

Validasi fisik dapat dilakukan setelah nilai berhasil diparsing. Misalkan tegangan dalam eksperimen seharusnya berada pada rentang berikut.

```math
0
\leq V
\leq
20\text{ V}.
```

Program dapat menolak nilai di luar rentang setelah parsing. Dengan demikian, validasi sintaks dan validasi fisik dilakukan sebagai dua tahap berbeda.

```c
if (m.voltage < 0.0 ||
    m.voltage > 20.0)
{
    printf("Invalid voltage.\n");
    continue;
}
```

Pemisahan tersebut merupakan kebiasaan yang baik dalam pemrosesan data. Data pertama-tama harus dapat dibaca, kemudian harus diperiksa apakah masuk akal.

### Skema berkas

Sebelum menulis program pembaca, kita harus mengetahui skema atau struktur berkas. Skema sederhana mencakup urutan kolom, tipe data, satuan, dan keberadaan *header*.

Nama kolom dapat sekaligus menyimpan informasi satuan. Sebagai contoh, skema berikut cukup informatif.

```text
time_s,voltage_V,current_A
```

Skema dengan satuan tersebut lebih informatif daripada nama kolom yang terlalu umum. Contoh bentuk yang kurang informatif adalah sebagai berikut.

```text
time,voltage,current
```

karena satuan terlihat langsung pada nama kolom. Pemilihan skema yang jelas mengurangi kemungkinan kesalahan interpretasi data.

### Format numerik dan presisi

Ketika menulis data ke berkas, jumlah digit yang ditampilkan harus disesuaikan dengan kebutuhan. Format `%.3f`, misalnya, membatasi tampilan menjadi tiga digit setelah titik desimal.

Pembatasan digit dapat mengurangi ukuran berkas dan meningkatkan keterbacaan. Namun, terlalu sedikit digit juga dapat membuang informasi numerik yang masih diperlukan untuk analisis.

Untuk data komputasi yang akan diproses kembali, gunakan presisi yang memadai. Untuk `double`, format seperti `%.15g` dapat berguna jika kita ingin mempertahankan lebih banyak digit signifikan.

### Mode tambah `"a"`

Mode `"a"` digunakan ketika data baru ingin ditambahkan ke akhir berkas yang sudah ada. Mode ini cocok untuk pencatatan sederhana yang berlangsung beberapa kali.

Fungsi `fputs` dapat digunakan ketika teks yang akan ditulis sudah lengkap dan tidak membutuhkan format numerik. Contoh penggunaannya ditunjukkan berikut ini.

```c
FILE *fp =
    fopen("log.txt", "a");
```

Jika berkas belum ada, implementasi standar akan membuat berkas baru untuk mode ini. Jika berkas sudah ada, penulisan dilakukan pada bagian akhir tanpa menghapus isi sebelumnya.

### Contoh log pengukuran

```c
FILE *fp =
    fopen("log.txt", "a");

if (fp == NULL)
{
    perror("log.txt");
    return 1;
}

fprintf(fp,
        "%.3f %.3f\n",
        time,
        value);

fclose(fp);
```

Pola ini berguna untuk menyimpan catatan pengukuran bertahap. Namun, program tetap harus menjaga konsistensi format setiap baris.

## Membaca dan menulis teks biasa

Tidak semua berkas harus berisi angka. Kita dapat menggunakan `fgets`, `fputs`, atau `fprintf` untuk bekerja dengan teks.

Metadata sederhana juga dapat ditulis menggunakan fungsi format. Contoh penulisan keterangan eksperimen ditunjukkan berikut ini.

```c
FILE *fp =
    fopen("info.txt", "w");

if (fp == NULL)
{
    return 1;
}

fprintf(fp,
        "Experiment: Pendulum\n");

fprintf(fp,
        "Operator: Student A\n");

fclose(fp);
```

Berkas teks semacam ini dapat digunakan sebagai metadata sederhana. Pada sistem yang lebih besar, metadata dan data numerik dapat dipisahkan atau digabung dalam format yang lebih terstruktur.

### Fungsi `fputs`

`fputs` menulis satu *string* ke aliran berkas. Fungsi ini sesuai ketika kita sudah memiliki teks lengkap yang tidak memerlukan format numerik.

```c
fputs("Measurement started\n",
      fp);
```

Berbeda dari beberapa fungsi lain, `fputs` tidak otomatis menambahkan karakter baris baru. Jika diperlukan, `'\n'` harus dituliskan sendiri.

### Membaca teks dengan `fgets`

`fgets` dapat digunakan untuk membaca metadata atau baris komentar. Fungsi ini membaca karakter sampai baris berakhir, kapasitas habis, atau akhir berkas tercapai.

Fungsi `fputs` dapat digunakan ketika teks yang akan ditulis sudah lengkap dan tidak membutuhkan format numerik. Contoh penggunaannya ditunjukkan berikut ini.

```c
char line[256];

while (fgets(line,
             sizeof(line),
             fp) != NULL)
{
    printf("%s", line);
}
```

Pola ini juga menjadi fondasi untuk parser teks yang lebih kompleks. Kita dapat memeriksa awalan baris, memisahkan token, atau meneruskan isi baris ke `sscanf`.

## Kesalahan umum dalam penggunaan `struct`

### Menggunakan anggota yang salah

Ketika `struct` memiliki banyak anggota dengan tipe sama, kesalahan nama anggota mungkin tetap dapat dikompilasi. Karena itu, nama anggota harus jelas dan pemeriksaan hasil tetap diperlukan.

Contoh `time`, `voltage`, dan `current` lebih informatif daripada nama umum seperti `a`, `b`, dan `c`. Penamaan yang baik membantu mengurangi kesalahan semantik.

### Tidak menginisialisasi semua anggota

Objek lokal yang belum diinisialisasi dapat berisi nilai yang tidak dapat diandalkan. Jika hanya sebagian anggota diisi, bagian lain harus diperlakukan dengan hati-hati.

Untuk data pengukuran, sebaiknya setiap rekaman hanya dianggap valid setelah seluruh anggota wajib berhasil dibaca. Pola ini sangat relevan ketika parsing CSV.

## Kesalahan umum dalam operasi berkas

### Tidak memeriksa `fopen`

Menggunakan `FILE *` yang bernilai `NULL` dapat menyebabkan program gagal. Karena itu, pemeriksaan harus dilakukan segera setelah `fopen`.

### Menggunakan mode yang salah

Membuka berkas penting dengan `"w"` dapat menghapus isi lama. Sebelum menulis, pastikan apakah tujuan program memang membuat ulang berkas atau hanya menambahkan data.

### Lupa menutup berkas

Berkas yang sudah selesai digunakan harus ditutup. Kebiasaan ini mengurangi kebocoran sumber daya dan memastikan operasi penulisan diselesaikan.

### Mengabaikan hasil pembacaan

Jangan menganggap `fscanf` atau `sscanf` selalu berhasil. Jumlah item yang berhasil dikonversi harus dibandingkan dengan jumlah kolom yang diharapkan.

### Menggunakan `while (!feof(fp))`

Pola tersebut sering menyebabkan satu iterasi tambahan setelah pembacaan terakhir gagal. Gunakan keberhasilan operasi baca sebagai kondisi pengulangan.

### Tidak memeriksa kapasitas larik

Ketika data dibaca dari berkas ke larik, jumlah rekaman dapat melebihi kapasitas. Program harus berhenti, menolak data tambahan, atau menggunakan strategi lain yang dirancang dengan jelas.

## Kebiasaan pemrograman yang baik

Gunakan satu representasi data yang konsisten antara memori dan berkas. Jika satu baris CSV merepresentasikan satu pengukuran, satu `struct` sebaiknya juga merepresentasikan satu pengukuran.

Dokumentasikan urutan kolom dan satuan. Nama seperti `time_s` dan `voltage_V` dapat mengurangi ambiguitas ketika berkas dibaca kembali beberapa minggu kemudian.

Pisahkan operasi I/O dari perhitungan sejauh masuk akal. Fungsi pembacaan sebaiknya bertanggung jawab pada parsing, sedangkan fungsi analisis bertanggung jawab pada model dan algoritma.

Periksa semua kondisi yang secara realistis dapat gagal. Sekurang-kurangnya, periksa `fopen`, hasil parsing, kapasitas penyimpanan, dan jumlah data sebelum melakukan pembagian.

Disiplin alur I/O lebih penting daripada menghafal banyak fungsi sekaligus. Pertahankan pola berikut secara konsisten.

```text
open
  ↓
check
  ↓
read / write
  ↓
close
```

secara konsisten. Pola yang sederhana tetapi disiplin ini mencegah banyak kesalahan I/O dasar.

## Cek pemahaman

Cobalah menjawab pertanyaan berikut tanpa melihat kembali catatan. Pertanyaan-pertanyaan ini memeriksa hubungan antara struktur data, berkas, dan pengolahan data.

- Apa tujuan utama `struct` dalam C?
- Apa perbedaan satu `struct` dengan larik dari `struct`?
- Apa fungsi operator `.` pada `struct`?
- Apa fungsi operator `->` ketika bekerja dengan *pointer* ke `struct`?
- Mengapa `typedef struct` sering digunakan?
- Bagaimana satu baris data pengukuran dapat dipetakan ke satu objek `struct`?
- Mengapa anggota *string* pada `struct` tetap memerlukan null terminator?
- Apa fungsi `FILE *`?
- Apa arti mode `"r"`, `"w"`, dan `"a"`?
- Mengapa hasil `fopen` harus dibandingkan dengan `NULL`?
- Apa tujuan `fclose`?
- Apa perbedaan `printf` dan `fprintf`?
- Apa perbedaan `scanf` dan `fscanf`?
- Mengapa nilai kembalian `fscanf` perlu diperiksa?
- Mengapa `while (!feof(fp))` bukan pola pembacaan yang baik?
- Kapan `fgets` lebih sesuai daripada `fscanf`?
- Apa fungsi `sscanf` dalam parsing CSV?
- Bagaimana cara melewati *header* CSV?
- Mengapa kapasitas larik harus diperiksa ketika membaca data dari berkas?
- Apa perbedaan validasi format dan validasi fisik?
- Mengapa hasil analisis sebaiknya ditulis ke berkas baru daripada selalu menimpa data mentah?
- Apa manfaat memisahkan fungsi pembacaan, analisis, dan penulisan?
- Mengapa skema dan satuan kolom perlu didokumentasikan?
- Apa makna pola `open -> check -> read/write -> close`?

## Latihan

### 1. `struct` untuk gerak lurus

Buat `struct` bernama `MotionSample` yang memiliki anggota waktu, posisi, dan kecepatan. Buat larik berisi sekurang-kurangnya lima sampel lalu tampilkan seluruh rekaman dalam bentuk tabel.

Tambahkan fungsi yang menerima satu `MotionSample` dan menghitung energi kinetik jika massa benda diberikan sebagai parameter tambahan. Gunakan data sederhana agar hasil dapat diperiksa secara manual.

### 2. Larik `struct` untuk eksperimen kalor

Buat tipe `ThermalSample` yang menyimpan waktu dan temperatur. Bacalah $N$ data ke larik `struct`, kemudian cari temperatur minimum, maksimum, dan waktu ketika temperatur maksimum terjadi.

Gunakan fungsi terpisah untuk analisis tersebut. Program harus menolak `N <= 0` dan tidak boleh mengakses larik di luar batas.

### 3. Menulis data pegas ke berkas

Pada latihan ini, gunakan Hukum Hooke sebagai model fisika sederhana. Hubungan gaya dan perpindahan dituliskan pada persamaan berikut.

```math
F=-kx
```

dengan nilai $k$ yang dibaca dari pengguna. Buat tabel untuk beberapa nilai $x$ lalu tulis hasil ke berkas `spring.csv` dengan kolom `x_m,force_N`.

Program harus memeriksa keberhasilan `fopen` dan `fclose`. Buka berkas hasil secara manual dan periksa apakah formatnya sesuai dengan skema yang dirancang.

### 4. Membaca data posisi dari CSV

Buat program yang membaca `motion.csv` dengan kolom `time,position`. Simpan data valid ke larik `MotionSample`, lalu hitung kecepatan rata-rata pada setiap interval.

Program harus menolak baris dengan format salah dan selang waktu yang tidak positif. Tulis hasil ke `velocity.csv` dengan kolom `time_start,time_end,velocity`.

### 5. Data rangkaian listrik

Buat program yang membaca berkas CSV dengan kolom `time,voltage,current`. Gunakan `struct` untuk setiap rekaman dan hitung daya dari $P=VI$. Energi kemudian didekati dengan hubungan diskrit berikut.

```math
E
\approx
\sum_i P_i\Delta t_i.
```

Gunakan selang waktu dari data, bukan nilai `dt` yang diasumsikan tetap. Program harus memeriksa bahwa waktu bertambah secara monoton sebelum melakukan akumulasi energi.

### 6. Intensitas cahaya dan nilai maksimum

Buat berkas CSV sederhana berisi `time,intensity`. Program harus membaca seluruh data valid, mencari intensitas maksimum, dan menampilkan waktu ketika maksimum terjadi.

Tuliskan kembali data ke berkas baru dengan kolom tambahan `relative_intensity`, yang didefinisikan sebagai $I_i/I_{\max}$. Pastikan program menangani kasus ketika maksimum tidak positif.

### 7. Parser CSV sederhana dengan baris rusak

Siapkan berkas yang memiliki beberapa baris valid dan beberapa baris tidak valid. Gunakan `fgets` dan `sscanf` untuk membaca tiga kolom numerik per baris.

Program harus menghitung jumlah baris valid dan tidak valid secara terpisah. Hanya baris valid yang boleh disimpan ke larik `struct` dan digunakan pada analisis berikutnya.

### 8. Mode tambah untuk log eksperimen

Buat program yang meminta nama eksperimen dan satu nilai hasil pengukuran. Setiap kali program dijalankan, data baru ditambahkan ke `experiment.log` menggunakan mode `"a"`.

Setiap baris harus memiliki format yang konsisten. Jalankan program beberapa kali dan verifikasi bahwa data lama tidak terhapus.

### 9. Metadata dan data numerik

Buat dua berkas, yaitu `info.txt` untuk menyimpan nama eksperimen, nama operator, dan satuan, serta `data.csv` untuk menyimpan data numerik. Program harus menulis kedua berkas dan kemudian membaca kembali `info.txt` untuk menampilkan metadata.

Jelaskan keuntungan memisahkan metadata dan data numerik pada contoh ini. Diskusikan juga kelemahannya dibandingkan menyimpan seluruh informasi dalam satu format terstruktur.

### 10. Fungsi pemuatan data modular

Pisahkan proses pemuatan data ke dalam sebuah fungsi khusus. Gunakan prototipe fungsi berikut sebagai acuan.

```c
int load_data(
    const char filename[],
    Measurement data[],
    int max_data);
```

yang membuka berkas, melewati *header*, membaca data CSV, menolak baris tidak valid, menutup berkas, dan mengembalikan jumlah rekaman valid. Fungsi harus mengembalikan nilai negatif jika berkas tidak dapat dibuka.

Buat `main` yang menggunakan fungsi tersebut lalu menghitung rata-rata salah satu kolom. Pastikan bagian analisis tidak melakukan operasi `fopen` secara langsung.

### 11. Proyek mini: analisis data ayunan

Buat format CSV dengan kolom `time_s,angle_deg` untuk data sudut pendulum sederhana. Program harus membaca data, mencari sudut maksimum absolut, menghitung rata-rata sudut, dan menghitung berapa data yang memenuhi $|\theta|>10^\circ$.

Gunakan `struct`, larik `struct`, fungsi analisis, dan pemeriksaan baris CSV. Tulis ringkasan hasil ke berkas `summary.txt`.

### 12. Proyek mini: pipeline data sensor

Pada proyek mini terakhir, rancang program sebagai pipeline data sederhana. Alur minimumnya adalah sebagai berikut.

```text
raw.csv
   ↓
read + validate
   ↓
array of struct
   ↓
analysis
   ↓
processed.csv
```

Pilih salah satu konteks sederhana, misalnya tegangan, temperatur, tekanan, intensitas cahaya, atau posisi. Tentukan sendiri skema CSV, rentang data valid, besaran turunan yang dihitung, dan bentuk berkas keluaran.

Program harus memiliki sekurang-kurangnya tiga fungsi selain `main`, memeriksa kesalahan `fopen`, memeriksa hasil parsing, membatasi jumlah data sesuai kapasitas larik, dan selalu menutup berkas. Jelaskan struktur program dan alasan pembagian fungsi yang dipilih.

## Rangkuman

- `struct` digunakan untuk mengelompokkan beberapa nilai yang berkaitan menjadi satu tipe data. Anggota `struct` dapat memiliki tipe yang berbeda, termasuk angka dan larik karakter.

- Larik dari `struct` cocok untuk merepresentasikan banyak rekaman pengukuran. Setiap elemen larik merepresentasikan satu baris atau satu kejadian pengukuran.

- Operator `.` digunakan untuk mengakses anggota dari objek `struct`. Operator `->` digunakan ketika objek diakses melalui *pointer*.

- `typedef struct` membuat nama tipe lebih ringkas. Bentuk ini sangat berguna ketika tipe data digunakan berulang pada banyak fungsi.

- Data pengukuran sebaiknya memiliki representasi yang konsisten antara berkas dan memori. Satu baris CSV dapat dipetakan menjadi satu objek `struct`.

- *String* dapat menjadi anggota `struct` karena *string* dalam C merupakan larik karakter. Kapasitas dan null terminator tetap harus diperhatikan.

- Berkas dalam pustaka standar C dikelola melalui `FILE *`. Fungsi `fopen`, `fclose`, `fprintf`, `fscanf`, `fgets`, dan `fputs` merupakan beberapa alat dasar untuk operasi berkas teks.

- Pola operasi berkas yang perlu dibiasakan adalah

```math
\boxed{
\text{open}
\rightarrow
\text{check}
\rightarrow
\text{read/write}
\rightarrow
\text{close}.
}
```

- Mode `"r"` digunakan untuk membaca, `"w"` untuk menulis dari awal, dan `"a"` untuk menambahkan data pada akhir berkas. Pemilihan mode harus disesuaikan dengan tujuan program agar data lama tidak hilang secara tidak sengaja.

- Hasil `fopen` harus diperiksa terhadap `NULL`. Operasi baca dan tulis juga memiliki nilai kembalian yang dapat digunakan untuk mendeteksi kegagalan.

- `fprintf` bekerja seperti `printf`, tetapi tujuan keluarannya adalah berkas. `fscanf` bekerja seperti `scanf`, tetapi sumber masukannya adalah berkas.

- Untuk pembacaan terstruktur, kondisi loop sebaiknya didasarkan pada keberhasilan operasi baca. Pola `while (!feof(fp))` sebaiknya dihindari karena EOF baru diketahui setelah percobaan membaca melewati akhir berkas.

- `fgets` membaca satu baris lengkap dengan batas kapasitas yang jelas. Baris tersebut dapat diuraikan menggunakan `sscanf` untuk CSV sederhana.

- CSV sederhana dapat dibaca dengan memetakan setiap kolom ke anggota `struct`. Program harus memeriksa jumlah kolom yang berhasil diparsing dan menolak baris yang tidak sesuai skema.

- Validasi format berbeda dari validasi fisik. Baris yang berhasil dibaca masih dapat mengandung nilai yang tidak masuk akal untuk sistem yang sedang dianalisis.

- Pemisahan fungsi pembacaan, analisis, dan penulisan membuat program lebih modular. Fungsi analisis dapat diuji pada data di memori tanpa bergantung langsung pada berkas.

- Pada kuliah berikutnya kita akan mengintegrasikan berbagai konsep C yang telah dipelajari dalam satu studi kasus Teknik Fisika. Larik, fungsi, `struct`, berkas, validasi data, dan pemeriksaan hasil akan digunakan bersama dalam sebuah program yang lebih lengkap.
