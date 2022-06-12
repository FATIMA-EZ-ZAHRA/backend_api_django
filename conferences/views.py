# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for Conference
from .serializers import ConferenceSerializer
# Conference model
from .models import Conference
# Participant model
from participants.models import Participant
# API definition for Participant
from participants.serializers import ParticipantSerializer


@csrf_exempt
def conferences(request):
    '''
    List all conferences snippets
    '''
    if(request.method == 'GET'):
        # get all the Conferences
        Conferences = Conference.objects.all()
        # serialize the Conference data
        serializer = ConferenceSerializer(Conferences, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = ConferenceSerializer(data=data)
        # check if the sent information is okay
        print(serializer)
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def conference_detail(request, pk):
    try:
        # obtain the conference with the passed id.
        conference = Conference.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if(request.method == 'GET'):
        serializer = ConferenceSerializer(conference)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = ConferenceSerializer(conference, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the conference
        conference.delete() 
        # return a no content response.
        return HttpResponse(status=204) 


@csrf_exempt
def conferenciers(request):
    '''
    List all conferenciers snippets
    '''
    if(request.method == 'GET'):
        # get all the Participants
        Participants = Participant.objects.filter(type="Conferencier")
        # serialize the Participant data
        serializer = ParticipantSerializer(Participants, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)