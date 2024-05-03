from django.contrib import admin
from .models import IPTMaster, IPTStudent, IPTMentors, UpdateStudent, AdminCourse, HRMADPositionHeld, SISStudentInfo, HRMPersonnelInfo,PlacementMaster,PlacementStudent

@admin.register(IPTMaster)
class IPTMasterAdmin(admin.ModelAdmin):
    list_display = ('cname', 'pcode', 'batch', 'academic_year', 'enterby', 'enter_datetime')
    list_filter = ('batch', 'academic_year')

@admin.register(IPTStudent)
class IPTStudentAdmin(admin.ModelAdmin):
    list_display = ('regno', 'from_date', 'to_date', 'noofdays', 'academic_year', 'status', 'enterby', 'enter_datetime')
    list_filter = ('academic_year', 'status')

@admin.register(IPTMentors)
class IPTMentorsAdmin(admin.ModelAdmin):
    list_display = ('regno', 'empid', 'academicyear', 'enterby', 'datetime')
    list_filter = ('academicyear',)

@admin.register(UpdateStudent)
class UpdateStudentAdmin(admin.ModelAdmin):
    list_display = ('regno', 'tenth', 'aqure_skill', 'required_skill', 'focus')
    list_filter = ('tenth', 'focus')

@admin.register(AdminCourse)
class AdminCourseAdmin(admin.ModelAdmin):
    list_display = ('DegreeShortForm', 'TyprOfPgm', 'DeptName', 'CourseCode', 'Duration', 'Graduate', 'BelongstoDept', 'TimeTableTypes', 'AcademicYear', 'ApplicationCourseCode', 'School', 'DegreeType', 'Coursecompletion', 'Course_ShortForm')
    list_filter = ('DegreeShortForm', 'TyprOfPgm', 'DeptName', 'Duration', 'Graduate', 'TimeTableTypes', 'AcademicYear')

@admin.register(HRMADPositionHeld)
class HRMADPositionHeldAdmin(admin.ModelAdmin):
    list_display = ('EmpId', 'PositionHeld', 'Facsimile', 'Management_Authority', 'Position_Priority', 'Priority_Level', 'Email', 'Belongstodept')
    list_filter = ('Management_Authority', 'Position_Priority', 'Priority_Level')

@admin.register(SISStudentInfo)
class SISStudentInfoAdmin(admin.ModelAdmin):
    list_display = ('StudentType', 'StudentName','Section', 'RegNo','Password', 'email', 'Batch',  'Adno', 'ActualValue',)
    list_filter = ('StudentType', 'Section', 'Religion', 'R_L', 'Nationality', 'Gender', 'FeesType', 'Community', 'Caste', 'BloodGroup')

@admin.register(HRMPersonnelInfo)
class HRMPersonnelInfoAdmin(admin.ModelAdmin):
    list_display = ('EmpId', 'EmpName', 'DepartmentCode', 'Designation', 'NatureOfEmp', 'TypeOfEmp', 'DateOnRelived', 'DOB', 'Gender', 'MartialStatus', 'SpouseName', 'WeddingDate', 'MotherTongue', 'LanguageKnown', 'BloodGroup', 'FathersName', 'MothersName', 'Nationality', 'Religion', 'Caste', 'Community', 'PDoorNo', 'PStreetName', 'PTown', 'PDistrict', 'PState', 'PPincode', 'PEmailID', 'PTelNo', 'PMobNo', 'CDoorNo', 'CStreetName', 'CTown', 'CDistrict', 'CState', 'CPincode', 'CEmailID', 'CTelNo', 'CMobNo', 'Payscale', 'BankAcc', 'EPF', 'PanCard', 'image', 'Password', 'WorkingStatus', 'SalaryStatus', 'Libdue', 'barcode', 'barcodename', 'Salutation', 'AadharNumber', 'Working_Type', 'Alloted_CL', 'Priority', 'SalaryAccDeatils', 'OTP')
    list_filter = ('DepartmentCode', 'Designation', 'NatureOfEmp', 'TypeOfEmp', 'Gender', 'MartialStatus', 'BloodGroup', 'Nationality', 'Religion', 'Caste', 'Community')

@admin.register(PlacementMaster)
class PlacementMasterAdmin(admin.ModelAdmin):
    list_display = ('pcid', 'cname', 'jobrole', 'Idate', 'batch', 'pcode', 'academic_year', 'enterby', 'enter_datetime')
    search_fields = ('cname', 'jobrole', 'Idate', 'batch', 'pcode', 'academic_year', 'enterby')
    list_filter = ('cname', 'jobrole', 'Idate', 'batch', 'pcode', 'academic_year', 'enterby')

class PlacementStudentAdmin(admin.ModelAdmin):
    list_display = ('pid', 'pcid', 'regno', 'placeddate', 'academicyear', 'enterby', 'datetime')
    search_fields = ('regno', 'academicyear', 'enterby')
    list_filter = ('academicyear', 'enterby')

admin.site.register(PlacementStudent, PlacementStudentAdmin)