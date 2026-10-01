ilksayi = int(input("ilk sayıyı giriniz: "))
ikincisayi = int(input("2 sayıyı giriniz: "))

işlem = input("""lütfen işlem yapmak istiyorsanız bunlara basın
toplama için + çıkarma için - çarpma için  * bölme işlemi için / """)

if işlem == "+":
    print("sonuç:", str(ilksayi + ikincisayi))

if işlem == "-":
    print("sonuç:", str(ilksayi - ikincisayi))

if işlem == "*":
    print("sonuç:",(ilksayi * ikincisayi))

if işlem == "/":
    print("sonuc:", (ilksayi / ikincisayi))
