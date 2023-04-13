from django.shortcuts import render, redirect
from .models import Article, Comment, Re_comment
from django.utils import timezone
# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('list') #redirect는 여기로 보내준다는 뜻 즉, 글 작성을 완료하면 list 패이지로 보내준다는 것이다.
    
    return render(request, 'new.html')

def list(request):
    hobbies = Article.objects.filter(category='hobby')
    hobbies_len = len(hobbies)

    foods = Article.objects.filter(category='food')
    foods_len = len(foods)

    programmings = Article.objects.filter(category='programming')
    programmings_len = len(programmings)

    return render(request, 'list.html', {'hobbies_len': hobbies_len, 'foods_len': foods_len, 'programmings_len': programmings_len})

def detail(request, article_id):

    article_detail = Article.objects.get(id = article_id)
    created_dt = article_detail.dt

    if request.method == 'POST':
        pk_list = []
        for i in Comment.objects.all():
            pk_list.append(i.pk)
        comment_id = max(pk_list)

        if 'content' in request.POST:
            Comment.objects.create(
                post = article_detail,
                content = request.POST['content'],
            )

        
        elif 'recomment' in request.POST:
            Re_comment.objects.create(
                comment = Comment.objects.get(id = comment_id),
                content = request.POST['recomment'],
            )
        
        return redirect('detail', article_id)
    
    
    return render(request, 'detail.html', {'article_detail': article_detail, 'created_dt':created_dt})


def category(request, category_kind):
    category_kind_templates = category_kind
    categorized_articles = Article.objects.filter(category=category_kind)

    return render(request, 'category.html', {'categorized_articles': categorized_articles, 'category_kind_templates':category_kind_templates,})
