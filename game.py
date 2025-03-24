import random
import time


player_scores = {}


def guess_number():
    name = input("Masukkan nama Anda: ")
    target = random.randint(1, 100)  # Angka acak antara 1-100
    attempts = 5  # Batas percobaan
    print(f"Halo {name}, tebak angka antara 1 hingga 100. Anda memiliki {attempts} kesempatan.\n")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Percobaan {attempt}: Masukkan tebakan Anda: "))

        if guess < target:
            print("Terlalu kecil!")
        elif guess > target:
            print("Terlalu besar!")
        else:
            print(f"Selamat {name}! Anda menebak dengan benar dalam {attempt} percobaan.")
            player_scores[name] = attempt
            break
        time.sleep(1)  # Jeda agar terlihat lebih natural

    else:
        print(f"Maaf {name}, Anda kehabisan kesempatan. Angka yang benar adalah {target}.")


def show_scores():
    if player_scores:
        print("\nSkor Pemain:")
        for player, score in player_scores.items():
            print(f"{player}: {score} percobaan")
    else:
        print("\nBelum ada skor yang tercatat.")


def main():
    while True:
        print("\n1. Main Tebak Angka\n2. Lihat Skor\n3. Keluar")
        choice = input("Pilih opsi: ")

        if choice == "1":
            guess_number()
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("Terima kasih telah bermain!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
