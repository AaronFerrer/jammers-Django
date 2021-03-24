from django.db import models

# Create your models here.
# TODO: Scale up to include ring types.
# TODO: Height/Weight as custon models

class Deformity(models.Model):
	"""Model Representing the Patient Deformity"""
	name = models.CharField(max_length = 200, help_text="Enter the patient's deformity.")

	def __str__(self):
		"""String to represent the Patient Deformity"""
		return self.name

from django.urls import reverse # generates URLS by reversing the URL patterns
import uuid

class Patient(models.Model):
	"""Model representing a patient."""

	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this patient')
	first_name = models.CharField(max_length = 200, help_text="First Name")
	middle_name = models.CharField(max_length = 200, help_text="Middle Name")
	last_name = models.CharField(max_length = 200, help_text="Last Name")
	date_of_birth = models.DateField(null = False, blank = False)
	comment = models.TextField(max_length = 200, help_text="Comment or Description of condition.")
	
	# TODO: Find specific Models for these.
	height = models.IntegerField(max_length = 200, help_text="Height")
	weight = models.IntegerField(max_length = 200, help_text="Weight")
	surgery_date = models.DateField(null = False, blank = False)  # Consider if these can be empty
	deform_class = models.ForeignKey('Deformity', on_delete=models.SET_NULL, null= True)
	'''
	# Brace 
	brace_one = models.IntegerField(blank=True, null=True,help_text="Brace 1")
	brace_two = models.IntegerField(blank=True, null=True,help_text="Brace 2")
	brace_three = models.IntegerField(blank=True, null=True,help_text="Brace 3")
	brace_four = models.IntegerField(blank=True, null=True,help_text="Brace 4")
	brace_five = models.IntegerField(blank=True, null=True,help_text="Brace 5")
	brace_six = models.IntegerField(blank=True, null=True,help_text="Brace 6")
	'''
	class Meta:
		ordering = ['last_name','first_name']

	def __str__(self):
		"""String for representing the Patient."""
		return f'{self.last_name}, {self.first_name}'

	# TODO: Consider if this is necessary
	def get_absolute_url(self):
		"""Returns a URL for a patient's record"""
		return reverse('patient-detail', args=[str(self.id)])

class RxInstance(models.Model):
	"""Model representing the prescription instance"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique Prescription ID')
	patient = models.ForeignKey('Patient', on_delete= models.RESTRICT)

	 # Brace 
	brace_one = models.IntegerField(blank=True, null=True,help_text="Brace 1")
	brace_two = models.IntegerField(blank=True, null=True,help_text="Brace 2")
	brace_three = models.IntegerField(blank=True, null=True,help_text="Brace 3")
	brace_four = models.IntegerField(blank=True, null=True,help_text="Brace 4")
	brace_five = models.IntegerField(blank=True, null=True,help_text="Brace 5")
	brace_six = models.IntegerField(blank=True, null=True,help_text="Brace 6")

	PT_STATUS = (
        ('a', 'Ongoing'),
        ('r', 'Resolved'),
    )

	status = models.CharField(
	    max_length=1,
	    choices=PT_STATUS,
	    blank=True,
	    default='m',
	    help_text='Prescription Ongoing',
    )

	class Meta:
		ordering = ['status']

	def __str__(self):
		"""String to represent the object"""
		return f'{self.id} ({self.patient.last_name}, {self.patient.first_name})'

class Surgeon(models.Model):
	"""Model representing the prescription instance"""
	#id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this patient')
	first_name = models.CharField(max_length = 200, help_text="First Name")
	middle_name = models.CharField(max_length = 200, help_text="Middle Name")
	last_name = models.CharField(max_length = 200, help_text="Last Name")
	
	class Meta:
		ordering = ['last_name','first_name']	

	# TODO: Determine if this is necessary
	#def get_absolute_url(self):
		"""Returns a URL for a surgeon's record"""
	#	return reverse('surgeon-detail',args=[str(self.id)])

	def __str__(self):
		"""String to represent the Surgeon"""
		return f'{self.last_name}, {self.first_name}'
