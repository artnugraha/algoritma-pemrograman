# Solusi Latihan Kuliah 5: Pola Algoritma Iteratif

## 1. Analisis data arus listrik metode *streaming*

### Soal

Sebuah sistem akuisisi membaca arus listrik satu per satu tanpa mengetahui jumlah data sebelumnya. Input dihentikan menggunakan sentinel `-999`, sedangkan data valid harus berada pada rentang

```math
-20
\leq I
\leq
20\text{ A}.
```

Buat algoritma dan program C yang dalam satu kali penelusuran menghitung jumlah data valid, rata-rata, minimum, maksimum, RMS, serta jumlah data yang memenuhi

```math
|I|>10\text{ A}.
```

Program tidak boleh menyimpan seluruh data dalam larik. Jelaskan mengapa kebutuhan memori tambahannya tetap $O(1)$ dan lakukan tracing menggunakan sekurang-kurangnya enam input yang mencakup data valid, data tidak valid, dan sentinel.

### Solusi

### Algoritma

Sentinel diperiksa lebih dahulu, lalu rentang valid diperiksa sebelum keadaan statistik diperbarui. Simpan `count`, `sum`, `sum_square`, `minimum`, `maximum`, dan `count_high` sebagai keadaan yang berubah selama pembacaan.

```text
count ← 0
sum ← 0
sum_square ← 0
count_high ← 0
WHILE true
    INPUT I
    IF input gagal THEN tampilkan kesalahan; STOP
    IF I = -999 THEN BREAK
    IF I < -20 OR I > 20 THEN tampilkan "Invalid data"; CONTINUE
    IF count = 0 THEN minimum ← I; maximum ← I
    ELSE
        IF I < minimum THEN minimum ← I
        IF I > maximum THEN maximum ← I
    END IF
    count ← count + 1
    sum ← sum + I
    sum_square ← sum_square + I*I
    IF |I| > 10 THEN count_high ← count_high + 1
END WHILE
IF count > 0 THEN
    mean ← sum / count
    rms ← sqrt(sum_square / count)
    OUTPUT count, mean, minimum, maximum, rms, count_high
ELSE
    OUTPUT "No valid data"
END IF
```

