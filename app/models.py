from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title

class Barangay_Official(models.Model):
    Full_Name = models.CharField(max_length=100)
    Position =  models.CharField(max_length=100, choices = [ ('SK Chairman', 'SK Chairman'), ('SK Kagawad', 'SK Kagawad'),
                                                          ('Brgy Captain', 'Brgy Captain'), ('Brgy Secretary', 'Brgy Secretary'),])
    StartDate_Term = models.DateField()
    End_Term = models.DateField()
    Contact_Details = models.TextField()

    def __str__(self):
        return self.Position

    def get_absolute_url(self):
        return reverse("Barangay_Official_detail", kwargs={"pk": self.pk})

class Barangay_Project(models.Model):
    Project_Name = models.CharField(max_length=100)
    Project_Type = models.CharField(max_length=100, choices= [ ('Job Fairs and Training', 'Job Fairs and Training'),
                                                               ('Education', 'Education'), ('Infrastructure', 'Infrastructure'),
                                                               ('Sports Activities', 'Sports Activities')])
    Description = models.TextField()
    Project_Budget = models.DecimalField(max_digits=10, decimal_places=2)
    Project_Leader = models.ForeignKey("Barangay_Official", on_delete=models.CASCADE)
    Start_Date = models.DateTimeField()
    End_Date = models.DateTimeField()
    Current_Status = models.CharField(max_length=100, choices=[ ('Ongoing', 'Ongoing'),
                                                                ('Peding', 'Pending'),
                                                                ('Completed', 'Completed')])

    def __str___(self):
        return self.Project_Name

    def get_absolute_url(self):
        return reverse("Barangay_Project_detail", kwargs={"pk": self.pk})

class Complaint(models.Model):
    Resident_Name = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    Date_Filed = models.DateTimeField()
    Complaint_Type = models.CharField(max_length=100, choices=[ ('Noise', 'Noise'),
                                                                ('Waste management', 'Waste management'),
                                                                ('Illegal Activities', 'Illegal Activities')])
    Description = models.TextField()
    Status = models.CharField(max_length=100, choices=[ ('Resolved', 'Resolved'),
                                                        ('Pending', 'Pending')])
    Action_Take = models.CharField(max_length=200)

    def __str__(self):
        return self.Complaint_Type

    def get_absolute_url(self):
        return reverse("Complaint_detail", kwargs={"pk": self.pk})

class Barangay_Service(models.Model):
    Service_Type = models.CharField(max_length=100, choices=[ ('Health Service', 'Health Service'),
                                                              ('Education and training Service', 'Education and Training'),
                                                              ('Social Service', 'Social Service'), ('Environmental Services', 'Environmental Services'),])
    Description = models.TextField()
    Officials_Involved = models.ManyToManyField(Barangay_Official)
    Venue = models.CharField(max_length=100)
    Budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Service_Type

    def get_absolute_url(self):
        return reverse("Barangay_Service_detail", kwargs={"pk": self.pk})

class Request(models.Model):
    Request_Type = models.CharField(max_length=100, choices=[ ('Business Permit', 'Business Permit'),
                                                              ('Clearance', 'Clearance'), ('Certificate of Indigency', 'Certificate of Indigency'), ])
    Personnel = models.ForeignKey("Barangay_Official", on_delete=models.CASCADE )
    Requested_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    Status = models.CharField(max_length=100, choices=[ ('Completed', 'Completed'),
                                                        ('Pending', 'Pending'), ('Processing', 'Processing'), ])

    def __str__(self):
        return self.Request_Type

    def get_absolute_url(self):
        return reverse("Request_detail", kwargs={"pk": self.pk})










