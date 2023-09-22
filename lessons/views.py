from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Users, Product, Lesson, Access
from .serializers import (ProductSerializer, LessonSerializer, 
                          AccessSerializer, UsersSerializer)


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonViewset(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        lesson = Lesson.objects.create(title=data['title'], duration=data['duration'], 
                                       viewing_status=True if ((data['duration'] / 100) * data['viewing_time']) >= 80 else False, 
                                       viewing_time=data['viewing_time'], 
                                       last_viewing_date=data['last_viewing_date'], url=data['url'])
        
        lesson.save()
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)
        
        
        
class AccessViewset(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    
    
class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


@api_view(['GET'])
def lessons_list(request, username):
        products = {Users.objects.get(name=username).name: list(Lesson.objects.filter(products__users__name=username, products__access__access_status=True).
                    values('title', 'viewing_status', 'viewing_time'))}
        return Response(products)


@api_view(['GET'])
def product_lessons_list(request, username, product_title):
        products = {Product.objects.get(title=product_title).title:list(Product.objects.filter(
                users__name=username, access__access_status=True).get(title=product_title).lesson_set.values('title',
        'viewing_status', 'viewing_time', 'last_viewing_date'))}
        return Response(products)


@api_view(['GET'])
def statistic(request):
        products = Product.objects.all()
        result_dict = {}
        for i in products:
                result_dict[i.title] = {'viewed count': i.lesson_set.filter(viewing_status=True).count(),
                                        'overall viewing time': i.lesson_set.aggregate(viewed=Sum('viewing_time'))[
                                                'viewed'],
                                        'number of students': i.users.count(),
                                        'acquisition percentage': round(
                                                i.access_set.filter(access_status=True).count() / Users.objects.count(),2)
                                        }
        return Response(result_dict)


    
        
