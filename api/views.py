from rest_framework import viewsets, status
from .models import Event, Attendee, Speaker, Sponsor
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer, AttendeeSerializer, AttendeeRegistrationSerializer, SpeakerSerializer, SponsorSerializer, UserSerializer, SpeakerRegistrationSerializer, SponsorRegistrationSerializer, ScheduleRegistrationSerializer, AttendeeLoginSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.tokens import RefreshToken

from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from reportlab.lib.pagesizes import letter




def generate_attendees_pdf(event):
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendees.pdf"'

    c = canvas.Canvas(buffer)
    c.drawString(100, 750, "Event Attendees:")

    attendees = event.attendees.all()

    y = 730  # Initial y-position
    for attendee in attendees:
        y -= 20  # Adjust the y-position for the next entry
        c.drawString(100, y, f"{attendee.fullname} {attendee.phone}")

    c.showPage()
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def generate_event_report_pdf(event):
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="event_report.pdf'

    c = canvas.Canvas(buffer, pagesize=letter)

    # Set bold font
    c.setFont("Helvetica-Bold", 14)

    # Event Title
    c.drawCentredString(300, 700, "Event Report")

    # Set normal font
    c.setFont("Helvetica", 12)

    c.drawString(100, 680, f"Title: {event.title}")

    # Event Description
    c.drawString(100, 660, f"Description: {event.description}")

    # Event Address and Location
    c.drawString(100, 640, f"Address: {event.address}")
    c.drawString(100, 620, f"Location: {event.location}")

    # Event Duration (formatted date)
    start_date = event.start_date.strftime("%Y-%m-%d")
    end_date = event.end_date.strftime("%Y-%m-%d")
    event_duration = f"Duration: {start_date} - {end_date}"
    c.drawString(100, 600, event_duration)

    # Number of Participants
    num_participants = event.attendees.count()
    c.drawString(100, 580, f"Number of Participants: {num_participants}")

    # Event Speakers Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 560, "Honoured Speakers:")

    # Set normal font
    c.setFont("Helvetica", 12)

    # Event Speakers (in a numbered list format)
    speakers = event.speakers.all()
    y_speakers = 540
    for i, speaker in enumerate(speakers, start=1):
        y_speakers -= 20
        c.drawString(100, y_speakers,
                     f"{i}. {speaker.fullname} - {speaker.organization}")

    # Event Sponsors Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_speakers - 20, "Honoured Sponsors")

    # Set normal font
    c.setFont("Helvetica", 12)

    # Event Sponsors (in a numbered list format)
    sponsors = event.sponsors.all()
    y_sponsors = y_speakers - 40  # Adjust the y-position for sponsors
    for i, sponsor in enumerate(sponsors, start=1):
        y_sponsors -= 20
        c.drawString(100, y_sponsors,
                     f"{i}. {sponsor.name} - {sponsor.description}")

    c.showPage()
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def generate_schedule_pdf(event):
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="event_schedule.pdf'

    c = canvas.Canvas(buffer)
    c.drawString(100, 750, "Event Schedule:")

    schedules = event.schedules.all().order_by('date', 'start_time')

    y = 730  # Initial y-position
    for schedule in schedules:
        y -= 20  # Adjust the y-position for the next entry
        display_text = f"{schedule.date} {schedule.start_time} - {schedule.end_time}: {schedule.activity}"
        c.drawString(100, y, display_text)

    c.showPage()
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


class AttendeesPDFDownload(APIView):
    def get(self, request, event_id):
        # You need to fetch the event data
        event = Event.objects.get(pk=event_id)
        response = generate_attendees_pdf(event)
        return response


class EventReportPDFDownload(APIView):
    def get(self, request, event_id):
        # You need to fetch the event data
        event = Event.objects.get(pk=event_id)
        response = generate_event_report_pdf(event)
        
        # def create(self, request, *args, **kwargs):
        #     serializer = self.get_serializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
            
        #     # Call the create method of the serializer to create the event
        #     # along with its associated entities
        #     self.perform_create(serializer)
            
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response


