# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import template
from django.http import HttpResponse
from restaurants.models import Restaurant, Food

def menu(request):
	path = request.path #扣除網域名稱的請求路徑 (開頭一反斜線)
	restaurants = Restaurant.objects.all()	
	return render_to_response('menu.html', locals())