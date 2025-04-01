import os
vd ="" #"C:/Users/Euan/Downloads/dateien/"
class movingstuff(vd):
    lp, lt, lc = [], [], []
    dp, dt, dc = ["jpg", "png", "svg", "gif"], ["txt", "doc", "docx"], ["py", "bat", "exe"]
    pp, pt, pc, = "./Pictures", "./Text", "./Code"
    def sort(d,p):
        for x in os.listdir(vd):
            l = x.split(".")
            if d.__contains__(l[-1]):
                p.append(x) 

    def move(l,p):
        for x in l:
            os.rename(f"{vd}{x}", f"{p}/{x}")

    sort(dp, lp)        
    sort(dt, lt)
    sort(dc, lc)
    os.mkdir(pp)
    os.mkdir(pt)
    os.mkdir(pc)
    move(lp, pp)
    move(lt, pt)
    move(lc, pc)
