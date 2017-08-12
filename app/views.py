from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Post


class Index(generic.ListView):
    model = Post


class Create(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:index')

    def form_valid(self, form):
        post = form.save()
        action = self.request.POST['action']

        # 保存してもう一つ追加ボタンのとき
        if action == 'save_and_create':
            return redirect('app:create')

        # 保存して編集を続けるボタン
        elif action == 'save_and_update':
            return redirect('app:update', pk=post.pk)

        # それ以外、送信ボタン        
        else:
            return redirect('app:index')


class Update(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:index')

    def form_valid(self, form):
        post = form.save()
        action = self.request.POST['action']

        # 保存してもう一つ追加ボタンのとき
        if action == 'save_and_create':
            return redirect('app:create')

        # 保存して編集を続けるボタン
        elif action == 'save_and_update':
            return redirect('app:update', pk=post.pk)

        # それ以外、送信ボタン        
        else:
            return redirect('app:index')


class Delete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('app:index')
