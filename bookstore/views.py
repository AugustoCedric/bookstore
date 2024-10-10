from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import git
import os


@csrf_exempt
def update(request):
    if request.method == "POST":
        # Especifique o caminho do diretório onde seu projeto está armazenado
        repo_path = '/home/augustocedric/bookstore'

        # Verifica se o diretório existe antes de tentar usar o git.Repo
        if not os.path.exists(repo_path):
            return HttpResponse("Diretório do repositório não encontrado.", status=404)

        try:
            repo = git.Repo(repo_path)
            origin = repo.remotes.origin
            origin.pull()  # Atualiza o repositório com as alterações remotas
            return HttpResponse("Código atualizado com sucesso no PythonAnywhere.")
        except Exception as e:
            return HttpResponse(f"Erro ao atualizar o código: {str(e)}", status=500)
    else:
        return HttpResponse("Método não permitido. Use POST para atualizar o código.", status=405)


def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')  # Certifique-se de que o arquivo home.html existe
    return HttpResponse(template.render())