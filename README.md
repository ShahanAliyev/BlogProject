# BlogProject

env faylı yaradılmalıdır

pip install -r requirements.txt

.env faylı yaradılmalıdır və aşağıdakı hissələr əlavə olunmalıdır.

.env faylında sonuncu key weather apidan gələn keydir

POSTGRES_DB = Blog_db

POSTGRES_USER = sahan

POSTGRES_HOST = db

POSTGRES_PORT = 5432

POSTGRES_PASSWORD = 123

DEBUG=False

key = '97a718f8f6ef703241dbb3b5c06afff0'

docker-compose up -d --build

docker -ps a

c_id =  IMAGE-də blogproject_webin qarşısındakı CONTAINER ID götürülür

docker exec -it  c_id bash

python manage.py migrate

python manage.py createsuperuser (superuserin username-i shahan olsa məqsədəuyğundur about us hissəsi üçün mütləqdir)

python manageşpy runserver

localhost-da proyekt açılır

Admin paneldə superuser üçün ad soyad əlavə olunmalıdır.

About us üçün
admin paneldə Custom User hissəsinə userə aid məlumatlar əlavə olmalıdır, 
admin paneldə categories, blogs hissələri doldurulmalıdır. 
Bir neçə category və blog əlavə etsəz filtrləmələri də görə bilərsiz. 
Əlavə olaraq sağ yuxarıda search hissəsində blogun header və ya textinə görə axtarış mümkündür. Custom filter hissəsində oxunma sayına və yaranma vaxtına görə filterləmələr tətbiq etmişəm (Bu arada hər bloga daxil olanda həmin blogun oxunma sayı 1 vahid artır). 
Digər şeylər taskda qeyd olunan formada işləyir.