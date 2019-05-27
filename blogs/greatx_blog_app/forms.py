# from django import forms


# class Registration(forms.Form):
#     firstname = forms.CharField(widget=TextInput,lable='First Name:')
#     lastname = forms.CharField(max_length=100,lable='Last Name:')
#     conactno = forms.IntegerField(widget=NumberInput,lable='Contact_No:')
#     username = forms.CharField(widget=TextInput,lable='User Name:')
#     email = forms.CharField(widget=EmailInput,lable=Email_ID)
#     password = forms.CharField(widget=PasswordInput,lable=Password)


# class BlogDetails(forms.Form):
#     authorname = forms.CharField(widget=TextInput,lable='Author Name:')
#     title = forms.CharField(widget=TextInput,lable='Title')
#     description = forms.CharField(widget=TextInput,lable='Description')
#     image = forms.ImageField()
#     created_date = forms.DateTimeField(lable=Created_Date)
#     years=range()
#     modified_date = forms.DateTimeField(widget=SelectDtaeWidget(years=years),lable='Modified_date')
#     published_date = forms.DateTimeField(widget=SelectDtaeWidget(years=years),lable='Published_date')