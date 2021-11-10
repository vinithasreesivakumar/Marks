import pymysql
db = pymysql.connect(host = 'localhost',database = 'student',user = 'root',password = 'root')

def insert():
    c = db.cursor()
    id = int(input('Enter the number:'))
    name = input('Enter the name:')
    address = input('Enter the address:')
    phonenumber = input('Enter the number:')
    sql = "insert into details values('%d','%s','%s','%s')" % (id,name,address,phonenumber)
    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()
def update():
    c = db.cursor()
    id = int(input("Enter the id : "))
    q = input('Enter the column name: ')
    q1 =input('Enter the changing value: ')
    sql = "update details set %s='%s' where id='%d'"% (q,q1,id)
    c.execute(sql)
    db.commit()
    
def view():
    i = int(input('Enter 31 to view particular details \nEnter 32 to view entire details \nEnter the number:'))
    if i==31:
        c = db.cursor()
        sql = "select * from details"
        y = input('Enter the column name you want to view: ')
        try:
            if y == 'id':
                c.execute(sql)
                val = c.fetchall()
                for x in val:
                    id = x[0]
                    print('id-> ',id)
        except:
            db.rollback()
        
        
        try:
            if y == 'name':
                c.execute(sql)
                val = c.fetchall()
                for x in val:
                    name = x[1]
                    print('name-> ',name)
        except:
            db.rollback()
        
        try:
            if y == 'address':
                c.execute(sql)
                val = c.fetchall()
                for x in val:
                    address = x[2]
                    print('address-> ',address)
        except:
            db.rollback()

        try:
            if y == 'phonenumber':
                c.execute(sql)
                val = c.fetchall()
                for x in val:
                    phonenumber = x[3]
                    print('phonenumber-> ',phonenumber)
        except:
            db.rollback()
        
    
    if i==32:
        c = db.cursor()
        sql = "select * from details"
        try:
            c.execute(sql)
            val = c.fetchall()
            for x in val:
                id = x[0]
                name = x[1]
                address = x[2]
                phonenumber = x[3]
                print('id-> ',id, 'name-> ',name,'address-> ',address, 'phonenumber-> ',phonenumber)
        except:
            db.rollback()

def delete():
    r = int(input('Enter 41 to delete particular details \nEnter 42 to delete entire details \nEnter the number: '))
    if r==31:
        c = db.cursor()
        id = int(input('Enter the id:'))
        sql = "delete from details where id = %d" % (id)
        try:
            c.execute(sql)
            db.commit()
        except:
            db.rollback()
    if r==32:
        c = db.cursor()
        r1 = input('Enter the table name: ')
        sql = "delete from %s" % (r1)

def option():
    a = int(input("Enter 1 to create \nEnter 2 to View \nEnter 3 to delete \nEnter 4 to Update \nEnter 5 to Exit \nEnter your Option : "))
    if a == 1:
        insert()
    elif a == 2:
        view()
    elif a == 3:
        delete()
    elif a == 4:
        update()
    elif a == 5:
        return

        
    return option()


option()
