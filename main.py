from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
import json
from django.db.models import Q
import pdfkit

# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='kusumachandashwini'


# this is for getting unique user access
login_manager = LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/sms'
db=SQLAlchemy(app)

# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Department(db.Model):
    cid=db.Column(db.Integer,primary_key=True)
    branch=db.Column(db.String(100))

class Attendence(db.Model):
    aid=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(100))
    attendance=db.Column(db.Integer())

class addarrear(db.Model):
    arid=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(100))
    arrear=db.Column(db.Integer())

class Trig(db.Model):
    tid=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(100))
    action=db.Column(db.String(100))
    timestamp=db.Column(db.String(100))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))





class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(50))
    sname=db.Column(db.String(50))
    sem=db.Column(db.Integer)
    gender=db.Column(db.String(50))
    branch=db.Column(db.String(50))
    email=db.Column(db.String(50))
    number=db.Column(db.String(12))
    address=db.Column(db.String(100))
    
class Year(db.Model):
    SL_NO = db.Column(db.Integer, primary_key=True)
    APPL_NO	= db.Column(db.String(50))
    ROLL_NO	= db.Column(db.Integer)
    NAME = db.Column(db.String(50))	
    DOB_YYYY_MM_DD	= db.Column(db.String(50))	
    GENDER = db.Column(db.String(50))
    DEGREE = db.Column(db.String(50))
    BRANCH	= db.Column(db.String(50))
    MODE = db.Column(db.String(50))	
    TYPE = db.Column(db.String(100)) 	
    BLOOD_GROUP	= db.Column(db.String(100)) 
    NATIONALITY	= db.Column(db.String(100)) 
    RELIGION = db.Column(db.String(100)) 	
    COMMUNITY	= db.Column(db.String(100)) 
    SUB_CASTE	= db.Column(db.String(100)) 
    PERSONAL_IDENTIFICATION	= db.Column(db.String(100)) 
    ID_TYPE	= db.Column(db.String(100)) 
    ID_NUMBER	= db.Column(db.String(100)) 
    MOTHER_LANGUAGE	= db.Column(db.String(100)) 
    OTHER_LANGUAGE	= db.Column(db.String(100)) 
    HEIGHT	= db.Column(db.String(100)) 
    WEIGHT	= db.Column(db.String(100)) 
    ANY_ALIGNMENT	= db.Column(db.String(100)) 
    ALERGIC	= db.Column(db.String(100)) 
    HOBBIES	= db.Column(db.String(100)) 
    MOBILE	= db.Column(db.String(100)) 
    E_MAIL	= db.Column(db.String(100)) 
    PMS	= db.Column(db.String(100)) 
    DA	= db.Column(db.String(100)) 
    FG	= db.Column(db.String(100)) 
    Column_10TH_REGISTER_NO	= db.Column(db.String(100)) 
    Column_10TH_MARK = db.Column(db.String(100)) 	
    Column_10TH_OVERALLPERCENTAGE	= db.Column(db.String(100)) 
    Column_12TH_REGISTER_NO	= db.Column(db.String(100)) 
    Column_12TH_MARK	= db.Column(db.String(100)) 
    Column_12TH_OVERALLPERCENTAGE	= db.Column(db.String(100)) 
    MATHS	= db.Column(db.String(100)) 
    PHYSICS	= db.Column(db.String(100)) 
    CHEMISTRY	= db.Column(db.String(100)) 
    COUNCILING_CUTOFF	= db.Column(db.String(100)) 
    COUNCELING_RANK	= db.Column(db.String(100)) 
    BOARD_OF_EXAM	= db.Column(db.String(100)) 
    SCHOOL_UNDER	= db.Column(db.String(100)) 
    SCHOOL_NAME	= db.Column(db.String(100)) 
    MEDIUM	= db.Column(db.String(100)) 
    DIPLOMA_STATUS	= db.Column(db.String(100)) 
    DIPLOMA_IN	= db.Column(db.String(100)) 
    OVERALLPERCENTAGE	= db.Column(db.String(100)) 
    COLLEGE_NAME	= db.Column(db.String(100)) 
    UG_PG_STATUS	= db.Column(db.String(100)) 
    UG_PG	= db.Column(db.String(100)) 
    OVERALLPERCENTAGE_1	= db.Column(db.String(100)) 
    COLLEGE_NAME_1	= db.Column(db.String(100)) 
    EXTRA_CURRICULAR	= db.Column(db.String(100)) 
    ACHIVEMENT	= db.Column(db.String(100)) 
    HOSTEL_REQUIREMENT	= db.Column(db.String(100)) 
    FATHER_NAME	= db.Column(db.String(100)) 
    FATHER_OCCUPATION	= db.Column(db.String(100)) 
    FATHER_MOBILE	= db.Column(db.String(100)) 
    FATHER_MAIL	= db.Column(db.String(100)) 
    MOTHER_NAME	= db.Column(db.String(100)) 
    MOTHER_OCCUPATION	= db.Column(db.String(100)) 
    MOTHER_MOBILE	= db.Column(db.String(100)) 
    MOTHER_MAIL	= db.Column(db.String(100)) 
    PERMENANT_ADDRESS_1	= db.Column(db.String(100)) 
    PERMENANT_ADDRESS_2	= db.Column(db.String(100)) 
    DISTRICT	= db.Column(db.String(100)) 
    STATE	= db.Column(db.String(100)) 
    PINCODE	= db.Column(db.String(100)) 
    COMMUNICATION_ADDRESS_1	= db.Column(db.String(100)) 
    COMMUNICATION_ADDRESS_2	= db.Column(db.String(100)) 
    DISTRICT_1	= db.Column(db.String(100)) 
    STATE_1	= db.Column(db.String(100)) 
    PINCODE_1	= db.Column(db.String(100)) 
    CATEGORY	= db.Column(db.String(100)) 
    GURDIAN	= db.Column(db.String(100)) 
    MOBILE_1	= db.Column(db.String(100)) 
    GURD_ADDRESS_1	= db.Column(db.String(100)) 
    GURD_ADDRESS_2	= db.Column(db.String(100)) 
    DISTRICT_2	= db.Column(db.String(100)) 
    STATE_2	= db.Column(db.String(100)) 
    PINCODE_2	= db.Column(db.String(100)) 
    SIBILING_REGNO	= db.Column(db.String(100)) 
    RELATION_TYPE = db.Column(db.String(100)) 
    ANNUAL_INCOME	= db.Column(db.String(100)) 
    PROGRAMME	= db.Column(db.String(100)) 
    CAMPCODE	= db.Column(db.String(100)) 
    ADMISSION_DATE_YYYY_MM_DD	= db.Column(db.String(100)) 
    
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    # Get the HTML content
    html = open('studentdetails.html').read()

    # Generate the PDF file
    pdf = pdfkit.from_string(html, False)

    # Create a response with the PDF file
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response