class SchedulePDFDownload(APIView):
    def get(self, request, event_id):
        # You need to fetch the event data
        event = Event.objects.get(pk=event_id)
        response = generate_schedule_pdf(event)
        return response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    
# class AttendeeLoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         name = request.data.get('fullname')
#         user = Attendee.objects.filter(email=email).first()

#         if user is None:
#             return Response({'detail': 'Invalid email'}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-start_date')
    serializer_class = EventSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    
    
class EventRegistrationView(APIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        
        if serializer.is_valid():
            event = serializer.save()

            read_serializer = EventSerializer(event)

            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
           
    def delete(self, request, id):
        try:
            get_event = Event.objects.get(id=id)
            
        except Event.DoesNotExist:
            return Response({'errors': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        get_event.delete()
            
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    


class AttendeeRegistrationView(APIView):
    def post(self, request):
        serializer = AttendeeRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Extract the event ID from the request data
            event_id = request.data.get('event')

            # Check if the event with the given ID exists
            try:
                event = Event.objects.get(pk=event_id)
            except Event.DoesNotExist:
                return Response({"event": "Event with this ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the event is fully booked
            if event.attendees.count() >= event.available_seat:
                return Response({"event": "This event is fully booked."}, status=status.HTTP_400_BAD_REQUEST)

            # Create the attendee
            attendee = serializer.save()

            # Add the attendee to the event
            event.attendees.add(attendee)

            response_data = {
                "message": "Attendee registered successfully",
                "data": serializer.data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class AttendeeLoginView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = AttendeeLoginSerializer(data=request.data)

        if serializer.is_valid():
            event_id = serializer.validated_data.get('event_id')
            attendee_email = serializer.validated_data.get('email')

            # Check if the event with the given ID exists
            try:
                event = Event.objects.get(pk=event_id)
            except Event.DoesNotExist:
                return Response({"event": "Event with this ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the attendee with the given email exists and is registered for the event
            try:
                attendee = Attendee.objects.get(email=attendee_email, events_attending=event)
            except Attendee.DoesNotExist:
                return Response({"attendee": "Attendee is not registered for this event."}, status=status.HTTP_400_BAD_REQUEST)

           
            refresh = RefreshToken.for_user(attendee) 
            return Response({"message": "Attendee logged in successfully", "refresh": str(refresh), "access": str(refresh.access_token)}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeakerRegistrationView(APIView):
    def post(self, request):
        serializer = SpeakerRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Extract the event ID from the request data
            event_id = request.data.get('event')

            # Check if the event with the given ID exists
            try:
                event = Event.objects.get(pk=event_id)
            except Event.DoesNotExist:
                return Response({"event": "Event with this ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Create the speaker
            speaker = serializer.save()

            # Add the speaker to the event
            event.speakers.add(speaker)

            response_data = {
                "message": "speaker registered successfully",
                "data": serializer.data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SponsorRegistrationView(APIView):
    def post(self, request):
        serializer = SponsorRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Extract the event ID from the request data
            event_id = request.data.get('event')

            # Check if the event with the given ID exists
            try:
                event = Event.objects.get(pk=event_id)
            except Event.DoesNotExist:
                return Response({"event": "Event with this ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Create the sponsor
            sponsor = serializer.save()

            # Add the sponsor to the event
            event.sponsors.add(sponsor)

            response_data = {
                "message": "Sponsor registered successfully",
                "data": serializer.data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleRegistrationView(APIView):
    def post(self, request):
        serializer = ScheduleRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Extract the event ID from the request data
            event_id = request.data.get('event')

            # Check if the event with the given ID exists
            try:
                event = Event.objects.get(pk=event_id)
            except Event.DoesNotExist:
                return Response({"event": "Event with this ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Create the schedule
            schedule = serializer.save()

            # Add the schedule to the event
            event.schedules.add(schedule)

            response_data = {
                "message": "schedule registered successfully",
                "data": serializer.data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
