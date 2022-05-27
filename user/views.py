from django.shortcuts import render, redirect   # render: html파일 화면에 보여준다
from .models import UserModel
from django.http import HttpResponse    # 화면에 글자 띄워주기


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/index.html')
    elif request.method == 'POST':
        # html에서 name='username' 이름으로된 데이터를 가져온다. 없다면 빈칸처리
        email = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)

        if password != password2:
            return HttpResponse('로그인성공!')
        else:
            new_user = UserModel()
            new_user.email = email
            new_user.password = password
            new_user.save()

        return HttpResponse('로그인성공!')

