from app import app
from flask import Flask,redirect, url_for, request, render_template
from .queries import *
from app import json
app.config['SECRET_KEY'] = "YOU-WILL-NEVER-GUESS-THIS"


#To create the database for the first time

create_db()

User_Data = None
i = None
q=[]
#0:UID , 1:name , 2:email, 3: password 


@app.route('/')
def login():
    return render_template('abstract.html')
    

@app.route('/login')
def begin():
       return render_template('login.html') 

@app.route('/verifysignup',methods = ['POST','GET'])
def verifysignup():
    if (request.method == "POST"):
        fn = request.form['Fname']
        ln = request.form['Lname']
        name = fn+' '+ln
        email = request.form['email']
        password = request.form['password']
        flag = add_user(name,email,password)



        if flag==0:
            return render_template('login.html',msg2 = "Email is already registered")

        elif flag==1: 

            return render_template('login.html',msg1 = "Registration Successful, please login!")    
       




@app.route('/verifylogin',methods = ['POST'])
def verifylogin():
    global User_Data
    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        flag,data = verify_user(email,password)

        if flag==0:

         return render_template('login.html',msg = "Incorrect email or password")

            #print("invalid user")

        else:
            User_Data = list(data)
            data = getpath(1)
            temp = list(data)
            f = open(temp[1],"r")
            s = f.read()
            import json
            book = json.loads(s)
            global q
            #q=[]
            for j in range(1,11):
                x = "pg" + str(j) + ".html"
                #x = "".join(["pg",str(i),".html"])
                q.append(x)
            return render_template('pg1.html',username = User_Data[1],p = book)
        

#qz1--------------------------------------------------------------------------
@app.route('/qz1')
def qz1():
    return render_template('qz1.html')
#check qz1--------------------------------------------------------------------
@app.route('/checkqz1',methods = ['POST'])
def checkqz1():
    r = 0
    if (request.method == "POST"):
        a1 = request.form['1']
        a2 = request.form['2']
        a3 = request.form['3']
        a4 = request.form['4']
        a5 = request.form['5']
        if a1 == '1':
            r = r+1
        if a2 == '1':
            r = r+1
        if a3 == '2':
            r = r+1
        if a4 == '2':
            r = r+1
        if a5 == '3':
            r = r+1
        qz1up(User_Data,r)
        data = getpath(4)
        temp = list(data)
        f = open(temp[1],"r")
        s = f.read()
        import json
        book = json.loads(s)
        return render_template('pg4.html',username = User_Data[1],p = book)
#quiz 2--------------------------------------------------------------------
@app.route('/qz2')
def qz2():
    return render_template('qz2.html')

@app.route('/checkqz2',methods = ['POST'])
def checkqz2():
    r = 0
    if (request.method == "POST"):
        a1 = request.form['1']
        a2 = request.form['2']
        a3 = request.form['3']
        a4 = request.form['4']
        a5 = request.form['5']
        if a1 == '2':
            r = r+1
        if a2 == '1':
            r = r+1
        if a3 == '3':
            r = r+1
        if a4 == '1':
            r = r+1
        if a5 == '2':
            r = r+1
        qz2up(User_Data,r)
        data = getpath(7)
        temp = list(data)
        f = open(temp[1],"r")
        s = f.read()
        import json
        book = json.loads(s)
        return render_template('pg7.html',username = User_Data[1],p = book)

#forget password----------------------------------------------------------------
@app.route('/fp')
def fpw():
    return render_template('forgetpass.html')

@app.route('/forgetpass',methods = ['POST'])
def forget():
    if request.method == 'POST':

        email = request.form['email']
        flag,data = forgetpassword(email)

        if flag==0:

         return render_template('forgetpass.html',msg2 = "Incorrect email")

            #print("invalid user")

        else:
            tem = list(data)
            return render_template('forgetpass.html',msg1 = tem[3])
#-------------------------------------------------------------------------------
# profile---------------------------------------------------------------------
@app.route('/profile')
def profile():
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

