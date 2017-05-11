from django.db import models

class LeapClass(models.Model):
	classCode = models.CharField(max_length=4, unique=True, verbose_name='Class Code')
	className = models.CharField(max_length=100, verbose_name='Class Name')
	capacity = models.IntegerField()

	def freeSlots(self):
		return self.capacity-len(self.student_set.all())

class Student(models.Model):
	idNo = models.CharField(max_length=8, unique=True, verbose_name='ID Number')
	name = models.CharField(max_length=100, verbose_name='Full Name')
	cellNo = models.CharField(max_length=11, verbose_name='Mobile Number')
	enrolledClass = models.ForeignKey(LeapClass, null=True)

