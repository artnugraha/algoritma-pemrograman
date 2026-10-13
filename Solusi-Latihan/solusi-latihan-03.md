# Solusi Latihan Kuliah 3: Dasar Pemrograman C

## 1. Struktur program C

### Soal

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
gcc -Wall -Wextra program.c -o program
```

Pastikan tidak muncul peringatan.

### Solusi

Program lengkap berikut dapat disimpan sebagai `program.c`. Karakter `\n` pada setiap `printf` memindahkan keluaran berikutnya ke baris baru.

```c
#include <stdio.h>

int main(void)
{
    printf("Algoritma dan Pemrograman\n");
    printf("Teknik Fisika\n");

    return 0;
}
```

Kompilasi dan jalankan program:

```bash
gcc -Wall -Wextra program.c -o program.x
./program.x
```

Keluaran yang diperoleh adalah

```text
Algoritma dan Pemrograman
Teknik Fisika
```

Fungsi `main` mengembalikan 0 untuk menandakan program selesai dengan normal. Kedua baris `printf` memakai teks sesuai soal dan dapat dikompilasi tanpa peringatan.

## 2. Variabel dan tipe data

### Soal

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

### Solusi

Deklarasi berikut dapat diletakkan di dalam fungsi `main`; nilainya hanya contoh. Pustaka `<stdbool.h>` diperlukan agar nama tipe `bool` serta nilai `true` dan `false` dikenali oleh C.

```c
#include <stdbool.h>

/* Di dalam fungsi main: */
int jumlah_sensor = 4;
double temperatur = 29.5;
double tekanan = 101325.0;
char status = 'N';
bool alarm_aktif = false;
```

| Besaran | Tipe | Alasan |
|---|---|---|
| Jumlah sensor | `int` | Banyaknya sensor merupakan bilangan bulat. |
| Temperatur | `double` | Pengukuran dapat memuat pecahan, misalnya $29.5^\circ\text{C}$. |
| Tekanan | `double` | Hasil pengukuran dapat memuat pecahan dan membutuhkan rentang serta presisi bilangan real. |
| Karakter status | `char` | Status berupa satu karakter, misalnya `'N'`. |
| Alarm aktif atau tidak | `bool` | Kondisinya hanya `true` atau `false`. |

Tanda petik tunggal pada `'N'` menandakan satu karakter. Jika status kelak memerlukan beberapa karakter, satu variabel `char` tidak lagi cukup.

## 3. Ukuran tipe data

### Soal

Buat program yang menampilkan

```c
sizeof(char)
sizeof(int)
sizeof(float)
sizeof(double)
sizeof(bool)
```

Jalankan pada komputer masing-masing.

Bandingkan hasilnya dengan teman yang menggunakan sistem operasi atau arsitektur berbeda jika tersedia.

Apakah semua hasil harus sama?

### Solusi

Ukuran tipe ditampilkan dalam **byte** dengan `sizeof`; format `%zu` dipakai karena hasil `sizeof` bertipe `size_t`. Simpan program sebagai `ukuran_tipe.c`.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    printf("sizeof(char)   = %zu byte\n", sizeof(char));
    printf("sizeof(int)    = %zu byte\n", sizeof(int));
    printf("sizeof(float)  = %zu byte\n", sizeof(float));
    printf("sizeof(double) = %zu byte\n", sizeof(double));
    printf("sizeof(bool)   = %zu byte\n", sizeof(bool));

    return 0;
}
```

```bash
gcc -Wall -Wextra ukuran_tipe.c -o ukuran_tipe
./ukuran_tipe
```

Pada lingkungan uji yang dipakai untuk memeriksa solusi ini, hasilnya adalah

```text
sizeof(char)   = 1 byte
sizeof(int)    = 4 byte
sizeof(float)  = 4 byte
sizeof(double) = 8 byte
sizeof(bool)   = 1 byte
```

Hasil semua komputer **tidak harus sama**. Bahasa C menetapkan `sizeof(char) == 1` menurut definisi byte C, tetapi banyaknya bit per byte serta ukuran beberapa tipe lainnya dapat berbeda menurut implementasi. Karena itu, jalankan program pada komputer masing-masing dan bandingkan angka aktualnya.

