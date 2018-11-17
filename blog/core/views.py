from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from templated_email import send_templated_mail

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by('-created_date')
        return context


#padrão de código(dar dois enters para criação de outra view)
def ContactView(request):
    if request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        #print(name)
        #print(email)
        #print(mensagem)
        send_templated_mail (
            template_name='email',
            from_email='email',
            recipient_list=['tmrp@cin.ufpe.br'],
            context={
                'nome': name,
                'email': email, 
                'mensagem': mensagem,
            }
        )
        return HttpResponseRedirect(reverse_lazy('home'))

    return(render(request, 'contact.html'))
    