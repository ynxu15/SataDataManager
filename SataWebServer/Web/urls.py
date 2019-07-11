"""SataWebServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from . import indexView
from . import govPolicyView
from . import comSupportView
from . import talentCultivationView
from . import proIntroView
from . import devPredictionView
from . import testView

urlpatterns = [
    url(r'^$', indexView.indexView, name='index'),
    url(r'^back/$', views.back_page),
    url(r'^login/$', views.login),
    url('index', indexView.indexView),
    url('about', govPolicyView.govPolicyView),
    url('rooms', comSupportView.comSupportView),
    url('gallery', talentCultivationView.talentCultivationView),
    url('dinning', proIntroView.proIntroView),
    url('predictMain', devPredictionView.predictMainView),
    url('predictPart',devPredictionView.predictPartView),
    url('predictCom',devPredictionView.predictComView),
    url('dataImport', devPredictionView.dataImport),
    url('dataExport', devPredictionView.dataExport),
    url('dataClean', devPredictionView.dataClean),
    url('dataUpdate', devPredictionView.dataUpdate),
    url('dataSearch', devPredictionView.dataSearch),
    url('test', devPredictionView.test),
    url('getByComName',devPredictionView.getByComName),
    url('charts',devPredictionView.charts),
    url('flushMain',devPredictionView.flushMain),
    url('flushPart',devPredictionView.flushPart),
    url('flushCom',devPredictionView.flushCom)
]
