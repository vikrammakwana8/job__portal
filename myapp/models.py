from django.db import models

# Create your models here.
class User(models.Model):
	userchoice=(
		   ('employe','employe'),
		   ('company','company')
		)
	usertype=models.CharField(max_length=100,choices=userchoice)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100,default="")
	email=models.EmailField()
	
	password=models.CharField(max_length=100)
	

	def __str__(self):
		return self.fname+"  "+self.lname

class Company(models.Model):
	company=models.ForeignKey(User,on_delete=models.CASCADE)
	address=models.TextField(default="")
	fname=models.CharField(max_length=100,default="")
	mobile=models.CharField(max_length=100,default="")
	email=models.EmailField(default="")

	def __str__(self):
		return self.company.fname

class Employe(models.Model):
	employe=models.ForeignKey(User,on_delete=models.CASCADE)
	address=models.TextField(default="")
	fname=models.CharField(max_length=100,default="")
	mobile=models.CharField(max_length=100,default="")
	experience=models.TextField(default="")
	qualification=models.TextField(default="")
	email=models.EmailField(default="")

	def __str__(self):
		return self.employe.fname



class Job(models.Model):	
	post_name=models.CharField(max_length=100)
	post_type=models.CharField(max_length=100)
	selery=models.CharField(max_length=100)
	vacancy=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	time=models.CharField(max_length=100)	
	discription=models.TextField(default="")

	def __str__(self):
		return self.post_name


class Apply_job(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	company=models.ForeignKey(Company,on_delete=models.CASCADE)
	job=models.ForeignKey(Job,on_delete=models.CASCADE)
	post_name=models.CharField(max_length=100)
	post_type=models.CharField(max_length=100)
	selery=models.CharField(max_length=100)
	vacancy=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	time=models.CharField(max_length=100)	
	discription=models.TextField(default="")
	def __str__(self):
		return self.post_name




class Appointment(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	company=models.ForeignKey(Company,on_delete=models.CASCADE)
	job=models.ForeignKey(Job,on_delete=models.CASCADE,default="")
	date=models.CharField(max_length=100)
	time=models.CharField(max_length=100)	
	appointment_status=models.CharField(max_length=100,default="Pending")
	
	def __str__(self):
		return self.user.fname