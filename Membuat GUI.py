# Import tkinter dan ttk untuk membuat GUI
import tkinter as tk
from tkinter import ttk

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    # Mengatur teks pada label hasil menjadi "Prodi Pilihan: Teknologi Informasi"
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()  # Inisialisasi jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menetapkan judul jendela
root.geometry("1080x1080")  # Menentukan ukuran jendela (1080x1080 piksel)
root.configure(bg="#FC8F54")  # Menentukan warna latar belakang jendela utama

# Membuat label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 20))  # Membuat label judul
judul_label.pack(pady=10)  # Menampilkan label dengan padding vertikal 10 piksel
judul_label.configure(bg="#A6AEBF")  # Menetapkan warna latar belakang label judul

# Membuat frame untuk nilai mata pelajaran
nilai_frame = tk.Frame(root)  # Membuat frame untuk menampung input nilai mata pelajaran
nilai_frame.pack(pady=20)  # Menampilkan frame dengan jarak padding vertikal 20 piksel

# Membuat label dan input untuk 10 nilai mata pelajaran
nilai_entries = []  # List untuk menyimpan entry nilai mata pelajaran
for i in range(10):  # Loop untuk membuat 10 pasangan label dan input
    # Membuat label untuk setiap mata pelajaran
    mata_pelajaran_label = tk.Label(nilai_frame, text=f"Nilai Mata Pelajaran {i+1}")
    mata_pelajaran_label.grid(row=i, column=0, padx=5, pady=5, sticky="w")  # Menempatkan label pada grid dengan padding
    
    # Membuat entry untuk mengisi nilai mata pelajaran
    nilai_entry = tk.Entry(nilai_frame)  # Membuat input nilai
    nilai_entry.grid(row=i, column=1, padx=5, pady=5)  # Menempatkan entry pada grid di sebelah label
    nilai_entries.append(nilai_entry)  # Menyimpan setiap entry dalam list nilai_entries

# Membuat tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)  # Membuat tombol untuk memicu fungsi hasil_prediksi
prediksi_button.pack(pady=20)  # Menampilkan tombol dengan jarak padding vertikal 20 piksel

# Membuat label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="Prodi Pilihan: ", font=("Times New Roman", 16))  # Membuat label untuk hasil prediksi
hasil_label.pack(pady=10)  # Menampilkan label hasil dengan jarak padding vertikal 10 piksel

# Menjalankan aplikasi
root.mainloop()  # Memulai loop utama aplikasi untuk menampilkan jendela GUI
