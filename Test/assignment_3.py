"""
Name: {panadda luangna}
SID: {363411760007}
Group: {MIT431}
"""

"""
เขียนโปรแกรมไพธอนเพื่อนำเลขบัตรประชาชนมาบวกกันเพื่อทำนายดวงชะตาดังนี้
• สร้างฟังก์ชันเพื่อหาผลรวมของเลขบัตรประชาชน โดยใช้ชื่อฟังก์ชั่นว่า sumPID()
• สร้างฟังชั่นชื่อ getFortune() เพื่อทำนายดวงชะตา ถ้าเป็นเลขคู่ให้ทำนายว่า your fortune is good
• ถ้าเป็นเลขคี่ ให้ทำนายว่า your fortune is very good
"""


pid = input("Enter your pid: ")
print(pid)

l_pid =[]

for x in pid:
    l_pid.append(int(x))
print(l_pid)

l_pid2 = [int(x) for x in pid]
print(l_pid2)

def sumPID(pid):
    s = 0
    for x in pid:
        s += x
    print(s)
    return s
def getfortune(sumpid):
    if sumpid%2 ==0:
        print("four fortune is good.")
    else:
        print("your fortune is very good")


sumpid = sumPID(l_pid)
getfortune(sumpid)


