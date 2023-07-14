from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# LOGIN VIEW
class LoginView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if 'username' not in data:
                response['message'] = 'Username not found'
                raise Exception('Username not found')

            if 'password' not in data:
                response['message'] = 'Password not found'
                raise Exception('Password not found')

            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid username or password'
                raise Exception('Invalid username or password')

        except Exception as e:
            print(e)

        return Response(response)

LoginView = LoginView.as_view()


# REGISTER VIEW
class RegisterView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if 'username' not in data:
                response['message'] = 'Username not found'
                raise Exception('Username not found')

            if 'password' not in data:
                response['message'] = 'Password not found'
                raise Exception('Password not found')

            check_user = User.objects.filter(username = data['username']).first()

            if check_user is not None:
                response['message'] = 'username already taken'
                raise Exception('username already taken')

            user_obj = User(username = data['username'])
            user_obj.set_password(data['password'])
            user_obj.save()
            
            response['message'] = 'User created successfully'
            response['status'] = 200

        except Exception as e:
            print(e)

        return Response(response)

RegisterView = RegisterView.as_view()