# coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime



def detail(request):
	list1 = Goods.objects.all()[0:1]

	# list1 = goods.goodscomment_set.all()
	# list2 =GoodSort.objects.filter(goodSort_id=1)
	dic ={'list':list1,

		'comment':list1,

	}


	return render(request,'freshFruit/detail.html',dic)




				
			
			