@app.route('/main')
def main():
    data = getpath(1)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg1.html',username = User_Data[1],p = book)

#---------------------------------------------------------------------------------------
#change password------------------------------------------------------------------------
@app.route('/change')
def change():
    return render_template('changepass.html',username = User_Data[1])

@app.route('/alter_password', methods = ['POST'])

def change_password():

    global User_Data

    old_password = request.form['old_password']

    new_password = request.form['new_password']

    confirm_password = request.form['Confirm_password']



    #checking if the old password entered is right

    if old_password == User_Data[3]:

        if old_password == new_password:

            return render_template('changepass.html',msg1 = 'Enter a new password')

        elif confirm_password!=new_password:

            return render_template('changepass.html',msg1 = 'Passwords don/t match')

        else:

            update_password(User_Data,new_password)

            User_Data[3] = new_password

            return render_template('changepass.html',msg2 = "Password updated succesfully, please go to profile page!!")

            #return render_template('user_home.html',username = User_Data[1])

    else:

        return render_template('changepass.html',msg1 = 'Wrong password')

#--page 1-------------------------------------------------------------------------------
#main page next button
@app.route('/pg1')
def main1():
    nextfunction(User_Data,1)
    data = getpath(2)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg2.html',username = User_Data[1],p = book)

#----page 2----------------------------------------------------------------------------
@app.route('/pg2')
def main2():
    nextfunction(User_Data,2)
    data = getpath(3)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg3.html',username = User_Data[1],p = book)



@app.route('/pg2p')
def main2p():
    data = getpath(1)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg1.html',username = User_Data[1],p = book)

#---------------------------------------------------------------------------------------------
#page 3---------------------------------------------------------------------------
#@app.route('/pg3')
#def main3():
    #nextfunction(User_Data,3)
    #data = getpath(4)
    #temp = list(data)
    #f = open(temp[1],"r")
    #s = f.read()
    #import json
    #book = json.loads(s)
    #return render_template('pg4.html',username = User_Data[1],p = book)

@app.route('/pg3p')
def main3p():
    data = getpath(2)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg2.html',username = User_Data[1],p = book)

#---------------------------------------------------------------------------------
#page 4-------------------------------------------------------------------------
@app.route('/pg4')
def main4():
    nextfunction(User_Data,4)
    data = getpath(5)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg5.html',username = User_Data[1],p = book)

@app.route('/pg4p')
def main4p():
    data = getpath(3)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg3.html',username = User_Data[1],p = book)

#-----------------------------------------------------------------------------------------------------
#page 5-----------------------------------------------------------------------------
@app.route('/pg5')
def main5():
    nextfunction(User_Data,5)
    data = getpath(6)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg6.html',username = User_Data[1],p = book)

@app.route('/pg5p')
def main5p():
    data = getpath(4)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg4.html',username = User_Data[1],p = book)

#---------------------------------------------------------------------------------------------------------
#page 6----------------------------------------------------------------------------------------------
#@app.route('/pg6')
#def main6():
    #nextfunction(User_Data,6)
    #data = getpath(7)
    #temp = list(data)
    #f = open(temp[1],"r")
    #s = f.read()
    #import json
    #book = json.loads(s)
    #return render_template('pg7.html',username = User_Data[1],p = book)

@app.route('/pg6p')
def main6p():
    data = getpath(5)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg5.html',username = User_Data[1],p = book)

#------------------------------------------------------------------------------------------------------
#page 7------------------------------------------------------------------------------------------------
@app.route('/pg7')
def main7():
    nextfunction(User_Data,7)
    data = getpath(8)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg8.html',username = User_Data[1],p = book)

@app.route('/pg7p')
def main7p():
    data = getpath(6)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg6.html',username = User_Data[1],p = book)

#---------------------------------------------------------------------------------------------------
#page 8---------------------------------------------------------------------------------------------
@app.route('/pg8')
def main8():
    nextfunction(User_Data,8)
    data = getpath(9)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg9.html',username = User_Data[1],p = book)

