import tkinter as tk
import random
import math

def t0(vec):
    return vec[0]=='0'
def t1(vec):
    return vec[len(vec)-1]=='1'
def smf(st1,st2):
    iss=True
    for i in range(len(st2)):
        if st1[i]>st2[i]:
            return False
    return iss
def mono(vec):
    dim=int(math.log2(len(vec)))
    ismono=True
    for i in range(len(vec)-1):
        for j in range(i+1,len(vec)):
            if vec[i]>vec[j]:
                if smf(format(i,'b').rjust(dim,'0'),format(j,'b').rjust(dim,'0'))==True:
                    return False
    return ismono
def sd(vec):
    sd=True
    dim=int(math.log2(len(vec)))
    if dim==0:
        return False
    else:
        for i in range(len(vec)//2):
            if vec[i]==vec[len(vec)-1-i]:
                return False
    return sd
def lin(vec):
    dim=int(math.log2(len(vec)))
    if dim==0:
        return True
    else:
        bf=vec
        koef=[]
        koef.append(bf[0])
        while(len(bf)>1):
            v=''
            for i in range(len(bf)-1):
                if bf[i]!=bf[i+1]:
                    v=v+'1'
                else:
                    v=v+'0'
            bf=v
            koef.append(bf[0])
        for i in range(len(koef)):
            if koef[i]=='1':
                if format(i,'b').rjust(dim,'0').count('1')>1:
                    return False
    return True

def runn0(event):

    def makef(event):
        strf=''
        dim=var.get()
        for i in range(2**int(dim)):
            strf=strf+str(random.randint(1,100)%2)
        f.delete(0,tk.END)
        f.insert(0,strf)
    
    window=tk.Tk()
    window.geometry('300x200')
    var=tk.Entry(master=window)
    var.pack()
    btn=tk.Button(master=window,text='OK')
    btn.bind('<Button-1>',makef)
    btn.pack()
    f=tk.Entry(master=window,width=65)
    f.pack()
    window.mainloop()

def runn1(event):
    def ost(event):
        v=vec.get()
        n=int(var.get())
        dim=1
        while 2**dim<len(v):
            dim+=1
        s=[]   
        step=len(v)//(2**n)                     
        for i in range(0,len(v),len(v)//(2**n)):
            s.append(v[i:step])
            step+=int(len(v)/(2**n))

        ansW=""

        if zoo.get()=='0':
            for i in range(0,len(s),2):
                ansW+=s[i]
        else:
            for i in range(1,len(s),2):
                ansW+=s[i]
        answ2.delete(0,tk.END)
        answ2.insert(0,ansW)
        
    window=tk.Tk()
    window.geometry('300x200')

    d1=tk.Label(master=window,text='вектор')
    vec=tk.Entry(master=window)
    d1.grid(row=0,column=0,sticky="e")
    vec.grid(row=0,column=1)

    d2=tk.Label(master=window,text='0/1')
    zoo=tk.Entry(master=window)
    d2.grid(row=1,column=0,sticky="e")
    zoo.grid(row=1,column=1)

    d3=tk.Label(master=window,text='n')
    var=tk.Entry(master=window)
    d3.grid(row=2,column=0,sticky="e")
    var.grid(row=2,column=1)

    btn=tk.Button(master=window,text='OK')
    btn.bind('<Button-1>',ost)
    btn.grid(row=3)

    d4=tk.Label(master=window,text='остаточная')
    answ2=tk.Entry(master=window)
    d4.grid(row=4,column=0,sticky="e")
    answ2.grid(row=4,column=1)
    
    window.mainloop()

def runn2(event):
    def fost(event):
        ost0=o0.get()
        ost1=o1.get()
        n=int(var.get())
        s=[]
        step = int(len(ost0)/2**(n-1))
        for i in range(0,len(ost0),int(len(ost0)/2**(n-1))):
            s.append(ost0[i:step])
            s.append(ost1[i:step])
            step+=int(len(ost0)/2**(n-1))
        ansW = ""
        for i in s:
            ansW=ansW+i    
        answ.delete(0,tk.END)
        answ.insert(0,ansW)
    
    window=tk.Tk()
    window.geometry('300x200')

    d1=tk.Label(master=window,text='ост0')
    o0=tk.Entry(master=window)
    d1.grid(row=0,column=0,sticky="e")
    o0.grid(row=0,column=1)

    d2=tk.Label(master=window,text='ост1')
    o1=tk.Entry(master=window)
    d2.grid(row=1,column=0,sticky="e")
    o1.grid(row=1,column=1)

    d3=tk.Label(master=window,text='n')
    var=tk.Entry(master=window)
    d3.grid(row=2,column=0,sticky="e")
    var.grid(row=2,column=1)

    btn=tk.Button(master=window,text='OK')
    btn.bind('<Button-1>',fost)
    btn.grid(row=3)

    d4=tk.Label(master=window,text='функция')
    answ=tk.Entry(master=window)
    d4.grid(row=4,column=0,sticky="e")
    answ.grid(row=4,column=1)    
    
    window.mainloop()

def runn3(event):
    lib={
        "0000":"тождественный ноль",
        "0001":"конъюнкция",
        "0010":"НЕ импликация",
        "0011":"икс",
        "0100":"НЕ обратная импликация",
        "0101":"игрек",
        "0110":"сумма Жегалкина",
        "0111":"дизъюнкция",
        "1000":"стрелка Пирса",
        "1001":"эквивалентность",
        "1010":"НЕ игрек",
        "1011":"обратная импликация",
        "1100":"НЕ икс",
        "1101":"импликация",
        "1110":"штрих Шеффера",
        "1111":"тождественная единица"
        }
    f=[format(a,'b').rjust(4,'0') for a in range(16)]
    random_f=random.sample(f,k=4)
    random_answ=lib[random_f[0]]
    def clicked(event):
        if event.widget['text']==random_answ:
            l3['bg']='lightgreen'
        else:
            l3['bg']='red'
    def newtask(event):
        nonlocal random_f
        random_f=random.sample(f,k=4)
        nonlocal random_answ
        random_answ=lib[random_f[0]]
        l3['text']=random_f[0]
        l3['bg']='snow'
        random.shuffle(random_f)
        for i in range(4):
            btn[i]['text']=lib[random_f[i]]
    
    window = tk.Tk()

    title=tk.Frame(master=window)
    l3=tk.Label(master=title,text=random_f[0],bg='snow')
    l3.pack()
    title.grid(row=1,column=0)

    random.shuffle(random_f)

    btn=[]
    frm=[]
    for i in range(4):
        frm.append(tk.Frame(master=window))
        frm[i].grid(row=2,column=i)
        btn.append(tk.Button(master=frm[i],text=lib[random_f[i]],width=20))
        btn[i].bind("<Button-1>",clicked)
        btn[i].pack()

    ntplace=tk.Frame(master=window)
    ntplace.grid(row=1,column=3)
    newt=tk.Button(master=ntplace,text="новый пример",width=20)
    newt.bind("<Button-1>",newtask)
    newt.pack()

    window.mainloop()


def runn4(event):

    def foi():
        v=vec.get()
        dim=1
        ansW=''
        while 2**dim<len(v):
            dim+=1
        for i in range(1,dim+1):
            s=[]
            step=int(len(v)/(2**i))
            for j in range(0,len(v),int(len(v)/(2**i))):
                s.append(v[j:step])
                step+=int(len(v)/(2**i))
            f0=""
            f1=""
            for j in range(0,len(s)-1):
                f0+=s[j]
                f1+=s[j+1]
            if f0==f1:
                ansW=ansW+'переменная x'+str(i)+' фиктивная\n'
            else:
                ansW=ansW+'переменная x'+str(i)+' существенная\n'
        answ.delete('1.0',tk.END)
        answ.insert('1.0',ansW)
    
    window=tk.Tk()
    window.geometry('400x300')
    d1=tk.Label(master=window,text='вектор')
    vec=tk.Entry(master=window,width=70)
    d1.pack()
    vec.pack()
    btn=tk.Button(master=window,text="OK",command=foi)
    btn.pack()
    answ=tk.Text(master=window)
    answ.pack()
    window.mainloop()

def runn5(event):

    def chd(event):
        def absorption(ssdnf,impl):
            bf=True
            for i in range(len(impl)):
                if impl[i]!='-' and impl[i]!=ssdnf[i]:
                    bf=False
            return bf
        vv=v.get()
        dim=int(math.log2(len(vv)))
        eq=dnf.get()
        eq=eq.replace('x','')
        eq=eq.replace(' ','')
        leq=eq.split('v')
        limp=[]
        for i in leq:
            ss='-'.rjust(dim,'-')
            sss=''
            negan=False
            for j in i:
                if j=='-':
                    negan=True
                else:
                    if negan:
                        for u in range(len(ss)):
                            if u!=int(j)-1:
                                sss=sss+ss[u]
                            else:
                                sss=sss+'0'
                        negan=False
                    else:
                        for u in range(len(ss)):
                            if u!=int(j)-1:
                                sss=sss+ss[u]
                            else:
                                sss=sss+'1'
            limp.append(sss)
        sdnf=set()
        for i in range(len(vv)):
            if vv[i]=='1':
                sdnf=sdnf.union({format(i,'b').rjust(dim,'0')})
        for i in limp:
            for j in sdnf:
                if absorption(j,i):
                    sdnf=sdnf-{j}
        if len(sdnf)==0:
            event.widget['bg']='green'
        else:
            event.widget['bg']='red'
            
                
    
    window=tk.Tk()
    window.geometry('300x200')
    rdim=random.randint(0,2)
    vec=format(random.randint(0,2**(2**rdim)-1),'b').rjust(2**rdim,'0')
    v=tk.Entry(master=window)
    v.pack()
    v.insert(0,vec)
    dnf=tk.Entry(master=window)
    dnf.pack()
    btn=tk.Button(master=window,text='OK',width=10,heigh=5)
    btn.bind('<Button-1>',chd)
    btn.pack()
    window.mainloop()

def runn6(event):
    def chk(event):
        def absorption(ssdnf,impl):
            bf=True
            for i in range(len(impl)):
                if impl[i]!='-' and impl[i]!=ssdnf[i]:
                    bf=False
            return bf
        vv=v.get()
        dim=int(math.log2(len(vv)))
        eq=dnf.get()
        eq=eq.replace('(','')
        eq=eq.replace(')','')
        eq=eq.replace(' ','')
        eq=eq.replace('x','')
        eq=eq.replace('+','')
        leq=eq.split('*')
        print(leq)
        limp=[]
        for i in leq:
            ss='-'.rjust(dim,'-')
            sss=''
            negan=False
            for j in i:
                print(j)
                if j=='-':
                    negan=True
                else:
                    if negan:
                        for u in range(len(ss)):
                            if u!=int(j)-1:
                                sss=sss+ss[u]
                            else:
                                sss=sss+'1'
                        negan=False
                    else:
                        for u in range(len(ss)):
                            if u!=int(j)-1:
                                sss=sss+ss[u]
                            else:
                                sss=sss+'0'
            limp.append(sss)
        sknf=set()
        for i in range(len(vv)):
            if vv[i]=='0':
                sknf=sknf.union({format(i,'b').rjust(dim,'0')})
        for i in limp:
            for j in sknf:
                if absorption(j,i):
                    sknf=sknf-{j}
        if len(sknf)==0:
            event.widget['bg']='green'
        else:
            event.widget['bg']='red'
                
    window=tk.Tk()
    window.geometry('300x200')
    rdim=random.randint(0,2)
    vec=format(random.randint(0,2**(2**rdim)-1),'b').rjust(2**rdim,'0')
    v=tk.Entry(master=window)
    v.pack()
    v.insert(0,vec)
    dnf=tk.Entry(master=window)
    dnf.pack()
    btn=tk.Button(master=window,text='OK',width=10,heigh=5)
    btn.bind('<Button-1>',chk)
    btn.pack()
    window.mainloop()

def runn7(event):
    def makesdnf(event):
        v=vec.get()
        dim=int(math.log2(len(v)))
        ssdnf=[]
        for i in range(len(v)):
            if v[i]=='1':
                ssdnf.append(format(i,'b').rjust(dim,'0'))
        answl=[]
        for i in ssdnf:
            bf=''
            for j in range(len(i)):
                if i[j]=='0':
                    bf=bf+'-X'+str(j+1)
                else:
                    bf=bf+'X'+str(j+1)
            answl.append(bf)
        sdnf.delete(0,tk.END)
        sdnf.insert(0,' v '.join(answl))
    window=tk.Tk()
    window.geometry('400x200')
    vec=tk.Entry(master=window)
    vec.pack()
    btn=tk.Button(master=window,text='OK')
    btn.bind('<Button-1>',makesdnf)
    btn.pack()
    sdnf=tk.Entry(master=window,width=65)
    sdnf.pack()
    window.mainloop()

def runn8(event):
    def makesknf(event):
        v=vec.get()
        dim=int(math.log2(len(v)))
        ssdnf=[]
        for i in range(len(v)):
            if v[i]=='0':
                ssdnf.append(format(i,'b').rjust(dim,'0'))
        answl=[]
        for i in ssdnf:
            bf=''
            bff=[]
            for j in range(len(i)):
                if i[j]=='0':
                    bff.append('X'+str(j+1))
                else:
                    bff.append('-X'+str(j+1))
            bf='('+'v'.join(bff)+')'
            answl.append(bf)
        sknf.delete(0,tk.END)
        sknf.insert(0,'&'.join(answl))
    window=tk.Tk()
    window.geometry('400x200')
    vec=tk.Entry(master=window)
    vec.pack()
    btn=tk.Button(master=window,text='OK')
    btn.bind('<Button-1>',makesknf)
    btn.pack()
    sknf=tk.Entry(master=window,width=65)
    sknf.pack()
    window.mainloop()

def runn9(event):

    def is0(event):
        if t0(vec):
            event.widget['bg']='green'
        else:
            event.widget['bg']='red'
                    
    def is1(event):
        if t1(vec):
            event.widget['bg']='green'
        else:
            event.widget['bg']='red'

    def ismono(event):
        if mono(vec):
            event.widget['bg']='green'
        else:
            event.widget['bg']='red'
    
    def issd(event):
        if sd(vec):
            event.widget['bg']='green'
        else:
            event.widget['bg']='red'

    def islin(event):
        if lin(vec):
            event.widget['bg']='green'
        else:
            event.widget['bg']='red'
    
    window=tk.Tk()
    window.geometry('300x200')
    rdim=random.randint(0,2)
    vec=format(random.randint(0,2**(2**rdim)-1),'b').rjust(2**rdim,'0')
    lvec=tk.Label(master=window,text=vec)
    lvec.grid(row=0)

    bt0=tk.Button(master=window,text='сохраняет 0')
    bt1=tk.Button(master=window,text='сохраняет 1')
    btmono=tk.Button(master=window,text='монотонная')
    btsd=tk.Button(master=window,text='самодвойственная')
    btlin=tk.Button(master=window,text='линейная')
    bt0.bind('<Button-1>',is0)
    bt1.bind('<Button-1>',is1)
    btmono.bind('<Button-1>',ismono)
    btsd.bind('<Button-1>',issd)
    btlin.bind('<Button-1>',islin)
    bt0.grid(row=1,column=0)
    bt1.grid(row=1,column=1)
    btmono.grid(row=1,column=2)
    btsd.grid(row=2,column=0)
    btlin.grid(row=2,column=1)
    
    window.mainloop()

def runn10(event):
    def isf(event):
        d=dict()
        vt=[]
        vt=entry.get().split()
        d['t0']=set()
        d['t1']=set()
        d['mono']=set()
        d['sd']=set()
        d['lin']=set()
        for i in vt:
            if t0(i):
                d['t0']=d['t0'].union({i})
            if t1(i):
                d['t1']=d['t1'].union({i})
            if mono(i):
                d['mono']=d['mono'].union({i})
            if sd(i):
                d['sd']=d['sd'].union({i})
            if lin(i):
                d['lin']=d['lin'].union({i})
        isfull='ПОЛНЫЙ'
        for i in d:
            if d[i]==set(vt):
                isfull='НЕ ПОЛНЫЙ'  
        if event.widget['text']=='ПОЛНЫЙ':
            if isfull=='ПОЛНЫЙ':
                event.widget['bg']='green'
            else:
                event.widget['bg']='red'
        else:
            if isfull=='НЕ ПОЛНЫЙ':
                event.widget['bg']='green'

                def is0(event):
                    if d['t0']==set(vt):
                        event.widget['bg']='green'
                    else:
                        event.widget['bg']='red'
                    
                def is1(event):
                    if d['t1']==set(vt):
                        event.widget['bg']='green'
                    else:
                        event.widget['bg']='red'

                def ismono(event):
                    if d['mono']==set(vt):
                        event.widget['bg']='green'
                    else:
                        event.widget['bg']='red'
    
                def issd(event):
                    if d['sd']==set(vt):
                        event.widget['bg']='green'
                    else:
                        event.widget['bg']='red'

                def islin(event):
                    if d['lin']==set(vt):
                        event.widget['bg']='green'
                    else:
                        event.widget['bg']='red'
                
                wnd=tk.Tk()
                bt0=tk.Button(master=wnd,text='сохраняют 0')
                bt1=tk.Button(master=wnd,text='сохраняют 1')
                btmono=tk.Button(master=wnd,text='монотонные')
                btsd=tk.Button(master=wnd,text='самодвойственные')
                btlin=tk.Button(master=wnd,text='линейные')
                bt0.bind('<Button-1>',is0)
                bt1.bind('<Button-1>',is1)
                btmono.bind('<Button-1>',ismono)
                btsd.bind('<Button-1>',issd)
                btlin.bind('<Button-1>',islin)
                bt0.pack()
                bt1.pack()
                btmono.pack()
                btsd.pack()
                btlin.pack()
                wnd.mainloop()
            else:
                event.widget['bg']='red'
            
                
    window=tk.Tk()
    window.geometry('300x200')
    hmv=random.randint(1,3)
    vec=[]
    for i in range(hmv):
        rdim=random.randint(0,2)
        vec.append(format(random.randint(0,2**(2**rdim)-1),'b').rjust(2**rdim,'0'))
    title=tk.Label(master=window,text='НАБОР БФ')
    entry=tk.Entry(master=window)
    entry.delete(0,tk.END)
    entry.insert(0,' '.join(vec))
    title.pack()
    entry.pack()
    pole=tk.Frame(master=window)
    pole.pack()
    b1=tk.Frame(master=pole)
    b1.grid(row=0,column=0)
    b2=tk.Frame(master=pole)
    b2.grid(row=0,column=1)
    btp=tk.Button(master=b1,text='ПОЛНЫЙ')
    btp.bind('<Button-1>',isf)
    btp.pack()
    btn=tk.Button(master=b2,text='НЕ ПОЛНЫЙ')
    btn.bind('<Button-1>',isf)
    btn.pack()
    window.mainloop()

def runn11(event):
    def makemin(event):
        class mc:
            def __str__(self):
                return self.imp
            def __hash__(self):
                return hash(str(self))
            def __eq__(self, other):
                return self.imp==other.imp
            def __init__(self,imp):
                self.imp=imp
                self.canskley=False
            def __len__(self):
                return len(self.imp)
        def sortdict(dict_):
            s_t=sorted(dict_.items(),key=lambda x: -len(x[1]))
            return dict(s_t)
        def skley(st1,st2):
            a=mc(st1)
            b=mc(st2)
            bf=mc('')
            diff=0
            for i in range(len(st1)):
                if st1[i]!=st2[i]:
                    if diff==0:
                        bbf=st1
                        bbf=bbf[:i]+'-'+bbf[i+1:]
                        bf.imp=bbf
                        diff+=1
                    else:
                        return(mc(''))
            return bf
        def absorption(ssdnff,impl):
            bf=True
            for i in range(len(impl.imp)):
                if impl.imp[i]!='-' and impl.imp[i]!=ssdnff.imp[i]:
                    bf=False
            return bf
        def hmv(set_):
            hv=0
            for i in set_:
                hv+=i.imp.count('0')
                hv+=i.imp.count('1')
            return hv
        vec=vect.get()
        dim=int(math.log2(len(vec)))
        func={}
        sdnf=[]
        for i in range(len(vec)):
            func[format(i,'b').rjust(dim,'0')]=vec[i]
            if vec[i]=='1':
                sdnf.append(mc(format(i,'b').rjust(dim,'0')))

        ssdnf=sorted(sdnf,key=lambda x: x.imp.count('1'))

        oneos=[]
        bb=[]
        bb.append(ssdnf[0])
        oneos.append(bb)
        grp=0
        for i in range(1,len(ssdnf)):    
            if ssdnf[i].imp.count('1')== oneos[grp][0].imp.count('1'):
                oneos[grp].append(ssdnf[i])
            else:
                bf=[]
                bf.append(ssdnf[i])
                grp+=1
                oneos.append(bf)
        implicant=[]
        while(True):
            buffer=[]
            for i in range(len(oneos)-1):
                for j in range(len(oneos[i])):
                    for k in range(len(oneos[i+1])):    
                        if skley(oneos[i][j].imp,oneos[i+1][k].imp).imp!='':
                            bf=mc(skley(oneos[i][j].imp,oneos[i+1][k].imp).imp)
                            oneos[i][j].canskley=True
                            oneos[i+1][k].canskley=True
                            buffer.append(bf)
            buffer=list(set(buffer))
            buffer.sort(key=lambda x: x.imp.count('1'))
            for i in oneos:
                for j in i:
                    if j.canskley==False:
                        implicant.append(j)
                implicant=list(set(implicant))
            implicant.sort(key=lambda x: x.imp.count('1'))
            if buffer==[]:
                break
            else:
                for i in buffer:
                    i.canskley=False
                oneos=[]
                bb=[]
                bb.append(buffer[0])
                oneos.append(bb)
                grp=0
                for i in range(1,len(buffer)):
                    if buffer[i].imp.count('1')== oneos[grp][0].imp.count('1'):
                        oneos[grp].append(buffer[i])
                    else:
                        bf=[]
                        bf.append(buffer[i])
                        grp+=1
                        oneos.append(bf)
        ssdnf=set(ssdnf)
        implicant.sort(key=lambda x: x.imp.count('1'))

        imtos=dict()
        for i in implicant:
            bf=set()
            for j in ssdnf:
                if absorption(j,i):
                    bf=bf.union({j})
            imtos[i]=bf
        over=[]
        mindnf=set(implicant)
        for i in range(2**len(implicant)):
            over.append(format(i,'b').rjust(len(implicant),'0'))
        for i in over:
            bf=set()
            impvar=set()
            for j in range(len(i)):
                if(i[j]=='1'):
                    bf=bf.union(imtos[implicant[j]])
                    impvar=impvar.union({implicant[j]})
            if bf==ssdnf:
                if hmv(impvar)<hmv(mindnf):
                    mindnf=impvar
            
        mindnf=list(mindnf)
        answ=[]
        for i in mindnf:
            bf='1'
            for j in range(len(i.imp)):
                if i.imp[j]=='0':
                    bf=bf+'-X'+str(j+1)
                if i.imp[j]=='1':
                    bf=bf+'X'+str(j+1)
            if bf!='1':
                bf=bf.replace('1','', 1)
                answ.append(bf)
        ansW=' v '.join(answ)
        aw.delete(0,tk.END)

        aw.insert(0,ansW)
        
    window=tk.Tk()
    window.geometry("400x170")
    title=tk.Label(master=window,text='Минимизация ДНФ')
    vect=tk.Entry(master=window,width=50)
    title.pack()
    vect.pack()
    btn=tk.Button(master=window,text='ОК')
    btn.bind("<Button-1>",makemin)
    btn.pack()
    aw=tk.Entry(master=window,width=65)
    aw.pack()
    window.mainloop()

######################
window=tk.Tk()
window.geometry("400x300")

frame = tk.Frame(master=window, width=500, height=500,bg="cyan")
frame.pack()

btn=[]
for i in range(12):
    btn.append(tk.Button(master=frame,text="Задача "+str(i+1), width=10,height=5,bg="lightgreen"))
    btn[i].grid(row=int(i/4),column=i%4,padx=5, pady=5)
btn[0].bind("<Button-1>", runn0)
btn[1].bind("<Button-1>", runn1)
btn[2].bind("<Button-1>", runn2)
btn[3].bind("<Button-1>", runn3)
btn[4].bind("<Button-1>", runn4)
btn[5].bind("<Button-1>", runn5)
btn[6].bind("<Button-1>", runn6)
btn[7].bind("<Button-1>", runn7)
btn[8].bind("<Button-1>", runn8)
btn[9].bind("<Button-1>", runn9)
btn[10].bind("<Button-1>", runn10)
btn[11].bind("<Button-1>", runn11)

window.mainloop()
