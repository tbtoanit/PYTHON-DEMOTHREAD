import threading

listData = range(1,200)

def sendEmail():
    print("Starting email sending.....")
    for i in listData:
        print("Gia tri send email thu: ", i)
    print("Ending email sending!")

def insertData():
    print("Starting data inserting.....")
    for i in listData:
        print("Gia tri save data thu: ", i)
    print("Ending data saving!")

t1 = threading.Thread(target=sendEmail)
t2 = threading.Thread(target=insertData)
t1.start()
t1.join()
t2.start()
