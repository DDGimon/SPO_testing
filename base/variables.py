"""Укажите тестируемый и мастер стенд в формате как указано ниже

"Пример формата:
testing_stand = "https://interglossa.t12.test.eljur.tech"   слеш в конце не нужен"""


class Url:
    testing_stand = "https://ntptis.t12.test.eljur.tech"
    url_after_authorization = 'https://ntptis.t12.test.eljur.tech/?user=sysadmin&domain=ntptis'
    url_study_plan = 'https://ntptis.t12.test.eljur.tech/journal-study-action/s.plan/p.spo'
    url_add_plan = 'https://ntptis.t12.test.eljur.tech/journal-study-action/s.plan/p.spo/t.title?action=create'
