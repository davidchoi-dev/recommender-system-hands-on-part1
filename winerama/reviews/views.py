from django.shortcuts import render, get_object_or_404
from .models import Review, Wine
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import ReviewForm
import datetime

# Page 13
def review_list(request):
  latest_review_list = Review.objects.order_by('-pub_date')[:9]
  context = {'latest_review_list': latest_review_list}
  return render(request, 'reviews/review_list.html', context)

def review_detail(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  context = {'review': review}
  return render(request, 'reviews/review_detail.html', context)

# Page 17
def wine_list(request):
  wine_list = Wine.objects.order_by('-name')
  context = {'wine_list': wine_list}
  return render(request, 'reviews/wine_list.html', context)

# Page 23
def wine_detail(request, wine_id):
  wine = get_object_or_404(Wine, pk=wine_id)
  form = ReviewForm()
  context = {'wine': wine, 'form': form}
  return render(request, 'reviews/wine_detail.html', context)

def add_review(request, wine_id):
  wine = get_object_or_404(Wine, pk=wine_id)
  if request.POST:
    form = ReviewForm(request.POST)
  else:
    form = ReviewForm()

  if form.is_valid():
    user_name = request.user.username
    review = form.save(commit=False)
    review.wine = wine
    review.user_name = user_name
    review.pub_date = datetime.datetime.now()
    review.save()
    return HttpResponseRedirect(reverse_lazy('reviews:wine_detail', args=(wine.id,)))
  return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})