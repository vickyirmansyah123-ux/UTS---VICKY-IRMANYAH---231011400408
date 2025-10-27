###  **1. Pengantar Operasi Morfologi**

Operasi morfologi adalah **teknik pengolahan citra digital** yang berfokus pada **bentuk dan struktur objek** di dalam citra, khususnya **citra biner** (hitam–putih).
Operasi ini menggunakan **structuring element (SE)** sebagai alat untuk memeriksa dan memodifikasi pixel berdasarkan **hubungan spasial**.

**Fungsi utama:**

* Menghilangkan noise
* Mengekstrak batas objek (boundary)
* Menutup lubang (hole filling)
* Menganalisis bentuk (shape analysis)
* Segmentasi objek

---

###  **2. Citra Biner dan Structuring Element**

* **Citra biner** hanya memiliki 2 nilai:
  `0 = hitam (background)` dan `255 = putih (foreground)`.
  Biasanya dihasilkan dari proses **thresholding**.

* **Structuring Element (SE)**:
  Matriks kecil (mis. 3×3, 5×5) yang digunakan sebagai “jendela” analisis.
  Bentuk umum SE:

  * **Rectangular (persegi)**
  * **Elliptical (elips)**
  * **Cross (salib)**

Contoh kode:

```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
```

---

###  **3. Operasi Morfologi Dasar**

#### a. **Erosion (Erosi)**

* Mengikis tepi objek.
* Pixel bernilai 1 tetap 1 **hanya jika semua pixel di bawah SE adalah 1.**
* Efek: menghapus noise kecil dan mengecilkan objek.

```python
erosion = cv2.erode(image_binary, kernel, iterations=1)
```

---

#### b. **Dilation (Dilasi)**

* Memperbesar objek.
* Pixel bernilai 0 menjadi 1 jika **ada** pixel 1 di bawah SE.
* Efek: menutup lubang, menyambung objek terputus.

```python
dilation = cv2.dilate(image_binary, kernel, iterations=1)
```

---

#### c. **Opening (Buka)**

* Kombinasi **Erosion → Dilation**
  (A ◦ B = (A⊖B)⊕B)
* Menghapus noise di background tanpa mengubah bentuk objek utama.

```python
opening = cv2.morphologyEx(image_binary, cv2.MORPH_OPEN, kernel)
```

---

#### d. **Closing (Tutup)**

* Kombinasi **Dilation → Erosion**
  (A • B = (A⊕B)⊖B)
* Menutup lubang kecil dalam objek dan menyatukan bagian terputus.

```python
closing = cv2.morphologyEx(image_binary, cv2.MORPH_CLOSE, kernel)
```

---

###  **4. Operasi Morfologi Turunan**

#### a. **Morphological Gradient**

* Menghasilkan **outline** dari objek.
  Rumus: `Gradient = Dilation - Erosion`
* Berguna untuk deteksi tepi (edge detection).

```python
gradient = cv2.morphologyEx(image_binary, cv2.MORPH_GRADIENT, kernel)
```

---

#### b. **Top Hat**

* `Top Hat = Original - Opening`
* Menonjolkan **objek kecil yang lebih terang** dari background.

```python
tophat = cv2.morphologyEx(image_binary, cv2.MORPH_TOPHAT, kernel)
```

#### c. **Black Hat**

* `Black Hat = Closing - Original`
* Menonjolkan **objek kecil yang lebih gelap** dari background.

```python
blackhat = cv2.morphologyEx(image_binary, cv2.MORPH_BLACKHAT, kernel)
```

---

###  **5. Aplikasi Praktis**

* **Noise Removal:** Gunakan kombinasi Opening + Closing untuk membersihkan hasil thresholding.
* **Boundary Extraction:** Gunakan Morphological Gradient untuk mengambil tepi objek.
* **Shape Detection:** Gunakan Top Hat / Black Hat untuk mendeteksi detail kecil.

---

###  **6. Ringkasan**

| Operasi                 | Fungsi Utama                | Efek Visual        |
| ----------------------- | --------------------------- | ------------------ |
| **Erosion**             | Menghapus noise kecil       | Mengecilkan objek  |
| **Dilation**            | Menyambung objek            | Memperbesar objek  |
| **Opening**             | Noise removal di background | Membersihkan citra |
| **Closing**             | Noise removal di foreground | Menutup lubang     |
| **Gradient**            | Boundary extraction         | Menampilkan tepi   |
| **Top Hat / Black Hat** | Deteksi objek kecil         | Koreksi background |

## Refensi Materi
*Dr. Arya Adhyaksa Waskita (2025)*  
Pengolahan Citra Digital – Operasi Morfologi pada Citra Biner (Pekan 5)

## Disusun oleh
*Vicky Irmansyah - 231011400408 - 05TPLP009*  
UTS Pengolahan Citra Digital  
Universitas Pamulang
