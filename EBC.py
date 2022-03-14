print("welcome to electrical calculator program")
count = 0
money = 0
total = 0
i = int(input("Number of electrical appliances to be calculated : "))

while count < i:
    quantity = int(input("quantity : "))
    watt =  int(input("Power(watt) : "))
    hour = float(input("Number of hours power on : "))
    
    unit = watt * quantity / 1000 * hour
    month = unit * 30
    print('{:.3f}'.format(unit) ,"Unit per day")
    print('{:.2f}'.format(month) , "Unit per month")
    total = total + month
    count += 1
    
print("-------------------")
print(total, "total unit")
print("-------------------")
    
if total >= 400:
    money = money + 85.21
    money = 115 * 1.1236 + money
    money = 250 * 2.1329 + money
    total = total - 400
    money = total * 2.4226 + money
    

print('{:.2f}'.format(money), "total money")

#ลองทำโปรแกรมคำนวณค่าไฟผลลัพธ์ตามโจทย์ อ้างอิงจากเว็บ https://erdi.cmu.ac.th/?p=564