## 4. Rentang integer

### Soal

Gunakan

```c
#include <limits.h>
```

untuk menampilkan

```text
INT_MIN
INT_MAX
```

Bandingkan dengan prediksi berdasarkan jumlah bit `int` pada sistem operasi dan lingkungan pemrograman masing-masing.

### Solusi

Pustaka `<limits.h>` menyediakan batas nilai `int` untuk implementasi yang sedang dipakai. Program berikut juga menampilkan `CHAR_BIT` agar jumlah bit per byte dapat diperiksa.

```c
#include <stdio.h>
#include <limits.h>

int main(void)
{
    printf("CHAR_BIT = %d\n", CHAR_BIT);
    printf("sizeof(int) = %zu byte\n", sizeof(int));
    printf("INT_MIN = %d\n", INT_MIN);
    printf("INT_MAX = %d\n", INT_MAX);

    return 0;
}
```

```bash
gcc -Wall -Wextra rentang_int.c -o rentang_int
./rentang_int
```

Jika `CHAR_BIT = 8` dan `sizeof(int) = 4`, maka satu `int` memakai $4\times 8=32$ bit penyimpanan. Dengan representasi *two's complement* 32 bit tanpa bit pengisi, prediksinya adalah

```math
\text{INT\_MIN}=-2^{31}=-2147483648,\\
\text{INT\_MAX}=2^{31}-1=2147483647.
```

Prediksi itu perlu dibandingkan dengan keluaran nyata. Ukuran dan rentang `int` ditentukan oleh implementasi C pada komputer dan *compiler*, sehingga tidak cukup disimpulkan hanya dari nama sistem operasinya.

## 5. Pembagian integer

### Soal

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

### Solusi

Karena `a` dan `b` sama-sama bertipe `int`, ekspresi `a / b` melakukan pembagian bilangan bulat. Hasil $7/2$ dipotong menuju nol menjadi 3 sebelum disimpan sebagai `double`, sehingga `x` bernilai $3.0$.

Pada `(double)a / b`, nilai `a` terlebih dahulu dikonversi menjadi `double`. Pembagian kemudian berlangsung sebagai operasi bilangan real dan menghasilkan $3.5$. Dengan format `%f` pada program dalam soal, keluarannya adalah

```text
x = 3.000000
y = 3.500000
```

Mengubah tipe variabel tujuan menjadi `double` tidak mengubah jenis operasi yang **sudah dilakukan** di ruas kanan. Konversi salah satu operand harus terjadi sebelum pembagian agar bagian pecahannya tidak hilang.

## 6. Konversi temperatur

### Soal

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

### Solusi

Hasil hitung tangan untuk tiga masukan adalah

| $T_C$ ($^\circ\text{C}$) | Perhitungan | $T_K$ (K) |
|---:|---:|---:|
| 0 | $0+273.15$ | 273.15 |
| 25 | $25+273.15$ | 298.15 |
| 100 | $100+273.15$ | 373.15 |

Program berikut membaca satu temperatur untuk setiap eksekusi. Simpan sebagai `celsius_kelvin.c` dan jalankan tiga kali dengan masukan pada tabel.

```c
#include <stdio.h>

int main(void)
{
    double celsius;

    printf("Temperature (C): ");
    if (scanf("%lf", &celsius) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    double kelvin = celsius + 273.15;
    printf("Temperature = %.2f K\n", kelvin);

    return 0;
}
```

```bash
gcc -Wall -Wextra celsius_kelvin.c -o celsius_kelvin
./celsius_kelvin
```

Untuk masukan `0`, `25`, dan `100`, keluaran numeriknya berturut-turut adalah `273.15 K`, `298.15 K`, dan `373.15 K`. Format `%lf` pada `scanf` membaca `double`, sedangkan `%.2f` menampilkan dua angka setelah titik desimal.

## 7. Hukum Ohm

### Soal

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

