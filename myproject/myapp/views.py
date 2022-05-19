from django.shortcuts import render
from .models import *


def index(request):
    stu = Student.objects.select_related()
    stu1 = Student.objects.select_related().all()
    stu2 = Student.objects.prefetch_related().all()
    stu3 = Student.objects.prefetch_related()
    print(stu, '0000000000000000')
    print(stu1, '1111111111111111')
    print(stu2, '222222222222222')
    print(stu3, '33333333333333')
    return render(request, 'index.html', {'stu': stu, 'stu1': stu1, 'stu2': stu2, 'stu3': stu3})
