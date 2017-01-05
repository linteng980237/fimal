from django.shortcuts import render


from dog.models import Dog


def dog(request):
    '''
    Render the dog 
    '''
    dogs = Dog.objects.all()
    itemsList = []
    for dog in dogs:
        items = [dog] 
        itemsList.append(items)
    context = {'itemsList':itemsList}   
    return render(request, 'dog/dog.html', context)