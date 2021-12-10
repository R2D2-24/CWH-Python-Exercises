# Health Management System
def getdate():
    import datetime
    dt = datetime.datetime.now()
    return dt.replace(microsecond=0)


print("What is your Name?\n"
      "Write 'R' for Rishav, 'V' for Vaibhav and "
      "'T' for Taman")
name = input()

if name == "R":
    print("What do you want to do?\n"
          "Write 'U' to update information and 'R' to "
          "retrieve")
    action1 = input()
    if action1 == "U":
        print("Diet('D') or Exercise('E')")
        type1 = input()
        if type1 == "D":
            rd = open("Rishav_diet.txt", "a")
            d1 = input("What have you eaten today: ")
            rd.write("\n ")
            rd.write(f"{getdate()} {d1}")
            print("Updated")
            rd.close()
        elif type1 == "E":
            re = open("Rishav_ex.txt", "a")
            e1 = input("Which exercise did you do: ")
            re.write("\n ")
            re.write(f"{getdate()} {e1}")
            print("Updated")
            re.close()
    elif action1 == "R":
        print("Diet('D') or Exercise('E')")
        type2 = input()
        if type2 == "D":
            rdr = open("Rishav_diet.txt")
            print(rdr.read())
        elif type2 == "E":
            rer = open("Rishav_ex.txt")
            print(rer.read())

elif name == "V":
    print("What do you want to do?\n"
          "Write 'U' to update information and 'R' to "
          "retrieve")
    action2 = input()
    if action2 == "U":
        print("Diet('D') or Exercise('E')")
        type3 = input()
        if type3 == "D":
            vd = open("Vaibhav_diet.txt", "a")
            d2 = input("What have you eaten today: ")
            vd.write("\n ")
            vd.write(f"{getdate()} {d2}")
            print("Updated")
            vd.close()
        elif type3 == "E":
            ve = open("Vaibhav_ex.txt", "a")
            e2 = input("Which exercise did you do: ")
            ve.write("\n ")
            ve.write(f"{getdate()} {e2}")
            print("Updated")
            ve.close()
    elif action2 == "R":
        print("Diet('D') or Exercise('E')")
        type4 = input()
        if type4 == "D":
            vdr = open("Vaibhav_diet.txt")
            print(vdr.read())
        elif type4 == "E":
            ver = open("Vaibhav_ex.txt")
            print(ver.read())
elif name == "T":
    print("What do you want to do?\n"
          "Write 'U' to update information and 'R' to "
          "retrieve")
    action3 = input()
    if action3 == "U":
        print("Diet('D') or Exercise('E')")
        type5 = input()
        if type5 == "D":
            td = open("Taman_diet.txt", "a")
            d3 = input("What have you eaten today: ")
            td.write("\n ")
            td.write(f"{getdate()} {d3}")
            print("Updated")
            td.close()
        elif type5 == "E":
            te = open("Taman_ex.txt", "a")
            e3 = input("Which exercise did you do: ")
            te.write("\n ")
            te.write(f"{getdate()} {e3}")
            print("Updated")
            te.close()
    elif action3 == "R":
        print("Diet('D') or Exercise('E')")
        type6 = input()
        if type6 == "D":
            tdr = open("Taman_diet.txt")
            print(tdr.read())
        elif type6 == "E":
            ter = open("Taman_ex.txt")
            print(ter.read())
