# Solusi Latihan Kuliah 4: Percabangan dan Pengulangan

## 1. Klasifikasi temperatur

### Soal

Buat program yang membaca temperatur dan menampilkan

```text
DINGIN
```

jika

```math
T<20^\circ\text{C},
```

```text
NORMAL
```

jika

```math
20^\circ\text{C}
\leq T
\leq
30^\circ\text{C},
```

dan

```text
PANAS
```

jika

```math
T>30^\circ\text{C}.
```

Uji tepat pada nilai

```math
20
```

dan

```math
30.
```

### Solusi

Gunakan batas dalam urutan yang membuat kedua titik ujung masuk kategori `NORMAL`. Program berikut membaca satu temperatur dan menampilkan tepat satu status.

```c
#include <stdio.h>

int main(void)
{
    double temperature;

    if (scanf("%lf", &temperature) != 1)
    {
        puts("Invalid input.");
        return 1;
    }

    if (temperature < 20.0)
    {
        puts("DINGIN");
    }
    else if (temperature <= 30.0)
    {
        puts("NORMAL");
    }
    else
    {
        puts("PANAS");
    }

    return 0;
}
```

Untuk $T=20$ dan $T=30$, keluaran sama-sama `NORMAL`. Nilai tepat di bawah 20 masuk `DINGIN`, sedangkan nilai tepat di atas 30 masuk `PANAS`.

## 2. Status tekanan

### Soal

Sebuah sistem memiliki rentang tekanan aman

```math
95\text{ kPa}
\leq P
\leq
105\text{ kPa}.
```

Buat program yang menampilkan

```text
LOW
NORMAL
HIGH
```

sesuai nilai tekanan.

### Solusi

Kondisi aman meliputi kedua batasnya, yaitu 95 kPa dan 105 kPa. Dengan demikian, tiga cabang dapat ditulis tanpa tumpang tindih sebagai berikut.

```c
#include <stdio.h>

int main(void)
{
    double pressure;

    if (scanf("%lf", &pressure) != 1)
    {
        puts("Invalid input.");
        return 1;
    }

    if (pressure < 95.0)
    {
        puts("LOW");
    }
    else if (pressure <= 105.0)
    {
        puts("NORMAL");
    }
    else
    {
        puts("HIGH");
    }

    return 0;
}
```

Untuk contoh pemeriksaan batas, $P=94{,}9$ menghasilkan `LOW`, $P=95$ dan $P=105$ menghasilkan `NORMAL`, sedangkan $P=105{,}1$ menghasilkan `HIGH`.

## 3. Bilangan Reynolds

### Soal

Buat program yang menghitung

```math
Re
=
\frac{\rho vL}{\mu}
```

dan mengklasifikasikan aliran sebagai

```text
laminar      : Re < 2300
transition   : 2300 <= Re < 4000
turbulent    : Re >= 4000
```

Gunakan `else if`.

### Solusi

Program menerima massa jenis $\rho$, laju $v$, panjang karakteristik $L$, dan viskositas dinamis $\mu$. Nilai $\mu=0$ harus ditolak agar pembagian terdefinisi.

```c
#include <stdio.h>

int main(void)
{
    double rho, v, length, mu;

    if (scanf("%lf %lf %lf %lf",
              &rho, &v, &length, &mu) != 4 ||
        rho < 0.0 || v < 0.0 ||
        length <= 0.0 || mu <= 0.0)
    {
        puts("Invalid input.");
        return 1;
    }

    double reynolds = rho * v * length / mu;
    printf("Re = %.2f\n", reynolds);

    if (reynolds < 2300.0)
    {
        puts("laminar");
    }
    else if (reynolds < 4000.0)
    {
        puts("transition");
    }
    else
    {
        puts("turbulent");
    }

    return 0;
}
```

Cabang kedua hanya diperiksa jika $Re\geq2300$, sehingga `Re = 2300` masuk `transition`. Nilai `Re = 4000` masuk `turbulent`.

## 4. Mode alat

### Soal

Buat program menggunakan `switch` untuk menu

