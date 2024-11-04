from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post
def FacultyHomepage(request):
    return render(request,'facultyapp/FacultyHomepage.html')

def Blog(request):
    return render(request,'facultyapp/blog.html')
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Create a new post
        Post.objects.create(title=title, content=content)
        return redirect('view_posts')  # Redirect to the view posts page after adding

    return render(request, 'add_post.html')  # Render the form for adding a post

def view_posts(request):
    posts = Post.objects.all()  # Retrieve all posts
    return render(request, 'view_posts.html', {'posts': posts})  # Pass posts to the template


########## ADD COURSE ##############


from .forms import AddCourseForm
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/add_course.html', {'form': form})


from .models import AddCourse
from adminapp.models import studentList

def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = studentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/view_student_list.html', context)


from django.core.mail import send_mail
from django.contrib.auth.models import User
from.forms import MarksForm


def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.user
            if student_user and hasattr(student_user, 'email'):
                user_email = student_user.email
            else:
                return HttpResponse("User associated with the student is not valid or does not have an email.")
            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = 'annanyatiwary4@gmail.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'facultyapp/marks_success.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})