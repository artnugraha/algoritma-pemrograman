# Kuliah 3: Dasar-dasar Pemrograman dalam Bahasa C

## Dari algoritma menuju program C

Pada dua kuliah sebelumnya kita telah membangun dua fondasi penting.

Pertama, kita melihat hubungan

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

Kedua, kita mempelajari bagaimana suatu persoalan dapat dirumuskan menjadi langkah-langkah algoritmik melalui dekomposisi, diagram alir, *pseudocode*, *tracing*, serta pemeriksaan kebenaran secara sederhana.

Pada kuliah ini kita mulai memusatkan perhatian pada bagian

```math
\boxed{
\text{algoritma}
\longrightarrow
\text{program C}.
}
```

Tujuan kita bukan sekadar menghafal sintaks. Kita ingin memahami bagaimana konsep algoritmik seperti

```text
masukan
penyimpanan nilai
perhitungan
keputusan logika
keluaran
```

direpresentasikan dalam bahasa C.

Bahasa C dipilih sebagai bahasa utama pada bagian awal mata kuliah karena beberapa alasan.

- C memiliki sintaks yang relatif kecil dan terstruktur.
- Hubungan antara program, tipe data, memori, dan representasi data cukup terlihat.
- C banyak digunakan dalam sistem tertanam, mikrokontroler, instrumentasi, sistem operasi, komputasi berperforma tinggi, dan perangkat lunak rekayasa.
- Banyak bahasa pemrograman modern menggunakan konsep sintaks yang dipengaruhi oleh C.
- C memaksa kita memahami beberapa konsep komputasi secara eksplisit, misalnya tipe data, alamat memori, dan proses kompilasi.

Bagi mahasiswa Teknik Fisika, bahasa C juga relevan karena banyak sistem akuisisi data, perangkat instrumentasi, mikrokontroler, dan sistem kendali menggunakan C atau bahasa yang sangat dekat dengan C.

### Algoritma yang sama, bahasa yang berbeda

Misalkan kita ingin menghitung energi kinetik,

```math
E_k
=
\frac{1}{2}mv^2.
```

Secara algoritmik,

```text
INPUT m
INPUT v

Ek ← 0.5 * m * v * v

OUTPUT Ek
```

Dalam C kita dapat menulis

```c
double kinetic_energy = 0.5 * mass * velocity * velocity;
```

Dalam Python, algoritma yang sama dapat ditulis

```python
kinetic_energy = 0.5 * mass * velocity**2
```

Sintaks berbeda, tetapi algoritmanya sama.

Hal ini penting karena pemrograman tidak identik dengan bahasa pemrograman tertentu. Bahasa pemrograman adalah media untuk mengekspresikan algoritma.

## Struktur dasar program C

Perhatikan program C berikut.

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, Teknik Fisika!\n");

    return 0;
}
```

Program tersebut terdiri atas beberapa bagian penting.

### Direktif `#include`

Baris

```c
#include <stdio.h>
```

meminta *preprocessor* C untuk menyertakan deklarasi dari pustaka standar input-output.

`stdio` merupakan singkatan dari

```text
standard input/output
```

sedangkan `.h` menunjukkan *header file*.

Kita memerlukan `stdio.h` ketika menggunakan fungsi seperti

```c
printf()
```

dan

```c
scanf()
```

Secara konseptual, pustaka standar menyediakan fungsi-fungsi yang telah ditulis dan diuji sehingga kita tidak perlu membuat semuanya dari awal.

### Fungsi `main`

Setiap program C yang dapat dieksekusi memiliki titik awal eksekusi.

Dalam contoh kita,

```c
int main(void)
```

menyatakan fungsi utama program.

Kata

```c
int
```

menunjukkan bahwa fungsi `main` mengembalikan sebuah nilai bertipe integer kepada lingkungan yang menjalankan program.

Bagian

```c
(void)
```

menyatakan bahwa fungsi tersebut tidak menerima argumen.

Tubuh fungsi dituliskan di antara kurung kurawal,

```c
{
    ...
}
```

Program mulai menjalankan pernyataan-pernyataan di dalam `main` dari atas menuju bawah, kecuali aliran kontrol mengubah urutannya.

### Pernyataan

Baris

```c
printf("Hello, Teknik Fisika!\n");
```

merupakan suatu **pernyataan** (*statement*).

Dalam C, banyak pernyataan diakhiri dengan titik koma,

```text
;
```

Titik koma merupakan bagian dari sintaks.

Jika kita menulis

```c
printf("Hello, Teknik Fisika!\n")
```

tanpa titik koma, *compiler* akan menghasilkan galat sintaksis.

### `return 0`

Baris

```c
return 0;
```

mengakhiri fungsi `main` dan mengembalikan nilai `0`.

Secara konvensi, nilai nol menunjukkan bahwa program selesai secara normal.

Program dapat menggunakan nilai selain nol untuk menunjukkan kondisi gagal atau kesalahan.

Kita akan menggunakan pola

```c
return 0;
```

secara konsisten untuk program-program sederhana.

## Kompilasi program

Program C tidak langsung dijalankan dari kode sumber.

Kita telah melihat alur

```math
\boxed{
\text{source code}
\longrightarrow
\text{compiler}
\longrightarrow
\text{executable}
\longrightarrow
\text{execution}.
}
```

Misalkan program disimpan sebagai

```text
hello.c
```

Kita dapat mengompilasinya menggunakan GCC.

Pada Linux atau WSL,

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 hello.c -o hello
```

Kemudian program dijalankan dengan

```bash
./hello
```

Pada Windows dengan GCC,

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 hello.c -o hello.exe
```

dan dapat dijalankan dengan

```bash
.\hello.exe
```

Opsi

```text
-Wall
-Wextra
-Wpedantic
```

meminta *compiler* menampilkan lebih banyak peringatan.

Opsi

```text
-std=c17
```

meminta GCC menggunakan standar C17.

Sepanjang mata kuliah ini, peringatan *compiler* harus diperlakukan sebagai informasi penting, bukan sebagai gangguan.

Program yang dapat dikompilasi belum tentu benar, tetapi program yang menghasilkan banyak peringatan sebaiknya diperiksa sebelum dilanjutkan.

## Komentar dalam C

Komentar digunakan untuk memberikan informasi kepada manusia yang membaca program.

Komentar tidak dieksekusi oleh komputer.

Komentar satu baris ditulis menggunakan

```c
// komentar satu baris
```

Komentar beberapa baris dapat ditulis menggunakan

```c
/*
    komentar
    beberapa baris
*/
```

Sebagai contoh,

```c
#include <stdio.h>

int main(void)
{
    // Massa dalam kilogram
    double mass = 2.0;

    // Kecepatan dalam meter per sekon
    double velocity = 3.0;

    double energy = 0.5 * mass * velocity * velocity;

    printf("Kinetic energy = %f J\n", energy);

    return 0;
}
```

Komentar sebaiknya menjelaskan sesuatu yang tidak langsung terlihat dari kode.

Komentar seperti

```c
x = x + 1;  // tambah x dengan 1
```

sering kali tidak memberikan informasi tambahan.

Sebaliknya,

```c
double velocity = 20.0;  // m/s
```

berguna karena menjelaskan satuan.

## Variabel dan nilai