### Program C

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    int count = 0, count_high = 0;
    double sum = 0.0, sum_square = 0.0;
    double minimum = 0.0, maximum = 0.0;

    while (1)
    {
        double current;
        if (scanf("%lf", &current) != 1)
        {
            puts("Invalid input.");
            return 1;
        }
        if (current == -999.0) break;
        if (current < -20.0 || current > 20.0)
        {
            puts("Invalid data.");
            continue;
        }

        if (count == 0)
        {
            minimum = current;
            maximum = current;
        }
        else
        {
            if (current < minimum) minimum = current;
            if (current > maximum) maximum = current;
        }

        count++;
        sum += current;
        sum_square += current * current;
        if (fabs(current) > 10.0) count_high++;
    }

    if (count == 0)
    {
        puts("No valid data.");
        return 0;
    }

    printf("Count   = %d\n", count);
    printf("Mean    = %.3f A\n", sum / count);
    printf("Minimum = %.3f A\n", minimum);
    printf("Maximum = %.3f A\n", maximum);
    printf("RMS     = %.3f A\n", sqrt(sum_square / count));
    printf("|I| > 10 A = %d\n", count_high);
    return 0;
}
```

Kompilasi dengan `gcc -Wall -Wextra -Wpedantic -std=c17 arus.c -lm -o arus`. Contoh tracing untuk tujuh input berikut memakai `-999` sebagai input ketujuh.

| Input $I$ (A) | Tindakan | `count` | `sum` | `sum_square` | `minimum` | `maximum` | `count_high` |
|---:|---|---:|---:|---:|---:|---:|---:|
| 8 | diterima | 1 | 8 | 64 | 8 | 8 | 0 |
| 25 | ditolak | 1 | 8 | 64 | 8 | 8 | 0 |
| -12 | diterima | 2 | -4 | 208 | -12 | 8 | 1 |
| 0 | diterima | 3 | -4 | 208 | -12 | 8 | 1 |
| -25 | ditolak | 3 | -4 | 208 | -12 | 8 | 1 |
| 15 | diterima | 4 | 11 | 433 | -12 | 15 | 2 |
| -999 | berhenti | 4 | 11 | 433 | -12 | 15 | 2 |

Hasilnya adalah rata-rata $11/4=2{,}75$ A, RMS $\sqrt{433/4}\approx10{,}404$ A, minimum $-12$ A, dan maksimum $15$ A. Hanya sejumlah tetap variabel skalar disimpan, terlepas dari banyak data yang masuk. Karena itu, kebutuhan memori tambahan adalah $O(1)$; satu kali penelusuran atas $M$ input membutuhkan waktu $O(M)$.

## 2. Statistik getaran dengan dua ambang

### Soal

Sebuah akselerometer menghasilkan data percepatan $a_i$. Gunakan dua ambang,

```math
a_{\text{warning}}=5\text{ m/s}^2
```

dan

```math
a_{\text{danger}}=10\text{ m/s}^2.
```

Buat program yang mengklasifikasikan amplitudo setiap data berdasarkan $|a_i|$ menjadi `NORMAL`, `WARNING`, atau `DANGER`. Dalam satu loop, hitung jumlah data pada setiap kategori, RMS keseluruhan, dan persentase kategori `DANGER`.

### Solusi

Karena soal tidak menentukan sentinel, gunakan banyak data $N>0$ sebagai masukan awal. Agar setiap data masuk tepat satu kategori, tetapkan `NORMAL` untuk $|a_i|\leq5$, `WARNING` untuk $5<|a_i|\leq10$, dan `DANGER` untuk $|a_i|>10$ dalam satuan m/s$^2$.

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    int n;
    int normal = 0, warning = 0, danger = 0;
    double sum_square = 0.0;

    if (scanf("%d", &n) != 1 || n <= 0)
    {
        puts("Invalid number of data.");
        return 1;
    }

    for (int i = 0; i < n; i++)
    {
        double a;
        if (scanf("%lf", &a) != 1)
        {
            puts("Invalid data.");
            return 1;
        }

        double amplitude = fabs(a);
        sum_square += a * a;

        if (amplitude <= 5.0)
        {
            normal++;
            printf("Data %d: NORMAL\n", i + 1);
        }
        else if (amplitude <= 10.0)
        {
            warning++;
            printf("Data %d: WARNING\n", i + 1);
        }
        else
        {
            danger++;
            printf("Data %d: DANGER\n", i + 1);
        }
    }

    printf("NORMAL  = %d\n", normal);
    printf("WARNING = %d\n", warning);
    printf("DANGER  = %d\n", danger);
    printf("RMS     = %.3f m/s^2\n", sqrt(sum_square / n));
    printf("DANGER  = %.2f%%\n", 100.0 * danger / n);
    return 0;
}
```

Kompilasi dengan `gcc -Wall -Wextra -Wpedantic -std=c17 getaran.c -lm -o getaran`. Untuk lima data $-12,-5,0,8,10$, jumlah tiap kategori berturut-turut adalah 2, 2, dan 1. Jumlah kuadratnya 333, sehingga RMS $=\sqrt{333/5}\approx8{,}161$ m/s$^2$, dan persentase `DANGER` adalah $20\%$. Nilai yang tepat sama dengan 5 masuk `NORMAL`, sedangkan yang tepat sama dengan 10 masuk `WARNING`.

## 3. Studi konvergensi deret

### Soal

Hitung

```math
S_N
=
\sum_{n=1}^{N}
\frac{1}{n^2}
```

untuk

```math
N=10,\quad100,\quad1000,\quad10000.
```

Bandingkan setiap hasil dengan

```math
S_\infty
=
\frac{\pi^2}{6}.
```

Buat tabel yang berisi $N$, $S_N$, dan galat absolut. Setelah itu, modifikasi program agar berhenti berdasarkan ukuran suku berikutnya, lalu jelaskan perbedaan antara penghentian berdasarkan $N$ dan penghentian berdasarkan toleransi.

### Solusi

Program berikut terlebih dahulu membuat tabel untuk empat nilai $N$. Setelah itu, program menghitung jumlah lain dengan toleransi pada **suku berikutnya**: jika $1/(n+1)^2<\tau$, jumlah berhenti pada suku ke-$n$. Contoh menggunakan $\tau=10^{-6}$.

