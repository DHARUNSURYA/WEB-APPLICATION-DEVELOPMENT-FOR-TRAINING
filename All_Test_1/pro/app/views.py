from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.core import serializers

from .models import *
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, reverse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib import messages
import io
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import csv
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PlacementMaster


def login(request):
    if request.method == 'POST':
        userid = request.POST.get('regno')
        passd = request.POST.get('password')
        
        # Check if the user is a student
        student_adno = SISStudentInfo.objects.filter(RegNo=userid, Password=passd).values_list('Adno', flat=True).first()
        if student_adno:
            return redirect('student_profile', regno=student_adno)
        
        # Check if the user is an employee
        employee = HRMPersonnelInfo.objects.filter(EmpId=userid, Password=passd).first()
        if employee:
            position = HRMADPositionHeld.objects.filter(EmpId=userid).first()
            if position:
                if 'hod' in position.PositionHeld.lower():
                    role = 'hod'
                elif 'cuii' in position.PositionHeld.lower():
                    role='cuii' 
                else:
                    role = 'staff'
                
                return redirect('employee_profile', empid=employee.EmpId, role=role)
            else:
                role = 'staff'
                return redirect('employee_profile', empid=employee.EmpId, role=role)
        
        # Add an error message for invalid credentials
        # messages.error(request, 'Invalid user ID or password. Please try again.')
    
    # Return login page for GET requests and unsuccessful login attempts
    return render(request, 'login.html')

    

def student_profile(request, regno):

    academic_year_courses = defaultdict(list)
    unique_courses = AdminCourse.objects.values( 'DeptName', 'CourseCode','DegreeShortForm').distinct()
    
   
    program = ''  # Initialize program variable
    academic_year_courses = defaultdict(dict)
    for course in unique_courses:
        academic_year_courses[course['CourseCode']] = {
            'DeptName': course['DeptName'],
            'DegreeShortForm': course['DegreeShortForm']
        }
 
    try:
        student = SISStudentInfo.objects.get(Adno=regno)
    except SISStudentInfo.DoesNotExist:
        return HttpResponseNotFound("Student not found")
    dcode=student.DCode
    course_info = academic_year_courses.get(dcode)
    if course_info:
        program = f"{course_info['DeptName']} {course_info['DegreeShortForm']}"
    print(program)    
    return render(request, 'student.html', {'student':student,'program':program})

def employee_profile(request, empid, role):
    try:
        employee = HRMPersonnelInfo.objects.get(EmpId=empid)
    except HRMPersonnelInfo.DoesNotExist:
        return HttpResponseNotFound("Employee not found")
    print(role)
    
    return render(request, 'profile.html', {'employee':employee,'role':role})

def updata_student(request, adno):
    if request.method == 'POST':
        regno = request.POST.get('regno')
        aquer_skill = request.POST.get('aquer_skills')
        required_skill = request.POST.get('required_skills')
        tenth = request.POST.get('tenth')
        focus = request.POST.get('focus')
        
        # Create or update the student's information
        UpdateStudent.objects.create(regno=regno, aqure_skill=aquer_skill, required_skill=required_skill, tenth=tenth, focus=focus)
        messages.success(request, 'Profile updated successfully.')
        
        # Redirect to the student profile page
        return redirect(reverse('student_profile', kwargs={'regno': adno}))
    else:
        unique_courses = AdminCourse.objects.values( 'DeptName', 'CourseCode','DegreeShortForm').distinct()
        program = ''  
        academic_year_courses = defaultdict(dict)
        for course in unique_courses:
            academic_year_courses[course['CourseCode']] = {
            'DeptName': course['DeptName'],
            'DegreeShortForm': course['DegreeShortForm']
        }

        try:
            student = SISStudentInfo.objects.get(Adno=adno)
            student_docde=student.DCode
            course_info = academic_year_courses.get(student_docde)
            if course_info:
                program = f"{course_info['DeptName']} {course_info['DegreeShortForm']}"

            return render(request, 'update.html', {'student': student,'program':program})
        except SISStudentInfo.DoesNotExist:
            return render(request, 'error.html', {'message': 'Student not found'})
        
        
from collections import defaultdict