Dalam program, kita sering perlu menyimpan nilai yang dapat digunakan kembali.

Tempat penyimpanan bernama disebut **variabel**.

Sebagai contoh,

```c
double mass = 2.0;
```

mendeklarasikan variabel bernama

```text
mass
```

dengan tipe

```text
double
```

dan memberikan nilai awal

```math
2.0.
```

Secara konseptual,

```text
mass
  |
  v
+-------+
|  2.0  |
+-------+
 memory
```

Nama `mass` digunakan agar kita tidak perlu memikirkan alamat memori secara langsung.

### Deklarasi

Pernyataan

```c
double mass;
```

disebut deklarasi variabel.

Deklarasi memberitahu *compiler* bahwa kita ingin menggunakan variabel bernama `mass` dengan tipe `double`.

Jika kita ingin langsung memberikan nilai awal,

```c
double mass = 2.0;
```

proses pemberian nilai awal ini disebut **inisialisasi**.

### Assignment

Setelah variabel dibuat, nilainya dapat diperbarui.

```c
mass = 3.5;
```

Operasi tersebut disebut **assignment** atau pemberian nilai.

Perhatikan bahwa simbol

```text
=
```

dalam C bukan merupakan tanda kesamaan matematika.

Dalam C,

```c
x = 5;
```

berarti

> simpan nilai 5 ke dalam variabel `x`.

Karena itu, pernyataan

```c
x = x + 1;
```

valid dalam C.

Maknanya adalah

1. ambil nilai lama `x`;
2. tambahkan satu;
3. simpan hasilnya kembali ke `x`.

Jika nilai awalnya

```math
x=4,
```

setelah

```c
x = x + 1;
```

nilai barunya adalah

```math
x=5.
```

### Variabel harus diberi nilai sebelum digunakan

Perhatikan program berikut.

```c
#include <stdio.h>

int main(void)
{
    double temperature;

    printf("%f\n", temperature);

    return 0;
}
```

Variabel `temperature` dibuat tetapi belum diberi nilai.

Menggunakan nilai variabel lokal yang belum diinisialisasi menghasilkan perilaku yang tidak dapat diandalkan.

Karena itu, biasakan memberikan nilai sebelum variabel digunakan.

```c
double temperature = 25.0;
```

Kebiasaan inisialisasi yang jelas akan mengurangi banyak kesalahan.

## Aturan penamaan variabel

Nama variabel dalam C disebut **identifier**.

Contoh identifier yang valid adalah

```text
mass
velocity
temperature
sensor_value
x0
pressure_1
```

Secara umum, identifier dapat menggunakan

- huruf;
- angka;
- garis bawah `_`.

Namun, identifier tidak boleh dimulai dengan angka.

Contoh yang tidak valid:

```text
2mass
3temperature
```

C bersifat **case-sensitive**.

Artinya,

```text
temperature
Temperature
TEMPERATURE
```

dianggap sebagai tiga nama yang berbeda.

### Gunakan nama yang bermakna

Bandingkan

```c
double a = 12.0;
double b = 2.5;
double c = a * b;
```

dengan

```c
double voltage = 12.0;
double current = 2.5;
double power = voltage * current;
```

Keduanya dapat menghasilkan nilai yang sama, tetapi program kedua jauh lebih mudah dipahami.

Untuk program teknik, nama variabel sebaiknya memberikan informasi mengenai makna fisik.

Contoh:

```c
double mass;
double velocity;
double temperature;
double resistance;
double pressure;
double time_step;
```

Jika diperlukan, satuan dapat dicantumkan dalam komentar atau bahkan nama variabel.

```c
double temperature_celsius = 25.0;
double pressure_pa = 101325.0;
```

Pendekatan tersebut sangat membantu ketika beberapa sistem satuan digunakan sekaligus.

## Tipe data dasar

Tipe data menentukan

- jenis nilai yang dapat disimpan;
- cara nilai direpresentasikan;
- operasi yang dapat dilakukan;
- jumlah memori yang biasanya digunakan.

Beberapa tipe data dasar yang penting adalah

```text
char
int
float
double
bool
```

Kita akan membahas masing-masing secara bertahap.

### `int`

Tipe

```c
int
```

digunakan untuk bilangan bulat.

Contoh:

```c
int number_of_sensors = 8;
int iteration = 0;
int sample_count = 100;
```

Bilangan seperti

```math
-5,\quad0,\quad27
```

dapat direpresentasikan menggunakan tipe integer selama masih berada dalam rentang tipe tersebut.

Ukuran `int` tidak harus sama pada semua sistem.

Untuk memeriksanya kita dapat menggunakan

```c
sizeof
```

misalnya,

```c
#include <stdio.h>

int main(void)
{
    printf("sizeof(int) = %zu byte\n", sizeof(int));

    return 0;
}
```

Pada banyak komputer modern,

```text
sizeof(int) = 4 byte
```

tetapi program sebaiknya tidak menganggap hal tersebut sebagai aturan universal tanpa alasan.

### Batas integer

Pustaka

```c
#include <limits.h>
```

menyediakan informasi seperti

```c
INT_MIN
INT_MAX
```

Contoh:

```c
#include <stdio.h>
#include <limits.h>

int main(void)
{
    printf("INT_MIN = %d\n", INT_MIN);
    printf("INT_MAX = %d\n", INT_MAX);

    return 0;
}
```

Pada banyak sistem dengan `int` 32-bit, hasilnya adalah sekitar

```math
-2^{31}
\leq x
\leq
2^{31}-1.
```

Konsep ini berkaitan langsung dengan representasi integer yang telah dibahas pada Kuliah 1.

### `float`

Tipe

```c
float
```

digunakan untuk bilangan *floating-point* dengan presisi terbatas.

Contoh:

```c
float temperature = 25.5f;
```

Huruf

```text
f
```

pada

```c
25.5f
```

menunjukkan bahwa literal tersebut bertipe `float`.

Tanpa `f`, literal seperti

```c
25.5
```

secara default bertipe `double`.

### `double`

Untuk banyak perhitungan sains dan rekayasa, kita akan lebih sering menggunakan

```c
double
```

daripada `float`.

Contoh:

```c
double pi = 3.141592653589793;
double pressure = 101325.0;
double energy = 1.23e-6;
```

`double` biasanya memiliki presisi lebih tinggi daripada `float`.

Secara umum, untuk komputasi numerik pada mata kuliah ini, `double` akan menjadi pilihan bawaan untuk besaran real kecuali ada alasan khusus menggunakan `float`.

### Presisi `float` dan `double`

Kita dapat menggunakan

```c
#include <float.h>
```

untuk melihat karakteristik tipe *floating-point*.

Contoh:

```c
#include <stdio.h>
#include <float.h>

int main(void)
{
    printf("FLT_DIG = %d\n", FLT_DIG);
    printf("DBL_DIG = %d\n", DBL_DIG);

    return 0;
}
```

`FLT_DIG` dan `DBL_DIG` memberikan gambaran jumlah digit desimal signifikan yang dapat direpresentasikan secara andal.

Pada banyak sistem,

```text
float   ≈ 6–7 digit desimal signifikan
double  ≈ 15–16 digit desimal signifikan
```

Nilai pastinya bergantung pada implementasi.

Konsep ini berkaitan dengan IEEE 754 yang dibahas sebelumnya.

