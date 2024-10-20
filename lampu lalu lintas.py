import time
import os
def clear():
    os.system("cls || clear")
while True:

#red light
    for detik in range(30, 0, -1):
        clear()
        print(f"""----------------------------------------
| 🔴 |______________
| ⚫ |        | {detik} |
| ⚫ |        ------
----------------------------------------""")
        time.sleep(1)

#green light
    for detik in range(30, 0, -1):
        clear()
        print(f"""----------------------------------------
| ⚫ |______________
| 🟢 |        | {detik} |
| ⚫ |        ------
----------------------------------------""")
        time.sleep(1)

#yellow light
    for detik in range(10, 0, -1):
        clear()
        print(f"""----------------------------------------
| ⚫ |______________
| ⚫ |        | {detik} |
| 🟡 |        ------
----------------------------------------""")
        time.sleep(1)