def mentor_allocate(request, empid, role):
    cc=AdminCourse.objects.values_list('DeptName','CourseCode','DegreeShortForm','TyprOfPgm').distinct()
    staff_list = HRMPersonnelInfo.objects.values_list('EmpId', 'EmpName')
    batch=SISStudentInfo.objects.filter(CourseCompletion=0).values_list('Batch', flat=True).distinct()  
    EmpId=empid
    employee={
        'EmpId':empid
    }
    return render(request, 'mentor_allocate.html', {'courses': cc, 'batch':batch,'staff_list': staff_list, 'enterby': empid, 'role': role,'empid':EmpId,'employee':employee})

def get_regno(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        pcode = request.POST.get('pcode')
        print(pcode)
        batch = request.POST.get('batch')
        section = request.POST.get('section')
        
        # Query the SISStudentInfo table to get the corresponding regno based on the selected values
        regno_list = SISStudentInfo.objects.filter(DCode=pcode, Batch=batch, Section=section).values_list('RegNo', flat=True)
        name_list = SISStudentInfo.objects.filter(DCode=pcode, Batch=batch, Section=section).values_list('StudentName', flat=True)
        
        # Convert QuerySet to list
        regno_list = list(regno_list)
        name_list = list(name_list)
        print(regno_list)
        return JsonResponse({'regno_list': regno_list, 'name_list': name_list})
    
    return JsonResponse({}, status=400)

def redirect_to_employee_profile(enter, role):
    return HttpResponseRedirect(reverse('employee_profile', kwargs={'empid': enter, 'role': role}))

def save_ment_data(request):
    if request.method == 'POST':
        selected_regnos_str = request.POST.get('appendreg')
        print('-----------------',selected_regnos_str)
        selected_regnos = selected_regnos_str.split(',')
        streg = request.POST.get('streg')
        enter = request.POST.get('enterby')
        batch = request.POST.get('batch')
        role = request.POST.get('e')

        try:
            # Retrieve staff member based on EmpId
            staff_member = HRMPersonnelInfo.objects.get(EmpId=streg)
        except HRMPersonnelInfo.DoesNotExist:
            return JsonResponse({'message': 'Staff member not found'}, status=400)

        # Save mentor data for each selected regno
        for regno in selected_regnos:
            ment_obj = IPTMentors(regno=regno, empid=streg, academicyear=batch, enterby=enter)
            ment_obj.save()

        # Redirect to employee_profile with parameters
        return redirect('employee_profile', empid=enter, role=role)

    # Handle other cases, like GET requests
    return JsonResponse({}, status=400)



def ipt_companies_view(request, empid, role):
    if request.method == 'POST':
        print(empid)
        company_name = request.POST.get('companyName')
        batch = request.POST.get('b')
        academic_year = request.POST.get('a')
        department = request.POST.get('department')
        pname=request.POST.get('ContactName')
        cemail=request.POST.get('E-MailId')
        des=request.POST.get('Designation')
        pno=request.POST.get('phon')
        current_st_reg = empid  # Assigning the regno parameter to current_st_reg
        # Create a new record in IPT_master
        ipt_master_instance = IPTMaster.objects.create(
            cname=company_name,
            pcode=department,  # You need to define how you get this value
            batch=batch,
            academic_year=academic_year,
            pname=pname,
            pdes=des,
            phone=pno,
            pemail=cemail,
            enterby=current_st_reg  # Assuming enterby is related to the current user
        )

        # Redirect to the appropriate page after successful submission
        # Assuming 'employee_profile' is the name of the template
        return redirect('employee_profile', empid=empid, role=role)
    else:
        
        
        cc=AdminCourse.objects.values_list('DeptName','CourseCode','DegreeShortForm','TyprOfPgm').distinct()
        batch=SISStudentInfo.objects.filter(CourseCompletion=0).values_list('Batch', flat=True).distinct()  

        employee={
        'EmpId':empid,
        'role':role
         }
        print(employee)
        role=role
        # Handle GET request
    return render(request, 'ipt_company.html', {'employee': employee, 'role': role,'courses': cc,'batch':batch})
 


from django.db.models import F
#20-21 mca,
def iptstatus(request, empid, role):
    # academic_year_courses = defaultdict(list)

    unique_courses = AdminCourse.objects.values( 'DeptName', 'CourseCode','DegreeShortForm').distinct()
    print(unique_courses)
    academic_year_courses = defaultdict(dict)

    # Populate the dictionary with the desired format
    for course in unique_courses:
        dept_name = course['DeptName']
        course_code = course['CourseCode']
        DegreeShortForm=course['DegreeShortForm']
        dept_degree = dept_name + DegreeShortForm
        academic_year_courses[course_code] = {'cname':dept_degree}

        # academic_year_courses[None].append({course_code: dept_degree})
    
    # # Sort the dictionary based on academic years
    # academic_year_courses = dict(sorted(academic_year_courses.items()))
    # course_c=academic_year_courses.get(course_code,[])
    # print(course_c)
    # print(academic_year_courses)
    # Extract the courses for the academic year '2021-2022'
    courses_2021_2022 = academic_year_courses.get('2021-2022', [])
    # print(courses_2021_2022)

    if role == 'hod':
        try:
            employee={
                    'EmpId':empid,
                    'role':role
                    }
            hrm_personnel = HRMPersonnelInfo.objects.get(EmpId=empid)
            department_code = hrm_personnel.DepartmentCode
            print(department_code)
            # Get department names and their corresponding department codes from AdminCourse objects
            departments = AdminCourse.objects.values_list('BelongstoDept', 'CourseCode')
            print(len(departments))
            # Convert the values to a dictionary where department names are keys and department codes are values
# Convert the values to a dictionary where department names are keys and department codes are values
            department_dict = {f"{dept_name}_{idx}": course_code for idx, (dept_name, course_code) in enumerate(departments)}
            
            print(department_dict)
            print(len(department_dict))
            # Initialize an empty list to store filtered departments
# Initialize an empty list to store filtered course codes
            filtered_departments = []

            # Iterate through the department dictionary to find matching departments
            for dept_name, course_code in department_dict.items():
                if department_code in dept_name:
                    filtered_departments.append(course_code)            
            print(filtered_departments)

            # Check if any departments match the department code
            if not filtered_departments:
                return JsonResponse({'error': 'Department code does not match any department name'})
            
            # Get RegNos of students enrolled in the courses
            sis_students = SISStudentInfo.objects.filter(DCode__in=filtered_departments)
            regnos = [student.RegNo for student in sis_students]
            
            # Get IPT students based on RegNos and status=1
            ipt_students = IPTStudent.objects.filter( status=1, regno__in=regnos)
            
            # Get IPT masters for the students
            ipt_status_data = []
            for student in ipt_students:
                ipt_master = IPTMaster.objects.get(pk=student.iptcid_id)
                sis_student = SISStudentInfo.objects.get(RegNo=student.regno)
                dname = sis_student.DCode
                dname_str = str(dname)  # Convert to string
                cname = academic_year_courses.get(dname_str, {}).get('cname')
                ipt_status_data.append({
                    'student': student,
                    'ipt_master': ipt_master,
                    'sis_student': sis_student,
                    'cname': cname
                })
                print('-------------')
                print(cname)

                
                employee={
                    'EmpId':empid,
                    'role':role
                    }
                role=role
                
            return render(request, 'ipt_status.html', {'ipt_status_data': ipt_status_data,'employee':employee,'role':role})
        except HRMPersonnelInfo.DoesNotExist:
            return JsonResponse({'error': 'HRM Personnel not found'})
    elif role == 'staff':
        employee = {'EmpId': empid,
                    'role':role}

        try:
            ipt_mentors = IPTMentors.objects.filter(empid=empid)
            print(ipt_mentors)
            ipt_status_data = []
            for mentor in ipt_mentors:
                ipt_students = IPTStudent.objects.filter(regno=mentor.regno, status=0)
                print(ipt_students)    
                for student in ipt_students:
                    ipt_master = IPTMaster.objects.get(pk=student.iptcid_id)
                    print(ipt_master)
                    sis_student = SISStudentInfo.objects.get(RegNo=student.regno)
                    print(sis_student.StudentName)
                    dname = sis_student.DCode
                    dname_str = str(dname)  # Convert to string
                    cname = academic_year_courses.get(dname_str, {}).get('cname')
                    ipt_status_data.append({
                        'student': student,
                        'ipt_master': ipt_master,
                        'sis_student': sis_student,
                        'cname': cname
                    })
                    print('---------------------')
                    print(cname)
                    
            
                    role=role
            return render(request, 'ipt_status.html', {'ipt_status_data': ipt_status_data,'employee':employee,'role':role})
        except IPTMentors.DoesNotExist:
            return JsonResponse({'error': 'Mentor not found'})
    if role == 'cuii':
        try:
            ipt_status_data = []
            employee = {'EmpId': empid, 'role': role}  # Define employee variable outside the loop

            ipt_students = IPTStudent.objects.filter(status=2)
            for student in ipt_students:
                try:
                    ipt_master = IPTMaster.objects.get(pk=student.iptcid_id)
                    sis_student = SISStudentInfo.objects.get(RegNo=student.regno)
                    dname = sis_student.DCode
                    dname_str = str(dname)  # Convert to string
                    cname = academic_year_courses.get(dname_str, {}).get('cname')
                    ipt_status_data.append({
                        'student': student,
                        'ipt_master': ipt_master,
                        'sis_student': sis_student,
                        'cname': cname
                    })
                except SISStudentInfo.DoesNotExist:
                    # Handle the case where SISStudentInfo does not exist for this student
                    print(f"SISStudentInfo does not exist for RegNo: {student.regno}")
                    continue  # Skip to the next iteration of the loop
                except Exception as e:
                    # Handle any other unexpected exceptions
                    print(f"An unexpected error occurred: {e}")
                    continue  # Skip to the next iteration of the loop

            return render(request, 'ipt_status.html', {'ipt_status_data': ipt_status_data, 'employee': employee, 'role': role})
        except IPTMentors.DoesNotExist:
            return JsonResponse({'error': 'Mentor not found'})
    else:
        return JsonResponse({'error': 'Invalid role'})




def generate_pdf(ipt_student):
    # Retrieve the corresponding SISStudentInfo object
    sis_student = SISStudentInfo.objects.get(RegNo=ipt_student.regno)
    print(sis_student.DCode)
    
    unique_courses = AdminCourse.objects.values( 'DeptName', 'CourseCode','DegreeShortForm').distinct()
    program = ''  
    academic_year_courses = defaultdict(dict)
    for course in unique_courses:
        academic_year_courses[course['CourseCode']] = {
            'DeptName': course['DeptName'],
            'DegreeShortForm': course['DegreeShortForm']
        }
    # Retrieve mentor details
    dcode=sis_student.DCode
    course_info = academic_year_courses.get(dcode)
    if course_info:
        program = f"{course_info['DeptName']} {course_info['DegreeShortForm']}"
    print(program)    
    
    
    mentor = IPTMentors.objects.filter(regno=sis_student.RegNo).first()
    print(mentor)
    if mentor:
        name = HRMPersonnelInfo.objects.get(EmpId=mentor.empid)
        
        mentor_name=name.EmpName
        print(mentor_name)
    else:
        mentor_name = "hiiiii"
        
    ipt_master = IPTMaster.objects.get(pk=ipt_student.iptcid_id)
    print(ipt_master.cname)
    academic_year_courses1 = defaultdict(dict)

    unique_courses1 = AdminCourse.objects.values( 'CourseCode','BelongstoDept').distinct()
    for cours in unique_courses1:
        academic_year_courses1[cours['CourseCode']] = {
            'Belongstodept': cours['BelongstoDept']
        }
    hod_name=''
    ccode=sis_student.DCode
    hod_dep = academic_year_courses1.get(ccode)
    if hod_dep:
        hod_dep = f"{hod_dep['Belongstodept']}"
    print('hod dep',hod_dep)    
    if hod_dep:
            Belongstodept=HRMADPositionHeld.objects.get(Belongstodept=hod_dep)
            hod_empid=Belongstodept.EmpId
    print('hod empid',hod_empid)        
    if hod_empid:
        hod_obj=HRMPersonnelInfo.objects.get(EmpId=hod_empid)
        hod_name=hod_obj.EmpName
    print(hod_name) 
    
    # Render HTML template with IPT student, SIS student, and mentor data
    html = render_to_string('ipt_student_template.html', {'ipt_student': ipt_student, 'sis_student': sis_student, 'mentor_name': mentor_name,'ipt_master':ipt_master,'program':program,'hod_name':hod_name})

    # Create a PDF document
    pdf_data = io.BytesIO()
    pisa.CreatePDF(html, dest=pdf_data)

    return pdf_data.getvalue()


from django.shortcuts import get_object_or_404, HttpResponse

def download_pdf(request, ipdid):
    # Retrieve the IPT student object
    ipt_student = get_object_or_404(IPTStudent, pk=ipdid)

    # Generate the PDF data using a utility function
    pdf_data = generate_pdf(ipt_student)

    # Create an HTTP response with PDF content type
    response = HttpResponse(content_type='application/pdf')

    # Set the content disposition to force download
    response['Content-Disposition'] = f'attachment; filename="ipt_student_{ipt_student.regno}.pdf"'

    # Write the PDF data to the response
    response.write(pdf_data)

    return response


    
def approve_student(request, ipdid):
    # Retrieve the IPT student object
    ipt_student = IPTStudent.objects.get(pk=ipdid)
    


    # If status is 2, download the PDF
    if ipt_student.status == 2:
        ipt_student.status = 3
        ipt_student.save()

        # Generate the PDF data
        pdf_data = generate_pdf(ipt_student)

        # Create the HTTP response with PDF content
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="ipt_student_{ipt_student.regno}.pdf"'
        
        response.write(pdf_data)

        return response
        # Check the current status and update accordingly
    if ipt_student.status == 0:
        ipt_student.status = 1
    elif ipt_student.status == 1:
        ipt_student.status = 2
    elif ipt_student.status == 2:
        ipt_student.status = 3
    else:
        # Handle any other status cases if needed
        pass

    # Save the updated status
    ipt_student.save()

    # If status is not 2, redirect back to the previous page
    previous_url = request.META.get('HTTP_REFERER')
    return redirect(previous_url)

def logout(request):
    # Clear session data
    request.session.flush()
    # Redirect to the login page
    return redirect('login')



def placenment(request,empid,role):
    employee = {'EmpId': empid,
                    'role':role}
    cc=AdminCourse.objects.values_list('DeptName','CourseCode','DegreeShortForm','TyprOfPgm').distinct()
    batch=SISStudentInfo.objects.filter(CourseCompletion=0).values_list('Batch', flat=True).distinct()  

   
    return render(request, 'placenment.html', {  'enterby': empid, 'role': role,'empid':empid,'employee':employee,'courses': cc,'batch':batch})




def save_data_placenment(request,empid,role):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        jobrole = request.POST.get('jobrole')
        jobdescription = request.POST.get('jobd')  # Assuming this corresponds to 'jobdescription' in your model
        ten = request.POST.get('ten')
        twelve = request.POST.get('twelth')  # Corrected field name from 'twelve' to 'twelth'
        cgpa = request.POST.get('CGPA')  # Corrected field name from 'cgpa' to 'CGPA'
        idate = request.POST.get('idate')
        venue = request.POST.get('venu')  # Corrected field name from 'venue' to 'venu'
        link = request.POST.get('link')
        batch = request.POST.get('batch')
        pcode = request.POST.get('dep')  # Assuming 'dep' corresponds to 'pcode' in your model
        academic_year = request.POST.get('academic_year')
        enterby = empid  # Assuming this corresponds to 'enterby' in your model
        # Assuming that 'enter_datetime' should automatically get the current date and time
        enter_datetime = timezone.now()

        # Create a new PlacementMaster instance with the provided data
        PlacementMaster.objects.create(
            cname=cname,
            jobrole=jobrole,
            jobdescription=jobdescription,
            ten=ten,
            twelve=twelve,
            cgpa=cgpa,
            Idate=idate,
            venue=venue,
            link=link,
            batch=batch,
            pcode=pcode,
            academic_year=academic_year,
            enterby=enterby,
            enter_datetime=enter_datetime
        )
        
        # Redirect to a success page after successful submission
        return redirect('employee_profile', empid=empid, role=role)
    
    # If the request method is not POST, render the form page again
    return render(request, 'placenment.html')

def placenment_data(request, empid, role):
    cc = AdminCourse.objects.values_list('DeptName', 'CourseCode', 'DegreeShortForm', 'TyprOfPgm').distinct()
    staff_list = HRMPersonnelInfo.objects.values_list('EmpId', 'EmpName')
    batch = SISStudentInfo.objects.filter(CourseCompletion=0).values_list('Batch', flat=True).distinct()
    companies = PlacementMaster.objects.values_list('pcid', 'cname')
    EmpId = empid
    employee = {
        'EmpId': empid
    }
    return render(request, 'placenment_sstudent.html', {'courses': cc, 'batch': batch, 'staff_list': staff_list,
                                                       'enterby': empid, 'role': role, 'empid': EmpId,
                                                       'employee': employee, 'companies': companies})

# def get_regno_placnenment(request):
#     if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#         pcode = request.POST.get('pcode')
#         print(pcode)
#         batch = request.POST.get('batch')
#         section = request.POST.get('section')
        
#         # Query the SISStudentInfo table to get the corresponding regno based on the selected values
#         regno_list = SISStudentInfo.objects.filter(DCode=pcode, Batch=batch, Section=section).values_list('RegNo', flat=True)
#         name_list = SISStudentInfo.objects.filter(DCode=pcode, Batch=batch, Section=section).values_list('StudentName', flat=True)
        
#         # Convert QuerySet to list
#         regno_list = list(regno_list)
#         name_list = list(name_list)
#         print(regno_list)
#         return JsonResponse({'regno_list': regno_list, 'name_list': name_list})
    
#     return JsonResponse({}, status=400)
from django.db.models import Q

import json
from django.core.serializers import serialize

def get_regno_placnenment(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        pcode = request.POST.get('pcode')
        batch = request.POST.get('batch')
        section = request.POST.get('section')
        a = request.POST.get('a')  # Assuming 'a' is the date you want to compare with Idate
        print('data', pcode, section, batch)
        print(type(pcode))
        
        # Filter SISStudentInfo objects based on the provided criteria
        student_info_queryset = SISStudentInfo.objects.filter(DCode=pcode, Batch=batch, Section=section)
        
        # Serialize QuerySet to JSON
        student_info_json = serialize('json', student_info_queryset)
        
        # Extract regno and name from parsed data
        regno_list = list(student_info_queryset.values_list('RegNo', flat=True))
        name_list = list(student_info_queryset.values_list('StudentName', flat=True))
        print('namelist/regnolist', name_list, regno_list)
        
        # Filter PlacementMaster objects based on the provided date ('a') and other criteria
        companies = PlacementMaster.objects.filter(Q(Idate=a) & Q(pcode=pcode)).values_list('pcid', 'cname')
        
        return JsonResponse({'companies': list(companies), 'regno_list': regno_list, 'name_list': name_list})
    
    return JsonResponse({}, status=400)


@csrf_exempt
def fetch_companies(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        selected_date = request.POST.get('selectedDate')
        # Filter PlacementMaster objects based on the interview date
        companies = PlacementMaster.objects.filter(Idate=selected_date).all()
        # Extract company names and PCodes from the filtered objects
        print(companies)
        company_data = [{'id': company.pcid, 'name': company.cname} for company in companies]
        print('hi',company_data)
        return JsonResponse({'companies': company_data})
    else:
        return JsonResponse({'error': 'Invalid request method or not an AJAX request'})
    
def fetch_pcode(request):
    selected_company_name = request.POST.get('selectedCompany')
    print('Selected company:', selected_company_name)
    unique_courses = AdminCourse.objects.values('DeptName', 'CourseCode', 'DegreeShortForm').distinct()
    program=''
    # Fetching unique courses
    academic_year_courses = defaultdict(dict)
    for course in unique_courses:
        academic_year_courses[course['CourseCode']] = {
            'DeptName': course['DeptName'],
            'DegreeShortForm': course['DegreeShortForm']
        }   
    # Check if selected_company_name is provided
    if not selected_company_name:
        return JsonResponse({'error': 'No company name provided'}, status=400)

    try:
        # Fetch placement master object based on selected company name
        placement_master = PlacementMaster.objects.get(pcid=selected_company_name)
        print('lllllllllll',placement_master)
        p_codes = [int(code.strip()) for code in placement_master.pcode.split(',')]
        pcodes_programs = []
        print('ooooooooooooo',p_codes)
        print(type(p_codes))
        # Retrieve program information for each PCode
        for code in p_codes:
            code=str(code)
            course_info = academic_year_courses.get(code)
            if course_info:
                program = f"{course_info['DeptName']} {course_info['DegreeShortForm']}"
                print('pro',program)
            pcodes_programs.append({'pcode': code, 'program': program})            
        print(pcodes_programs)        
        return JsonResponse({'pcodes': pcodes_programs})

    except PlacementMaster.DoesNotExist:
        return JsonResponse({'error': 'PlacementMaster object not found for selected company name'}, status=404)

    except ValueError as ve:
        return JsonResponse({'error': 'Invalid value: {}'.format(ve)}, status=400)

    except Exception as e:
        return JsonResponse({'error ': str(e)}, status=500)



def save_placenment_data(request):
    if request.method == 'POST':
        selected_regnos_str = request.POST.get('selectregno')
        selected_regnos = selected_regnos_str.split(',')  # Split the string into a list of individual regnos
        pdate=request.POST.get('pdate')
        company_id = request.POST.get('company')
        enterby = request.POST.get('enterby')
        academic_year = request.POST.get('ac')
        role = request.POST.get('e')
        
        print(selected_regnos,company_id,enterby,role)
        # Save placement data for each selected regno

        try:
            placement_master = PlacementMaster.objects.get(pk=company_id)
        except PlacementMaster.DoesNotExist:
            # Handle the case when the PlacementMaster instance does not exist
            return JsonResponse({'error': 'PlacementMaster with the specified ID does not exist'}, status=400)

        for regno in selected_regnos:
            placement_obj = PlacementStudent(pcid=placement_master, regno=regno,placeddate=pdate,academicyear=academic_year, enterby=enterby)
            placement_obj.save()

        # Redirect to employee profile with parameters
        return redirect('employee_profile', empid=enterby, role=role)

    # Handle other cases, like GET requests
    return JsonResponse({}, status=400)

def viewsf(request, empid, role):
    employee = {'EmpId': empid, 'role': role}  
    placement_companies = PlacementMaster.objects.all()
    print(placement_companies)
    
    
    return render(request, 'files.html', {'employee': employee, 'role': role, 'placement_companies': placement_companies})


def download_csv(request):
    # Retrieve IPT students with status = 3
    ipt_students = IPTStudent.objects.filter(status=3)
    
    # Retrieve unique courses
    unique_courses = AdminCourse.objects.values('DeptName', 'CourseCode', 'DegreeShortForm').distinct()
    
    # Create a dictionary to store course information by DCode
    academic_year_courses = defaultdict(dict)
    for course in unique_courses:
        academic_year_courses[course['CourseCode']] = {
            'DeptName': course['DeptName'],
            'DegreeShortForm': course['DegreeShortForm']
        }
    
    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ipt_students_and_course_info.csv"'
    
    # Write data to CSV
    writer = csv.writer(response)
    writer.writerow(['Reg No','Name','Program','Section','Batch', 'Company Name','From Date','To Date','No Of Days'])  # CSV header

    # Write IPT student data to CSV
    for student in ipt_students:
        # Access related IPTMaster object through iptcid
        ipt_master = student.iptcid
        # Retrieve the program name
        program = ''
        if ipt_master:
            # Access the Dcode from SISStudentInfo
            sis_student_info = SISStudentInfo.objects.filter(RegNo=student.regno).first()
            if sis_student_info:
                # Check if DCode exists in unique courses
                dcode = sis_student_info.DCode
                course_info = academic_year_courses.get(dcode)
                if course_info:
                    program = f"{course_info['DeptName']} {course_info['DegreeShortForm']}"
                    
        writer.writerow([
            student.regno,
            sis_student_info.StudentName,
            program,
            sis_student_info.Section,
            sis_student_info.Batch,
            ipt_master.cname,
            student.from_date,
            student.to_date,
            student.noofdays
            ])

    return response



def placenement_csv(request, pcid):
    mas=PlacementMaster.objects.filter(pcid=pcid).first()
    unique_courses = AdminCourse.objects.values('DeptName', 'CourseCode', 'DegreeShortForm').distinct()
    
    # Create a dictionary to store course information by DCode
    academic_year_courses = defaultdict(dict)
    for course in unique_courses:
        academic_year_courses[course['CourseCode']] = {
            'DeptName': course['DeptName'],
            'DegreeShortForm': course['DegreeShortForm']
        }
    placed_students = PlacementStudent.objects.filter(pcid=pcid)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="placement_students_{pcid}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Reg. No', 'Name','Section','Program','Placed Date', 'Academic Year','Company Name'])

    for student in placed_students:
        stinfo=SISStudentInfo.objects.filter(RegNo=student.regno).first()
        if stinfo:
                # Check if DCode exists in unique courses
                dcode = stinfo.DCode
                course_info = academic_year_courses.get(dcode)
                if course_info:
                    program = f"{course_info['DeptName']} {course_info['DegreeShortForm']}"
                    

        writer.writerow([student.regno, stinfo.StudentName,stinfo.Section,program,student.placeddate, student.academicyear,mas.cname])

    return response

    