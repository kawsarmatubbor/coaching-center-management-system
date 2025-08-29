from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from . import models

class RegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    password_2 = serializers.CharField(
        write_only = True,
        required = True,
    )
    class Meta:
        model = models.CustomUser
        fields = [
            'id',
            'phone_number', 
            'first_name',
            'last_name',
            'fathers_name', 
            'fathers_phone_number', 
            'mothers_name', 
            'mothers_phone_number', 
            'gender',
            'date_of_birth',
            'present_address', 
            'permanent_address', 
            'school',
            's_class',
            'section',
            'roll',
            'profile_picture',
            'is_active',
            'password_1',
            'password_2'
        ]
        extra_kwargs = {
            'phone_number' : {'required' : True},
            'first_name' : {'required' : True},
            'last_name' : {'required' : True},
            'fathers_name' : {'required' : True},
            'fathers_phone_number' : {'required' : False},
            'mothers_name' : {'required' : True},
            'mothers_phone_number' : {'required' : False},
            'gender' : {'required' : False},
            'date_of_birth' : {'required' : False},
            'present_address' : {'required' : False},
            'school' : {'required' : False},
            's_class' : {'required' : False},
            'section' : {'required' : False},
            'roll' : {'required' : False},
            'is_active' : {'read_only' : True},
        }

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError("Passwords don't match.")
        return attrs

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(
            phone_number = validated_data['phone_number'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            fathers_name = validated_data['fathers_name'],
            fathers_phone_number = validated_data.get('fathers_phone_number'),
            mothers_name = validated_data['mothers_name'],
            mothers_phone_number = validated_data.get('mothers_phone_number'),
            gender = validated_data.get('gender', ''),
            date_of_birth = validated_data.get('dob', None),
            present_address = validated_data.get('present_address'),
            permanent_address = validated_data.get('permanent_address'),
            school = validated_data.get('school'),
            s_class = validated_data.get('s_class'),
            section = validated_data.get('section'),
            roll = validated_data.get('roll'),
            password = validated_data['password_1'],
            profile_picture=validated_data.get('profile_picture')
        )
        return user