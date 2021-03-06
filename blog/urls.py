from django.urls import path, include
from blog import views

handler404 = 'blog.views.handler404'
handler505 = 'blog.views.handler500'

urlpatterns = [
    path('', views.index, name="index"),
    path('all/', views.BlogListView.as_view(), name="blogs"),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name="blog"),

    path('new/', views.NewBlogCreateView.as_view(), name="new-blog"),

    path('comments/<int:pk>/deleted/', views.CommentDeleteView.as_view(), name='delete-comment'),
    path('comments/<int:pk>/edit/', views.UpdateCommentUpdateView.as_view(), name='update-comment'),

    path('authors/', views.AuthorListView.as_view(), name="authors"),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name="author"),

    path('author/new/', views.AuthorCreate.as_view(), name="create-author"),

    path('comments/<int:pk>', views.comment, name="comment"),

    path('signup/', views.signup, name="signup"),

    path('<int:pk>/update/', views.UpdatePostUpdateView.as_view(), name="update-post"),
]
