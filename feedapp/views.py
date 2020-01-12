from django.shortcuts import render
from feedapp.models import FeedbackData
from feedapp.forms import FeedbackForm
from django.http.response import HttpResponse

import datetime as dt
date1=dt.datetime.now()

# Create your views here.
def feedbackview(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('Name')
            rating=request.POST.get('Rating')
            feedback=request.POST.get('Feedback')
            data=FeedbackData(
                Name=name,
                Rating=rating,
                Date=date1,
                Feedback=feedback

            )
            data.save()
            fform=FeedbackForm()
            feed=FeedbackData.objects.all()
            return render(request,'feedback.html',{'ffrom':fform,'feed':feed})

        else:
          return HttpResponse("user missed value")
    else:
        fform=FeedbackForm()
        feed=FeedbackData.objects.all()
        return render(request,'feedback.html',{'ffrom':fform,'feed':feed})
