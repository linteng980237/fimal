from django.core.paginator import Page
from django.shortcuts import render, redirect



from django.contrib import messages


from final.settings import LOGIN_URL



def main(request):
    '''
    Render the main Page
    '''
    return render(request, 'main/main.html')

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

def reason(request):
    '''
    Render the reason page
    '''
    return render(request, 'main/reason.html')

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect('account:login')
        return func(request, *args, **kwargs)
    return auth