```text
1. Standby
2. Measurement
3. Calibration
4. Shutdown
```

Jika input di luar

```math
1,2,3,4,
```

tampilkan

```text
Invalid mode.
```

### Solusi

Variabel `mode` bertipe `int`, sesuai dengan empat pilihan bilangan bulat pada menu. Setiap `case` diakhiri `break` agar satu pilihan tidak meneruskan eksekusi ke pilihan berikutnya.

```c
#include <stdio.h>

int main(void)
{
    int mode;

    puts("1. Standby");
    puts("2. Measurement");
    puts("3. Calibration");
    puts("4. Shutdown");

    if (scanf("%d", &mode) != 1)
    {
        puts("Invalid mode.");
        return 1;
    }

    switch (mode)
    {
        case 1: puts("Standby");     break;
        case 2: puts("Measurement"); break;
        case 3: puts("Calibration"); break;
        case 4: puts("Shutdown");    break;
        default: puts("Invalid mode.");
    }

    return 0;
}
```

Misalnya, masukan `3` menghasilkan `Calibration`; masukan `0` atau `5` menghasilkan `Invalid mode.` setelah menu ditampilkan.

## 5. `while`

### Soal

Gunakan `while` untuk mencetak

```text
1
2
3
...
20
```

Kemudian modifikasi agar hanya mencetak bilangan genap.

### Solusi

Pada bentuk pertama, `i` dimulai dari 1 dan bertambah satu setiap kali dicetak. Syarat `i <= 20` membuat 20 menjadi nilai terakhir yang dicetak.

```c
#include <stdio.h>

int main(void)
{
    int i = 1;

    while (i <= 20)
    {
        printf("%d\n", i);
        i++;
    }

    return 0;
}
```

Untuk versi yang hanya mencetak bilangan genap, ganti inisialisasi dan pembaruan pengulangannya dengan bentuk berikut. Kerangka program selebihnya tetap sama.

```c
int i = 2;

while (i <= 20)
{
    printf("%d\n", i);
    i += 2;
}
```

Keluaran versi kedua ialah `2, 4, 6, ..., 20`, masing-masing pada baris tersendiri. Pembaruan `i` pada kedua versi wajib ada agar pengulangan berhenti.

## 6. `for`

### Soal

Gunakan `for` untuk mencetak nilai

```math
t=0,1,\ldots,10
```

dan posisi

```math
x(t)
=
x_0+v_0t+\frac12at^2
```

dengan

```math
x_0=0,
```

```math
v_0=2\text{ m/s},
```

dan

```math
a=1\text{ m/s}^2.
```

### Solusi

Substitusi $x_0=0$, $v_0=2$, dan $a=1$ menghasilkan $x(t)=2t+0{,}5t^2$ meter. Gunakan `int` untuk waktu $t$ yang diminta dan `double` untuk hasil posisi.

```c
#include <stdio.h>

int main(void)
{
    const double x0 = 0.0;
    const double v0 = 2.0;
    const double a = 1.0;

    puts("t (s)  x (m)");
    for (int t = 0; t <= 10; t++)
    {
        double x = x0 + v0 * t + 0.5 * a * t * t;
        printf("%5d  %5.2f\n", t, x);
    }

    return 0;
}
```

Sebelas baris data dihasilkan: untuk $t=0$, $x=0{,}00$ m; untuk $t=1$, $x=2{,}50$ m; dan untuk $t=10$, $x=70{,}00$ m.

## 7. Jumlah dan rata-rata

### Soal

Buat program yang membaca

```math
N
```

data real, kemudian menghitung

```math
S
=
\sum_{i=1}^{N}x_i
```

dan

```math
\overline{x}
=
\frac{S}{N}.
```

Pastikan program menolak

```math
N\leq0.
```

### Solusi

Inisialisasikan `sum` dengan nol, lalu tambahkan setiap bilangan yang berhasil dibaca. Jumlah data $N$ harus diketahui dan positif sebelum menghitung rata-rata.

