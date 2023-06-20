from django.shortcuts import redirect

def auth_user(func):
    def wrap(request,*args,**kwargs):
        if 'signup' in request.session:
            return func(request,*args,**kwargs)
        else:
            return redirect('login')
    return wrap