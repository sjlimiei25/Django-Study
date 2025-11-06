from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
# 게시글 조회 기능에 대한 처리
def post_list(request):
  # 게시글 목록 조회
  posts = Post.objects.all()
  return render(request, 'myapp/post_list.html', {'list':posts})

# 기본적으로 view 에서 '앱이름/템플릿명.html' 으로 작성하게 되면,
#     실제 파일은 '앱이름/templates/앱이름/템플릿명.html' 로 찾게 됨.

# 만약, 공용 템플릿 폴더를 사용하고자 할 경우
#     settings.py 파일에 설정 추가
#     * BASE_DIR / 'templates' 설정 시 BASE_DIR/templates/앱이름/템플릿명.html' 로 찾게 됨

# 게시글 추가 기능에 대한 처리
def new_post(request):
  # 요청 방식에 따른 처리
  if request.method == 'POST':
    # 게시글 추가 기능

    # 전달된 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 추가
    Post.objects.create(title=title, content=content)

    # 게시글 목록 페이지로 이동
    return redirect('post_list')

  # 게시글 추가 페이지 응답
  return render(request, 'myapp/new_post.html')