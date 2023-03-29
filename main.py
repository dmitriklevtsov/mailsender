import smtplib
from dotenv import load_dotenv


str = """\n\nПривет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

link = 'https://dvmn.org/referrals/j1SL9wPFr8pdxzoHcDMPj103CwzjXh6vVUDEqwus'
friendname = 'info@gqdesign.gq'
myname = 'Petr'

str = str.replace('%website%', link)
str = str.replace('%friend_name%', friendname)
str = str.replace('%my_name%', myname)

letter = """From: {a}
To: {b}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";""".format(a=myname, b=friendname) + str

letter = letter.encode("UTF-8")

load_dotenv()

login = os.environ.get("LOGIN")
password = os.environ.get("PASSWORD")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(login, friendname, letter)
server.quit()
