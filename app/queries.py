import sqlite3

def connect():

    conn = sqlite3.connect("./project_database.db")

    cur = conn.cursor()

    return conn,cur

#Creation 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------



def create_db():

    conn,cur = connect()

    #cur.execute("CREATE TABLE user_info(UID integer primary key autoincrement,name varchar(50) NOT NULL,email varchar(50) NOT NULL,password varchar(20) NOT NULL);")
    #cur.execute("CREATE TABLE prog_cnt(pid integer,progress integer NOT NULL,foreign key(pid) references user_info(UID));")
    #cur.execute("CREATE TABLE indexno(id integer NOT NULL,path varchar(50) NOT NULL);")
    #cur.execute("CREATE TABLE quize(qid integer,q1m integer NOT NULL,q2m integer NOT NULL,foreign key(qid) references user_info(UID));")
    #cur.execute("INSERT INTO quize values(1,0,0);")

    #----------------------------------------------------------------------------------------------
    #--------------trigger function for quize and prog_cnt table---------------------------------------------------------------
    #cur.execute("CREATE TRIGGER newquizprog AFTER INSERT ON user_info BEGIN INSERT INTO quize values(NEW.UID,0,0); INSERT INTO prog_cnt values(NEW.UID,0); END;")
    
    #-------------------view---------------------------------------------------------------------
    #cur.execute("CREATE VIEW profile_view AS SELECT u.name as name,u.email as email,p.progress as progress,q.q1m as q1m,q.q2m as q2m FROM user_info u JOIN prog_cnt p ON u.UID=p.pid JOIN quize q on q.qid = u.UID;")
    #cur.execute("DROP VIEW profile_view;")
    #----------------------------------------------------------------------------------
    #-----------------------Index-----------------------------------------------------
    #cur.execute("CREATE INDEX email_index ON user_info(email);")
    #-------------------------path-----------------------------------------------------------
    #cur.execute("CREATE INDEX path_index ON indexno(path);")

    cur.execute("INSERT INTO indexno values(1,'Z://my project//json_files//book.txt');")
    cur.execute("INSERT INTO indexno values(2,'Z://my project//json_files//book2.txt');")
    cur.execute("INSERT INTO indexno values(3,'Z://my project//json_files//book3.txt');")
    cur.execute("INSERT INTO indexno values(4,'Z://my project//json_files//book4.txt');")
    cur.execute("INSERT INTO indexno values(5,'Z://my project//json_files//book5.txt');")
    cur.execute("INSERT INTO indexno values(6,'Z://my project//json_files//book6.txt');")
    cur.execute("INSERT INTO indexno values(7,'Z://my project//json_files//book7.txt');")
    cur.execute("INSERT INTO indexno values(8,'Z://my project//json_files//book8.txt');")
    cur.execute("INSERT INTO indexno values(9,'Z://my project//json_files//book9.txt');")
    cur.execute("INSERT INTO indexno values(10,'Z://my project//json_files//book10.txt');")
    
    conn.commit()
    conn.close()
#----------------------------------------------------------------
#insertion------------------------------------------------

def add_user(name,email,password):
    conn,cur = connect()
    cur.execute("SELECT * FROM user_info where email = ?;",(email,))
    data = cur.fetchall()
    if(data):
        conn.close()
        return 0
    else:
        cur.execute("INSERT INTO user_info values(null,?,?,?);",(name,email,password,))
        #cur.execute("SELECT UID FROM user_info where email = ?;",(email,))
        #data1 = cur.fetchone()
        #cur.execute("INSERT INTO prog_cnt values(?,0);",(data1))
        #cur.execute("call pc(data1)",(data1,))
        conn.commit()
        conn.close()
        return 1
#verify---------------------------------------------------------
def verify_user(email,password):
    conn,cur = connect()
    cur.execute("SELECT * FROM user_info where email = ? and password = ?;",(email,password,))
    data = cur.fetchone()
    cur.execute("Select * FROM user_info;")
    data1 = cur.fetchall()
    print(data1)
    if(data):
        conn.close()
        print(data)
        return 1,data
    else:
        conn.close()
        return 0,[]

#for forget password---------------------------------------------------------
def  forgetpassword(email):
    conn,cur = connect()
    cur.execute("SELECT * FROM user_info where email = ?;",(email,))
    data = cur.fetchone()
    if(data):
        conn.close()
        print(data)
        return 1,data
    else:
        conn.close()
        return 0,[]

#profile----------------------------------------------------------------------------------------
def profileview(User_Data):
    conn,cur = connect()
    cur.execute("SELECT * FROM profile_view where email = ?;",(User_Data[2],))
    data = cur.fetchone()
    conn.close()
    print(data)
    return data 

#-----------------------------------------------------------------------------------------------
#to increment progress count
def nextfunction(User_Data,value):
    conn,cur = connect()
    cur.execute("SELECT * FROM prog_cnt where pid = ?;",(User_Data[0],))
    temp = cur.fetchone()
    data = list(temp)
    if(data[1] < value):
        cur.execute("UPDATE prog_cnt set progress = ? where pid = ?;",(value,User_Data[0],))
    conn.commit()
    conn.close()

#-------------------------------------------------------------------------------------------------------
#to get path of files
def getpath(val):
    conn,cur = connect()
    cur.execute("SELECT * FROM indexno where id = ?;",(val,))
    data = cur.fetchone()
    conn.close()
    print(data)
    return data

#-------------------------------------------------------------------------------------------------------
#change password-------------------------------------------------------------------------------------

def update_password(User_Data,new_password):

    conn,cur = connect()

    cur.execute("UPDATE user_info SET password = ? where UID = ?;",(new_password,User_Data[0],))

    conn.commit()

    conn.close()

#define qz 1------------------------------------------------------------------------------
def qz1up(User_Data,r):
    conn,cur = connect()
    cur.execute("UPDATE quize SET q1m = ? where qid = ?;",(r,User_Data[0],))
    conn.commit()

    conn.close()

#define qz 2------------------------------------------------------------------------------
def qz2up(User_Data,r):
    conn,cur = connect()
    cur.execute("UPDATE quize SET q2m = ? where qid = ?;",(r,User_Data[0],))
    conn.commit()

    conn.close()

#define erase--------------------------------------------------------------------------------
def erase(User_Data):
    conn,cur = connect()
    cur.execute("UPDATE quize SET q1m = ?,q2m = ? where qid = ?;",(0,0,User_Data[0],))
    cur.execute("UPDATE prog_cnt SET progress = ? where pid = ?;",(0,User_Data[0],))
    conn.commit()

    conn.close()
