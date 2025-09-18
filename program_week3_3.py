print("length/temperature/weight")
string =input("選擇輸入類型")
string2 =input("輸入數值")
float = float(string2)

if string == "length":
    n1 = float * 0.621371
    print(f"英里數為{n1}")
    n2 = float / 0.621371
    print(f"公里數為{n2}")
if string =="temperature":
    n3 = (float * 9/5) + 32
    print(f"華氏溫度為{C}")
    n4 = (float - 32) * 5/9
    print(f"攝氏溫度為{C2}")
if string =="weight":
    n5 = float * 2.20462
    print(f"磅數為{n5}")
    n6 = float / 2.20462
    print(f"公斤數為{n6}")