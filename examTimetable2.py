import datetime as dt
import time

while True:
    x = dt.datetime.now()
    lis = []
    q = input("Check or Add? ").lower()

    if q in ["check", "c"]:
        with open("examFile.txt") as file:
            for line in file:
                f = line.strip().split(", ")
                s = f[1].split("/")
                if int(s[0]) < int(x.strftime("%d")) and int(s[1]) <= int(x.strftime("%m")):
                    print(f"{f[0]} is done.")
                elif int(s[1]) < int(x.strftime("%m")):
                    print(f"{f[0]} is done.")
                else:
                    lis.append((dt.datetime.strptime(f[1], "%d/%m/%Y"), f[0]))
            lis.sort()
            print("Next 3 exams are:")
            for i in range(min(3, len(lis))):
                print(f"{lis[i][1]} on ----> {lis[i][0].strftime('%d/%m/%Y')} <---- at {f[2]}")
            time.sleep(20)
            break

    elif q in ["add", "a"]:
        while True:
            testName = input("Enter Exam Name: ")
            testDate = input("Enter Exam Date (dd/mm/yyyy): ")
            testTime = input("Enter Exam Time: ")
            with open("examFile.txt", "a") as file:
                file.write(f"{testName}, {testDate}, {testTime}\n")
            loop = input("Add another exam? (yes/no): ").lower()
            if loop in ["n", "no"]:
                break
        print(open("examFile.txt").read())
        break

    else:
        print("Invalid input. Please try again.")
