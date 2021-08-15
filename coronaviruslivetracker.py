import requests
from bs4 import BeautifulSoup
import plyer
def datacollected():
    def notification(title,message):
        plyer.notification.notify(
        title=title,
        message=message,
        #app_icon="covid.jpg",
        timeout = 15
        )

    url = "https://www.worldometers.info/coronavirus/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    tbody = soup.find('tbody')
    abc = tbody.find_all('tr')
    countrynotification = cntdata.get()
    #we will keep world as by default when no country is entered
    if(countrynotification==""):
        countrynotification="world"
    serial_number, countries, total_cases, new_cases, total_death, new_death, total_recovered,active_cases=[],[],[],[],[],[],[],[]
    serious_critical,total_cases_permn,total_death_pernm,total_tests,total_test_permillion,total_pop=[],[],[],[],[],[]

    header = ['serial_number', 'countries', 'total_cases', 'new_cases', 'total_death', 'new_death', 'total_recovered',
          'active_cases', 'serious_critical', 'total_cases_permn', 'total_death_pernm', 'total_tests',
          'total_test_permillion',
          'total_pop']


    for i in abc:
        id = i.find_all('td')
        if(id[1].text.strip().lower() == countrynotification):
            totalcases1 = id[2].text.strip().replace(',',"")
            totaldeath = id[4].text.strip()
            newcases = id[3].text.strip()
            newdeath = id[5].text.strip()
            notification("corona recent updates{}".format(countrynotification), "total cases{}\ntotal death:{}\nnew cases:{}\nnew death:{}".format(
            totalcases1,totaldeath,newcases,newdeath))
    serial_number.append(id[0].text.strip())
    countries.append(id[1].text.strip())
    total_cases.append(id[2].text.strip().replace(',',"")) #remove comma bw numbers
    new_cases.append(id[3].text.strip())
    total_death.append(id[4].text.strip())
    new_death.append(id[5].text.strip())
    total_recovered.append(id[6].text.strip())
    active_cases.append(id[7].text.strip())
    serious_critical.append(id[8].text.strip())
    total_cases_permn.append(id[9].text.strip())
    total_death_pernm.append(id[10].text.strip())
    total_tests.append(id[11].text.strip())
    total_pop.append(id[12].text.strip())
    total_pop.append(id[13].text.strip())

from tkinter import*
coro = Tk()
coro.title("corona virus Information")
coro.geometry('800x500+200+100')
coro .configure(bg='#046173')
   #coro.iconbitmap('corona.ico') #download only ico files

# #Labels
mainlabel = Label(coro,text='corona virus Live Tracker',font=("Times 20 bold",30,"bold"),bg ='#05897A',width=33,
fg="black",bd=5 )
mainlabel.place(x=0,y=0)

label1= Label(coro,text='Country Name',font=("arial",20,"italic bold"),bg ='#05857A')
label1.place(x=15,y=100)

label2 = Label(coro,text='Download File',font=("arial",20,"italic bold"), bg ='#05297A' )

label2.place(x=15,y=200)

cntdata = StringVar()
entry1 = Entry(coro, textvariable = cntdata ,font = ("arial",20,"italic bold"), relief = RIDGE,bd = 2 , width = 32)
entry1.place(x = 280,y = 100)

# ##Buttons

Inhtml = Button(coro,text="Html", bg='#2DAE9A',font = ("arial",15,"italic bold"),relief=RIDGE,activebackground = "#05945B",
 activeforeground="white",bd=5,width=5)
Inhtml.place(x=300,y=200)

Injson=  Button(coro,text="json", bg='#2DAE9A',font = ("arial",15,"italic bold"),relief=RIDGE,activebackground = "#05945B",
 activeforeground="white",bd=5,width=5)
Injson.place(x=300, y=260)

Inexcel=  Button(coro,text="Excel", bg='#2DAE9A',font = ("arial",15,"italic bold"),relief=RIDGE,activebackground = "#05945B",
 activeforeground="white",bd=5,width=5)
Inexcel.place(x=300,y=320)


Submit=  Button(coro,text="submit", bg='#2DCE9A',font = ("arial",15,"italic bold"),relief=RIDGE,activebackground = "#05945A",
 activeforeground="white",bd=5,width=5,command = datacollected)
Submit.place(x=450,y=260)


coro.mainloop()