@app.route('/pg8p')
def main8p():
    data = getpath(7)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg7.html',username = User_Data[1],p = book)

#---------------------------------------------------------------------------------------------------
#page 9--------------------------------------------------------------------------------------------
@app.route('/pg9')
def main9():
    nextfunction(User_Data,9)
    data = getpath(10)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg10.html',username = User_Data[1],p = book)

@app.route('/pg9p')
def main9p():
    data = getpath(8)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg8.html',username = User_Data[1],p = book)

#---------------------------------------------------------------------------------------------------
#page 10--------------------------------------------------------------------------------------------
@app.route('/pg10')
def main10():
    nextfunction(User_Data,10)
    return render_template('finalquiz.html')

@app.route('/pg10p')
def main10p():
    data = getpath(9)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg9.html',username = User_Data[1],p = book)

#profile 1-----------------------------------------------------------------------------------------
@app.route('/profile1')
def f1():
    global i
    i = 1
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 2----------------------------------------------------------------------------------
@app.route('/profile2')
def f2():
    global i
    i = 2
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 3--------------------------------------------------------------------------------
@app.route('/profile3')
def f3():
    global i
    i = 3
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 4--------------------------------
@app.route('/profile4')
def f4():
    global i
    i = 4
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 5-----
@app.route('/profile5')
def f5():
    global i
    i = 5
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 6--------------
@app.route('/profile6')
def f6():
    global i
    i = 6
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 7------------
@app.route('/profile7')
def f7():
    global i
    i = 7
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 8---------------
@app.route('/profile8')
def f8():
    global i
    i = 8
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 9-----------------
@app.route('/profile9')
def f9():
    global i
    i = 9
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#profile 10----------------
@app.route('/profile10')
def f10():
    global i
    i = 10
    data = profileview(User_Data)
    temp = list(data)
    return render_template('profile.html',m1 = temp[0],m2 = temp[1],m3 = (temp[2]/10)*100,m4 = temp[3],m5 = temp[4])

#choose html--------------------------------------------
@app.route('/chfl')
def wat():
    data = getpath(i)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template(q[i-1],username = User_Data[1],p = book)

#--------------------------------------------------------------------------------------------------
#final quiz-------------------------------------------------------------------------------------------
@app.route('/checkfqz',methods = ['POST'])
def checkfqz():
    r = 0
    if (request.method == "POST"):
        a1 = request.form['1']
        a2 = request.form['2']
        a3 = request.form['3']
        a4 = request.form['4']
        a5 = request.form['5']
        a6 = request.form['6']
        a7 = request.form['7']
        a8 = request.form['8']
        a9 = request.form['9']
        a10 = request.form['10']
        if a1 == '1':
            r = r+1
        if a2 == '2':
            r = r+1
        if a3 == '2':
            r = r+1
        if a4 == '3':
            r = r+1
        if a5 == '1':
            r = r+1
        if a6 == '3':
            r = r+1
        if a7 == '2':
            r = r+1
        if a8 == '1':
            r = r+1
        if a9 == '3':
            r = r+1
        if a10 == '2':
            r = r+1
        y = r*5
        data = profileview(User_Data)
        temp = list(data)
        x = (temp[3] + temp[4])*5
        result = y + x
        if result >= 50 :
            return render_template('success.html',r = r,result = result,temp = temp)
        else:
            return render_template('failure.html',r = r,result = result,temp = temp)

           # temp  0:name 1:email 2:progresscount 3:qz1_marks 4:qz2_marks 
        
#After completing course logout------------------------------------------------------------
@app.route('/loginc')
def beginc():
    erase(User_Data) 
    data = getpath(1)
    temp = list(data)
    f = open(temp[1],"r")
    s = f.read()
    import json
    book = json.loads(s)
    return render_template('pg1.html',username = User_Data[1],p = book)

