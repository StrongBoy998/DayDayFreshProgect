# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
import json

# 拿到产品分类信息
SortsMsg=GoodSort.objects.all()
# 分类1
sort1=GoodSort.objects.filter(id=1)
# 分类2
sort2=GoodSort.objects.filter(id=2)
# 分类3
sort3=GoodSort.objects.filter(id=3)
# 分类4
sort4=GoodSort.objects.filter(id=4)
# 分类5
sort5=GoodSort.objects.filter(id=5)
# 分类6
sort6=GoodSort.objects.filter(id=6)
# 拿到分类为新鲜水果的产品的前4条
goodMsg1=Goods.objects.filter(goodSort_id=1).order_by('goodsName')[0:4]
# 拿到分类为新鲜水果的产品的其他3条信息
goodOther1=Goods.objects.filter(goodSort_id=1).order_by('goodsName')[4:7]
# 拿到分类为海鲜水产的产品的前4条
goodMsg2=Goods.objects.filter(goodSort_id=2).order_by('goodsName')[0:4]
# 拿到分类为海鲜水产的产品的其他3条信息
goodOther2=Goods.objects.filter(goodSort_id=2).order_by('goodsName')[4:7]
# 拿到分类为猪牛羊肉的产品的前4条
goodMsg3=Goods.objects.filter(goodSort_id=3).order_by('goodsName')[0:4]
# 拿到分类为猪牛羊肉的产品的其他3条信息
goodOther3=Goods.objects.filter(goodSort_id=3).order_by('goodsName')[4:7]
# 拿到分类为禽类蛋品的产品的前4条
goodMsg4=Goods.objects.filter(goodSort_id=4).order_by('goodsName')[0:4]
# 拿到分类为禽类蛋品的产品的其他3条信息
goodOther4=Goods.objects.filter(goodSort_id=4).order_by('goodsName')[4:7]
# 拿到分类为新鲜蔬菜的产品的前4条
goodMsg5=Goods.objects.filter(goodSort_id=5).order_by('goodsName')[0:4]
# 拿到分类为新鲜蔬菜的产品的其他3条信息
goodOther5=Goods.objects.filter(goodSort_id=5).order_by('goodsName')[4:7]
# 拿到分类为速冻食品的产品的前4条
goodMsg6=Goods.objects.filter(goodSort_id=6).order_by('goodsName')[0:4]
# 拿到分类为速冻食品的产品的其他3条信息
goodOther6=Goods.objects.filter(goodSort_id=6).order_by('goodsName')[4:7]
dic={
	'sorts':SortsMsg,
	'goodsMsg1':goodMsg1,
	'goodsMsg2':goodMsg2,
	'goodsMsg3':goodMsg3,
	'goodsMsg4':goodMsg4,
	'goodsMsg5':goodMsg5,
	'goodsMsg6':goodMsg6,
	'sortMs1':sort1,
	'sortMs2':sort2,
	'sortMs3':sort3,
	'sortMs4':sort4,
	'sortMs5':sort5,
	'sortMs6':sort6,
	'other1':goodOther1,
	'other2':goodOther2,
	'other3':goodOther3,
	'other4':goodOther4,
	'other5':goodOther5,
	'other6':goodOther6
}
# 首页
def index(request):
	# 拿到session中用户名字[取不到会返回一个默认值，方便js根据传过去的值做处理]
	Uname=request.session.get('name',default='')
	dic['uname']=Uname
	return render(request,'freshFruit/index.html',dic)
# 退出登陆的实现
def loginOut(request):
	del request.session['name']
	# 拿到session中用户名字[取不到会返回一个默认值，方便js根据传过去的值做处理]
	Uname=request.session.get('name',default='')
	dic['uname']=Uname
	return render(request,'freshFruit/index.html',dic)
# 关于我们页面
def aboutus(request):
	return render(request,'freshFruit/aboutus.html')
# 联系我们页面
def callus(request):
	return render(request,'freshFruit/callus.html')
# 招聘人才界面
def joinus(request):
	return render(request,'freshFruit/joinus.html')
