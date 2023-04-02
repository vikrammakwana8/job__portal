from django.shortcuts import render,redirect
from .models import User,Company,Job,Employe,Appointment

import random

from django.http import JsonResponse

# Create your views here.
def validate_email(request):
	email=request.GET.get('email')
	data={
		'is_taken':User.objects.filter(email__iexact=email).exists()
	}
	return JsonResponse(data)


def index(request):
	jobs=Job.objects.all()
	return render(request,'index.html',{'jobs':jobs})

def company_index(request):
	jobs=Job.objects.all()
	return render(request,'company-index.html',{'jobs':jobs})

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def company_about(request):
	return render(request,'company-about.html')

def job_list(request):
	return render(request,'job-list.html')

def job_detail(request):
	return render(request,'job-detail.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			print(email)
			msg="Email Already Exist"
			return render(request,'signup.html')
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					usertype=request.POST['usertype'],
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					
					password=request.POST['password'],
					)  
				msg="User Sign Up Sucessfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password aand Confirm Password does not matched"
				return render(request,'signup.html',{'msg': msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				print("hi")
				if user.usertype=='employe':
				 	request.session['email']=user.email
				 	request.session['fname']=user.fname
				 	return redirect('index')
				else:
				 	request.session['email']=user.email
				 	request.session['fname']=user.fname
				 	return redirect('company-index')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:			
		 	msg="Email not registered"
		 	return render (request,'login.html',{'msg':msg})
	else:

		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def post_job(request):
	 
	 user=User.objects.get(email=request.session['email'])
	 job=Job()
	 if request.method=="POST":
	 	        post_name=request.POST['post-name']
	 	        post_type=request.POST['post-type']
	 	        selery=request.POST['selery']
	 	        vacancy=request.POST['vacancy']
	 	        date=request.POST['date']
	 	        time=request.POST['time']
	 	        discription=request.POST['discription']

	 	        obj=Job (post_name=post_name,post_type=post_type,selery=selery,vacancy=vacancy,date=date,time=time,discription=discription)
	 	        obj.save()
	 	        
	 	        # print(post_type,selery,vacancy,date,time)
	 	        msg="Post Sucessfully"
	 	        return render(request,'post-job.html',{'msg':msg,'job':job})
	 else:
	 	return render(request,'post-job.html')

def company_profile(request):
	user=User.objects.get(email=request.session['email'])
	company=Company()
	try:
		company=Company.objects.get(company=user)
	except:
		pass
	if request.method=="POST":
		company.company=user
		ddress=request.POST['address']
		company.mobile=request.POST['mobile']
		company.email=request.POST['email']
		company.save()
		# objects=Company(company.company==user,address==address,company.mobile==mobile,company.email==email)
		# objects.save()
		msg="profile updated"
		return render(request,'company-profile.html',{'user':user,'company':company,'msg':msg})

	return render(request,'company-profile.html',{'user':user,'company':company})
	
def employe_profile(request):
	user=User.objects.get(email=request.session['email'])
	employe=Employe()
	try:
		employe=Employe.objects.get(employe=user)
	except:
		pass
	if request.method=="POST":

		employe.employe=user
		employe.address=request.POST['address']
		employe.mobile=request.POST['mobile']
		employe.email=request.POST['email']
		employe.qualification=request.POST['qualification']
		employe.experience=request.POST['experience']
		employe.save()
		msg="profile updated"
		return render(request,'employe-profile.html',{'user':user,'employe':employe,'msg':msg})

	return render(request,'employe-profile.html',{'user':user,'employe':employe})

def delete_post(request):
	pass

def apply_now(request,pk):	
	pass
	job=Job.objects.get(pk=pk)
	
	user=User.objects.get(email=request.session['email'])

	# apply_job=Apply_job.objects.get(apply_job=job)
	if request.method=="POST":
		Job.objects.create(
			post_name=request.POST['post-name']
		
		)
		msg="appointment Booked Successfully"
		return render(request,'apply.html',{'job':job,'user':user,'msg':msg})
	else:
		return render(request,'apply.html',{'job':job,'user':user})

def employe_appointment(request):
	user=User.objects.get(email=request.session['email'])
	appointments=Appointment.objects.filter(user=user)
	return render(request,'employe-appointment.html',{'appointments':appointments})

def delete_post(request):
	user=User.objects.get(email=request.session['email'])
	company=Company.objects.get(company=user)
	appointments=Appointment.objects.filter(company=company,appointment_status="Cancelled")
	return render(request,'company-index.html',{'appointments':appointments})

def forgot_password(request):
	if request.method=="POST":
		try:
			otp=random.randint(1000,9999)
			user=User.objects.get(email=request.POST['email'])
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"DwF5Auzh16qo3fXC2JMSTcOiyBEZmWH0eR8GIg4NbQrpUnKsjvhz0YwyOCGvHJEFuXRrTc7feDVaM1NA","variables_values":str(otp),"route":"otp","numbers":str(user.mobile)}
			headers = {
			    'cache-control': "no-cache"
			}
			response = requests.request("GET", url, headers=headers, params=querystring)
			msg="Please Enter OTP Sent To Your Mobile"
			return render(request,'otp.html',{'email':user.email,'otp':otp,'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new-password.html',{'email':email})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'email':email,'otp':otp,'msg':msg})

def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=email)
		user.password=np
		user.save()
		msg="Password Updated Successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="New Password & Confirm New Password Does Not Matched"
		return render(request,'new-password.html',{'email':email,'msg':msg})