```c
#include <stdio.h>

int main(void)
{
    int n;
    double sum = 0.0;

    if (scanf("%d", &n) != 1 || n <= 0)
    {
        puts("Invalid number of data.");
        return 1;
    }

    for (int i = 0; i < n; i++)
    {
        double x;
        if (scanf("%lf", &x) != 1)
        {
            puts("Invalid data.");
            return 1;
        }
        sum += x;
    }

    printf("Sum  = %.3f\n", sum);
    printf("Mean = %.3f\n", sum / n);

    return 0;
}
```

Contoh untuk $N=3$ dan data $2,4,6$ memberikan $S=12$ dan $\overline{x}=4$. Penolakan $N\leq0$ juga mencegah pembagian dengan nol.

## 8. Minimum dan maksimum

### Soal

Buat program yang membaca

```math
N
```

data dan menampilkan nilai minimum serta maksimum.

Uji menggunakan data positif:

```math
3,\quad5,\quad2,\quad8
```

dan data negatif:

```math
-3,\quad-5,\quad-2,\quad-8.
```

Pastikan algoritma benar untuk keduanya.

### Solusi

Gunakan data pertama sebagai nilai awal minimum dan maksimum. Cara ini tetap benar ketika seluruh data negatif; mengawali maksimum dengan nol justru akan memberi hasil keliru pada kasus tersebut.

```c
#include <stdio.h>

int main(void)
{
    int n;
    double x, minimum, maximum;

    if (scanf("%d", &n) != 1 || n <= 0)
    {
        puts("Invalid number of data.");
        return 1;
    }
    if (scanf("%lf", &x) != 1)
    {
        puts("Invalid data.");
        return 1;
    }

    minimum = x;
    maximum = x;

    for (int i = 1; i < n; i++)
    {
        if (scanf("%lf", &x) != 1)
        {
            puts("Invalid data.");
            return 1;
        }
        if (x < minimum) minimum = x;
        if (x > maximum) maximum = x;
    }

    printf("Minimum = %.2f\n", minimum);
    printf("Maximum = %.2f\n", maximum);

    return 0;
}
```

Untuk $3,5,2,8$, minimum 2 dan maksimum 8. Untuk $-3,-5,-2,-8$, minimum $-8$ dan maksimum $-2$.

## 9. Counter ambang

### Soal

Baca

```math
N
```

data temperatur.

Hitung berapa data yang memenuhi

```math
T>30^\circ\text{C}.
```

Tampilkan jumlah dan persentasenya.

### Solusi

Variabel `count` bertambah hanya jika temperatur lebih besar secara ketat dari 30. Persentase dihitung setelah seluruh $N$ data dibaca.

```c
#include <stdio.h>

int main(void)
{
    int n, count = 0;

    if (scanf("%d", &n) != 1 || n <= 0)
    {
        puts("Invalid number of data.");
        return 1;
    }

    for (int i = 0; i < n; i++)
    {
        double temperature;
        if (scanf("%lf", &temperature) != 1)
        {
            puts("Invalid data.");
            return 1;
        }
        if (temperature > 30.0)
        {
            count++;
        }
    }

    printf("Count = %d\n", count);
    printf("Percentage = %.2f%%\n",
           100.0 * count / n);

    return 0;
}
```

Misalnya, untuk $29,30,31,32$, terdapat 2 dari 4 data di atas 30, sehingga persentasenya $50{,}00\%$. Data yang sama dengan 30 tidak ikut dihitung.

## 10. Validasi input

### Soal

Gunakan `do-while` untuk membaca efisiensi

```math
\eta
```

sampai memenuhi

```math
0\leq\eta\leq1.
```

Program harus terus meminta input jika nilai tidak valid.

### Solusi

Pengulangan `do-while` menjalankan pembacaan sekurang-kurangnya sekali. Jika masukan bukan bilangan, sisa baris dibuang agar pembacaan berikutnya dapat berlangsung; jika akhir berkas tercapai, program berhenti.

