from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import ApplicantForm, ContactForm
from .models import Applicant, Contact

# Create your views here.
context = {}

steps = {
    'step1': {
        'title': 'Шаг 1: Встреча в аэропорту и сопровождение', 
        'text1': '''Представители нашей фирмы помогут Вам с подбором билетов до аэропорта Дюссельдорфа или Кёльна (Федеральная земля Северный Рейн-Вестфалия) 
                    и организуют встречу в день Вашего прилёта. Далее мы доставим Вас в место временного пребывания, где Вы сможете поесть, отдохнуть 
                    и принять душ с дороги.''',
        'text2': '''Под местом временного пребывания подразумевается отдельная комната у одного из наших волонтёров, 
                    в немецкой семье или обычный хостел.''',
        'imgpath': '/landing/images/greeting.svg'
        },
    'step2': {
        'title': 'Шаг 2: Подготовка необходимых документов', 
        'text1': '''После Вашего приезда мы поможем Вам собрать полный пакет документов. Пока Вы отдыхаете, мы займёмся переводами на немецкий. 
                    В идеале всё, что должно быть переведено, можно заранее выслать нам по электронной почте.'''
                    ,
        'list': ['(обязательно) паспорт с действующей шенгенской визой',
                '(обязательно) заявление на получение убежища на немецком языке с датой и подписью заявителя',
                '(обязательно) краткая биография в виде таблицы, содержащая информацию о месте проживания, учебе и работе за последние 10 лет',
                'распечатка банковского счёта',
                'свидетельство о браке',
                'свидетельство о рождении',
                'диплом об образовании',
                'военный билет'],
        'imgpath': '/landing/images/docs.svg'
        },
    'step3': {
        'title': 'Шаг 3: Подача заявления на убежище', 
        'text1': '''Как только все документы будут готовы, наши сотрудники в зависимости от Вашего местоположения пойдут с Вами в ближайшее ведомство 
                    по делам иностранцев (Ausländeramt) или сразу отправятся с Вами в пункт приёма беженцев в городе Bochum (NRW). Там происходит 
                    подача документов и сдача отпечатков пальцев.''',
        'text2': '''''',
        'imgpath': '/landing/images/asylum.svg'
        },
    'step4': {
        'title': 'Шаг 4: Оформление жилья и соцпомощи', 
        'text1': '''Поскольку скорее всего у Вас не будет своего жилья в Германии, либо знакомых, которые смогут Вас принять, мы оформим Вам бесплатное 
                    социальное жильё, в котором Вы сможете жить, пока идёт рассмотрение заявки на получение убежища. У Вас будет полная свобода перемещения. 
                    Единственные два ограничения: обязательство ночевать в социальном жилье и запрет на пересечение границы Германии, пока идёт процесс оформления убежища.''',
        'text2': '''Также, до окончания процесса подачи, который может затянуться на несколько недель, у Вас не будет права на работу. Поэтому, мы оформим Вам социальную помощь, 
                    которую Германия предоставляет всем нуждающимся. На август 2022 года размер соцпомощи составляет 360 евро на человека в месяц. Помимо этого, будут бесплатно 
                    предоставлены медицинская страховка и горячее питание.''',
        'imgpath': '/landing/images/money.svg'
        },
    'step5': {
        'title': 'Шаг 5: Получение статуса беженца', 
        'text1': '''При правильной подаче документов с помощью наших юристов, в среднем процесс получения убежища может занять от 2 до 6 недель. Длительность зависит 
                    от количества заявителей, а также от пакета документов.''',
        'text2': '''Как только процесс подачи будет завершен, Вы получите разрешение на работу, а также немецкий документ для поездок, с которым Вы сможете 
                    передвигаться по миру наравне с гражданами Германии. Социальная помощь (360 евро в месяц на человека + компенсация арендной платы) будет 
                    Вам сохранена до Вашего трудоустройства. Также Вы получите возможность посещать курсы немецкого языка.''',
        'imgpath': '/landing/images/success.svg'
        },
}

services = [
    {'title': 'Юридическая консультация',   'text': 'Если у Вас есть вопросы или нужна помощь квалифицированных специалистов - запишитесь на онлайн консультацию, и мы Вам поможем!'},
    {'title': 'Перевод денег в/из России',  'text': 'Срочно нужно вывести большую сумму денег из России? Мы Вам поможем! Хотите отправить деньги родственникам? Это мы тоже делаем.'},
    {'title': 'Поиск работы',               'text': 'Если Вы находитесь в поиске работы, но пока не знаете, как и где ее искать - поручите это дело нам.'},
    {'title': 'Признание диплома',          'text': 'У Вас иностранный диплом и Вы хотите работать в Германии? Мы поможем Вам его признать в кратчайшие сроки.'},
    {'title': 'Подбор языковых курсов',     'text': 'Хотите улучшить свой немецкий или же выучить его с нуля? Мы подберем для Вас качественную и недорогую языковую школу с индивидуальным графиком занятий.'},
    {'title': 'Получение образования',      'text': 'Хотите получить образование в Германии? Мы поможем Вам поступить в немецкий вуз или получить профессиональное техническое образование.'},
    {'title': 'Поиск долгосрочного жилья',  'text': 'Ищете себе жилье, но пока не можете его найти? Не беда, мы знаем - как!'},
    {'title': 'Покупка недвижимости',       'text': 'Хотите инвестировать в немецкую недвижимость? Мы поможем Вам с юридическим оформлением и переводами.'},
    {'title': 'Регистрация брака',          'text': 'Хотите заключить брак в Германии или же хотите признать в Германии свой иностранный брак? Мы подскажем, как.'},
]
  
context['steps'] = steps
context['services'] = services


def render_home(request):
    context["navbar"] = "home"
    return render(request, 'landing/home.html', context)


def render_services(request):
    context["navbar"] = "services"
    return render(request, 'landing/services.html', context)


def render_about(request):
    context["navbar"] = "about"
    return render(request, 'landing/about.html', context)


def render_contact(request):
    context["navbar"] = "contact"
    return render(request, 'landing/contact.html', context)


def render_quote(request):
    return render(request, 'landing/quote.html', context)

def render_thankyou(request):
    context = {}
    return render(request, "landing/thankyou.html", context)


class CreateApplicant(CreateView):
    form_class = ApplicantForm
    model = Applicant
    template_name = "landing/quote.html"
    success_url = "/thankyou"

class CreateContact(CreateView):
    form_class = ContactForm
    model = Contact
    template_name = "landing/contact.html"
    success_url = "/thankyou"