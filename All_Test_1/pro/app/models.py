from django.db import models
from django.utils import timezone

class IPTMaster(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    pcode = models.CharField(max_length=20)
    batch = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=20)
    pname=models.CharField(max_length=30)
    pdes=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    pemail=models.CharField(max_length=40)
    enterby = models.CharField(max_length=50)
    enter_datetime = models.DateTimeField()

    class Meta:
        db_table = 'ipt_master'

class IPTStudent(models.Model):
    ipdid = models.AutoField(primary_key=True)
    iptcid = models.ForeignKey(IPTMaster, on_delete=models.CASCADE)
    regno = models.CharField(max_length=20, unique=True)
    from_date = models.DateField()
    to_date = models.DateField()
    noofdays = models.IntegerField()
    academic_year = models.CharField(max_length=20)
    status = models.IntegerField(default=0)
    enterby = models.CharField(max_length=30)
    enter_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'iptstudent'

class IPTMentors(models.Model):
    mid = models.AutoField(primary_key=True)
    regno = models.CharField(max_length=20)
    empid = models.CharField(max_length=10)
    academicyear = models.CharField(max_length=20)
    enterby = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ipt_mentors'

class UpdateStudent(models.Model):
    id = models.AutoField(primary_key=True)
    regno = models.CharField(max_length=20)
    tenth = models.CharField(max_length=5)
    aqure_skill = models.CharField(max_length=80)
    required_skill = models.CharField(max_length=100)
    focus = models.CharField(max_length=10)

    class Meta:
        db_table = 'updatestudent'
        
class AdminCourse(models.Model):
    DegreeShortForm = models.CharField(max_length=50)
    TyprOfPgm = models.CharField(max_length=50)
    DeptName = models.CharField(max_length=50)
    CourseCode = models.CharField(max_length=50)
    Duration = models.IntegerField()
    Graduate = models.CharField(max_length=50)
    BelongstoDept = models.CharField(max_length=50)
    TimeTableTypes = models.CharField(max_length=200)
    AcademicYear = models.CharField(max_length=50)
    ApplicationCourseCode = models.CharField(max_length=50)
    School = models.CharField(max_length=50)
    DegreeType = models.CharField(max_length=50)
    Coursecompletion = models.CharField(max_length=50)
    Course_ShortForm = models.CharField(max_length=50)

    class Meta:
        db_table='Admin_Course'
        


class HRMADPositionHeld(models.Model):
    EmpId = models.CharField(max_length=50,primary_key=True)
    PositionHeld = models.CharField(max_length=255)
    Facsimile = models.ImageField()  # Assuming Facsimile is an image field
    Management_Authority = models.IntegerField()
    Position_Priority = models.IntegerField()
    Priority_Level = models.IntegerField()
    Email = models.CharField(max_length=255)
    Belongstodept = models.CharField(max_length=255)

    def __str__(self):
        return self.PositionHeld

    class Meta:
        db_table = 'HRM_AD_PositionHeld'

        
class SISStudentInfo(models.Model):
    StudentType = models.CharField(max_length=50)
    StudentName = models.CharField(max_length=50)
    Student_MobNo = models.CharField(max_length=50)
    StrengthStatus = models.CharField(max_length=50)
    Sportsperson = models.CharField(max_length=50)
    Section = models.CharField(max_length=50)
    RoomType = models.CharField(max_length=50)
    Religion = models.CharField(max_length=50)
    RegNo = models.CharField(max_length=50)
    R_L = models.CharField(max_length=50)
    PURA_Villages = models.CharField(max_length=50)
    Password_status = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    P_Town = models.CharField(max_length=50)
    P_StreetName = models.CharField(max_length=50)
    P_State = models.CharField(max_length=50)
    P_Pincode = models.CharField(max_length=50)
    P_DoorNo = models.CharField(max_length=50)
    P_District = models.CharField(max_length=50)
    P_Country = models.CharField(max_length=50)
    Other_EmailId = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=50)
    Mothertongue = models.CharField(max_length=50)
    MotherOccupation = models.CharField(max_length=50)
    Mothername = models.CharField(max_length=50)
    Mother_MonthlyIncome = models.CharField(max_length=50)
    Mother_Mobno = models.CharField(max_length=50)
    MonthlyIncome = models.IntegerField()
    MobNo_Verify_Status = models.CharField(max_length=50)
    Mobno_verifiedon = models.CharField(max_length=50)
    MobNo_Verification_Code = models.CharField(max_length=50)
    Mobno = models.CharField(max_length=50)
    Maxvalue = models.IntegerField()
    MailId_Verifiedon = models.CharField(max_length=50)
    MailId_Status = models.CharField(max_length=50)
    Libdue = models.IntegerField()
    Landlineno = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='student_images/')
    HostelRequired = models.CharField(max_length=50)
    Guardian_MobNo = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    FeesType = models.CharField(max_length=50)
    FatherOccupation = models.CharField(max_length=50)
    Fathername = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Eligibility_Criteria = models.CharField(max_length=50)
    DOJ = models.DateField(default=timezone.now)
    DOB = models.DateField(default=timezone.now)
    Discontinueddate = models.DateField(default=timezone.now)
    Differentabled = models.CharField(max_length=50)
    DCode = models.CharField(max_length=50)
    CourseType = models.CharField(max_length=50)
    CourseCompletion = models.CharField(max_length=50)
    Community = models.CharField(max_length=50)
    Caste = models.CharField(max_length=50)
    C_Town1 = models.CharField(max_length=50)
    C_StreetName11 = models.CharField(max_length=50)
    C_State1 = models.CharField(max_length=50)
    C_Pincode1 = models.CharField(max_length=50)
    C_DoorNo11 = models.CharField(max_length=50)
    C_District1 = models.CharField(max_length=50)
    C_Country1 = models.CharField(max_length=50)
    BloodGroup = models.CharField(max_length=50)
    Batch = models.CharField(max_length=50)
    barcodename = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50)
    Appno = models.CharField(max_length=50)
    Adno = models.CharField(max_length=50,primary_key=True)
    ActualValue = models.CharField(max_length=50)
    Aadharnumber = models.CharField(max_length=50, null=True, default='')
    Maxvalue = models.CharField(max_length=50)
   

    def __str__(self):
        return self.StudentName  # Or any other field you prefer to display

   

    class Meta:
        db_table = 'SIS_StudentInfo'        
        
