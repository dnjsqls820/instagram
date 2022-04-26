from json.decoder import JSONDecodeError
from django.shortcuts import render
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Account
from django.contrib.auth.models import User
# Create your views here.
@csrf_exempt

def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            user_instance = signup_form.save(commit=False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            return render(request, 'accounts/signup_complete.html', {'username':user_instance.username})

    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':signup_form.as_p})
        # todo : 입력 받은 내용을 이용해서 회원 객체 생성
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        #password2 = request.POST.get('password2')
        #print(username, password, password2)
        #회원 객체 생성하기
        #user = User()
        #user.username = username
        #user.set_password(password)
        #user.save()
        #return render(request, 'accounts/signup_complete.html')
    #else:
        # todo :  from 객체를 만들어서 전달.
        #context_values = {'form' : 'this is form'}
        #return render(request, 'accounts/signup.html', context_values)
