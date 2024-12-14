import subprocess
import time

# Çalıştırmak istediğiniz komutlar
commands = [
    "echo 'Selam, Ben Virus:)'",
    "ls",
    "touch test.txt",
    "echo 'Kanala Video At' > test.txt",
    "cat test.txt"
]

def execute_commands(commands):
    for command in commands:
        # Komutları 0.5 saniye aralıklarla çalıştırıyoruz
        time.sleep(0.5)  # 0.5 saniye bekleyelim

        try:
            # Komutu çalıştırıyoruz ve çıktıyı alıyoruz
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Komutun çıktısını ekrana yazdırıyoruz
            if result.stdout:
                print(result.stdout, end='')  # stdout çıktısını ekrana yazdır
            if result.stderr:
                print(f"Hata: {result.stderr}", end='')  # stderr çıktısını ekrana yazdır
        except subprocess.CalledProcessError as e:
            # Hata olursa hatayı yazdırıyoruz
            print(f"Komut hatası: {e}")

def main():
    time.sleep(2)  # Başlangıçta biraz bekleyelim
    execute_commands(commands)


if __name__ == "__main__":
    main()
