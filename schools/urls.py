"""schools URL Configuration

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
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from profiles.urls import (
    student_urls, parent_urls, teacher_urls
)

from profiles.api.urls import (
    student_urlpatterns, parent_urlpatterns, teacher_urlpatterns
)

from academic.urls import (
    attendance_urls, department_urls, subject_urls, course_urls,
    assessment_urls, exam_urls
)

urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),

    url(r'^student/', include(student_urls.urlpatterns)),       # Student URLs
    url(r'^teacher/', include(teacher_urls.urlpatterns)),       # Teacher URLs
    url(r'^parent/', include(parent_urls.urlpatterns)),         # Parent URLs
    url(r'^attendance/', include(attendance_urls.urlpatterns)), # Attendance urls
    url(r'^department/', include(department_urls.urlpatterns)), # Department URLs
    url(r'^course/', include(course_urls.urlpatterns)),         # subject urls
    url(r'^subject/', include(subject_urls.urlpatterns)),       # subject urls
    url(r'^assessment/', include(assessment_urls.urlpatterns)), # assessment urls
    url(r'^exam/', include(exam_urls.urlpatterns)),              # exam urls

    url(r'^api/student/', include(student_urlpatterns)),
    url(r'^api/parent/', include(parent_urlpatterns)),
    url(r'^api/teacher/', include(teacher_urlpatterns)),
]

urlpatterns += staticfiles_urlpatterns()
