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
from . import backModelView
from . import testView

urlpatterns = [
    url(r'^$', indexView.indexView, name='index'),
    #url(r'^$', views.index, name='index'),
    url(r'back/$', views.back_page),
    url(r'backModel', backModelView.backModelView),
    url(r'login/$', views.login),
    url('index', indexView.indexView),
    url('about', govPolicyView.govPolicyExampleView),
    url('rooms', comSupportView.comSupportView),
    url('gallery', talentCultivationView.talentCultivationView),
    url('dinning', proIntroView.proIntroView),
    url('predict', devPredictionView.devPredictionView),
    url('govPolicyMacroRegion.html$', govPolicyView.govPolicyRegionView),
    url('govPolicyMacroTime', govPolicyView.govPolicyTimeView),
    url('govPolicyMacroBusiness', govPolicyView.govPolicyBusinessView),
    url('govPolicyMicroCom', govPolicyView.govPolicyComView),
    url('govPolicyAnalysis.html$', govPolicyView.govPolicyAnalysisView),
    url('govPolicyAnalysisPrediction', govPolicyView.govPolicyAnalysisPredictionView),
    url('govPolicyExamples', govPolicyView.govPolicyExampleView),
    #url('addTest', testView.addTestView),
    url('addTest$', testView.addTest),
    url('add1', testView.add1),
    url('myget', testView.myget),
    url(r'^ajax_list/$', testView.ajax_list),
    url(r'^ajax_dict/$', testView.ajax_dict),
    url(r'testCelery$', testView.testCelery),
    url(r'testCeleryRe', testView.testCeleryRe),
    url(r'comNum', govPolicyView.comNum),
]