### `char`

Tipe

```c
char
```

digunakan untuk menyimpan satu karakter.

Contoh:

```c
char grade = 'A';
```

Perhatikan penggunaan tanda petik tunggal,

```text
'A'
```

untuk karakter.

Sementara itu,

```text
"A"
```

menggunakan tanda petik ganda dan merepresentasikan *string*.

Kita akan membahas *string* lebih lanjut ketika mempelajari larik karakter.

Karakter pada akhirnya direpresentasikan menggunakan nilai numerik.

Karena itu, `char` juga memiliki hubungan langsung dengan representasi data yang dibahas pada Kuliah 1.

### `bool`

Secara logika, kita sering membutuhkan nilai

```text
benar
salah
```

Dalam C17, kita dapat menggunakan

```c
#include <stdbool.h>
```

dan tipe

```c
bool
```

Contoh:

```c
#include <stdbool.h>

bool sensor_active = true;
bool alarm = false;
```

Nilai Boolean yang tersedia adalah

```c
true
false
```

Tipe Boolean akan menjadi sangat penting ketika kita mempelajari percabangan dan pengulangan.

## Melihat ukuran tipe data

Kita dapat menggunakan `sizeof` untuk memeriksa jumlah byte yang digunakan suatu tipe.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    printf("char   : %zu byte\n", sizeof(char));
    printf("int    : %zu byte\n", sizeof(int));
    printf("float  : %zu byte\n", sizeof(float));
    printf("double : %zu byte\n", sizeof(double));
    printf("bool   : %zu byte\n", sizeof(bool));

    return 0;
}
```

Pada suatu sistem, keluaran mungkin terlihat seperti

```text
char   : 1 byte
int    : 4 byte
float  : 4 byte
double : 8 byte
bool   : 1 byte
```

Namun, penting untuk memahami bahwa standar C tidak menetapkan ukuran yang sama untuk semua tipe pada semua arsitektur.

Yang lebih penting adalah memahami konsep:

```math
\boxed{
\text{tipe data}
\longrightarrow
\text{representasi}
\longrightarrow
\text{rentang dan presisi}.
}
```

## Konstanta

Tidak semua nilai dalam program seharusnya berubah.

Misalkan kita menggunakan percepatan gravitasi pendekatan

```math
g=9.81\text{ m/s}^2.
```

Kita dapat menuliskannya sebagai

```c
const double gravity = 9.81;
```

Kata

```c
const
```

menyatakan bahwa nilai tersebut tidak dimaksudkan untuk diubah setelah inisialisasi.

Contoh:

```c
const double pi = 3.141592653589793;
const double gas_constant = 8.314462618;
```

Menggunakan `const` membantu mendokumentasikan maksud program.

Bandingkan

```c
double gas_constant = 8.314462618;
```

dengan

```c
const double gas_constant = 8.314462618;
```

Versi kedua menyatakan dengan lebih jelas bahwa nilai tersebut diperlakukan sebagai konstanta.

## Literal numerik

Nilai yang ditulis langsung di dalam kode disebut **literal**.

Contoh literal integer:

```c
0
10
-25
1000
```

Contoh literal *floating-point*:

```c
3.14
2.5
1.0e-6
6.022e23
```

Notasi

```c
1.0e-6
```

merepresentasikan

```math
1.0\times10^{-6}.
```

Notasi ilmiah sangat berguna untuk besaran fisika yang sangat besar atau sangat kecil.

Contoh:

```c
double planck_constant = 6.62607015e-34;
double speed_of_light = 2.99792458e8;
```

## Ekspresi aritmetika

C menyediakan beberapa operator aritmetika dasar.

| Operator | Operasi |
|---|---|
| `+` | penjumlahan |
| `-` | pengurangan |
| `*` | perkalian |
| `/` | pembagian |
| `%` | sisa pembagian integer |

Contoh:

```c
double voltage = 12.0;
double current = 2.5;

double power = voltage * current;
```

Secara matematis,

```math
P=VI.
```

### Penjumlahan dan pengurangan

```c
double final_temperature = initial_temperature + delta_temperature;
```

merepresentasikan

```math
T_f
=
T_i+\Delta T.
```

### Perkalian

Dalam matematika kita dapat menulis

```math
E_k
=
\frac12mv^2.
```

Dalam C, kita harus menuliskan operator perkalian secara eksplisit.

```c
double energy = 0.5 * mass * velocity * velocity;
```

Tidak ada perkalian implisit seperti

```text
mv
```

dalam sintaks C.

### Pangkat

C tidak mempunyai operator pangkat `^` untuk bilangan real.

Ekspresi

```c
v ^ 2
```

bukan berarti

```math
v^2.
```

Operator `^` dalam C adalah operator bitwise XOR.

Untuk kuadrat sederhana,

```math
v^2
```

lebih baik ditulis

```c
v * v
```

Untuk operasi pangkat yang lebih umum, pustaka matematika menyediakan fungsi

```c
pow()
```

melalui

```c
#include <math.h>
```

Contoh:

```c
double y = pow(x, 3.5);
```

Namun, untuk kuadrat sederhana,

```c
x * x
```

sering lebih mudah dibaca dan tidak memerlukan pemanggilan fungsi `pow`.

## Pembagian integer

Salah satu sumber kesalahan umum bagi pemula adalah pembagian integer.

Perhatikan

```c
int a = 5;
int b = 2;

int result = a / b;
```

Hasilnya adalah

```math
2,
```

bukan

```math
2.5.
```

Karena kedua operand bertipe integer, C melakukan pembagian integer.

Bagian pecahan dibuang.

```math
\frac{5}{2}
\longrightarrow
2
```

dalam konteks pembagian integer.

Jika kita ingin hasil *floating-point*,

```c
double result = 5.0 / 2.0;
```

menghasilkan

```math
2.5.
```

### Kesalahan klasik pada rata-rata

Perhatikan kode

```c
int sum = 7;
int n = 2;

double mean = sum / n;
```

Mungkin kita berharap

```math
\overline{x}=3.5.
```

Namun, operasi

```c
sum / n
```

dilakukan sebagai pembagian integer terlebih dahulu,

```math
7/2=3,
```

kemudian nilai `3` dikonversi menjadi `double`.

Hasilnya menjadi

```math
3.0.
```

Salah satu perbaikannya adalah

```c
double mean = (double)sum / n;
```

atau menggunakan `double` sejak awal,

```c
double sum = 7.0;
int n = 2;

double mean = sum / n;
```

Contoh ini menunjukkan bahwa **tipe data memengaruhi hasil perhitungan**.

## Operator modulo `%`

Operator

```c
%
```

menghasilkan sisa pembagian integer.

Contoh:

```c
int remainder = 17 % 5;
```

menghasilkan

```math
2
```

karena

```math
17=3(5)+2.
```

Operator modulo banyak digunakan untuk

- memeriksa bilangan genap atau ganjil;
- pola periodik;
- pengindeksan;
- pengolahan data diskrit.

Sebagai contoh,

```c
int n = 8;

