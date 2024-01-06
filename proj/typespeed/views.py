# # from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from .models import Timestamp
# from django.utils import timezone

# def timestamp_view(request):
#     timestamp_instance = Timestamp.objects.first()

#     if request.method == 'POST':
#         if 'start' in request.POST:
#             timestamp_instance.start_time = timezone.now()
#             timestamp_instance.save()
#         elif 'end' in request.POST:
#             timestamp_instance.end_time = timezone.now()
#             timestamp_instance.save()
#             user_input = request.POST['typehere']


#             Timestamp.objects.create(start_time=timestamp_instance.start_time,end_time=timestamp_instance.end_time)
#             elapsed_time = timestamp_instance.end_time - timestamp_instance.start_time
#             words_per_minute = (len(user_input)/elapsed_time)*60


#             s=f"Words per Minute: {words_per_minute:.2f} WPM"


#             return render(request, 'index.html', {'typespeed':s,'timestamp_instance': timestamp_instance})
#         return redirect('timestamp_view')
#     else:
#       return render(request, 'index.html')

from django.shortcuts import render
from django.http import HttpResponse
from .typing_test import typing_test

# def typing_test_view(request):
#     if request.method == 'POST':
#         typing_speed, accuracy = typing_test(request.POST.get('user_input', ''))
#         return render(request, 'result.html', {'typing_speed': typing_speed, 'accuracy': accuracy})
#     else:
#         return render(request, 'typing_test.html')



def typing_test_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        typing_speed, accuracy = typing_test(user_input)
        return render(request, 'result.html', {'typing_speed': typing_speed, 'accuracy': accuracy})
    else:
        prompt_text = "The quick brown fox jumps over the lazy dog."
        return render(request, 'typing_test.html', {'prompt_text': prompt_text})