```c
#include <stdio.h>

int main(void)
{
    const double pi = 3.141592653589793;
    const double reference = pi * pi / 6.0;
    const double tolerance = 1e-6;

    puts("N       S_N          Absolute error");
    for (int target = 10; target <= 10000; target *= 10)
    {
        double sum = 0.0;
        for (int n = 1; n <= target; n++)
        {
            double value = (double) n;
            sum += 1.0 / (value * value);
        }
        printf("%-6d  %.9f  %.9f\n",
               target, sum, reference - sum);
    }

    int n = 0;
    double sum = 0.0;
    do
    {
        n++;
        double value = (double) n;
        sum += 1.0 / (value * value);
        double next = 1.0 / ((value + 1.0) * (value + 1.0));
        if (next < tolerance) break;
    } while (1);

    printf("By next term: N=%d, S_N=%.9f, error=%.9f\n",
           n, sum, reference - sum);
    return 0;
}
```

| $N$ | $S_N$ | $|S_\infty-S_N|$ |
|---:|---:|---:|
| 10 | 1,549767731 | 0,095166336 |
| 100 | 1,634983900 | 0,009950167 |
| 1000 | 1,643934567 | 0,000999500 |
| 10000 | 1,644834072 | 0,000099995 |

Dengan $N$ tetap, jumlah operasi dapat diketahui sejak awal. Dengan toleransi suku berikutnya, banyak operasi ditentukan oleh nilai $\tau$: untuk $\tau=10^{-6}$ program berhenti pada $N=1000$, tetapi galat jumlahnya masih sekitar $9{,}995\times10^{-4}$. Suku berikutnya yang kecil **tidak** menjamin bahwa semua suku yang tersisa berjumlah lebih kecil daripada $\tau$. Untuk deret ini, uji integral memberi batas $1/(N+1)\leq S_\infty-S_N\leq1/N$.

## 4. Pengaruh ukuran langkah pada pencarian akar

### Soal

Cari pendekatan untuk

```math
\sqrt{7}
```

dengan metode langkah tetap. Lakukan eksperimen menggunakan

```math
\Delta x
=
0.1,\quad0.01,\quad0.001,\quad0.0001.
```

Untuk setiap nilai $\Delta x$, catat hasil pendekatan, galat absolut terhadap nilai referensi, dan jumlah iterasi. Jelaskan hubungan antara ukuran langkah, ketelitian, dan biaya komputasi berdasarkan data yang diperoleh.

### Solusi

Pada setiap ukuran langkah, mulai dari $x=0$ dan naikkan indeks langkah sampai $x^2\geq7$. Perkalian indeks bulat dengan $\Delta x$ menghindari akumulasi kesalahan akibat menambahkan bilangan pecahan berulang kali.

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    const double reference = sqrt(7.0);
    double step = 0.1;

    puts("Step     Approximation  Absolute error  Iterations");
    for (int trial = 0; trial < 4; trial++)
    {
        int iterations = 0;
        double x = 0.0;

        while (x * x < 7.0)
        {
            iterations++;
            x = iterations * step;
        }

        printf("%.4f   %.7f      %.7f       %d\n",
               step, x, fabs(x - reference), iterations);
        step /= 10.0;
    }

    return 0;
}
```

Kompilasi dengan `gcc -Wall -Wextra -Wpedantic -std=c17 akar_langkah.c -lm -o akar_langkah`. Nilai pembandingnya $\sqrt{7}\approx2{,}6457513111$.

| $\Delta x$ | Pendekatan | Galat absolut | Iterasi |
|---:|---:|---:|---:|
| 0,1 | 2,7 | 0,0542487 | 27 |
| 0,01 | 2,65 | 0,0042487 | 265 |
| 0,001 | 2,646 | 0,0002487 | 2646 |
| 0,0001 | 2,6458 | 0,0000487 | 26458 |

Jika ukuran langkah diperkecil sepuluh kali, jumlah iterasi tumbuh kira-kira sepuluh kali. Metode berhenti pada nilai di atas atau tepat pada akar, sehingga galat pendekatan lebih kecil daripada satu langkah; batas itu tidak menjamin bahwa galat aktual selalu berkurang tepat sepuluh kali pada setiap percobaan.

## 5. Metode Babilonia dengan perlindungan iterasi

### Soal

Implementasikan metode Babilonia

```math
x_{k+1}
=
\frac{1}{2}
\left(
x_k+\frac{S}{x_k}
\right)
```

untuk menghitung $\sqrt{S}$. Program harus menerima $S>0$, menggunakan toleransi yang diberikan pengguna, dan memiliki batas maksimum iterasi agar program tetap berhenti jika kondisi konvergensi gagal tercapai.

Tampilkan nomor iterasi, $x_k$, $x_{k+1}$, dan

```math
|x_{k+1}-x_k|
```

pada setiap langkah. Uji untuk sekurang-kurangnya tiga nilai $S$ dan analisis seberapa cepat algoritma konvergen.

### Solusi

Ambil tebakan awal positif $x_0=\max(1,S)$. Perubahan antariterasi diuji sesudah $x_{k+1}$ dihitung, dan banyak pembaruan tidak boleh melewati `max_iteration`.

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    double s, tolerance;
    int max_iteration;

    if (scanf("%lf %lf %d",
              &s, &tolerance, &max_iteration) != 3 ||
        !(s > 0.0) || !(tolerance > 0.0) ||
        max_iteration <= 0)
    {
        puts("Invalid input.");
        return 1;
    }

    double x = (s >= 1.0) ? s : 1.0;
    int converged = 0;
    int iteration = 0;

    for (int k = 1; k <= max_iteration; k++)
    {
        double next = 0.5 * (x + s / x);
        double difference = fabs(next - x);
        printf("%2d  %.12f  %.12f  %.3e\n",
               k, x, next, difference);

        x = next;
        iteration = k;
        if (difference < tolerance)
        {
            converged = 1;
            break;
        }
    }

    printf("Approximation = %.12f\n", x);
    printf("Iterations = %d\n", iteration);
    puts(converged ? "Converged." : "Iteration limit reached.");
    return 0;
}
```

