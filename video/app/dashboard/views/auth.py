from django.shortcuts import redirect, reverse
from django.views.generic import View
from app.libs.base_render import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator

class Login(View):
    TEMPLATE = 'dashboard/auth/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('dashboard_index'))

        data = {'error': ''}
        return render_to_response(request, Login.TEMPLATE, data=data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = {}
        exists = User.objects.filter(username=username).exists()

        if not exists:
            data['error'] = '不存在该用户'
            return render_to_response(request, Login.TEMPLATE, data)
        user = authenticate(username=username, password=password)

        if not user:
            data['error'] = '用户名或密码错误'
            return render_to_response(request, Login.TEMPLATE, data)

        if not user.is_superuser:
            data['error'] = '你无权登录'
            return render_to_response(request, Login.TEMPLATE, data)

        login(request, user)
        return redirect(reverse('dashboard_index'))


class AdminManager(View):
    TEMPLATE = 'dashboard/auth/admin.html'

    def get(self, request):
        users = User.objects.all()
        page = request.GET.get('page', 1)
        p = Paginator(users, 1)

        total_page = p.num_pages
        if int(page) <= 1:
            page = 1
        current_page = p.get_page(int(page)).object_list


        data = {'users': current_page, 'total': total_page, 'page_num': int(page)}
        return render_to_response(request, AdminManager.TEMPLATE, data=data)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('dashboard_login'))

class UpdateAdminStatus(View):
    def get(self, request):
        status = request.GET.get('status', 'on')

        _status = True if status == 'on' else False
        request.user.is_superuser = _status
        request.user.save()

        return redirect(reverse('admin_manager'))