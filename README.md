projeto seletive da imersão pylab
criar uma rota para uma app (facil)
para exibir um html é necessário usar templates e para começar é configurado o path no arquivo settings na lista TEMPLATES[ DIR[] ]
    BASE_DIR é uma variavel que o django cria para nós que referencia a raiz do projeto


quando cria uma model e quer que ela vá pra area do ADMIN precisa cadastrar ela no arquivo admin do APP
    - from .models import <nome das classes>f

MODEL 
    no model o campo: models.ManyToManyField, armazena em um campo várias informações

FORM em empresas: <form action="" method="" enctype="multipart/form-data">
    - o enctype é para enviar a logo  atraves do formulário


aula 1 parou no tempo 1:35:00

getlist em VIEWS request.POST.get()    #get list
    para pegar valores de campos com multiplos valores como listas é necessário usar request.POST.getlist

FOR num linha 
    x = [i[0] for i in Empresa.choices_nicho_mercado]
    print('o' in x and 'N' in x and 'M' in x)


CRIAR TAGS
    primeiro cria uma pastas templatetags no app
    cria arquivo filtro.py
    importa template
    registra o template

    cria funcão no caso foi verificar se numero é impar ou par

    dentro de settings/templates/options cria um dicionario dentro da lista
        'libraries':{
            'filtro': 'empresa.templatetags.filtro'
        }

video parou no 2:27h

para exibir imagens no empresa_unica é necessario fazer import de 
    #import para urls de imagem da logo dos clientes em empresa_unica
   
    from django.conf import settings
    from django.conf.urls.static import static

criar uma url no cor do projeto, ex:
no settings da raiz 
    """
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    """
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


em select no template empresa_unica para exibir corretamente choices_nicho_mercado é necessario adicionar no html os seguinte codigo:
    <input disabled type="text" class="form-control" value="{{empresa.get_nicho_mercado_display}}">

    explicando: quando tem um campo choices (varias possibilidas) o django cria para a gente no model um get caracteristicas
        o GET sempre vai existir e no fianl o DISPLAY  também




aula parou no 57:59 minutos
