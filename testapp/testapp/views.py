from django.http import HttpResponse

def index(request):
    test_str = "test"
    def get():
        return HttpResponse("hello " + test_str)
    def post():
        return HttpResponse("hello ")

    return locals()[request.method.lower()]()

