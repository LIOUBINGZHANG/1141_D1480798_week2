print("1.公里 ↔ 英里")
print("2.英里 ↔ 公里")
print("3.攝氏 ↔ 華氏")
print("4.華氏 ↔ 攝氏")
print("5.公斤 ↔ 磅")
print("6.磅 ↔ 公斤")


string =input("輸入選項(1~6): ")
int = int(string)

#長度
if int == 1:
    str1 =input("輸入公里數: ")
    num1 = float(str1)
    length = num1 * 0.621371
    print(f"英里數為{length}")
if int == 2:
    str2 =input("輸入英里數: ")
    num2 = float(str2)
    length2 = num2 / 0.621371
    print(f"公里數為{length2}")
    #溫度
if int == 3:
    str3 =input("輸入攝氏溫度: ")
    num3 = float(str3)
    C = (num3 * 9/5) + 32
    print(f"華氏溫度為{C}")
if int == 4:
    str4 =input("輸入華氏溫度: ")
    num4 = float(str4)
    C2 = (num4 - 32) * 5/9
    print(f"攝氏溫度為{C2}")
    #重量
if int == 5:
    str5 =input("輸入公斤數: ")
    num5 = float(str5)
    kg = num5 * 2.20462
    print(f"磅數為{kg}")
if int == 6:
    str6 =input("輸入磅數: ")
    num6 = float(str6)
    lb = num6 / 2.20462
    print(f"公斤數為{lb}")
    