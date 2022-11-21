a = 100000000
listdata = []
bulan = 1

def bunga(n,t):
        bunga = (a*n)/100
        listdata.append(bunga)
        print(f"bunga bulan ke - {t} = {bunga}")

while bulan < 10:
            if bulan == 1:
                      bunga(0,bulan)
            if bulan == 2:
                      bunga(0,bulan)
            if bulan == 3:
                      bunga(1,bulan)
            if bulan == 4:
                      bunga(1,bulan)
            if bulan == 5:
                      bunga(5,bulan)
            if bulan == 6:
                      bunga(5,bulan)
            if bulan == 7:
                      bunga(5,bulan)
            if bulan == 8:
                      bunga(2,bulan)
            bulan +=1