### Solusi

Dari $V=IR$ dan $P=I^2R$, perhitungan manual untuk $I=2.5\ \text{A}$ serta $R=10\ \Omega$ adalah

```math
V=(2.5)(10)=25\ \text{V},
\qquad
P=(2.5)^2(10)=62.5\ \text{W}.
```

Simpan program berikut sebagai `hukum_ohm.c`. Program membaca arus dan hambatan, lalu menampilkan hasil dengan tiga angka setelah titik desimal.

```c
#include <stdio.h>

int main(void)
{
    double current;
    double resistance;

    printf("Current (A): ");
    if (scanf("%lf", &current) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    printf("Resistance (ohm): ");
    if (scanf("%lf", &resistance) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    double voltage = current * resistance;
    double power = current * current * resistance;

    printf("Voltage = %.3f V\n", voltage);
    printf("Power   = %.3f W\n", power);

    return 0;
}
```

```bash
gcc -Wall -Wextra hukum_ohm.c -o hukum_ohm
./hukum_ohm
```

Dengan masukan `2.5` dan `10`, dua baris hasilnya adalah `Voltage = 25.000 V` dan `Power   = 62.500 W`. Kedua angka sesuai dengan hitungan tangan dan satuan fisikanya.

## 8. Gerak lurus

### Soal

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

### Solusi

Substitusi $x_0=2\ \text{m}$, $v_0=5\ \text{m/s}$, $a=3\ \text{m/s}^2$, dan $t=4\ \text{s}$ memberikan prediksi

```math
\begin{aligned}
x(4)&=2+5(4)+\frac12(3)(4)^2
     =2+20+24=46\ \text{m},\\
v(4)&=5+3(4)=17\ \text{m/s}.
\end{aligned}
```

Simpan program berikut sebagai `gerak_lurus.c`. Dalam C, kuadrat waktu ditulis dengan perkalian `time * time`.

```c
#include <stdio.h>

int main(void)
{
    double x0;
    double v0;
    double acceleration;
    double time;

    printf("x0 (m): ");
    if (scanf("%lf", &x0) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    printf("v0 (m/s): ");
    if (scanf("%lf", &v0) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    printf("a (m/s^2): ");
    if (scanf("%lf", &acceleration) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    printf("t (s): ");
    if (scanf("%lf", &time) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    double position =
        x0 + v0 * time
        + 0.5 * acceleration * time * time;
    double velocity = v0 + acceleration * time;

    printf("Position = %.3f m\n", position);
    printf("Velocity = %.3f m/s\n", velocity);

    return 0;
}
```

```bash
gcc -Wall -Wextra gerak_lurus.c -o gerak_lurus
./gerak_lurus
```

Jika empat nilai masukan diberikan berurutan sebagai `2`, `5`, `3`, dan `4`, program menampilkan `Position = 46.000 m` dan `Velocity = 17.000 m/s`. Keduanya sama dengan prediksi sebelum program dijalankan.

## 9. Persamaan gas ideal

### Soal

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

### Solusi

Hitungan manual dengan $R=8.314462618\ \text{J mol}^{-1}\text{K}^{-1}$ menghasilkan

```math
P=\frac{(1)(8.314462618)(300)}{0.024}
 =103930.782725\ \text{Pa}
 \approx 1.0393\times 10^5\ \text{Pa}.
```

Simpan program sebagai `gas_ideal.c`. Volume harus positif agar pembagian terdefinisi dan masuk akal untuk gas ideal.

```c
#include <stdio.h>

int main(void)
{
    const double R = 8.314462618;
    double amount;
    double temperature;
    double volume;

    printf("Amount (mol): ");
    if (scanf("%lf", &amount) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    printf("Temperature (K): ");
    if (scanf("%lf", &temperature) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    printf("Volume (m^3): ");
    if (scanf("%lf", &volume) != 1 || volume <= 0.0)
    {
        printf("Invalid volume.\n");
        return 1;
    }

    double pressure = amount * R * temperature / volume;
    printf("Pressure = %.3f Pa\n", pressure);

    return 0;
}
```

