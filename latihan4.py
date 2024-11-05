# Nama: Ikhsan Nurul Haq
# Kelas: RPL 1A
# NIM: 2407833

PASS = "Latihan"  
USER = "Daspro2023"  

def check_login(stored_password, attempts=3):
    """Fungsi untuk memeriksa login password dengan jumlah kesempatan tertentu."""
    
    input_username = input("Masukkan username: ")

    for i in range(attempts):
        input_password = input("Masukkan password: ")

        if input_password == stored_password:
            print("Login berhasil! Selamat datang di sistem.")
            return True 
        else:
            print("Password salah!")
            remaining_attempts = attempts - (i + 1)
            if remaining_attempts > 0:
                print(f"Sisa kesempatan: {remaining_attempts}")
            else:
                print("Kesempatan habis. Anda telah dikeluarkan dari sistem.")
    
    return False

print("=== Selamat Datang di Sistem Login ===")
is_logged_in = check_login(PASS)
print("=== Program selesai ===")


