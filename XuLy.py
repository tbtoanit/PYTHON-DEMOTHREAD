#new version
import pyodbc
server = 'DLAP-0064'
database = 'QUAN_LY_KHACH_HANG'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database + ';Trusted_Connection=yes;')
cursor = cnxn.cursor()



def insertKH():
    cursor.execute('''INSERT INTO KHACH_HANG(MA_KHACH_HANG, TEN_KHACH_HANG) VALUES('KH002','TRAN VAN B');''')
    cnxn.commit()
    print("Them Du Lieu Thanh Cong")

insertKH()

def getKhachHang():
    cursor.execute("SELECT * FROM KHACH_HANG;")
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()

getKhachHang()