```c
#include <stdio.h>

int main(void)
{
    double eta = -1.0;

    do
    {
        printf("Efficiency [0, 1]: ");
        int status = scanf("%lf", &eta);

        if (status == EOF)
        {
            puts("No input.");
            return 1;
        }
        if (status != 1)
        {
            int ch;
            do
            {
                ch = getchar();
            } while (ch != '\n' && ch != EOF);

            if (ch == EOF)
            {
                puts("No input.");
                return 1;
            }
            eta = -1.0;
        }

        if (!(eta >= 0.0 && eta <= 1.0))
        {
            puts("Invalid efficiency.");
        }
    } while (!(eta >= 0.0 && eta <= 1.0));

    printf("Efficiency = %.3f\n", eta);
    return 0;
}
```

Nilai 0 dan 1 diterima, sedangkan $-0{,}1$, $1{,}1$, dan teks nonnumerik mengakibatkan permintaan ulang. Bentuk negasi pada kondisi juga menolak nilai bukan bilangan yang dapat dibaca sebagai `NaN`.

## 11. Deret

### Soal

Hitung

```math
S_N
=
\sum_{n=1}^{N}\frac{1}{n^2}
```

untuk beberapa nilai

```math
N.
```

Bandingkan dengan

```math
\frac{\pi^2}{6}.
```

Gunakan

```math
\pi
\approx
3.141592653589793.
```

Amati bagaimana hasil berubah ketika

```math
N
```

diperbesar.

### Solusi

Untuk membandingkan beberapa $N$ tanpa memasukkan data berulang kali, pilih $N=10,100,1000,10000$. Variabel `sum` diatur ulang pada setiap pilihan, kemudian dibandingkan dengan pendekatan $\pi^2/6$.

```c
#include <stdio.h>

int main(void)
{
    const double pi = 3.141592653589793;
    const double reference = pi * pi / 6.0;

    puts("N        S_N          pi^2/6       difference");
    for (int n = 10; n <= 10000; n *= 10)
    {
        double sum = 0.0;
        for (int k = 1; k <= n; k++)
        {
            sum += 1.0 / ((double) k * k);
        }
        printf("%-6d  %.9f  %.9f  %.9f\n",
               n, sum, reference, reference - sum);
    }

    return 0;
}
```

Contoh hasil perhitungan adalah sebagai berikut; nilai pembandingnya $\pi^2/6\approx1{,}644934067$.

| $N$ | $S_N$ | $\pi^2/6-S_N$ |
|---:|---:|---:|
| 10 | 1,549767731 | 0,095166336 |
| 100 | 1,634983900 | 0,009950167 |
| 1000 | 1,643934567 | 0,000999500 |
| 10000 | 1,644834072 | 0,000099995 |

Semua suku $1/k^2$ positif, sehingga jumlah parsial bertambah saat $N$ bertambah. Selisih terhadap $\pi^2/6$ berkurang, tetapi untuk setiap $N$ berhingga hasilnya masih lebih kecil daripada nilai pembanding tersebut.

## 12. Tabel Hukum Hooke

### Soal

Gunakan

```math
F=-kx
```

dengan

```math
k=100\text{ N/m}.
```

Cetak tabel untuk

```math
x=-0.10,-0.09,\ldots,0.10\text{ m}.
```

Gunakan `for`.

### Solusi

Gunakan indeks bilangan bulat $i=-10,-9,\ldots,10$ dan tetapkan $x=i/100{,}0$ m. Cara ini menghasilkan 21 baris tanpa mengandalkan penjumlahan berulang pada bilangan pecahan untuk menentukan kapan `for` berhenti.

```c
#include <stdio.h>

int main(void)
{
    const double k = 100.0;

    puts("x (m)    F (N)");
    for (int i = -10; i <= 10; i++)
    {
        double x = i / 100.0;
        double force = -k * x;
        printf("%6.2f  %7.2f\n", x, force);
    }

    return 0;
}
```

Sebagai pemeriksaan, pada $x=-0{,}10$ m didapat $F=10$ N, pada $x=0$ didapat $F=0$, dan pada $x=0{,}10$ m didapat $F=-10$ N. Tanda negatif menunjukkan bahwa gaya pemulih berlawanan arah dengan simpangan.

## 13. Pengulangan bersarang

### Soal

Buat program yang mencetak tabel perkalian

