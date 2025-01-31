from django.contrib import admin
from .models import Barangay_Official, Barangay_Project, Complaint, Barangay_Service, Request

admin.site.register(Barangay_Official)
admin.site.register(Barangay_Project)
admin.site.register(Complaint)
admin.site.register(Barangay_Service)
admin.site.register(Request)