int remainder = n % 2;
```

Jika

```text
remainder == 0
```

maka `n` genap.

## Prioritas operator

C memiliki aturan prioritas operator.

Sebagai contoh,

```c
double result = a + b * c;
```

perkalian dilakukan lebih dahulu.

Secara matematis,

```math
a+bc.
```

Jika kita ingin

```math
(a+b)c,
```

kita harus menulis

```c
double result = (a + b) * c;
```

Beberapa aturan dasar yang perlu diingat:

1. ekspresi dalam tanda kurung dievaluasi terlebih dahulu;
2. perkalian, pembagian, dan modulo memiliki prioritas lebih tinggi daripada penjumlahan dan pengurangan;
3. operator dengan prioritas sama mengikuti aturan asosiasi tertentu.

Namun, jangan terlalu bergantung pada hafalan tabel prioritas.

Jika ekspresi mulai sulit dibaca, gunakan tanda kurung.

Bandingkan

```c
double result = a + b * c / d - e;
```

dengan

```c
double result = a + (b * c / d) - e;
```

Versi kedua lebih eksplisit.

## Operator relasional

Program sering perlu membandingkan dua nilai.

C menyediakan operator relasional berikut.

| Operator | Arti |
|---|---|
| `<` | lebih kecil |
| `<=` | lebih kecil atau sama dengan |
| `>` | lebih besar |
| `>=` | lebih besar atau sama dengan |
| `==` | sama dengan |
| `!=` | tidak sama dengan |

Contoh:

```c
temperature > 30.0
```

menanyakan apakah temperatur lebih besar dari 30.

Ekspresi

```c
temperature >= 20.0
```

menanyakan apakah temperatur lebih besar atau sama dengan 20.

### Jangan tertukar antara `=` dan `==`

Ini merupakan salah satu kesalahan paling umum.

```c
x = 5;
```

berarti

> simpan nilai 5 ke `x`.

Sedangkan

```c
x == 5
```

berarti

> apakah nilai `x` sama dengan 5?

Operator pertama adalah assignment.

Operator kedua adalah operator perbandingan.

Perbedaannya sangat penting.

## Logika Boolean

Dalam matematika dan logika, kita mengenal operasi

```math
p\land q,
```

```math
p\lor q,
```

dan

```math
\neg p.
```

Dalam C, operator logikanya adalah

| Logika | C |
|---|---|
| AND | `&&` |
| OR | `||` |
| NOT | `!` |

Misalkan

```math
20\leq T\leq30.
```

Dalam C kita tidak menulis

```c
20.0 <= temperature <= 30.0
```

karena ekspresi tersebut tidak memiliki makna yang sama seperti notasi matematika.

Kita harus menulis dua kondisi dan menggabungkannya dengan AND.

```c
temperature >= 20.0 && temperature <= 30.0
```

Secara logika,

```math
(T\geq20)
\land
(T\leq30).
```

### Operator AND

Misalkan suatu sensor dianggap berada dalam rentang aman jika

```math
20\leq T\leq30.
```

Dalam C,

```c
bool safe =
    temperature >= 20.0 &&
    temperature <= 30.0;
```

Nilai `safe` akan menjadi `true` jika kedua kondisi benar.

### Operator OR

Misalkan alarm aktif jika

```math
T<10
```

atau

```math
T>50.
```

Dalam C,

```c
bool alarm =
    temperature < 10.0 ||
    temperature > 50.0;
```

### Operator NOT

Jika

```c
bool sensor_active = true;
```

maka

```c
!sensor_active
```

berarti

> sensor tidak aktif.

## Tabel kebenaran

Untuk dua nilai Boolean $p$ dan $q$, operasi AND dapat ditulis

| $p$ | $q$ | $p \land q$ |
|---|---|---|
| false | false | false |
| false | true | false |
| true | false | false |
| true | true | true |

Operasi OR:

| $p$ | $q$ | $p \lor q$ |
|---|---|---|
| false | false | false |
| false | true | true |
| true | false | true |
| true | true | true |

Operasi NOT:

| $p$ | $\neg p$ |
|---|---|
| false | true |
| true | false |

Konsep ini akan menjadi dasar utama ketika kita mempelajari percabangan pada kuliah berikutnya.

## Konversi tipe data

Dalam suatu ekspresi, kita kadang mencampur beberapa tipe data.

Contoh:

```c
int n = 4;
double sum = 10.0;

double mean = sum / n;
```

C akan melakukan konversi sehingga `n` dapat digunakan dalam operasi dengan `double`.

Konversi yang dilakukan otomatis disebut **implicit conversion**.

### Konversi eksplisit

Kita juga dapat meminta konversi secara eksplisit menggunakan **cast**.

Contoh:

```c
int sum = 7;
int n = 2;

double mean = (double)sum / n;
```

Bagian

```c
(double)sum
```

mengubah nilai `sum` menjadi `double` sebelum pembagian.

Dengan demikian,

```math
\frac{7.0}{2}
=
3.5.
```

### Konversi dapat kehilangan informasi

Perhatikan

```c
double x = 3.9;
int y = (int)x;
```

Nilai `y` menjadi

```math
3.
```

Bagian pecahan tidak disimpan.

Konversi dari tipe dengan informasi lebih banyak ke tipe dengan informasi lebih sedikit dapat kehilangan informasi.

Karena itu, cast tidak boleh digunakan hanya untuk menghilangkan peringatan *compiler* tanpa memahami konsekuensinya.

## Input dan output

Program yang hanya menggunakan nilai tetap memiliki kegunaan terbatas.

Kita ingin program dapat menerima masukan dari pengguna dan menampilkan hasil.

Pustaka

```c
#include <stdio.h>
```

menyediakan fungsi utama untuk kebutuhan awal ini:

```c
printf()
scanf()
```

### `printf`

Fungsi

```c
printf()
```

digunakan untuk menampilkan keluaran.

Contoh:

```c
printf("Hello!\n");
```

Karakter

```text
\n
```

menyatakan baris baru.

### Menampilkan integer

```c
int n = 25;

printf("n = %d\n", n);
```

`%d` digunakan untuk menampilkan nilai bertipe `int`.

Keluaran:

```text
n = 25
```

### Menampilkan bilangan real

```c
double temperature = 29.875;

printf("Temperature = %f C\n", temperature);
```

menghasilkan sesuatu seperti

```text
Temperature = 29.875000 C
```

Kita dapat mengatur jumlah digit setelah titik desimal.

```c
printf("Temperature = %.2f C\n", temperature);
```

menghasilkan

```text
Temperature = 29.88 C
```

Format

```text
%.2f
```

berarti menampilkan dua digit setelah titik desimal.

### Notasi ilmiah

Untuk nilai sangat besar atau kecil,

```c
double h = 6.62607015e-34;

printf("h = %e J s\n", h);
```

dapat menghasilkan

```text
h = 6.626070e-34 J s
```

Format `%e` menampilkan notasi ilmiah.

### Beberapa format yang sering digunakan

| Tipe | `printf` |
|---|---|
| `int` | `%d` |
| `char` | `%c` |
| `double` | `%f`, `%e`, `%g` |
| string | `%s` |

Untuk `printf`, argumen bertipe `float` dipromosikan menjadi `double`, sehingga `%f` digunakan untuk keduanya.

## Membaca masukan dengan `scanf`

Fungsi

```c
scanf()
```

digunakan untuk membaca masukan.

Contoh integer:

```c
int n;

scanf("%d", &n);
```

Contoh `double`:

```c
double temperature;