```math
1
```

sampai

```math
10.
```

Gunakan dua `for` bersarang.

Jelaskan mengapa jumlah operasi bertumbuh secara kuadratik terhadap ukuran tabel.

### Solusi

Pengulangan luar memilih baris pengali, sedangkan pengulangan dalam menghitung sepuluh hasil kali di baris itu. Lebar format `%4d` merapikan tampilan tabel.

```c
#include <stdio.h>

int main(void)
{
    for (int row = 1; row <= 10; row++)
    {
        for (int column = 1; column <= 10; column++)
        {
            printf("%4d", row * column);
        }
        printf("\n");
    }

    return 0;
}
```

Baris pertama memuat $1,2,\ldots,10$ dan baris terakhir memuat $10,20,\ldots,100$. Untuk tabel berukuran $M\times M$, blok dalam dijalankan $M$ kali untuk masing-masing dari $M$ baris, sehingga ada $M^2$ perhitungan hasil kali, yaitu $O(M^2)$. Tabel soal berisi $10^2=100$ hasil kali.

## 14. Mencari kesalahan

### Soal

Perhatikan program berikut.

```c
#include <stdio.h>

int main(void)
{
    int i = 1;

    while (i <= 10)
    {
        printf("%d\n", i);
    }

    return 0;
}
```

Jelaskan masalahnya dan perbaiki.

### Solusi

Nilai `i` tidak berubah di dalam `while` pada program asal. Karena kondisi `i <= 10` selalu benar setelah `i` mulai dari 1, program terus mencetak `1` dan tidak berhenti.

Tambahkan pembaruan `i++` setelah pencetakan.

```c
#include <stdio.h>

int main(void)
{
    int i = 1;

    while (i <= 10)
    {
        printf("%d\n", i);
        i++;
    }

    return 0;
}
```

Sekarang keluaran adalah bilangan 1 sampai 10, masing-masing sekali. Setelah `i` bernilai 11, kondisi `while` menjadi salah.

## 15. Mencari kesalahan batas

### Soal

Perhatikan:

```c
for (int i = 0; i <= 10; i++)
{
    printf("%d\n", i);
}
```

Berapa banyak nilai yang dicetak?

Jika tujuan sebenarnya adalah mencetak tepat 10 nilai mulai dari nol, perbaiki batasnya.

### Solusi

Pengulangan asal memiliki indeks $0,1,\ldots,10$, sehingga mencetak **11 nilai**. Angka nol dihitung sebagai nilai pertama, bukan sebagai batas yang diabaikan.

Untuk mencetak tepat sepuluh nilai mulai dari nol, gunakan syarat `i < 10`:

```c
for (int i = 0; i < 10; i++)
{
    printf("%d\n", i);
}
```

Keluaran yang benar adalah 0 sampai 9. Ketika `i` mencapai 10, kondisi sudah salah dan badan pengulangan tidak dijalankan lagi.

## 16. Monitoring temperatur

### Soal

Buat program lengkap yang membaca

- jumlah pengukuran;
- ambang temperatur;
- seluruh data temperatur;

kemudian menghitung

- rata-rata;
- minimum;
- maksimum;
- jumlah data di atas ambang.

Gunakan

```text
if
for
```

dan uji menggunakan

```math
T=
\{29.5,\ 30.2,\ 28.9,\ 31.1,\ 30.0\}.
```

### Solusi

Data dapat diproses saat dibaca, tanpa perlu disimpan dalam larik. Gunakan data pertama untuk inisialisasi minimum dan maksimum, lalu lanjutkan pembacaan data lainnya.

```c
#include <stdio.h>

int main(void)
{
    int n, above = 0;
    double threshold, temperature;
    double sum = 0.0, minimum, maximum;

    if (scanf("%d %lf", &n, &threshold) != 2 || n <= 0)
    {
        puts("Invalid input.");
        return 1;
    }

    for (int i = 0; i < n; i++)
    {
        if (scanf("%lf", &temperature) != 1)
        {
            puts("Invalid temperature.");
            return 1;
        }

        sum += temperature;
        if (i == 0)
        {
            minimum = temperature;
            maximum = temperature;
        }
        else
        {
            if (temperature < minimum) minimum = temperature;
            if (temperature > maximum) maximum = temperature;
        }

        if (temperature > threshold)
        {
            above++;
        }
    }

    printf("Mean = %.2f\n", sum / n);
    printf("Minimum = %.2f\n", minimum);
    printf("Maximum = %.2f\n", maximum);
    printf("Above threshold = %d\n", above);

    return 0;
}
```

