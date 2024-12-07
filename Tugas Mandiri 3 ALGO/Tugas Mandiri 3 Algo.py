def read_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return [
                (line.split(';')[0].strip(), float(line.split(';')[1].strip()))
                for line in file
                if ';' in line and line.split(';')[1].strip().replace('.', '', 1).isdigit()
            ]
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
        return []
    except ValueError:
        print(f"Format data tidak valid.")
        return []

def calculate_statistics(data):
    if not data:
        return 0, 0, (None, None), (None, None), []
    
    total = len(data)
    rata_rata = sum(score for _, score in data) / total
    lulus = [(name, score) for name, score in data if score > 80]
    tertinggi = max(lulus, key=lambda x: x[1], default=(None, None))
    terendah = min(data, key=lambda x: x[1], default=(None, None))
    return total, rata_rata, tertinggi, terendah, lulus

def write_results(file_name, stats):
    total, rata_rata, tertinggi, terendah, lulus = stats
    with open(file_name, 'w') as file:
        file.write(f"Total peserta: {total}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Tertinggi: {tertinggi[0]} ({tertinggi[1]:.2f})\n" if tertinggi[0] else "Tertinggi: Tidak ada\n")
        file.write(f"Terendah: {terendah[0]} ({terendah[1]:.2f})\n" if terendah[0] else "Terendah: Tidak ada\n")
        file.write("=== Peserta Lulus ===\n")
        file.writelines(f"{name} ({score:.2f})\n" for name, score in lulus)


data_file = 'sertifikasi.txt'
result_file = 'rekap-data.txt'

data = read_data(data_file)
stats = calculate_statistics(data)
write_results(result_file, stats)

with open(result_file, 'r') as file:
    print(file.read())
