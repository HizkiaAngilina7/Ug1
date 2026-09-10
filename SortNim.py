def InsertRecursive(sorted_array, current_value, current_length):
    # TODO 1: Implementasikan base case, logika komparasi pengurutan sesuai NIM, 
    # dan pemanggilan rekursi fungsi insert.
    last_digit = int(NIM_MAHASISWA[-1])
    
    if current_length == 0:
        sorted_array[0] = current_value
        return sorted_array

    compare_value = sorted_array[current_length - 1]

  
    if last_digit % 2 != 0:
        if current_value < compare_value:
            sorted_array[current_length] = compare_value
            return InsertRecursive(sorted_array, current_value, current_length - 1)
        else:
            sorted_array[current_length] = current_value
            return sorted_array
    else:
        if current_value > compare_value:
            sorted_array[current_length] = compare_value
            return InsertRecursive(sorted_array, current_value, current_length - 1)
        else:
            sorted_array[current_length] = current_value
            return sorted_array
        
def RecursiveFilterSort(data_array, current_length):
    # TODO 2: Implementasikan base case, pemecahan rekursif, dan filter kondisional 
    if current_length == 0:
        return []
    
    current_value = data_array[current_length - 1]
    sorted_partial = RecursiveFilterSort(data_array, current_length - 1)

    last_digit = int(NIM_MAHASISWA[-1])

    if last_digit % 2 != 0:
        if current_value % 2 != 0:
            sorted_partial.append(0)  # slot kosong untuk insert
            return InsertRecursive(sorted_partial, current_value, len(sorted_partial) - 1)
        else:
            return sorted_partial
    else:
        if current_value % 2 == 0:
            sorted_partial.append(0)
            return InsertRecursive(sorted_partial, current_value, len(sorted_partial) - 1)
        else:
            return sorted_partial

# Ganti Dengan NIM Anda
# Contoh, NIM_MAHASISWA = "71230994" -> nanti outputnya [4, 2, 0] 
NIM_MAHASISWA = "71241157"

if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)
    
    final_result = RecursiveFilterSort(raw_data, data_length)

    # TODO 3: cetak hasil akhir sesuai format yang diminta.
    last_digit = int(NIM_MAHASISWA[-1])

    print("===== FILTER & SORT NIM =====")
    print("NIM Mahasiswa  :", NIM_MAHASISWA)

    if last_digit % 2 != 0:
        print("Tipe           : GANJIL (Ascending)")
    else:
        print("Tipe           : GENAP (Descending)")

    print("Data Digit Awal:", raw_data)
    print("Hasil Akhir    :", final_result)