Untuk pengujian, pilih $N=5$ dan ambang $30{,}0^\circ\text{C}$, lalu masukkan $29{,}5$, $30{,}2$, $28{,}9$, $31{,}1$, dan $30{,}0$. Jumlahnya $149{,}7$, sehingga rata-ratanya $29{,}94^\circ\text{C}$; minimum $28{,}9^\circ\text{C}$, maksimum $31{,}1^\circ\text{C}$, dan jumlah di atas ambang adalah 2. Nilai tepat pada ambang tidak masuk hitungan.

## 17. Tantangan: berhenti dengan sentinel

### Soal

Buat program yang terus membaca temperatur sampai pengguna memasukkan

```math
-999.
```

Nilai

```math
-999
```

digunakan sebagai *sentinel* dan tidak ikut dihitung.

Setelah input selesai, tampilkan

- jumlah data valid;
- rata-rata.

Jika tidak ada data valid, jangan lakukan pembagian.

### Solusi

Periksa nilai sentinel segera setelah pembacaan dan sebelum memperbarui jumlah maupun banyak data. Dengan begitu, `-999` tidak ikut dalam statistik.

```c
#include <stdio.h>

int main(void)
{
    int count = 0;
    double sum = 0.0;

    while (1)
    {
        double temperature;
        if (scanf("%lf", &temperature) != 1)
        {
            puts("Invalid input.");
            return 1;
        }
        if (temperature == -999.0)
        {
            break;
        }

        sum += temperature;
        count++;
    }

    printf("Valid data = %d\n", count);
    if (count > 0)
    {
        printf("Mean = %.2f\n", sum / count);
    }
    else
    {
        puts("No valid data; mean is undefined.");
    }

    return 0;
}
```

Masukan `29 31 -999` menghasilkan banyak data valid 2 dan rata-rata 30. Jika masukan pertama adalah `-999`, banyak data valid 0 dan rata-rata tidak dihitung.

## 18. Tantangan: pendekatan akar

### Soal

Gunakan metode sederhana dengan langkah

```math
\Delta x=0.001
```

untuk mencari pendekatan

```math
\sqrt{2}.
```

Mulai dari

```math
x=0.
```

Naikkan `x` sampai

```math
x^2\geq2.
```

Bandingkan hasil dengan nilai referensi sekitar

```math
1.41421356.
```

Diskusikan kekurangan metode ini.

### Solusi

Mulai dari $x=0$ dan naikkan sebesar $0{,}001$ selama $x^2<2$. Pada iterasi pertama ketika $x^2\geq2$, tampilkan nilai tersebut dan bandingkan dengan referensi.

```c
#include <stdio.h>

int main(void)
{
    const double step = 0.001;
    const double reference = 1.41421356;
    double x = 0.0;
    int iterations = 0;

    while (x * x < 2.0)
    {
        x += step;
        iterations++;
    }

    printf("Approximation = %.3f\n", x);
    printf("Reference     = %.8f\n", reference);
    printf("Difference    = %.8f\n", x - reference);
    printf("Iterations    = %d\n", iterations);

    return 0;
}
```

Nilai yang pertama kali memenuhi syarat adalah sekitar $x=1{,}415$, setelah 1415 pembaruan. Selisihnya dari referensi sekitar $1{,}415-1{,}41421356=0{,}00078644$. Hasil hanya seteliti ukuran langkah dan selalu memilih nilai dari sisi atas untuk bilangan positif. Langkah yang lebih kecil memperbaiki resolusi tetapi menambah banyak iterasi; metode seperti Babilonia jauh lebih cepat untuk ketelitian tinggi.