@app.route('/studentdetails', methods=['POST', 'GET'])
def search_student():
    query=Year.query.all()
    reg = request.form['roll']
    search=Year.query.filter_by(APPL_NO=reg).first()
    return render_template('studentdetails.html',query=query)

@app.route('/studentdetails', methods=['POST', 'GET'])
def search_student():
    query = Year.query.all()
    search = None
    if request.method == 'POST':
        reg = request.form.get('roll')
        if reg:
            search = Year.query.filter_by(APPL_NO=reg).first()
    return render_template('studentdetails.html', query=query, search=search)

    
# @app.route('/studentdetails', methods=['POST', 'GET'])
# def search_student():
#     query = request.form.get('search', '')  # get the search query from the URL parameter
#     if query:
#         results = Year.query.filter(
#             (Student.APPL_NO.ilike(f'%{query}%')) |
#             (Student.ROLL_NO.ilike(f'%{query}%')) |
#             (Student.NAME.ilike(f'%{query}%'))
#         ).all()
#     else:
#         results = Year.query.all()
#     return render_template('scholarsearch.html', results=results)

# def index(request):
#     query = None
#     if request.GET.get('search'):
#         query = request.GET.get('search')
#         results = Student.objects.filter(
#             Q(APPL_NO__icontains=query) | Q(ROLL_NO__icontains=query) | Q(NAME__icontains=query)
#         )
#     else:
#         results = Student.objects.all()
#     return render(request, 'index.html', {'query': query, 'results': results})

@app.route('/triggers')
def triggers():
    # query=db.engine.execute(f"SELECT * FROM `trig`") 
    query=Trig.query.all()
    return render_template('triggers.html',query=query)



@app.route('/addattendance',methods=['POST','GET'])
def addattendance():
    # query=db.engine.execute(f"SELECT * FROM `student`") 
    query=Student.query.all()
    if request.method=="POST":
        rollno=request.form.get('rollno')
        attend=request.form.get('attend')
        print(attend,rollno)
        atte=Attendence(rollno=rollno,attendance=attend)
        db.session.add(atte)
        db.session.commit()
        flash("Attendance added","warning")

        
    return render_template('attendance.html',query=query)
# arrear
@app.route('/addarrear',methods=['POST','GET'])
def addarr():
    # query=db.engine.execute(f"SELECT * FROM `student`") 
    query=Student.query.all()
    if request.method=="POST":
        rollno=request.form.get('rollno')
        arr=request.form.get('arr')
        print(arr,rollno)
        atten=addarrear(rollno=rollno,arrear=arr)
        db.session.add(atten)
        db.session.commit()
        flash("Arrear added","warning")

        
    return render_template('arrear.html',query=query)

@app.route('/search',methods=['POST','GET'])
def search():
    if request.method=="POST":
        rollno=request.form.get('roll')
        bio=Student.query.filter_by(rollno=rollno).first()
        attend=Attendence.query.filter_by(rollno=rollno).first()
        arr=addarrear.query.filter_by(rollno=rollno).first()
        return render_template('search.html',bio=bio,attend=attend,arr=arr)
        
    return render_template('search.html')

