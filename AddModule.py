# Fungsi untuk input ya/tidak dengan validasi
def input_yes_no(choice):
    while True:
        user_input = input(choice + " (Y/T): ").upper()
        if user_input in ["Y", "T"]:
            return user_input
        
def input_non_empty_string(string):
    while True:
        user_input = input(string).strip()
        if user_input:
            return user_input
        else:
            print("Masukkan teks yang valid.")
            
def input_angka(angka_positif):
    while True:
        try:
            user_input = int(input(angka_positif))
            
            if user_input > 0:
                return user_input
            else:
                print("Masukkan angka positif.")
        except ValueError:
            print("Masukkan angka yang valid.")
