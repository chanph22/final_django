from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Barangay_Official, Barangay_Project, Complaint, Barangay_Service, Request
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

class Barangay_OfficialListView(ListView):
    model = Barangay_Official
    context_object_name = 'Barangay_Officials'
    template_name = 'app/Barangay_Official_list.html'

class Barangay_OfficialDetailView(DetailView):
    model = Barangay_Official
    context_object_name = 'Barangay_Official'
    template_name = 'app/Barangay_Official_detail.html'

class Barangay_OfficialCreateView(CreateView):
    model = Barangay_Official
    fields = ['Full_Name', 'Position', 'StartDate_Term', 'End_Term', 'Contact_Details']
    template_name = 'app/Barangay_Official_create.html'

class Barangay_OfficialUpdateView(UpdateView):
    model = Barangay_Official
    fields = ['Full_Name', 'Position', 'StartDate_Term', 'End_Term', 'Contact_Details']
    template_name = 'app/Barangay_Official_update.html'

class Barangay_OfficialDeleteView(DeleteView):
    model = Barangay_Official
    template_name = 'app/Barangay_Official_delete.html'
    success_url =  reverse_lazy('Barangay_Official')

'''Project'''

class Barangay_ProjectListView(ListView):
    model = Barangay_Project
    context_object_name = 'Barangay_Projects'
    template_name = 'app/Barangay_Project_list.html'

class Barangay_ProjectDetailView(DetailView):
    model = Barangay_Project
    context_object_name = 'Barangay_Project'
    template_name = 'app/Barangay_Project_detail.html'

class Barangay_ProjectCreateView(CreateView):
    model = Barangay_Project
    fields = ['Project_Name', 'Project_Type', 'Description', 'Project_Budget', 'Project_Leader', 'Start_Date', 'End_Date', 'Current_Status']
    template_name = 'app/Barangay_Project_create.html'

class Barangay_ProjectUpdateView(UpdateView):
    model = Barangay_Project
    fields =  ['Project_Name', 'Project_Type', 'Description', 'Project_Budget', 'Project_Leader', 'Start_Date', 'End_Date', 'Current_Status']
    template_name = 'app/Barangay_Project_update.html'

class Barangay_ProjectDeleteView(DeleteView):
    model = Barangay_Project
    template_name = 'app/Barangay_Project_delete.html'
    success_url =  reverse_lazy('Barangay_Project')

''''Complaint'''

class ComplaintListView(ListView):
    model = Complaint
    context_object_name = 'Complaints'
    template_name = 'app/Complaint_list.html'

class ComplaintDetailView(DetailView):
    model = Complaint
    context_object_name = 'Complaint'
    template_name = 'app/Complaint_detail.html'

class ComplaintCreateView(CreateView):
    model = Complaint
    fields = ['Resident_Name', 'Date_Filed', 'Complaint_Type', 'Description', 'Status', 'Action_Take']
    template_name = 'app/Complaint_create.html'



class ComplaintUpdateView(UpdateView):
    model = Complaint
    fields =  ['Resident_Name', 'Date_Filed', 'Complaint_Type', 'Description', 'Status', 'Action_Take']
    template_name = 'app/Complaint_update.html'

class ComplaintDeleteView(DeleteView):
    model = Complaint
    template_name = 'app/Complaint_delete.html'
    success_url =  reverse_lazy('Complaint')

'''Services'''

class Barangay_ServiceListView(ListView):
    model = Barangay_Service
    context_object_name = 'Barangay_Services'
    template_name = 'app/Barangay_Service_list.html'

class Barangay_ServiceDetailView(DetailView):
    model = Barangay_Service
    context_object_name = 'Barangay_Service'
    template_name = 'app/Barangay_Service_detail.html'

class Barangay_ServiceCreateView(CreateView):
    model = Barangay_Service
    fields = ['Service_Type', 'Description', 'Officials_Involved', 'Venue', 'Budget' ]
    template_name = 'app/Barangay_Service_create.html'

class Barangay_ServiceUpdateView(UpdateView):
    model = Barangay_Service
    fields =  ['Service_Type', 'Description', 'Officials_Involved', 'Venue', 'Budget' ]
    template_name = 'app/Barangay_Service_update.html'

class Barangay_ServiceDeleteView(DeleteView):
    model = Barangay_Service
    template_name = 'app/Barangay_Service_delete.html'
    success_url =  reverse_lazy('Barangay_Service')

'''Request'''

class RequestListView(ListView):
    model = Request
    context_object_name = 'Requests'
    template_name = 'app/Request_list.html'

class RequestDetailView(DetailView):
    model = Request
    context_object_name = 'Request'
    template_name = 'app/Request_detail.html'

class RequestCreateView(CreateView):
    model = Request
    fields = ['Request_Type', 'Personnel', 'Requested_by', 'Status']
    template_name = 'app/Request_create.html'

class RequestUpdateView(UpdateView):
    model = Request
    fields =  ['Request_Type', 'Personnel', 'Requested_by', 'Status']
    template_name = 'app/Request_update.html'

class RequestDeleteView(DeleteView):
    model = Request
    template_name = 'app/Request_delete.html'
    success_url =  reverse_lazy('Request')



