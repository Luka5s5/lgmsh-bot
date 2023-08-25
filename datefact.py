from datetime import datetime  
import requests

def factsoftheday():
    summ = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    mon =  datetime.now().month
    days = datetime.now().day
    if mon == 1:
        a = (summ[0] + days)
    if mon == 2:
        a = (summ[1] + days)
    if mon == 3:
        a = (summ[2] + days)
    if mon == 4:
        a = (summ[3] + days)
    if mon == 5:
        a = (summ[4] + days)
    if mon == 6:
        a = (summ[5] + days)
    if mon == 7:
        a = (summ[6] + days)
    if mon == 8:
        a = (summ[7] + days)
    if mon == 9:
        a = (summ[8] + days)
    if mon == 10:
        a = (summ[9] + days)
    if mon == 11:
        a = (summ[10] + days)
    if mon == 12:
        a = (summ[11] + days)

    s = "http://numbersapi.com/"
    u = a
    z = "/date"
    response = requests.get(s + str(u) + z)
    return response.text

if __name__ == '__main__':
    print(factsoftheday())
