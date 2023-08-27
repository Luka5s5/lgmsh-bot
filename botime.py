from datetime import datetime
from zoneinfo import ZoneInfo

def get_next_event():

    d={}
    d[(8,45)]="Линейка"
    d[(9,15)]="Завтрак"
    d[(10,0)]="Первая пара"
    d[(11,45)]="Вторая пара"
    d[(13,20)]="Обед"
    d[(14,15)]="Третья пара"
    d[(16,30)]="Клубы: первая волна"
    d[(17,55)]="Клубы: вторая волна"
    d[(19,20)]="Ужин"
    d[(19,40)]="Вечернее мероприятие"
    
    current_time=datetime.now(tz=ZoneInfo("Asia/Omsk"))
    h,m = current_time.hour, current_time.minute
    n_e="Линейка"
    h1=0
    m1=0
    f=1
    for i in d:
        now=h*60+m
        next_time=i[0]*60+i[1]
        if(next_time>now):
            f=0
            h1=(next_time-now)//60
            m1=(next_time-now)%60
            n_e=d[i]
            break

    if(f):
        return (n_e+"в 8:45") 
    else:
        return (n_e+" через "+str(h1)+"h "+str(m1)+"min")