```bash
gcc -Wall -Wextra gas_ideal.c -o gas_ideal
./gas_ideal
```

Untuk masukan `1`, `300`, dan `0.024`, keluaran numeriknya adalah `Pressure = 103930.783 Pa`. Hasil ini berada pada orde $10^5\ \text{Pa}$, dekat dengan tekanan atmosfer sekitar $101325\ \text{Pa}$.

## 10. Energi foton

### Soal

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

### Solusi

Untuk $f=5.0\times10^{14}\ \text{Hz}$, perhitungan manual memberikan

```math
E=hf=(6.62607015\times10^{-34})(5.0\times10^{14})
 =3.313035075\times10^{-19}\ \text{J}.
```

Simpan program berikut sebagai `energi_foton.c`. Penentu format `%e` menampilkan hasil dalam notasi ilmiah.

```c
#include <stdio.h>

int main(void)
{
    const double h = 6.62607015e-34;
    double frequency;

    printf("Frequency (Hz): ");
    if (scanf("%lf", &frequency) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    double energy = h * frequency;
    printf("Energy = %.9e J\n", energy);

    return 0;
}
```

```bash
gcc -Wall -Wextra energi_foton.c -o energi_foton
./energi_foton
```

Dengan masukan `5.0e14`, keluaran numeriknya adalah `Energy = 3.313035075e-19 J`. Penulisan `6.62607015e-34` di dalam kode berarti $6.62607015\times10^{-34}$.

## 11. Ekspresi Boolean

### Soal

Misalkan temperatur sistem adalah `temperature`.

Tuliskan ekspresi Boolean C untuk kondisi berikut.

1. Temperatur lebih besar dari $30^\circ\text{C}$.
2. Temperatur berada pada rentang $20^\circ\text{C} \leq T \leq 30^\circ\text{C}$.
3. Temperatur berada di luar rentang aman
   $10^\circ\text{C} \leq T \leq 50^\circ\text{C}$.
4. Sensor aktif dan temperatur lebih besar dari $40^\circ\text{C}$.
5. Sensor tidak aktif.

### Solusi

Misalkan `temperature` bertipe `double` dan `sensor_active` bertipe `bool`. Ekspresi yang diminta adalah sebagai berikut.

| Kondisi | Ekspresi Boolean C |
|---|---|
| Temperatur $>30^\circ\text{C}$ | `temperature > 30.0` |
| $20^\circ\text{C}\leq T\leq30^\circ\text{C}$ | `temperature >= 20.0 && temperature <= 30.0` |
| Di luar rentang aman $10^\circ\text{C}\leq T\leq50^\circ\text{C}$ | `temperature < 10.0 || temperature > 50.0` |
| Sensor aktif dan temperatur $>40^\circ\text{C}$ | `sensor_active && temperature > 40.0` |
| Sensor tidak aktif | `!sensor_active` |

Operator `&&` menyatakan “dan”, `||` menyatakan “atau”, dan `!` menyatakan negasi. Batas 20 dan 30 termasuk dalam rentang pada kondisi kedua; batas 10 dan 50 masih aman pada kondisi ketiga.

## 12. Mencari kesalahan

### Soal

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

### Solusi

Program pada soal memuat kesalahan berikut.

1. `int mass = 2.5;` membuang bagian pecahan dan menjadikan `mass` bernilai 2. Massa yang memuat pecahan harus disimpan dalam `double`.
2. `scanf("%f", velocity);` tidak sesuai untuk membaca `double`: gunakan `%lf` dan berikan alamat `&velocity`. Tanpa alamat yang sesuai, pemanggilan `scanf` juga dapat menyebabkan perilaku tak terdefinisi.
3. Nilai kembalian `scanf` tidak diperiksa. Jika pembacaan gagal, `velocity` belum mempunyai nilai yang aman dipakai.
4. `1 / 2` melakukan pembagian `int` dan bernilai 0. Gunakan `0.5` agar faktor setengah tidak hilang.
5. `^ 2` bukan operator pangkat dalam C; `^` adalah XOR bitwise dan tidak dapat diterapkan pada `double`. Kuadrat kecepatan ditulis `velocity * velocity`.
6. `printf("Energy = %d\n", energy)` memakai `%d` untuk bilangan bulat, padahal `energy` bertipe `double`. Gunakan `%f` dan tambahkan titik koma setelah pemanggilan `printf`.