Kompilasi dengan `gcc -Wall -Wextra -Wpedantic -std=c17 babilonia.c -lm -o babilonia`. Sebagai uji, gunakan toleransi $10^{-10}$ dan batas 50 iterasi untuk $S=2$, $S=7$, dan $S=0{,}25$. Hasilnya berturut-turut mendekati $1{,}414213562373$ dalam **5** iterasi, $2{,}645751311065$ dalam **6** iterasi, dan $0{,}5$ dalam **6** iterasi. Konvergensi dekat akar biasanya cepat karena galat baru kira-kira sebanding dengan kuadrat galat sebelumnya, tetapi toleransi perubahan berturut-turut bukan pemeriksaan langsung atas $|x^2-S|$.

## 6. Pemetaan daya pada dua parameter

### Soal

Gunakan dua pengulangan bersarang untuk menghitung

```math
P=VI
```

pada sekumpulan nilai tegangan dan arus. Tegangan berubah dari $5$ sampai $30$ V dengan langkah $5$ V, sedangkan arus berubah dari $0.5$ sampai $5.0$ A dengan langkah $0.5$ A.

Selain mencetak tabel, cari kombinasi yang menghasilkan daya maksimum tanpa melebihi

```math
P_{\max}=100\text{ W}.
```

Jelaskan bagaimana minimum-maksimum dan nested loop digabungkan pada persoalan ini. Tentukan pula banyak kombinasi parameter yang diperiksa program.

### Solusi

Indeks bilangan bulat menghasilkan tegangan $V=5v$ dengan $v=1,\ldots,6$ dan arus $I=0{,}5j$ dengan $j=1,\ldots,10$. Perbarui daya terbaik hanya jika $P\leq100$ W dan nilai baru lebih besar daripada nilai terbaik sebelumnya.

```c
#include <stdio.h>

int main(void)
{
    double best_power = 0.0;
    double best_voltage = 0.0, best_current = 0.0;
    int combinations = 0, found = 0;

    puts("V (V)  I (A)  P (W)");
    for (int v_index = 1; v_index <= 6; v_index++)
    {
        double voltage = 5.0 * v_index;
        for (int i_index = 1; i_index <= 10; i_index++)
        {
            double current = 0.5 * i_index;
            double power = voltage * current;
            combinations++;
            printf("%5.1f  %5.1f  %5.1f\n",
                   voltage, current, power);

            if (power <= 100.0 &&
                (!found || power > best_power))
            {
                best_power = power;
                best_voltage = voltage;
                best_current = current;
                found = 1;
            }
        }
    }

    printf("Combinations = %d\n", combinations);
    if (found)
    {
        printf("Best: V=%.1f V, I=%.1f A, P=%.1f W\n",
               best_voltage, best_current, best_power);
    }
    return 0;
}
```

