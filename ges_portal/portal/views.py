from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import *

@api_view(['POST','GET'])
def users_reg(request):
    if request.method == "POST":
        data = request.data
        data["username"] = data["email"]
        if data.get("ca_code"):
            ca,created = CA.objects.get_or_create(referral_code = data.get("ca_code"))
            if data["role"]=="Student" or data["role"]=="Professional" or data["role"]=="Startup":
                if ca is not None:
                    ca.no_of_regs +=1
                    ca.save()
                else:
                    return Response("Referralcode invalid")
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user=serializer.save()
            if data.get("ca_code"):
                ca.registered_users.add(user)
                ca.save()
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("Bad Request")




@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def contingent_reg(request):
    user = request.user
    users,created = Users.objects.get_or_create(username=user.username)
    if users.role == "Contingent":
        if request.method == "POST":
            serializer = ContingentSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save(user=users)
                return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def proff_reg(request):
    user = request.user
    users,created = Users.objects.get_or_create(username=user.username)
    if users.role == "Professional":
        if request.method == "POST":
            serializer = ProfessionalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=users)
                return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def startup_reg(request):
    user = request.user
    users,created = Users.objects.get_or_create(username=user.username)
    if request.method == "POST":
        serializer = StartupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=users)
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    return Response(
        {'error': 'Method not allowed.'},
        status=status.HTTP_405_METHOD_NOT_ALLOWED
    )
    
    
    

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def student_reg(request):
    user = request.user
    users,created = Users.objects.get_or_create(username=user.username)
    if users.role == "Student":
        if request.method == "POST":
            data=request.data
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=users)
                return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
        {'error': 'Method not allowed.'},
        status=status.HTTP_405_METHOD_NOT_ALLOWED
    )
    

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def ca_reg(request):
    user = request.user
    users,created = Users.objects.get_or_create(username=user.username)
    if users.role == "CA":
        if request.method == "POST":
            data = request.data
            data['user'] = users
            serializer = CASerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=users)
                return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    user = request.user
    users,created = Users.objects.get_or_create(username=user.username)
    users_serializer = UserSerializer(users)
    if users.role == "Student":
        student,created = Student.objects.get_or_create(user=users)
        student_serializer = StudentSerializer(student)
        data ={"user_data":users_serializer.data,
               "student_data":student_serializer.data}
        return Response(data)
    elif users.role == "Startup":
        startup,created = Startup.objects.get_or_create(user=users)
        startup_serializer = StartupSerializer(startup)
        data ={"user_data":users_serializer.data,
               "startup_data":startup_serializer.data}
        return Response(data)
    elif users.role == "Professional":
        prof,created = Professional.objects.get_or_create(user=users)
        professional_serializer = ProfessionalSerializer(prof)
        data ={"user_data":users_serializer.data,
               "professional_data":professional_serializer.data}
        return Response(data)
    

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def contingent_dashboard(request):
#     user = request.user
#     users,created = Users.objects.get_or_create(username=user.username)
#     users_serializer = UserSerializer(users)
#     if users.role == "Contingent":
#         contingent,created = Contingent.objects.get_or_create(user=users)
#         contingent_serializer = ContingentSerializer(contingent)
#         data={
#             "user_data":users_serializer.data,
#             "contingent_data":contingent_serializer.data
#         }
#         return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ca_dashboard(request):
    user = request.user
    users,created = Users.objects.get_or_create(username=user.username)
    users_serializer = UserSerializer(users)
    ca = CA.objects.get(user=user)
    registered_users = ca.registered_users.all()
    registered_users= UserSerializer(registered_users, many=True).data
    ca,created = CA.objects.get_or_create(user=users)
    ca_serializer = CASerializer(ca)
    data = {
        "user_data": users_serializer.data,
        "contingent_data": ca_serializer.data,
        "registered_users":registered_users
    }
    
    return Response(data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    if request.method == "GET":
        user = request.user
        user = Users.objects.get(username = user.username)
        user = Get_UserSerializer(user)
        return Response(user.data)


