from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Test

def test_view(request):
    tests = Test.objects.all()
    return render(request, 'calc.html', {'tests':tests})

@require_POST
def result_view(request):
    tests = Test.objects.all()
    count = 0
    for test in tests:
        try:
            if test.correct == request.POST[test.question]:
                count += 1
        except:
            return HttpResponse('You have to solve all problems')
    return render(request, 'result.html', {'count':count, 'all':(tests.count()-count)})