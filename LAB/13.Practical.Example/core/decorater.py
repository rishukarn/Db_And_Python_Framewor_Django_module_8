from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden

def login_and_role_required(req_role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(req,*args,**kwargs):
            user=req.user
            if req_role == 'customer' and not user.is_customer:
                return HttpResponseForbidden('you or not authized to access this page')
            if req_role == 'seller' and not user.is_seller:
                return HttpResponseForbidden('you or not authized to access this page')
            return view_func(req,*args,**kwargs)
        return _wrapped_view
    return decorator