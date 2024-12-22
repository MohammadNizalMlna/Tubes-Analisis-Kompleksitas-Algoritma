import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def binary_search_iterative(kontak, target):
    minim = 0
    maks = len(kontak) - 1

    while minim <= maks:
        tengah = (minim + maks) // 2
        if kontak[tengah] == target:
            return tengah
        elif kontak[tengah] < target:
            minim = tengah + 1
        else:
            maks = tengah - 1
    return -1

def binary_search_recursive(kontak, target, minim, maks):
    if minim > maks:
        return -1
    tengah = (minim + maks) // 2
    if kontak[tengah] == target:
        return tengah
    elif kontak[tengah] < target:
        return binary_search_recursive(kontak, target, tengah + 1, maks)
    else:
        return binary_search_recursive(kontak, target, minim, tengah - 1)

if __name__ == "__main__":
    kontak = [
        "Adam", "Brian", "Charlie", "David", "Emily",
        "Frank", "George", "Hannah", "Isabel", "Jack",
        "Katie", "Lily", "Mason", "Natalie", "Oscar",
        "Peter", "Quinn", "Rachel", "Sarah", "Tom",
        "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane",
    ]
    
    # List untuk menyimpan hasil waktu eksekusi untuk setiap pencarian
    iterative_times = []
    recursive_times = []
    targets = []

    # Loop untuk input target beberapa kali
    while True:
        target = input("Masukkan nama kontak (atau ketik 'exit' untuk berhenti): ")
        
        if target.lower() == 'exit':
            break

        # Ukur waktu untuk iteratif
        start_iterative = time.time()
        index_iterative = binary_search_iterative(kontak, target)
        durasi_iterative = time.time() - start_iterative

        # Ukur waktu untuk rekursif
        start_recursive = time.time()
        index_recursive = binary_search_recursive(kontak, target, 0, len(kontak) - 1)
        durasi_recursive = time.time() - start_recursive

        # Menyimpan data untuk grafik
        targets.append(target)
        iterative_times.append(durasi_iterative)
        recursive_times.append(durasi_recursive)

        # Tampilkan hasil dalam tabel
        table = PrettyTable()
        table.field_names = ["Metode", "Target", "Hasil", "Durasi (detik)"]

        if index_iterative != -1:
            table.add_row(["Iteratif", target, f"Ditemukan di indeks {index_iterative}", f"{durasi_iterative:.6f}"])
        else:
            table.add_row(["Iteratif", target, "Tidak ditemukan", f"{durasi_iterative:.6f}"])

        if index_recursive != -1:
            table.add_row(["Rekursif", target, f"Ditemukan di indeks {index_recursive}", f"{durasi_recursive:.6f}"])
        else:
            table.add_row(["Rekursif", target, "Tidak ditemukan", f"{durasi_recursive:.6f}"])

        print(table)

    # Visualisasi waktu pencarian menggunakan diagram garis
    plt.plot(targets, iterative_times, label="Iteratif", marker='o', color='blue')
    plt.plot(targets, recursive_times, label="Rekursif", marker='x', color='green')
    
    plt.xlabel("Target")
    plt.ylabel("Durasi (detik)")
    plt.title("Perbandingan Waktu Pencarian (Diagram Garis)")
    plt.legend()
    plt.xticks(rotation=45)  
    plt.tight_layout()  
    plt.show()