Versi yang benar berikut tetap memakai massa $2.5\ \text{kg}$ dan membaca kecepatan. Simpan sebagai `energi_kinetik_benar.c`.

```c
#include <stdio.h>

int main(void)
{
    double mass = 2.5;
    double velocity;

    printf("Velocity (m/s): ");
    if (scanf("%lf", &velocity) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    double energy = 0.5 * mass * velocity * velocity;
    printf("Energy = %.3f J\n", energy);

    return 0;
}
```

```bash
gcc -Wall -Wextra energi_kinetik_benar.c -o energi_kinetik_benar
./energi_kinetik_benar
```

Sebagai uji, masukan `3` memberikan $E_k=\tfrac12(2.5)(3)^2=11.25\ \text{J}$, sehingga baris hasilnya adalah `Energy = 11.250 J`. Hasil tersebut juga mempunyai satuan energi yang benar.

## 13. Pemeriksaan input sederhana

### Soal

Modifikasi program energi kinetik sehingga program memeriksa apakah `scanf` berhasil membaca nilai massa dan kecepatan.

Jika pembacaan gagal, tampilkan pesan

```text
Invalid input.
```

dan akhiri program dengan

```c
return 1;
```

### Solusi

Pemeriksaan harus dilakukan untuk **kedua** pembacaan sebelum nilainya dipakai dalam perhitungan. Program berikut membaca massa dan kecepatan secara terpisah sehingga lokasi kegagalan dapat diperiksa dengan jelas.

```c
#include <stdio.h>

int main(void)
{
    double mass;
    double velocity;

    printf("Mass (kg): ");
    if (scanf("%lf", &mass) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    printf("Velocity (m/s): ");
    if (scanf("%lf", &velocity) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    double energy = 0.5 * mass * velocity * velocity;
    printf("Kinetic energy = %.3f J\n", energy);

    return 0;
}
```

Simpan sebagai `energi_kinetik_input.c`, lalu kompilasi dengan `gcc -Wall -Wextra energi_kinetik_input.c -o energi_kinetik_input`. Jika dua masukan valid, misalnya `2` dan `3`, hasilnya adalah `Kinetic energy = 9.000 J`.

Jika massa atau kecepatan tidak dapat dibaca sebagai `double`, program mencetak tepat `Invalid input.` dan berhenti dengan status 1. Pemeriksaan ini hanya memastikan format masukan dapat dibaca; penolakan massa negatif merupakan pemeriksaan fisis tambahan yang dapat diterapkan sesudahnya.

## 14. Eksperimen presisi *floating-point*

### Soal

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

Jalankan program dan amati hasilnya. Bandingkan dengan
```math
0.3.
```
Jelaskan hubungan hasil eksperimen dengan pembahasan representasi *floating-point* pada Kuliah 1.

### Solusi

Gunakan program persis seperti yang diberikan pada soal, lalu kompilasi dan jalankan. Pada lingkungan uji dengan `double` biner 64 bit, keluaran `%.17f` adalah

```text
0.30000000000000004
```

Nilai matematis $0.1+0.2$ memang $0.3$. Namun, nilai $0.1$ dan $0.2$ tidak dapat dinyatakan secara eksak oleh pecahan biner dengan jumlah bit terbatas, sehingga operasi *floating-point* menyimpan hasil pendekatan terdekat. Digit tambahan yang terlihat pada keluaran memperlihatkan selisih pembulatan itu.

Tampilan `%.17f` sengaja memperlihatkan banyak angka setelah titik desimal. Tampilan yang lebih pendek, misalnya `%.1f`, dapat mencetak `0.3`, tetapi tidak mengubah nilai `double` yang tersimpan.