@app.route("/delete/<string:id>",methods=['POST','GET'])
@login_required
def delete(id):
    post=Student.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    # db.engine.execute(f"DELETE FROM `student` WHERE `student`.`id`={id}")
    flash("Slot Deleted Successful","danger")
    return redirect('/studentdetails')


@app.route("/edit/<string:id>",methods=['POST','GET'])
@login_required
def edit(id):
    # dept=db.engine.execute("SELECT * FROM `department`")    
    if request.method=="POST":
        rollno=request.form.get('rollno')
        sname=request.form.get('sname')
        sem=request.form.get('sem')
        gender=request.form.get('gender')
        branch=request.form.get('branch')
        email=request.form.get('email')
        num=request.form.get('num')
        address=request.form.get('address')
        # query=db.engine.execute(f"UPDATE `student` SET `rollno`='{rollno}',`sname`='{sname}',`sem`='{sem}',`gender`='{gender}',`branch`='{branch}',`email`='{email}',`number`='{num}',`address`='{address}'")
        post=Student.query.filter_by(id=id).first()
        post.rollno=rollno
        post.sname=sname
        post.sem=sem
        post.gender=gender
        post.branch=branch
        post.email=email
        post.number=num
        post.address=address
        db.session.commit()
        flash("Slot is Updates","success")
        return redirect('/studentdetails')
    dept=Department.query.all()
    posts=Student.query.filter_by(id=id).first()
    return render_template('edit.html',posts=posts,dept=dept)


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        encpassword=generate_password_hash(password)

        # new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")

        # this is method 2 to save data in db
        newuser=User(username=username,email=email,password=encpassword)
        db.session.add(newuser)
        db.session.commit()
        flash("Signup Succes Please Login","success")
        return render_template('login.html')

          

    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')    

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))



@app.route('/addstudent',methods=['POST','GET'])
@login_required
def addstudent():
    # dept=db.engine.execute("SELECT * FROM `department`")
    dept=Department.query.all()
    if request.method=="POST":
        rollno=request.form.get('rollno')
        sname=request.form.get('sname')
        sem=request.form.get('sem')
        gender=request.form.get('gender')
        branch=request.form.get('branch')
        email=request.form.get('email')
        num=request.form.get('num')
        address=request.form.get('address')
        # query=db.engine.execute(f"INSERT INTO `student` (`rollno`,`sname`,`sem`,`gender`,`branch`,`email`,`number`,`address`) VALUES ('{rollno}','{sname}','{sem}','{gender}','{branch}','{email}','{num}','{address}')")
        query=Student(rollno=rollno,sname=sname,sem=sem,gender=gender,branch=branch,email=email,number=num,address=address)
        db.session.add(query)
        db.session.commit()

        flash("Student data stored","info")


    return render_template('student.html',dept=dept)
@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'

# start

@app.route('/itdb')
def itdb():
    sdata = Student.query.filter(Student.branch.ilike("Information Technology"))
    results = [student.sname for student in sdata]
    return render_template('search.html',results=results)

@app.route('/csedb')
def csedb():
    sdata = Student.query.filter(Student.branch.ilike("computer science"))
    resultCse = [student.sname for student in sdata]
    return render_template('search.html',resultCse=resultCse)

@app.route('/ecedb')
def ecedb():
    sdata = Student.query.filter(Student.branch.ilike("Electronic and Communication"))
    resultEce = [student.sname for student in sdata]
    return render_template('search.html',resultEce=resultEce)

@app.route('/eeedb')
def eeedb():
    sdata = Student.query.filter(Student.branch.ilike("Electrical & Electronic"))
    resultEee = [student.sname for student in sdata]
    return render_template('search.html',resultEee=resultEee)

@app.route('/mechdb')
def mechdb():
    sdata = Student.query.filter(Student.branch.ilike("Mechanical"))
    resultMech = [student.sname for student in sdata]
    return render_template('search.html',resultMech=resultMech)

@app.route('/civildb')
def civildb():
    sdata = Student.query.filter(Student.branch.ilike("Civil "))
    resultCivil = [student.sname for student in sdata]
    return render_template('search.html',resultCivil=resultCivil)

@app.route('/mbadb')
def mbadb():
    sdata = Student.query.filter(Student.branch.ilike("Civil "))
    resultMba = [student.sname for student in sdata]
    return render_template('search.html',resultMba=resultMba)

# arrear
@app.route('/zeroar')
def zeroar():
    sdata = addarrear.query.filter(addarrear.arrear==0)
    str= [addarrear.rollno for addarrear in sdata]
    return render_template('search.html',str=str)

@app.route('/onear')
def onear():
    sdata = addarrear.query.filter(addarrear.arrear==0)
    str1= [addarrear.rollno for addarrear in sdata]
    return render_template('search.html',str1=str1)





# end

app.run(debug=True)    