from django.shortcuts import render

# Create your views here.
def count(request):

    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    input_text = text
    total_len=len(text)
    only_text = text.replace(" ", "")
    only_text_len = len(only_text)
    return render(request, 'result.html', {'total_len': total_len,
                                           'only_text_len': only_text_len,
                                           'input_text': input_text,})