Pengulangan dalam memeriksa sepuluh arus untuk setiap satu dari enam tegangan, sehingga ada $6\times10=60$ kombinasi. Daya maksimum yang tidak melampaui 100 W ialah **100 W**, misalnya pada $(V,I)=(20\text{ V},5\text{ A})$. Pasangan $(25\text{ V},4\text{ A})$ juga menghasilkan 100 W; program menyimpan pasangan yang ditemukan lebih dahulu karena syarat pembaruan memakai `power > best_power`. Ini menggabungkan pengulangan bersarang dengan pola maksimum di bawah kendala.

## 7. Validasi berlapis pada data sensor tekanan

### Soal

Sebuah sensor tekanan seharusnya menghasilkan data pada rentang

```math
80
\leq P
\leq
120\text{ kPa}.
```

Nilai `-1` digunakan sebagai sentinel, sedangkan nilai lain di luar rentang valid harus ditolak. Buat program yang menghitung rata-rata, minimum, maksimum, dan jumlah data yang menyimpang lebih dari $10$ kPa dari tekanan referensi $100$ kPa.

Program harus tetap benar jika beberapa input pertama tidak valid. Jelaskan secara eksplisit bagaimana nilai valid pertama digunakan untuk menginisialisasi minimum dan maksimum.

### Solusi

Periksa sentinel `-1` sebelum memeriksa rentang data. Nilai di luar $[80,120]$ kPa diabaikan, sehingga nilai valid pertama, meskipun didahului beberapa masukan tidak valid, tetap menginisialisasi minimum dan maksimum.

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    int count = 0, outside_band = 0;
    double sum = 0.0, minimum = 0.0, maximum = 0.0;

    while (1)
    {
        double pressure;
        if (scanf("%lf", &pressure) != 1)
        {
            puts("Invalid input.");
            return 1;
        }
        if (pressure == -1.0) break;
        if (pressure < 80.0 || pressure > 120.0)
        {
            puts("Invalid pressure.");
            continue;
        }

        if (count == 0)
        {
            minimum = pressure;
            maximum = pressure;
        }
        else
        {
            if (pressure < minimum) minimum = pressure;
            if (pressure > maximum) maximum = pressure;
        }

        sum += pressure;
        count++;
        if (fabs(pressure - 100.0) > 10.0) outside_band++;
    }

    if (count == 0)
    {
        puts("No valid data.");
        return 0;
    }

    printf("Mean = %.3f kPa\n", sum / count);
    printf("Minimum = %.3f kPa\n", minimum);
    printf("Maximum = %.3f kPa\n", maximum);
    printf("Deviation > 10 kPa = %d\n", outside_band);
    return 0;
}
```

Kompilasi dengan `gcc -Wall -Wextra -Wpedantic -std=c17 tekanan.c -lm -o tekanan`. Masukan `-10 121 100 89 111 -1` mula-mula menolak dua nilai, lalu menerima $100,89,111$ kPa. Hasilnya rata-rata 100 kPa, minimum 89 kPa, maksimum 111 kPa, dan dua data menyimpang lebih dari 10 kPa. Jika tidak ada data valid, program tidak membagi dengan nol.

## 8. Algoritma iteratif dengan dua kriteria penghentian

### Soal

Rancang algoritma yang memperbarui nilai menurut hubungan

```math
x_{k+1}
=
\frac{1}{2}
\left(
x_k+\frac{A}{x_k}
\right).
```

Pengulangan harus berhenti jika

```math
|x_{k+1}-x_k|
<
\varepsilon
```

atau jika jumlah iterasi telah mencapai `max_iteration`. Implementasikan dalam C dan tunjukkan melalui dua eksperimen mengapa keberadaan batas iterasi maksimum merupakan perlindungan yang penting.

### Solusi

Algoritma ini sama bentuknya dengan iterasi Babilonia, tetapi dua eksperimen berikut menonjolkan alasan diberlakukannya batas maksimum. Pilih $x_0=1$, $A>0$, $\varepsilon>0$, dan `max_iteration` positif.

```text
INPUT A, epsilon, max_iteration
IF A <= 0 OR epsilon <= 0 OR max_iteration <= 0 THEN STOP
x ← 1
converged ← false
FOR k ← 1 TO max_iteration
    next ← (x + A/x) / 2
    difference ← |next - x|
    x ← next
    IF difference < epsilon THEN
        converged ← true
        BREAK
    END IF
