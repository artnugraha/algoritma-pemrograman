# Solusi Latihan Kuliah 1: Pengenalan Algoritma, Komputer, dan Representasi Data

Solusi ini mengikuti bagian **Latihan** pada [catatan kuliah pertemuan pertama](https://github.com/artnugraha/algoritma-pemrograman/blob/main/Catatan-Kuliah/pertemuan-01.md). 

## 1. Representasi biner

### Soal

Konversikan bilangan berikut ke desimal:
```math
1011_2
```
```math
100101_2
```
```math
11111111_2
```
```math
10000000_2
```
Konversikan bilangan berikut ke biner:
```math
7_{10}
```
```math
18_{10}
```
```math
25_{10}
```
```math
42_{10}
```
```math
100_{10}
```

### Solusi

Untuk mengubah biner ke desimal, jumlahkan digit yang bernilai satu setelah dikalikan dengan nilai posisinya. Posisi dihitung mulai dari nol pada digit paling kanan.

```math
\begin{aligned}
1011_2 &= 1(2^3)+0(2^2)+1(2^1)+1(2^0)=8+2+1=11_{10},\\
100101_2 &= 1(2^5)+0(2^4)+0(2^3)+1(2^2)+0(2^1)+1(2^0)\\
&=32+4+1=37_{10},\\
11111111_2 &= 2^7+2^6+2^5+2^4+2^3+2^2+2^1+2^0=255_{10},\\
10000000_2 &= 1(2^7)=128_{10}.
\end{aligned}
```

Untuk mengubah desimal ke biner, tuliskan setiap bilangan sebagai jumlah pangkat dua yang berbeda. Koefisien pada setiap posisi kemudian menjadi digit biner, termasuk nol pada posisi yang dilewati.

```math
\begin{aligned}
7_{10} &= 4+2+1=111_2,\\
18_{10} &= 16+2=10010_2,\\
25_{10} &= 16+8+1=11001_2,\\
42_{10} &= 32+8+2=101010_2,\\
100_{10} &= 64+32+4=1100100_2.
\end{aligned}
```

Sebagai pemeriksaan untuk bilangan terakhir, `1100100` mempunyai bit satu pada posisi 6, 5, dan 2. Nilainya adalah $2^6+2^5+2^2=64+32+4=100$.

## 2. Representasi heksadesimal

### Soal

Ubah bilangan berikut dari biner menjadi heksadesimal:
```math
1111_2
```
```math
1010_2
```
```math
11111111_2
```
```math
10101111_2
```
```math
1100101011110000_2
```
Kemudian ubah
```math
3A_{16}
```
dan
```math
FF_{16}
```
ke bentuk desimal.

### Solusi

Satu digit heksadesimal menyatakan empat bit karena $16=2^4$. Kelompokkan digit biner menjadi kelompok empat dari kanan ke kiri, lalu ubah setiap kelompok menjadi satu digit heksadesimal.

| Bilangan biner | Pengelompokan empat bit | Heksadesimal |
|---|---|---|
| $1111_2$ | `1111` | $F_{16}$ |
| $1010_2$ | `1010` | $A_{16}$ |
| $11111111_2$ | `1111 1111` | $FF_{16}$ |
| $10101111_2$ | `1010 1111` | $AF_{16}$ |
| $1100101011110000_2$ | `1100 1010 1111 0000` | $CAF0_{16}$ |

Untuk arah sebaliknya, nilai digit $A$ adalah 10 dan nilai digit $F$ adalah 15. Karena kedua bilangan memiliki dua digit, digit di sebelah kiri dikalikan 16 dan digit di sebelah kanan dikalikan 1.

```math
\begin{aligned}
3A_{16} &= 3(16^1)+10(16^0)=48+10=58_{10},\\
FF_{16} &= 15(16^1)+15(16^0)=240+15=255_{10}.
\end{aligned}
```

## 3. Rentang integer

### Soal

Jika sebuah *unsigned integer* menggunakan 10 bit, tentukan:
- jumlah pola bit yang mungkin;
- nilai minimum;
- nilai maksimum.

Ulangi untuk *unsigned integer* 16 bit. 

Kemudian, tentukan rentang *signed integer* 8 bit dan *signed integer* 16 bit dengan asumsi representasi *two's complement*.

### Solusi

Sebanyak $n$ bit memberikan $2^n$ pola. Untuk *unsigned integer*, seluruh pola menyatakan bilangan dari 0 sampai $2^n-1$.

| Representasi | Banyak pola | Nilai minimum | Nilai maksimum |
|---|---:|---:|---:|
| *Unsigned* 10 bit | $2^{10}=1024$ | 0 | $2^{10}-1=1023$ |
| *Unsigned* 16 bit | $2^{16}=65536$ | 0 | $2^{16}-1=65535$ |

Dalam representasi *two's complement*, rentang bilangan bertanda dengan $n$ bit adalah $-2^{n-1}$ sampai $2^{n-1}-1$. Bagian negatif mempunyai satu nilai lebih banyak karena nol menggunakan salah satu pola yang tersedia.

| Representasi | Nilai minimum | Nilai maksimum | Rentang |
|---|---:|---:|---|
| *Signed* 8 bit | $-2^7=-128$ | $2^7-1=127$ | $[-128,127]$ |
| *Signed* 16 bit | $-2^{15}=-32768$ | $2^{15}-1=32767$ | $[-32768,32767]$ |

## 4. Memahami *overflow*

### Soal

Sebuah *unsigned integer* 8 bit memiliki nilai maksimum
```math
255.
```
Jelaskan mengapa nilai
```math
256
```
tidak dapat direpresentasikan menggunakan delapan bit.
Berapa banyak bit minimum yang diperlukan untuk merepresentasikan
```math
256
```
sebagai *unsigned integer*?

### Solusi

Delapan bit mempunyai $2^8=256$ pola yang menyatakan nilai 0 sampai 255. Karena $256=2^8=100000000_2$, penulisannya memerlukan satu bit bernilai satu pada posisi 8, disusul delapan bit nol.

Dengan demikian, **sembilan bit** merupakan jumlah minimum untuk menyimpan 256 sebagai *unsigned integer*. Jika operasi pada *unsigned integer* 8 bit menghasilkan 256 dalam aritmetika C, nilai yang tersimpan akan kembali menjadi 0 menurut aritmetika modulo $2^8$; hasil itu bukan representasi delapan bit dari nilai 256.

## 5. Floating-point

### Soal

Jelaskan dengan kalimat sendiri mengapa komputer tidak selalu dapat menyimpan nilai
```math
0.1
```
secara eksak.
Apa hubungan masalah tersebut dengan representasi
```math
\frac13=0.333333\ldots
```
dalam sistem desimal?
Mengapa perbandingan dua hasil floating-point menggunakan kesamaan eksak (misal $0.3 = 0.2 + 0.1$) dapat menimbulkan masalah?

### Solusi

Nilai $0.1=1/10$ mempunyai penulisan berulang dalam basis dua, sehingga sejumlah bit yang terbatas tidak dapat menyimpan semua digit binernya. Sistem *floating-point* menyimpan nilai biner terdekat yang dapat direpresentasikan; akibatnya, nilai yang tersimpan umumnya merupakan pendekatan terhadap $0.1$.

Keadaan ini serupa dengan $1/3=0.333333\ldots$ dalam basis sepuluh. Jika tersedia tempat untuk empat angka setelah koma, misalnya, kita hanya dapat menyimpan $0.3333$ atau hasil pembulatan lain yang masih mendekati $1/3$, bukan nilainya secara eksak.

Secara matematis, $0.3=0.2+0.1$. Dalam *floating-point*, ketiga bilangan tersebut dibulatkan ke nilai yang dapat disimpan, dan penjumlahannya juga dapat dibulatkan; karena itu, hasil yang tersimpan untuk `0.2 + 0.1` dapat berbeda sedikit dari nilai yang tersimpan untuk `0.3`. Untuk perhitungan yang membutuhkan penilaian kesamaan hampiran, bandingkan selisih mutlak dengan toleransi yang sesuai skala persoalan, misalnya $|a-b|<\varepsilon$, sambil memperhatikan ketelitian data yang dipakai.

## 6. Algoritma sederhana

### Soal

Tuliskan algoritma dengan kalimat biasa untuk menghitung daya listrik dari
```math
P=VI.
```
Tentukan dengan jelas yang mana
- input;
- proses;
- output.

Lakukan hal yang sama untuk persamaan gas ideal
```math
PV=nRT
```
dengan tujuan mencari tekanan $P$.

### Solusi

**Daya listrik.** *Input* adalah tegangan $V$ dalam volt dan arus $I$ dalam ampere. *Proses* adalah perkalian $P=VI$, dan *output* adalah daya $P$ dalam watt.

```text
Baca tegangan V
Baca arus I
Hitung P = V * I
Tampilkan P
```

**Tekanan gas ideal.** *Input* adalah jumlah zat $n$ dalam mol, temperatur mutlak $T$ dalam kelvin, volume $V$ dalam meter kubik, serta konstanta gas $R$ dalam joule per mol per kelvin. *Proses* adalah $P=nRT/V$, dan *output* adalah tekanan $P$ dalam pascal.

```text
Baca jumlah zat n
Baca temperatur T
Baca volume V
Tentukan konstanta gas R
Jika V <= 0, laporkan input tidak sah dan hentikan perhitungan
Hitung P = n * R * T / V
Tampilkan P
```

Langkah pemeriksaan volume memastikan pembagian dengan nol tidak terjadi. Dalam pemakaian fisis, jumlah zat dan temperatur mutlak juga perlu mempunyai nilai yang sesuai dengan kondisi sistem.

## 7. Program C sederhana

### Soal

Buat program
```text
power.c
```
untuk menghitung daya listrik dari
```math
P=VI.
```
Gunakan
```math
V=12.0\text{ V},
```
dan
```math
I=2.5\text{ A}.
```

Hitung terlebih dahulu hasilnya secara manual. Kemudian bandingkan dengan keluaran program.Kompilasi menggunakan
```bash
gcc -Wall -Wextra power.c -o power
```
Program yang baik pada tahap ini setidaknya harus dapat dikompilasi tanpa peringatan (*warning*).

### Solusi

Perhitungan manual memberikan
```math
P=VI=(12.0\text{ V})(2.5\text{ A})=30.0\text{ W}.
```
Program berikut menggunakan nilai masukan yang ditetapkan oleh soal. Simpan blok ini sebagai `power.c`.

```c
#include <stdio.h>

int main(void)
{
    double voltage = 12.0;
    double current = 2.5;

    double power = voltage * current;

    printf("Power = %f W\n", power);

    return 0;
}
```

Kompilasi dan jalankan program di Linux atau WSL:

```bash
gcc -Wall -Wextra power.c -o power
./power
```

Keluaran yang diharapkan adalah

```text
Power = 30.000000 W
```

Angka `30.000000` sama dengan hasil manual $30.0\text{ W}$ pada ketelitian tampilan yang dipilih oleh `printf`. Berhasilnya kompilasi tanpa peringatan tetap perlu disertai pemeriksaan hasil dan satuannya.

## 8. Program gerak lurus

### Soal

Buat program
```text
motion.c
```
yang menghitung
```math
x
=
x_0+v_0t+\frac12at^2.
```
Gunakan
```math
x_0=2.0\text{ m},
```
```math
v_0=5.0\text{ m/s},
```
```math
a=3.0\text{ m/s}^2,
```
dan
```math
t=4.0\text{ s}.
```

Program harus menampilkan nilai
- posisi awal;
- kecepatan awal;
- percepatan;
- waktu;
- posisi akhir.

Sebelum menjalankan program, hitung hasilnya secara manual. Setelah menjalankan program, periksa apakah kedua hasil tersebut sesuai.

### Solusi

Hitung terlebih dahulu perpindahan akibat kecepatan awal dan percepatan. Penjumlahan dengan posisi awal memberikan prediksi posisi akhir:

```math
\begin{aligned}
x &= x_0+v_0t+\frac12at^2\\
  &= 2.0+(5.0)(4.0)+\frac12(3.0)(4.0)^2\\
  &= 2.0+20.0+24.0=46.0\text{ m}.
\end{aligned}
```

Simpan program berikut sebagai `motion.c`. Kuadrat waktu dinyatakan dengan `time * time`, sesuai pola perkalian pada catatan kuliah.

```c
#include <stdio.h>

int main(void)
{
    double x0 = 2.0;
    double v0 = 5.0;
    double acceleration = 3.0;
    double time = 4.0;

    double position =
        x0
        + v0 * time
        + 0.5 * acceleration * time * time;

    printf("Initial position = %f m\n", x0);
    printf("Initial velocity = %f m/s\n", v0);
    printf("Acceleration     = %f m/s^2\n", acceleration);
    printf("Time             = %f s\n", time);
    printf("Final position   = %f m\n", position);

    return 0;
}
```

Kompilasi dan jalankan program di Linux atau WSL:

```bash
gcc -Wall -Wextra motion.c -o motion
./motion
```

Keluaran yang diharapkan adalah

```text
Initial position = 2.000000 m
Initial velocity = 5.000000 m/s
Acceleration     = 3.000000 m/s^2
Time             = 4.000000 s
Final position   = 46.000000 m
```

Posisi akhir program sesuai dengan hasil manual, yaitu $46.0\text{ m}$. Empat nilai lain pada keluaran juga sesuai dengan data awal yang ditetapkan dalam soal.
