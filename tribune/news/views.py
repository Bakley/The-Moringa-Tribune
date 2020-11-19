from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from .forms import NewsLetterForm
from .email import send_welcome_email
from .models import Article, NewsLetterRecipients


import datetime as dt


def welcome(request):
    return render(request, 'welcome.html')


def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            HttpResponseRedirect('news_today')
    else:
        form = NewsLetterForm()
    return render(
        request, 'all-news/today-news.html',
        {
            "date": date,
            "news": news,
            "letterForm": form
        }
    )


def past_days_news(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)
    return render(
        request, 'all-news/past-news.html',
        {"date": date, "news": news}
    )
