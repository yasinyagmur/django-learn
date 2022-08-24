from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "dsApp/index.html")
#     Django uygulamalarında geriye bir html sayfası döndürmek için render() metodunu kullanıyor olmalıyız.
# render() metodu ilk parametre olarak uygulamaya yapılan request nesnesini  parametre olarak alması gerekiyor. İkinci parametre olarak ise döndürülecek html sayfasının ismini alır
