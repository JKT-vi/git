print('hello')

def timo(function):
    def ko(request,*a,**k):
        return HttpResponse('ok')
    return ko