END FOR
OUTPUT x, k, converged
```

Implementasi C berikut melaporkan apakah program berhenti karena kriteria toleransi atau karena batas iterasi.

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    double a, epsilon;
    int max_iteration;

    if (scanf("%lf %lf %d",
              &a, &epsilon, &max_iteration) != 3 ||
        !(a > 0.0) || !(epsilon > 0.0) ||
        max_iteration <= 0)
    {
        puts("Invalid input.");
        return 1;
    }

    double x = 1.0;
    int iterations = 0, converged = 0;

    while (iterations < max_iteration)
    {
        double next = 0.5 * (x + a / x);
        double difference = fabs(next - x);
        x = next;
        iterations++;
        if (difference < epsilon)
        {
            converged = 1;
            break;
        }
    }

    printf("x = %.12f\n", x);
    printf("Iterations = %d\n", iterations);
    puts(converged ? "Converged." : "Iteration limit reached.");
    return 0;
}
```

Kompilasi dengan `gcc -Wall -Wextra -Wpedantic -std=c17 dua_kriteria.c -lm -o dua_kriteria`. Gunakan $A=2$ dan $\varepsilon=10^{-10}$ dalam kedua eksperimen:

| `max_iteration` | Hasil $x$ | Banyak iterasi | Alasan berhenti |
|---:|---:|---:|---|
| 1 | 1,500000000000 | 1 | batas maksimum |
| 20 | sekitar 1,414213562373 | 5 | selisih berturut-turut di bawah toleransi |

Eksperimen pertama berhenti meskipun belum konvergen. Tanpa batas maksimum, kondisi berhenti yang tidak pernah tercapai akibat toleransi terlalu ketat, gangguan pembulatan, atau rumus yang salah dapat membuat program terus berjalan.

## 9. Estimasi integral dengan penjumlahan Riemann

### Soal

Gunakan pola akumulator untuk mendekati integral

```math
\int_0^1 x^2\,dx
```

menggunakan jumlah Riemann titik tengah. Bagi interval menjadi $N$ bagian sama lebar dan hitung

```math
\Delta x
=
\frac{1}{N}.
```

Untuk setiap subinterval, evaluasi fungsi pada titik tengah lalu akumulasikan kontribusinya. Uji untuk $N=10$, $100$, $1000$, dan $10000$, kemudian bandingkan hasil numerik dengan nilai eksak $1/3$ dan analisis perubahan galat.

### Solusi

Lebar setiap subinterval $\Delta x=1/N$ dan titik tengah ke-$i$, untuk $i=0,\ldots,N-1$, adalah $x_i=(i+\tfrac12)\Delta x$. Karena itu, pendekatan integralnya adalah $\sum_{i=0}^{N-1}x_i^2\Delta x$.

```c
#include <stdio.h>

int main(void)
{
    const double exact = 1.0 / 3.0;

    puts("N       Midpoint sum   Absolute error");
    for (int n = 10; n <= 10000; n *= 10)
    {
        double dx = 1.0 / n;
        double integral = 0.0;

        for (int i = 0; i < n; i++)
        {
            double middle = (i + 0.5) * dx;
            integral += middle * middle * dx;
        }

        printf("%-6d  %.10f     %.10f\n",
               n, integral, exact - integral);
    }
    return 0;
}
```

| $N$ | Jumlah titik tengah | Galat absolut |
|---:|---:|---:|
| 10 | 0,3325000000 | 0,0008333333 |
| 100 | 0,3333250000 | 0,0000083333 |
| 1000 | 0,3333332500 | 0,0000000833 |
| 10000 | 0,3333333325 | 0,0000000008 |

Untuk fungsi $x^2$, jumlah titik tengah tepat sama dengan $1/3-1/(12N^2)$ dalam aritmetika eksak. Jadi, galatnya $1/(12N^2)$; meningkatkan $N$ sepuluh kali memperkecil galat kira-kira seratus kali, sampai keterbatasan ketelitian bilangan `double` mulai berpengaruh.

## 10. Proyek mini: analisis data getaran mesin

### Soal

Kembangkan studi kasus getaran mesin pada catatan ini menjadi program yang menerima data percepatan sampai sentinel `9999`. Program harus menolak data di luar rentang $-50$ sampai $50~\text{m/s}^2$ dan menghitung rata-rata, RMS, minimum, maksimum, jumlah data dengan $|a|>8~\text{m/s}^2$, serta persentasenya.

Tambahkan satu fitur baru: hitung **crest factor**

```math
C
=
\frac{
\max |a_i|
}{
a_{\text{RMS}}
}.
```