scanf("%lf", &temperature);
```

Perhatikan tanda

```text
&
```

di depan nama variabel.

Pada tahap ini kita cukup memahami bahwa `scanf` membutuhkan **alamat** variabel agar dapat menyimpan nilai yang dibaca.

Konsep alamat dan operator `&` akan dibahas lebih rinci ketika kita mempelajari *pointer*.

### `%f` dan `%lf` pada `scanf`

Perbedaan berikut sangat penting.

Untuk membaca `float`:

```c
float x;

scanf("%f", &x);
```

Untuk membaca `double`:

```c
double x;

scanf("%lf", &x);
```

Jadi pada `scanf`,

```text
%f   → float *
%lf  → double *
```

Hal ini berbeda dari `printf`, di mana `%f` digunakan untuk menampilkan `double`.

## Contoh input-output sederhana

Program berikut membaca massa dan kecepatan, kemudian menghitung energi kinetik.

```c
#include <stdio.h>

int main(void)
{
    double mass;
    double velocity;

    printf("Mass (kg): ");
    scanf("%lf", &mass);

    printf("Velocity (m/s): ");
    scanf("%lf", &velocity);

    double energy =
        0.5 * mass * velocity * velocity;

    printf("Kinetic energy = %.3f J\n", energy);

    return 0;
}
```

Jika masukan adalah

```text
Mass (kg): 2
Velocity (m/s): 3
```

keluarannya adalah

```text
Kinetic energy = 9.000 J
```

Sebelum menjalankan program, kita dapat memprediksi

```math
E_k
=
\frac12(2)(3)^2
=
9\text{ J}.
```

Kebiasaan membandingkan prediksi manual dengan keluaran program harus terus dipertahankan.

## Memeriksa keberhasilan `scanf`

`scanf` mengembalikan jumlah item yang berhasil dibaca.

Contoh:

```c
double mass;

int result = scanf("%lf", &mass);
```

Jika satu nilai `double` berhasil dibaca,

```text
result == 1
```

Kita dapat memanfaatkannya untuk pemeriksaan dasar.

```c
#include <stdio.h>

