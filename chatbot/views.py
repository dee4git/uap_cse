from django.http import JsonResponse

def get_response(request):
    user_message = request.GET.get('message', '').lower()

    responses = {
        "hi": "Hello! Welcome to the University Help Desk. How can I assist you today?",
        "admission portal": """<b>General Timing and Procedure : </b><br>
        <b>•Spring Semester</b> (in general): July to December<br>
        <b>•Fall Semester</b> (in general): January to June""",
        "admission info":"Undergraduate or Graduate?",
        "undergraduate": """<b>B.Sc. Engg. in CSE</b><br><br>
<b>Minimum GPA Requirements</b><br>
Total GPA in SSC & HSC = 7.50<br>
Total GPA in O & A level = 7.50<br>
(Candidates with minimum GPA of 2.5 in five subjects in O level and two subjects in A level).<br><br>
<b>Subject Requirements</b><br>
Students must have Physics, Mathematics in HSC (or equivalent) and Chemistry either in SSC or HSC (or equivalent).""",
        "graduate": """<b>M.Sc. in CSE</b><br><br>
<b>SSC, HSC & Graduation Requirements</b><br>
One 1st class / 1st Division<br>
50% Marks or CGPA 2.50 out of 4.00 in B.Sc Engineering<br>
Must not have 3rd Division / class in any public examination<br><br>
<b>Admission Test / Viva Voce</b><br>
Admission with the approval of the Head of Dept.""",

        "tuition fees": "Total Fee (8 Semester + Admission fee) = ৳ 8,13,200",
        "tuition fees ": "Total Fee (4 Semester + Admission fee) = ৳ 1,87,000",
        "administration": "",
        "about university": """A government approved private university established by the University of Asia Pacific Foundation (UAPF). University of Asia Pacific (UAP) was established in 1996 as a private university under the..<a href="https://uap-bd.edu/uap-profile.php" target="_blank">Read more</a>""",
        "more": "",
        "contact": "Contact address!",
        "uap administration": "<br>74/A , Green Road, Dhaka - 1205, Bangladesh</br><br> PABX:+8802-58157091-4, +8802-58157096</br><br> Ext: 107, 114 FAX:+8802-58157097</br><br> Email: registrar@uap-bd.edu, uapadmin@uap-bd.edu</br>",
        "admission office": "<br>Telephone: +8802-48114140 PABX: +8802-58157091-4, +8802-58157096 (Ext - 210, 211, 212, 213, 215)</br><br> FAX:+8802-58157097</br><br> Cell: +8801731681081, +8801768544208. +8801714088321 +8801789050383</br><br> Email: admission@uap-bd.edu</br>",
        "dept. cse": "<br>PABX:+8802-58157091-4, +8802-58157096 (Ext-777)</br><br> FAX:+8802-58157097</br><br> Email: headcse@uap-bd.edu</br>",
        "official website": """Visit our Official Website: <a href="https://uap-bd.edu/index.php" target="_blank">Click Here</a>""",
    }

    reply = responses.get(user_message, """Sorry, I didn't understand that.Visit our Official Website: <a href="https://uap-bd.edu/index.php" target="_blank">Click Here</a>""")
    return JsonResponse({"response": reply})
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