class HRMPersonnelInfo(models.Model):
    EmpId = models.CharField(max_length=50, primary_key=True)  # Assuming EmpId is the primary key
    EmpName = models.CharField(max_length=50)
    DOJ = models.DateField(null=True)
    DepartmentCode = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    NatureOfEmp = models.CharField(max_length=50)
    TypeOfEmp = models.CharField(max_length=50)
    DateOnRelived = models.DateField(null=True)
    DOB = models.DateField(null=True)
    Gender = models.CharField(max_length=50)
    MartialStatus = models.CharField(max_length=50)
    SpouseName = models.CharField(max_length=50)
    WeddingDate = models.DateField(null=True)
    MotherTongue = models.CharField(max_length=50)
    LanguageKnown = models.CharField(max_length=50)
    BloodGroup = models.CharField(max_length=50)
    FathersName = models.CharField(max_length=50)
    MothersName = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=50)
    Religion = models.CharField(max_length=50)
    Caste = models.CharField(max_length=50)
    Community = models.CharField(max_length=50)
    PDoorNo = models.CharField(max_length=50)
    PStreetName = models.CharField(max_length=50)
    PTown = models.CharField(max_length=50)
    PDistrict = models.CharField(max_length=50)
    PState = models.CharField(max_length=50)
    PPincode = models.CharField(max_length=50)
    PEmailID = models.CharField(max_length=50)
    PTelNo = models.CharField(max_length=50)
    PMobNo = models.CharField(max_length=50)
    CDoorNo = models.CharField(max_length=50)
    CStreetName = models.CharField(max_length=50)
    CTown = models.CharField(max_length=50)
    CDistrict = models.CharField(max_length=50)
    CState = models.CharField(max_length=50)
    CPincode = models.CharField(max_length=50)
    CEmailID = models.CharField(max_length=50)
    CTelNo = models.CharField(max_length=50)
    CMobNo = models.CharField(max_length=50)
    Payscale = models.CharField(max_length=50)
    BankAcc = models.CharField(max_length=50)
    EPF = models.CharField(max_length=50)
    PanCard = models.CharField(max_length=50)
    image = models.ImageField(upload_to='personnel_images/')
    Password = models.CharField(max_length=50)
    WorkingStatus = models.CharField(max_length=50)
    SalaryStatus = models.CharField(max_length=50)
    Libdue = models.IntegerField()
    barcode = models.CharField(max_length=50)
    barcodename = models.CharField(max_length=50)
    Salutation = models.CharField(max_length=50)
    AadharNumber = models.CharField(max_length=50)
    Working_Type = models.CharField(max_length=50)
    Alloted_CL = models.CharField(max_length=50)
    Priority = models.CharField(max_length=50)
    SalaryAccDeatils = models.CharField(max_length=50)
    OTP = models.CharField(max_length=50)

    def __str__(self):
        return self.EmpName  # Or any other field you prefer to display

    class Meta:
        db_table = 'HRM_PersonnelInfo'
        
        
class PlacementMaster(models.Model):
    pcid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)
    jobrole = models.CharField(max_length=100)
    jobdescription = models.TextField()
    ten = models.CharField(max_length=10)
    twelve = models.CharField(max_length=10)
    cgpa = models.CharField(max_length=10)
    Idate = models.CharField(max_length=20)
    venue = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    batch = models.CharField(max_length=20)
    pcode = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=20)
    enterby = models.CharField(max_length=100)
    enter_datetime = models.DateTimeField()

    class Meta:
        db_table = 'PlacementMaster'
        
        
class PlacementStudent(models.Model):
    pid = models.AutoField(primary_key=True)
    pcid = models.ForeignKey('PlacementMaster', on_delete=models.CASCADE,db_column='pcid')
    regno = models.CharField(max_length=50)
    placeddate = models.DateField()
    academicyear = models.CharField(max_length=50)
    enterby = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
      # To indicate that Django should not manage this table
        db_table = 'PlacementStudent'  # Specify the actual table name in your database
      