Program harus menghitung `max_abs` selama proses berlangsung tanpa menyimpan seluruh data. Lakukan tracing manual untuk satu himpunan data uji, bandingkan dengan keluaran program, lalu jelaskan mengapa rata-rata, RMS, dan crest factor memberikan informasi yang berbeda mengenai sinyal getaran.

### Solusi

Selama pembacaan, pelihara `sum`, `sum_square`, `minimum`, `maximum`, `max_abs`, `count`, dan `count_high`. Sentinel harus diperiksa sebelum validasi rentang; nilai di luar rentang diabaikan sebelum statistik diperbarui.

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    int count = 0, count_high = 0;
    double sum = 0.0, sum_square = 0.0;
    double minimum = 0.0, maximum = 0.0, max_abs = 0.0;

    while (1)
    {
        double a;
        if (scanf("%lf", &a) != 1)
        {
            puts("Invalid input.");
            return 1;
        }
        if (a == 9999.0) break;
        if (a < -50.0 || a > 50.0)
        {
            puts("Invalid measurement.");
            continue;
        }

        if (count == 0)
        {
            minimum = a;
            maximum = a;
        }
        else
        {
            if (a < minimum) minimum = a;
            if (a > maximum) maximum = a;
        }

        double amplitude = fabs(a);
        if (amplitude > max_abs) max_abs = amplitude;
        if (amplitude > 8.0) count_high++;
        sum += a;
        sum_square += a * a;
        count++;
    }

    if (count == 0)
    {
        puts("No valid data.");
        return 0;
    }

    double rms = sqrt(sum_square / count);
    printf("Count       = %d\n", count);
    printf("Mean        = %.3f m/s^2\n", sum / count);
    printf("RMS         = %.3f m/s^2\n", rms);
    printf("Minimum     = %.3f m/s^2\n", minimum);
    printf("Maximum     = %.3f m/s^2\n", maximum);
    printf("Above 8     = %d\n", count_high);
    printf("Percentage  = %.2f%%\n", 100.0 * count_high / count);
    printf("Max |a|     = %.3f m/s^2\n", max_abs);

    if (rms > 0.0)
    {
        printf("Crest factor = %.3f\n", max_abs / rms);
    }
    else
    {
        puts("Crest factor is undefined (RMS = 0).");
    }
    return 0;
}
```

Kompilasi dengan `gcc -Wall -Wextra -Wpedantic -std=c17 getaran_mesin.c -lm -o getaran_mesin`. Gunakan urutan input $1{,}2,-2{,}4,8{,}7,75,-9{,}1,3{,}6,9999$ untuk tracing manual.

| Input | Tindakan | `count` | `sum` | `sum_square` | `minimum` | `maximum` | `max_abs` | `count_high` |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1,2 | valid | 1 | 1,2 | 1,44 | 1,2 | 1,2 | 1,2 | 0 |
| -2,4 | valid | 2 | -1,2 | 7,20 | -2,4 | 1,2 | 2,4 | 0 |
| 8,7 | valid | 3 | 7,5 | 82,89 | -2,4 | 8,7 | 8,7 | 1 |
| 75 | ditolak | 3 | 7,5 | 82,89 | -2,4 | 8,7 | 8,7 | 1 |
| -9,1 | valid | 4 | -1,6 | 165,70 | -9,1 | 8,7 | 9,1 | 2 |
| 3,6 | valid | 5 | 2,0 | 178,66 | -9,1 | 8,7 | 9,1 | 2 |
| 9999 | berhenti | 5 | 2,0 | 178,66 | -9,1 | 8,7 | 9,1 | 2 |

Hasilnya adalah rata-rata $2/5=0{,}4$ m/s$^2$, RMS $\sqrt{178{,}66/5}\approx5{,}978$ m/s$^2$, minimum $-9{,}1$ m/s$^2$, maksimum $8{,}7$ m/s$^2$, dua data melampaui 8 m/s$^2$ atau $40\%$, serta `max_abs` $=9{,}1$ m/s$^2$. Crest factor bernilai $9{,}1/\sqrt{178{,}66/5}\approx1{,}522$. Rata-rata menunjukkan kecenderungan bertanda yang dapat saling menghapus, RMS mengukur besar efektif getaran, sedangkan crest factor membandingkan puncak absolut dengan besar efektif. Jika seluruh data valid bernilai nol, RMS nol dan crest factor tidak terdefinisi; program mencegah pembagian dengan nol. Memori tambahan tetap $O(1)$.