int main(void)
{
    double mass;

    printf("Mass (kg): ");

    if (scanf("%lf", &mass) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    printf("Mass = %.3f kg\n", mass);

    return 0;
}
```

Struktur `if` akan dibahas secara sistematis pada kuliah berikutnya.

Untuk sekarang, contoh tersebut menunjukkan bahwa program teknik sebaiknya tidak selalu menganggap masukan pengguna benar.

## Studi kasus 1: energi kinetik

Kita mulai dari model

```math
E_k
=
\frac12mv^2.
```

### Spesifikasi

Masukan:

```math
m,\quad v.
```

Keluaran:

```math
E_k.
```

Asumsi:

```math
m\geq0.
```

### Pseudocode

```text
INPUT mass
INPUT velocity

energy ← 0.5 * mass * velocity * velocity

OUTPUT energy
```

### Implementasi C

```c
#include <stdio.h>

int main(void)
{
    double mass;
    double velocity;

    printf("Mass (kg): ");
    scanf("%lf", &mass);

    printf("Velocity (m/s): ");
    scanf("%lf", &velocity);

    double energy =
        0.5 * mass * velocity * velocity;

    printf("Kinetic energy = %.6f J\n", energy);

    return 0;
}
```

### Pemeriksaan

Untuk

```math
m=2.0\text{ kg}
```

dan

```math
v=3.0\text{ m/s},
```

hasil yang diharapkan adalah

```math
E_k
=
9.0\text{ J}.
```

Jika program menghasilkan nilai yang sangat berbeda, kita harus memeriksa

- input;
- satuan;
- ekspresi;
- tipe data;
- format output.

## Studi kasus 2: Hukum Ohm

Hukum Ohm diberikan oleh

```math
V=IR.
```

Jika $I$ dan $R$ diketahui, kita dapat menghitung $V$.

### Pseudocode

```text
INPUT current
INPUT resistance

voltage ← current * resistance

OUTPUT voltage
```

### Implementasi C

```c
#include <stdio.h>

int main(void)
{
    double current;
    double resistance;

    printf("Current (A): ");
    scanf("%lf", &current);

    printf("Resistance (ohm): ");
    scanf("%lf", &resistance);

    double voltage =
        current * resistance;

    printf("Voltage = %.3f V\n", voltage);

    return 0;
}
```

Untuk

```math
I=2.5\text{ A}
```

dan

```math
R=10\ \Omega,
```

kita memperoleh

```math
V
=
(2.5)(10)
=
25\text{ V}.
```

## Studi kasus 3: konversi Celsius ke Kelvin

Hubungan antara Celsius dan Kelvin adalah

```math
T_K
=
T_C+273.15.
```

Program:

```c
#include <stdio.h>

int main(void)
{
    double temperature_c;

    printf("Temperature (C): ");
    scanf("%lf", &temperature_c);

    double temperature_k =
        temperature_c + 273.15;

    printf("Temperature = %.2f K\n", temperature_k);

    return 0;
}
```

Untuk

```math
T_C=25^\circ\text{C},
```

kita memperoleh

```math
T_K
=
298.15\text{ K}.
```

Contoh ini sederhana, tetapi menunjukkan pentingnya nama variabel yang menyertakan informasi satuan.

Bandingkan

```c
double t;
double x;
```

dengan

```c
double temperature_c;
double temperature_k;
```

Versi kedua jauh lebih aman untuk program teknik.

## Studi kasus 4: persamaan gas ideal

Persamaan gas ideal adalah

```math
PV=nRT.
```

Jika kita ingin menghitung tekanan,

```math
P
=
\frac{nRT}{V}.
```

Gunakan konstanta gas

```math
R
=
8.314462618\text{ J mol}^{-1}\text{K}^{-1}.
```

Implementasi:

```c
#include <stdio.h>

int main(void)
{
    const double gas_constant = 8.314462618;

    double amount;
    double temperature;
    double volume;

    printf("Amount of substance (mol): ");
    scanf("%lf", &amount);

    printf("Temperature (K): ");
    scanf("%lf", &temperature);

    printf("Volume (m^3): ");
    scanf("%lf", &volume);

    double pressure =
        amount * gas_constant * temperature / volume;

    printf("Pressure = %.6e Pa\n", pressure);

    return 0;
}
```

Misalkan

```math
n=1\text{ mol},
```

```math
T=300\text{ K},
```

dan

```math
V=0.024\text{ m}^3.
```

Secara manual,

```math
P
=
\frac{(1)(8.314462618)(300)}{0.024}.
```

Nilainya sekitar

```math
P
\approx
1.04\times10^5\text{ Pa}.
```

Nilai tersebut masuk akal karena berada pada orde tekanan atmosfer.

Di sini kita melihat pentingnya **orde besaran** sebagai pemeriksaan fisik.

## Studi kasus 5: energi foton

Energi foton diberikan oleh

```math
E
=
hf,
```

dengan

```math
h
=
6.62607015\times10^{-34}\text{ J s}.
```

Program:

```c
#include <stdio.h>

int main(void)
{
    const double planck_constant =
        6.62607015e-34;

    double frequency;

    printf("Frequency (Hz): ");
    scanf("%lf", &frequency);

    double energy =
        planck_constant * frequency;

    printf("Photon energy = %.6e J\n", energy);

    return 0;
}
```

Jika

```math
f
=
5.0\times10^{14}\text{ Hz},
```

maka

```math
E
=
(6.62607015\times10^{-34})
(5.0\times10^{14}),
```

sehingga

```math
E
\approx
3.31\times10^{-19}\text{ J}.
```

Contoh ini menunjukkan mengapa notasi ilmiah sangat berguna dalam program sains.

## Ekspresi gabungan

Program teknik sering menggunakan ekspresi yang lebih panjang.

Misalkan kita menghitung posisi

```math
x(t)
=
x_0+v_0t+\frac12at^2.
```

Dalam C,

```c
double position =
    x0
    + v0 * time
    + 0.5 * acceleration * time * time;
```

Menulis ekspresi dalam beberapa baris diperbolehkan.

C tidak menganggap baris baru sebagai akhir pernyataan.

Akhir pernyataan ditentukan oleh titik koma.

Karena itu,

```c
double position =
    x0
    + v0 * time
    + 0.5 * acceleration * time * time;
```

dan

```c
double position = x0 + v0 * time + 0.5 * acceleration * time * time;
```

memiliki makna yang sama.

Versi pertama mungkin lebih mudah dibaca untuk ekspresi panjang.

## Urutan evaluasi dan penggunaan variabel antara

Kadang-kadang lebih baik memecah ekspresi menjadi beberapa langkah.

Misalkan

```math
E_k
=
\frac12mv^2.
```

Alih-alih

```c
double energy =
    0.5 * mass * velocity * velocity;
```

kita dapat menulis

```c
double velocity_squared =
    velocity * velocity;

double energy =
    0.5 * mass * velocity_squared;
```

Versi kedua dapat lebih mudah diperiksa ketika perhitungan menjadi rumit.

Penggunaan variabel antara juga memudahkan *debugging*.

Namun, terlalu banyak variabel yang tidak perlu juga dapat membuat program panjang.

Kita perlu mencari keseimbangan antara

- keterbacaan;
- kesederhanaan;
- kemudahan pemeriksaan.

## Perbandingan bilangan *floating-point*

Pada Kuliah 1 kita telah melihat bahwa bilangan seperti

```math
0.1
```

tidak selalu dapat direpresentasikan secara eksak dalam biner.

Karena itu, perbandingan langsung bilangan *floating-point* perlu dilakukan dengan hati-hati.

Misalkan secara matematis kita mengharapkan

```math
0.1+0.2=0.3.
```

Namun representasi komputer dapat memberikan nilai yang sangat sedikit berbeda.

Daripada selalu menggunakan kesamaan eksak,

```c
x == y
```

dalam komputasi numerik kita sering memeriksa

```math
|x-y|<\varepsilon.
```

Dalam C, dengan pustaka matematika,

```c
#include <math.h>
```

kita dapat menulis

```c
fabs(x - y) < tolerance
```

Sebagai contoh,

```c
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main(void)
{
    double x = 0.1 + 0.2;
    double y = 0.3;

    const double tolerance = 1e-12;

    bool approximately_equal =
        fabs(x - y) < tolerance;

    printf("x = %.17f\n", x);
    printf("y = %.17f\n", y);
    printf("approximately equal = %d\n",
           approximately_equal);

    return 0;
}
```

Pada tahap ini kita belum perlu mendalami pemilihan toleransi.

Yang perlu dipahami adalah bahwa tipe data *floating-point* memiliki konsekuensi numerik.

## Galat kompilasi, peringatan, dan galat logika

Saat belajar C, kita akan sering bertemu tiga kategori masalah.

### Galat sintaksis

Contoh:

```c
double mass = 2.0
```

Titik koma hilang.

*Compiler* dapat mendeteksi masalah tersebut.

### Peringatan

Contoh:

```c
int x = 3.7;
```

Konversi dari bilangan real ke integer dapat kehilangan informasi.

Tergantung *compiler* dan opsi yang digunakan, kita mungkin memperoleh peringatan.

### Galat logika

Contoh:

```c
double energy =
    0.5 * mass * velocity;
```

Program mungkin dapat dikompilasi tanpa masalah.

Namun, model yang seharusnya

```math
E_k
=
\frac12mv^2
```

tidak diimplementasikan dengan benar.

*Compiler* tidak mengetahui fisika.

Karena itu, galat logika harus ditemukan melalui

- pengujian;
- perhitungan manual;
- pemeriksaan satuan;
- pemeriksaan orde besaran;
- penalaran terhadap algoritma.

## Compiler warning sebagai bagian dari proses belajar

Gunakan

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 program.c -o program
```

dan baca setiap pesan dengan teliti.

Sebagai kebiasaan awal:

```text
jangan abaikan warning tanpa memahami penyebabnya
```

Peringatan dapat menunjukkan

- variabel yang tidak digunakan;
- konversi tipe;
- format input-output yang tidak sesuai;
- kemungkinan kesalahan logika;
- bagian program yang mencurigakan.

Tujuan kita bukan hanya membuat *compiler* diam, tetapi memahami mengapa suatu peringatan muncul.

## Studi kasus terpadu: daya pada resistor

Misalkan kita ingin membuat program yang membaca hambatan dan arus, kemudian menghitung

```math
V=IR
```

dan

```math
P=VI.
```

Dengan substitusi,

```math
P=I^2R.
```

### Spesifikasi

Masukan:

```math
I,\quad R.
```

Keluaran:

```math
V,\quad P.
```

Asumsi:

```math
R\geq0.
```

### Pseudocode

```text
INPUT current
INPUT resistance

voltage ← current * resistance
power ← voltage * current

OUTPUT voltage
OUTPUT power
```

### Implementasi C

```c
#include <stdio.h>

int main(void)
{
    double current;
    double resistance;

    printf("Current (A): ");
    scanf("%lf", &current);

    printf("Resistance (ohm): ");
    scanf("%lf", &resistance);

    double voltage =
        current * resistance;

    double power =
        voltage * current;

    printf("\nVoltage = %.3f V\n", voltage);
    printf("Power   = %.3f W\n", power);

    return 0;
}
```

### Tracing manual

Gunakan

```math
I=2.5\text{ A},
```

```math
R=10\ \Omega.
```

Maka

```math
V
=
IR
=
(2.5)(10)
=
25\text{ V}.
```

Selanjutnya,

```math
P
=
VI
=
(25)(2.5)
=
62.5\text{ W}.
```

Program seharusnya menghasilkan nilai mendekati

```text
Voltage = 25.000 V
Power   = 62.500 W
```

### Pemeriksaan dimensi

Untuk tegangan,

```math
[I][R]
=
\text{A}\cdot\Omega
=
\text{V}.
```

Untuk daya,

```math
[V][I]
=
\text{V}\cdot\text{A}
=
\text{W}.
```

Pemeriksaan satuan merupakan salah satu alat *debugging* yang sangat kuat dalam komputasi fisika.

## Studi kasus terpadu: gerak dengan percepatan konstan

Model:

```math
x(t)
=
x_0+v_0t+\frac12at^2,
```

dan

```math
v(t)
=
v_0+at.
```

### Pseudocode

```text
INPUT x0
INPUT v0
INPUT a
INPUT t

position ← x0 + v0*t + 0.5*a*t*t
velocity ← v0 + a*t

OUTPUT position
OUTPUT velocity
```

### Implementasi

```c
#include <stdio.h>

int main(void)
{
    double x0;
    double v0;
    double acceleration;
    double time;

    printf("Initial position (m): ");
    scanf("%lf", &x0);

    printf("Initial velocity (m/s): ");
    scanf("%lf", &v0);

    printf("Acceleration (m/s^2): ");
    scanf("%lf", &acceleration);

    printf("Time (s): ");
    scanf("%lf", &time);

    double position =
        x0
        + v0 * time
        + 0.5 * acceleration * time * time;

    double velocity =
        v0 + acceleration * time;

    printf("\nPosition = %.3f m\n", position);
    printf("Velocity = %.3f m/s\n", velocity);

    return 0;
}
```

Untuk

```math
x_0=2\text{ m},
```

```math
v_0=5\text{ m/s},
```

```math
a=3\text{ m/s}^2,
```

dan

```math
t=4\text{ s},
```

kita memperoleh

```math
x
=
2+(5)(4)+\frac12(3)(4)^2
=
46\text{ m},
```

serta

```math
v
=
5+(3)(4)
=
17\text{ m/s}.
```

Keluaran program dapat dibandingkan langsung dengan hasil tersebut.

## Kesalahan umum pada tahap awal pemrograman C

### Melupakan titik koma

Salah:

```c
double mass = 2.0
```

Benar:

```c
double mass = 2.0;
```

### Menggunakan variabel sebelum diberi nilai

Salah:

```c
double x;
double y = x + 1.0;
```

Lebih baik:

```c
double x = 0.0;
double y = x + 1.0;
```

### Salah memilih tipe data

Contoh:

```c
int temperature = 25.75;
```

Nilai pecahan tidak dapat dipertahankan sebagai `int`.

Gunakan

```c
double temperature = 25.75;
```

### Pembagian integer yang tidak disadari

```c
double x = 1 / 2;
```

memberikan

```math
0.0
```

karena

```math
1/2
```

dihitung sebagai pembagian integer terlebih dahulu.

Gunakan

```c
double x = 1.0 / 2.0;
```

atau

```c
double x = 0.5;
```

### Salah menulis format `scanf`

Jika variabel bertipe `double`,

```c
double x;
```

gunakan

```c
scanf("%lf", &x);
```

bukan

```c
scanf("%f", &x);
```

### Melupakan `&` pada `scanf`

Salah:

```c
scanf("%lf", temperature);
```

Benar:

```c
scanf("%lf", &temperature);
```

### Menggunakan `=` ketika maksudnya membandingkan

Assignment:

```c
x = 5;
```

Perbandingan:

```c
x == 5
```

Keduanya memiliki makna berbeda.

### Menganggap `^` sebagai pangkat

Salah:

```c
energy = 0.5 * mass * velocity ^ 2;
```

Benar untuk kuadrat sederhana:

```c
energy =
    0.5 * mass * velocity * velocity;
```

## Kebiasaan pemrograman yang baik

Sejak awal, biasakan beberapa praktik berikut.

### Gunakan nama variabel yang informatif

Lebih baik:

```c
double temperature;
double pressure;
double velocity;
```

daripada

```c
double a;
double b;
double c;
```

kecuali konteksnya memang sangat sederhana.

### Nyatakan satuan

Contoh:

```c
double pressure_pa;
double temperature_k;
```

atau gunakan komentar.

```c
double velocity = 20.0;  // m/s
```

### Gunakan `const` untuk konstanta

```c
const double gravity = 9.81;
```

### Gunakan indentasi konsisten

```c
int main(void)
{
    double x = 1.0;

    printf("%f\n", x);

    return 0;
}
```

Indentasi membantu menunjukkan struktur program.

### Batasi panjang ekspresi

Jika ekspresi sulit dibaca, pecah menjadi variabel antara.

### Kompilasi dengan warning

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 program.c -o program
```

### Prediksi sebelum menjalankan

Untuk setiap program sederhana, lakukan

```text
tentukan input
    ↓
hitung manual
    ↓
prediksi output
    ↓
jalankan program
    ↓
bandingkan
```

Kebiasaan ini jauh lebih efektif daripada hanya menekan tombol *Run* berulang kali.

## Cek pemahaman

Cobalah menjawab pertanyaan berikut tanpa melihat kembali catatan.

- Apa peran fungsi `main` dalam program C?
- Mengapa `#include <stdio.h>` diperlukan ketika menggunakan `printf` dan `scanf`?
- Apa perbedaan deklarasi, inisialisasi, dan assignment?
- Mengapa variabel sebaiknya tidak digunakan sebelum diberi nilai?
- Apa perbedaan `int`, `float`, dan `double`?
- Mengapa `double` sering lebih sesuai daripada `float` untuk komputasi ilmiah?
- Apa fungsi `const`?
- Apa perbedaan antara literal `2`, `2.0`, dan `2.0f`?
- Mengapa `5 / 2` berbeda dari `5.0 / 2.0`?
- Apa fungsi operator `%`?
- Apa perbedaan antara `=` dan `==`?
- Bagaimana menuliskan kondisi matematis
  ```math
  20\leq T\leq30
  ```
  dalam C?
- Apa arti operator `&&`, `||`, dan `!`?
- Mengapa `v ^ 2` bukan cara yang benar untuk menulis $v^2$ dalam C?
- Apa perbedaan *implicit conversion* dan *explicit cast*?
- Mengapa konversi dari `double` ke `int` dapat kehilangan informasi?
- Format apa yang digunakan `scanf` untuk membaca `double`?
- Mengapa `scanf` membutuhkan `&` di depan variabel?
- Apa manfaat `-Wall`, `-Wextra`, dan `-Wpedantic`?
- Mengapa program yang berhasil dikompilasi belum tentu benar secara fisika?

## Latihan

### 1. Struktur program C

Tuliskan program C yang hanya menampilkan

```text
Algoritma dan Pemrograman
Teknik Fisika
```

Gunakan

```c
printf()
```

dan pastikan setiap teks tampil pada baris yang berbeda.

Kompilasi menggunakan

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 program.c -o program
```

Pastikan tidak muncul peringatan.

### 2. Variabel dan tipe data

Buat variabel untuk merepresentasikan

- jumlah sensor;
- temperatur;
- tekanan;
- karakter status;
- kondisi alarm aktif atau tidak.

Pilih tipe data yang sesuai dari

```text
int
double
char
bool
```

Jelaskan alasan pemilihan tipe masing-masing.

### 3. Ukuran tipe data

Buat program yang menampilkan

```c
sizeof(char)
sizeof(int)
sizeof(float)
sizeof(double)
sizeof(bool)
```

Jalankan pada komputer Anda.

Bandingkan hasilnya dengan teman yang menggunakan sistem operasi atau arsitektur berbeda jika tersedia.

Apakah semua hasil harus sama?

### 4. Rentang integer

Gunakan

```c
#include <limits.h>
```

untuk menampilkan

```text
INT_MIN
INT_MAX
```

Bandingkan dengan prediksi berdasarkan jumlah bit `int` pada sistem Anda.

### 5. Pembagian integer

Prediksi hasil program berikut sebelum menjalankannya.

```c
#include <stdio.h>

int main(void)
{
    int a = 7;
    int b = 2;

    double x = a / b;
    double y = (double)a / b;

    printf("x = %f\n", x);
    printf("y = %f\n", y);

    return 0;
}
```

Jelaskan mengapa `x` dan `y` berbeda.

### 6. Konversi temperatur

Buat program yang membaca temperatur Celsius dan menghitung Kelvin menggunakan

```math
T_K
=
T_C+273.15.
```

Gunakan `double`.

Uji menggunakan

```math
T_C=0^\circ\text{C},
```

```math
T_C=25^\circ\text{C},
```

dan

```math
T_C=100^\circ\text{C}.
```

Hitung hasil manual terlebih dahulu.

### 7. Hukum Ohm

Buat program yang membaca

```math
I
```

dan

```math
R,
```

kemudian menghitung

```math
V=IR
```

dan

```math
P=I^2R.
```

Tampilkan hasil dengan tiga digit setelah titik desimal.

Gunakan

```math
I=2.5\text{ A},
```

dan

```math
R=10\ \Omega
```

sebagai kasus uji.

### 8. Gerak lurus

Buat program yang membaca

```math
x_0,\quad v_0,\quad a,\quad t,
```

kemudian menghitung

```math
x(t)
=
x_0+v_0t+\frac12at^2
```

dan

```math
v(t)
=
v_0+at.
```

Gunakan kasus uji

```math
x_0=2\text{ m},
```

```math
v_0=5\text{ m/s},
```

```math
a=3\text{ m/s}^2,
```

```math
t=4\text{ s}.
```

Prediksi keluaran sebelum menjalankan program.

### 9. Persamaan gas ideal

Gunakan

```math
P
=
\frac{nRT}{V}
```

dengan

```math
R
=
8.314462618\text{ J mol}^{-1}\text{K}^{-1}.
```

Buat program yang membaca

```math
n,\quad T,\quad V
```

dan menampilkan tekanan dalam pascal.

Gunakan `const double` untuk $R$.

Uji menggunakan

```math
n=1\text{ mol},
```

```math
T=300\text{ K},
```

```math
V=0.024\text{ m}^3.
```

Periksa apakah orde besaran hasil mendekati tekanan atmosfer.

### 10. Energi foton

Energi foton diberikan oleh

```math
E=hf.
```

Gunakan

```math
h
=
6.62607015\times10^{-34}\text{ J s}.
```

Buat program yang membaca frekuensi dan menampilkan energi menggunakan format notasi ilmiah.

Uji menggunakan

```math
f
=
5.0\times10^{14}\text{ Hz}.
```

### 11. Ekspresi Boolean

Misalkan temperatur sistem adalah `temperature`.

Tuliskan ekspresi Boolean C untuk kondisi berikut.

1. Temperatur lebih besar dari $30^\circ\text{C}$.
2. Temperatur berada pada rentang
   ```math
   20^\circ\text{C}
   \leq T
   \leq
   30^\circ\text{C}.
   ```
3. Temperatur berada di luar rentang aman
   ```math
   10^\circ\text{C}
   \leq T
   \leq
   50^\circ\text{C}.
   ```
4. Sensor aktif dan temperatur lebih besar dari $40^\circ\text{C}$.
5. Sensor tidak aktif.

### 12. Mencari kesalahan

Perhatikan program berikut.

```c
#include <stdio.h>

int main(void)
{
    int mass = 2.5;
    double velocity;

    printf("Velocity: ");
    scanf("%f", velocity);

    double energy =
        1 / 2 * mass * velocity ^ 2;

    printf("Energy = %d\n", energy)

    return 0;
}
```

Program tersebut memiliki beberapa kesalahan konsep dan sintaks.

Identifikasi sebanyak mungkin masalah, kemudian tulis versi yang benar.

### 13. Pemeriksaan input sederhana

Modifikasi program energi kinetik sehingga program memeriksa apakah `scanf` berhasil membaca nilai massa dan kecepatan.

Jika pembacaan gagal, tampilkan pesan

```text
Invalid input.
```

dan akhiri program dengan

```c
return 1;
```

### 14. Eksperimen presisi *floating-point*

Buat program

```c
#include <stdio.h>

int main(void)
{
    double x = 0.1 + 0.2;

    printf("%.17f\n", x);

    return 0;
}
```

Jalankan program dan amati hasilnya.

Bandingkan dengan

```math
0.3.
```

Jelaskan hubungan hasil eksperimen dengan pembahasan representasi *floating-point* pada Kuliah 1.

## Rangkuman

- Pada kuliah ini kita mulai menerjemahkan algoritma menjadi program C.

- Struktur dasar program C dapat ditulis sebagai

```c
#include <stdio.h>

int main(void)
{
    /* program */

    return 0;
}
```

- Program C dikompilasi menjadi *executable* sebelum dijalankan.

- Variabel merupakan lokasi penyimpanan bernama yang mempunyai tipe tertentu.

- Deklarasi menentukan nama dan tipe variabel, sedangkan inisialisasi memberikan nilai awal.

- Assignment menggunakan operator

```text
=
```

dan berbeda dari perbandingan kesamaan

```text
==
```

- Tipe data dasar yang penting pada tahap ini meliputi

```text
char
int
float
double
bool
```

- Untuk komputasi ilmiah dasar, `double` akan sering digunakan karena menyediakan presisi lebih tinggi daripada `float`.

- Tipe data menentukan representasi, rentang nilai, dan presisi.

- Nilai yang tidak dimaksudkan berubah dapat dideklarasikan menggunakan

```c
const
```

- Operator aritmetika dasar meliputi

```text
+  -  *  /  %
```

- Pembagian integer harus diperhatikan karena

```math
5/2
=
2
```

jika kedua operand bertipe integer.

- C tidak menggunakan `^` sebagai operator pangkat. Untuk kuadrat sederhana, gunakan

```c
x * x
```

- Operator relasional meliputi

```text
<  <=  >  >=  ==  !=
```

- Operator logika meliputi

```text
&&  ||  !
```

yang masing-masing merepresentasikan AND, OR, dan NOT.

- Kondisi matematika seperti

```math
20\leq T\leq30
```

ditulis dalam C sebagai

```c
temperature >= 20.0 &&
temperature <= 30.0
```

- Konversi tipe dapat terjadi secara implisit atau dilakukan secara eksplisit menggunakan cast.

- `printf` digunakan untuk keluaran, sedangkan `scanf` digunakan untuk masukan.

- Untuk `scanf`,

```text
%d   → int
%f   → float
%lf  → double
```

- `scanf` memerlukan alamat variabel sehingga kita menggunakan operator `&`.

- Program teknik sebaiknya dikompilasi dengan peringatan aktif, misalnya

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 program.c -o program
```

- Program yang berhasil dikompilasi belum tentu benar. Hasil tetap perlu diperiksa menggunakan algoritma, perhitungan manual, satuan, orde besaran, dan penalaran fisika.

- Pada kuliah berikutnya kita akan menggunakan ekspresi Boolean yang telah dipelajari untuk membangun aliran kontrol program melalui percabangan dan pengulangan menggunakan `if`, `else`, `switch`, `while`, `do-while`, dan `for`.
