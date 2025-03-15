1. Greedy Best-First Search (GBFS)
Greedy Best-First Search hanya mempertimbangkan nilai heuristic h(n) tanpa memperhatikan biaya sebenarnya yang telah ditempuh. Algoritma ini selalu memilih node dengan nilai heuristic terkecil dari node yang tersedia.

Langkah-langkah GBFS untuk graf ini:

Mulai di S (h=6) → Pilih node dengan h terkecil: A (h=4) dan B (h=3)
Pilih B (h=3) karena lebih kecil dari A → B terhubung ke C (h=3)
Pilih C (h=3) → C terhubung ke D (h=1)
Pilih D (h=1) → D terhubung ke G (h=0)
Tujuan G tercapai!
Hasil jalur: S → B → C → D → G

Kelemahan GBFS: Bisa tersesat di jalur yang terlihat optimal berdasarkan heuristic, tetapi sebenarnya lebih mahal.

2. A Search (A Star)*
A* Search menggunakan fungsi:

𝑓
(
𝑛
)
=
𝑔
(
𝑛
)
+
ℎ
(
𝑛
)
f(n)=g(n)+h(n)
g(n) = biaya aktual dari start ke node n
h(n) = estimasi biaya dari n ke goal
Langkah-langkah A untuk graf ini:*

Mulai di S (f=0+6=6)

Pilihan: A (g=3, h=4, f=7) & B (g=2, h=3, f=5)
Pilih B (f terkecil = 5)
Dari B → C (g=4, h=3, f=7)

Dari C → D (g=7, h=1, f=8)

Dari D → G (g=8, h=0, f=8)

Goal tercapai dengan f=8!
Hasil jalur: S → B → C → D → G (sama seperti GBFS, tetapi lebih terkontrol)

Keunggulan A*: Tidak hanya mempertimbangkan heuristic h(n), tetapi juga biaya aktual g(n), sehingga lebih optimal dibanding GBFS.

