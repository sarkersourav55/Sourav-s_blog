from django.shortcuts import render,get_object_or_404
from post.models import post
from subscribe.models import sub
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Count,Q

def search(request):
	queryset=post.objects.all()
	searched=request.GET.get('q')
	if searched:
		find=queryset.filter(
			Q(title__icontains=searched) |
			Q(overview__icontains=searched)
			).distinct()
	context={'result':find}

	return render(request, 'search.html',context)


def get_cat_count():
	count=post.objects.values('cat__title').annotate(Count('cat'))

def index(request):
	ft=post.objects.filter(featured=True)
	latest=post.objects.order_by('-time')[0:3]
	if request.method == 'POST':
		email=request.POST['Email']
		reg=sub()
		reg.email=email
		reg.save()
	context={
		'post_data':ft,
		'latest':latest
	}
	return render(request,'index.html',context)


def blog(request):
	cat_count=get_cat_count()
	article = post.objects.all()
	pagination=Paginator(article,4)
	pg='page'
	page=request.GET.get(pg)
	latest=post.objects.order_by('-time')[0:4]
	try:
		set=pagination.page(page)
	except EmptyPage:
		set=pagination.page(Paginator.num_pages)
	except PageNotAnInteger:
		set = pagination.page(1)

	context={
		'post':set,
		'pg':pg,
		'latest':latest,
		'count':cat_count
	}
	return render(request,'blog.html',context)



def Post(request,id):
	data=get_object_or_404(post,id=id)
	latest=post.objects.order_by('-time')[0:4]
	context={
		"data":data,'latest':latest
	}
	return render(request,'post.html',context)