# Generated by Django 5.0.1 on 2024-03-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DegreeShortForm', models.CharField(max_length=1000)),
                ('TyprOfPgm', models.CharField(max_length=255)),
                ('DeptName', models.CharField(max_length=255)),
                ('CourseCode', models.CharField(max_length=255)),
                ('Duration', models.CharField(max_length=255)),
                ('Graduate', models.CharField(max_length=255)),
                ('BelongstoDept', models.CharField(max_length=255)),
                ('TimeTableTypes', models.CharField(max_length=255)),
                ('AcademicYear', models.CharField(max_length=255)),
                ('ApplicationCourseCode', models.CharField(max_length=255)),
                ('School', models.CharField(max_length=255)),
                ('DegreeType', models.CharField(max_length=255)),
                ('Coursecompletion', models.CharField(max_length=255)),
                ('Course_ShortForm', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Admin_Course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HRMADPositionHeld',
            fields=[
                ('EmpId', models.IntegerField(primary_key=True, serialize=False)),
                ('PositionHeld', models.CharField(max_length=255)),
                ('Facsimile', models.CharField(max_length=255)),
                ('Management_Authority', models.CharField(max_length=255)),
                ('Position_Priority', models.IntegerField()),
                ('Priority_Level', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Belongstodept', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'HRM_AD_PositionHeld',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HRMPersonnelInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('EmpId', models.CharField(max_length=255)),
                ('EmpName', models.CharField(max_length=255)),
                ('DOJ', models.DateField()),
                ('DepartmentCode', models.CharField(max_length=255)),
                ('Designation', models.CharField(max_length=255)),
                ('NatureOfEmp', models.CharField(max_length=255)),
                ('TypeOfEmp', models.CharField(max_length=255)),
                ('DateOnRelived', models.DateField(null=True)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('MartialStatus', models.CharField(max_length=255)),
                ('SpouseName', models.CharField(max_length=255)),
                ('WeddingDate', models.DateField(null=True)),
                ('MotherTongue', models.CharField(max_length=255)),
                ('LanguageKnown', models.CharField(max_length=255)),
                ('BloodGroup', models.CharField(max_length=5)),
                ('FathersName', models.CharField(max_length=255)),
                ('MothersName', models.CharField(max_length=255)),
                ('Nationality', models.CharField(max_length=255)),
                ('Religion', models.CharField(max_length=255)),
                ('Caste', models.CharField(max_length=255)),
                ('Community', models.CharField(max_length=255)),
                ('PDoorNo', models.CharField(max_length=255)),
                ('PStreetName', models.CharField(max_length=255)),
                ('PTown', models.CharField(max_length=255)),
                ('PDistrict', models.CharField(max_length=255)),
                ('PState', models.CharField(max_length=255)),
                ('PPincode', models.CharField(max_length=10)),
                ('PEmailID', models.EmailField(max_length=254)),
                ('PTelNo', models.CharField(max_length=20)),
                ('PMobNo', models.CharField(max_length=20)),
                ('CDoorNo', models.CharField(max_length=255)),
                ('CStreetName', models.CharField(max_length=255)),
                ('CTown', models.CharField(max_length=255)),
                ('CDistrict', models.CharField(max_length=255)),
                ('CState', models.CharField(max_length=255)),
                ('CPincode', models.CharField(max_length=10)),
                ('CEmailID', models.EmailField(max_length=254)),
                ('CTelNo', models.CharField(max_length=20)),
                ('CMobNo', models.CharField(max_length=20)),
                ('Payscale', models.CharField(max_length=255)),
                ('BankAcc', models.CharField(max_length=255)),
                ('EPF', models.CharField(max_length=255)),
                ('PanCard', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('WorkingStatus', models.CharField(max_length=255)),
                ('SalaryStatus', models.CharField(max_length=255)),
                ('Libdue', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('barcodename', models.CharField(max_length=255)),
                ('Salutation', models.CharField(max_length=255)),
                ('AadharNumber', models.CharField(max_length=255)),
                ('Working_Type', models.CharField(max_length=255)),
                ('Alloted_CL', models.CharField(max_length=255)),
                ('Priority', models.CharField(max_length=255)),
                ('SalaryAccDeatils', models.CharField(max_length=255)),
                ('OTP', models.CharField(max_length=255)),
                ('OTP_Status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'HRM_PersonnelInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IPTMaster',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('pcode', models.CharField(max_length=20)),
                ('batch', models.CharField(max_length=20)),
                ('academic_year', models.CharField(max_length=20)),
                ('enterby', models.CharField(max_length=50)),
                ('enter_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'ipt_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IPTMentors',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('regno', models.CharField(max_length=20)),
                ('empid', models.CharField(max_length=10)),
                ('academicyear', models.CharField(max_length=20)),
                ('enterby', models.CharField(max_length=20)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ipt_mentors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IPTStudent',
            fields=[
                ('ipdid', models.AutoField(primary_key=True, serialize=False)),
                ('regno', models.CharField(max_length=20, unique=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('noofdays', models.IntegerField()),
                ('academic_year', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('enterby', models.CharField(max_length=30)),
                ('enter_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'iptstudent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SISStudentInfo',
            fields=[
                ('Adno', models.IntegerField(primary_key=True, serialize=False)),
                ('RegNo', models.CharField(max_length=255)),
                ('StudentName', models.CharField(max_length=255)),
                ('DCode', models.CharField(max_length=255)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('Fathername', models.CharField(max_length=255)),
                ('Mothername', models.CharField(max_length=255)),
                ('P_DoorNo', models.CharField(max_length=255)),
                ('P_StreetName', models.CharField(max_length=255)),
                ('P_Town', models.CharField(max_length=255)),
                ('P_District', models.CharField(max_length=255)),
                ('P_State', models.CharField(max_length=255)),
                ('P_Country', models.CharField(max_length=255)),
                ('P_Pincode', models.CharField(max_length=10)),
                ('Mobno', models.CharField(max_length=20)),
                ('Landlineno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('Nationality', models.CharField(max_length=255)),
                ('Religion', models.CharField(max_length=255)),
                ('Community', models.CharField(max_length=255)),
                ('Caste', models.CharField(max_length=255)),
                ('C_DoorNo11', models.CharField(max_length=255)),
                ('C_StreetName11', models.CharField(max_length=255)),
                ('C_Town1', models.CharField(max_length=255)),
                ('C_District1', models.CharField(max_length=255)),
                ('C_State1', models.CharField(max_length=255)),
                ('C_Country1', models.CharField(max_length=255)),
                ('C_Pincode1', models.CharField(max_length=10)),
                ('Mothertongue', models.CharField(max_length=255)),
                ('FatherOccupation', models.CharField(max_length=255)),
                ('MotherOccupation', models.CharField(max_length=255)),
                ('MonthlyIncome', models.CharField(max_length=255)),
                ('HostelRequired', models.BooleanField(default=False)),
                ('Differentabled', models.BooleanField(default=False)),
                ('Sportsperson', models.BooleanField(default=False)),
                ('DOJ', models.DateField()),
                ('Batch', models.CharField(max_length=255)),
                ('Section', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Image', models.CharField(max_length=255)),
                ('BloodGroup', models.CharField(max_length=5)),
                ('CourseCompletion', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('barcodename', models.CharField(max_length=255)),
                ('R_L', models.CharField(max_length=10)),
                ('Libdue', models.CharField(max_length=255)),
                ('StrengthStatus', models.CharField(max_length=255)),
                ('PURA_Villages', models.CharField(max_length=255)),
                ('Discontinueddate', models.DateField(null=True)),
                ('Aadharnumber', models.CharField(max_length=255)),
                ('FeesType', models.CharField(max_length=255)),
                ('RoomType', models.CharField(max_length=255)),
                ('StudentType', models.CharField(max_length=255)),
                ('CourseType', models.CharField(max_length=255)),
                ('Appno', models.CharField(max_length=255)),
                ('MobNo_Verify_Status', models.BooleanField(default=False)),
                ('MobNo_Verification_Code', models.CharField(max_length=255)),
                ('Mobno_verifiedon', models.DateTimeField(null=True)),
                ('Student_MobNo', models.CharField(max_length=20)),
                ('MailId_Status', models.BooleanField(default=False)),
                ('MailId_Verifiedon', models.DateTimeField(null=True)),
                ('Password_status', models.CharField(max_length=255)),
                ('Other_EmailId', models.EmailField(max_length=254, null=True)),
                ('Mother_Mobno', models.CharField(max_length=20, null=True)),
                ('Guardian_MobNo', models.CharField(max_length=20, null=True)),
                ('Mother_MonthlyIncome', models.CharField(max_length=255, null=True)),
                ('Eligibility_Criteria', models.CharField(max_length=255, null=True)),
                ('Maxvalue', models.CharField(max_length=255, null=True)),
                ('ActualValue', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'SIS_StudentInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UpdateStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('regno', models.CharField(max_length=20)),
                ('tenth', models.CharField(max_length=5)),
                ('aqure_skill', models.CharField(max_length=80)),
                ('required_skill', models.CharField(max_length=100)),
                ('focus', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'updatestudent',
                'managed': False,
            },
        ),
    ]
