import numpy as np
import math
import os

from numpy.core.fromnumeric import size
np.set_printoptions(threshold=np.inf)

T = 150
req_num = 100
users = np.array(
    [[1001, 1, 1], [1002, 1, 1], [1003, 0, 1], [1004, 1, 1], [1005, 1, 1], [1006, 1, 1], [1007, 0, 1], [1008, 1, 1],
     [1009, 0, 1], [1010, 1, 1], [1011, 1, 1], [1012, 1, 1], [1013, 1, 1], [1014, 1, 1], [1015, 1, 1], [1016, 1, 1],
     [1017, 1, 1], [1018, 1, 1], [1019, 0, 1], [1020, 1, 1],
     [3001, 0, 0], [3002, 0, 0], [3003, 1, 0], [3004, 0, 0], [3005, 1, 0], [3006, 0, 0], [3007, 0, 0], [3008, 0, 0],
     [3009, 1, 0], [3010, 1, 0], [3011, 0, 0], [3012, 0, 0], [3013, 1, 0], [3014, 0, 0], [3015, 1, 0], [3016, 0, 0],
     [3017, 1, 0], [3018, 0, 0], [3019, 1, 0], [3020, 0, 0], [3021, 1, 0], [3022, 1, 0], [3023, 0, 0], [3024, 0, 0],
     [3025, 0, 0], [3026, 1, 0], [3027, 0, 0], [3028, 0, 0], [3029, 1, 0], [3030, 0, 0]])

drivers = np.array([[1001, 41, 65, 0],
                    [1002, 69, 13, 0],
                    [1003, 24, 56, 0],
                    [1004, 94, 5, 0],
                    [1005, 22, 25, 0],
                    [1006, 43, 90, 0],
                    [1007, 63, 60, 0],
                    [1008, 16, 17, 0],
                    [1009, 67, 61, 0],
                    [1010, 88, 9, 0],
                    [1011, 91, 61, 0],
                    [1012, 16, 80, 0],
                    [1013, 27, 38, 0],
                    [1014, 9, 85, 0],
                    [1015, 46, 55, 0],
                    [1016, 42, 65, 0],
                    [1017, 43, 15, 0],
                    [1018, 73, 87, 0],
                    [1019, 38, 67, 0],
                    [1020, 89, 10, 0]])

trips = np.array([[11111, 3018, 1, 94, 93, 37, 67],
                  [11112, 3004, 3, 3, 6, 13, 50],
                  [11113, 3013, 3, 95, 89, 12, 20],
                  [11114, 3004, 7, 37, 67, 84, 96],
                  [11115, 3012, 9, 58, 93, 30, 85],
                  [11116, 3017, 13, 5, 70, 18, 93],
                  [11117, 3017, 14, 6, 42, 97, 53],
                  [11118, 3022, 14, 5, 98, 89, 48],
                  [11119, 3019, 15, 36, 55, 40, 50],
                  [11120, 3025, 15, 38, 45, 3, 50],
                  [11121, 3014, 17, 50, 69, 14, 1],
                  [11122, 3011, 18, 51, 66, 16, 25],
                  [11123, 3012, 21, 16, 3, 57, 53],
                  [11124, 3026, 22, 4, 8, 75, 48],
                  [11125, 3001, 22, 91, 94, 84, 29],
                  [11126, 3001, 22, 22, 65, 23, 26],
                  [11127, 3001, 23, 7, 95, 83, 28],
                  [11128, 3008, 25, 56, 30, 70, 76],
                  [11129, 3026, 25, 39, 88, 22, 26],
                  [11130, 3030, 28, 94, 5, 10, 10],
                  [11131, 3013, 28, 64, 48, 62, 26],
                  [11132, 3025, 29, 15, 48, 95, 53],
                  [11133, 3002, 29, 73, 19, 93, 26],
                  [11134, 3022, 30, 29, 83, 65, 27],
                  [11135, 3011, 30, 39, 66, 50, 46],
                  [11136, 3013, 31, 85, 33, 46, 39],
                  [11137, 3013, 35, 4, 81, 1, 23],
                  [11138, 3004, 38, 50, 60, 36, 29],
                  [11139, 3025, 38, 4, 18, 56, 33],
                  [11140, 3011, 43, 41, 24, 5, 90],
                  [11141, 3024, 44, 42, 64, 81, 90],
                  [11142, 3012, 46, 15, 31, 66, 11],
                  [11143, 3001, 47, 15, 98, 7, 9],
                  [11144, 3009, 47, 59, 84, 99, 51],
                  [11145, 3023, 49, 60, 98, 73, 93],
                  [11146, 3023, 52, 16, 48, 50, 17],
                  [11147, 3007, 52, 18, 2, 51, 72],
                  [11148, 3007, 52, 45, 58, 72, 40],
                  [11149, 3017, 53, 42, 40, 49, 24],
                  [11150, 3013, 57, 93, 33, 32, 59],
                  [11151, 3003, 57, 8, 51, 78, 20],
                  [11152, 3020, 59, 64, 36, 6, 13],
                  [11153, 3014, 59, 2, 74, 17, 96],
                  [11154, 3020, 60, 59, 78, 86, 23],
                  [11155, 3023, 60, 82, 79, 66, 35],
                  [11156, 3009, 63, 70, 51, 13, 2],
                  [11157, 3016, 64, 86, 58, 94, 76],
                  [11158, 3030, 64, 32, 9, 39, 70],
                  [11159, 3030, 65, 97, 38, 43, 59],
                  [11160, 3017, 68, 24, 17, 67, 16],
                  [11161, 3005, 70, 82, 29, 22, 86],
                  [11162, 3011, 72, 73, 56, 84, 73],
                  [11163, 3026, 72, 45, 64, 4, 14],
                  [11164, 3002, 74, 52, 89, 99, 31],
                  [11165, 3028, 75, 13, 60, 43, 99],
                  [11166, 3014, 75, 57, 14, 27, 62],
                  [11167, 3014, 75, 5, 87, 49, 47],
                  [11168, 3003, 78, 74, 70, 36, 95],
                  [11169, 3012, 80, 12, 51, 1, 90],
                  [11170, 3011, 82, 4, 63, 9, 90],
                  [11171, 3008, 83, 4, 19, 88, 61],
                  [11172, 3014, 83, 72, 78, 95, 80],
                  [11173, 3012, 86, 64, 84, 90, 60],
                  [11174, 3008, 89, 34, 35, 77, 61],
                  [11175, 3010, 91, 88, 10, 76, 75],
                  [11176, 3006, 92, 28, 20, 46, 91],
                  [11177, 3007, 92, 94, 27, 71, 43],
                  [11178, 3024, 94, 55, 77, 64, 39],
                  [11179, 3027, 95, 88, 67, 66, 47],
                  [11180, 3026, 96, 12, 32, 69, 2],
                  [11181, 3009, 96, 26, 60, 82, 75],
                  [11182, 3008, 97, 62, 9, 29, 13],
                  [11183, 3009, 97, 42, 85, 92, 71],
                  [11184, 3018, 101, 45, 98, 19, 91],
                  [11185, 3015, 107, 4, 13, 81, 96],
                  [11186, 3008, 108, 18, 14, 22, 81],
                  [11187, 3002, 109, 21, 80, 96, 48],
                  [11188, 3027, 111, 60, 12, 99, 48],
                  [11189, 3030, 111, 23, 36, 86, 45],
                  [11190, 3006, 112, 18, 62, 13, 39],
                  [11191, 3002, 117, 15, 76, 58, 52],
                  [11192, 3021, 118, 55, 94, 10, 87],
                  [11193, 3014, 119, 48, 47, 88, 58],
                  [11194, 3025, 122, 32, 60, 93, 94],
                  [11195, 3017, 123, 75, 19, 43, 64],
                  [11196, 3004, 123, 47, 72, 18, 7],
                  [11197, 3016, 123, 66, 35, 53, 68],
                  [11198, 3015, 125, 68, 65, 49, 88],
                  [11199, 3028, 127, 29, 69, 7, 23],
                  [11200, 3029, 130, 15, 84, 58, 3],
                  [11201, 3027, 130, 36, 22, 70, 52],
                  [11202, 3013, 131, 31, 3, 84, 9],
                  [11203, 3020, 140, 65, 16, 87, 45],
                  [11204, 3001, 141, 97, 8, 36, 24],
                  [11205, 3017, 142, 71, 17, 22, 16],
                  [11206, 3020, 143, 66, 53, 76, 42],
                  [11207, 3018, 144, 39, 20, 54, 94],
                  [11208, 3007, 146, 60, 83, 60, 2],
                  [11209, 3023, 147, 43, 24, 75, 42],
                  [11210, 3018, 148, 36, 94, 63, 92]])

def diste(x1,y1,x2,y2):         # mohasebe masahate oghlidosi
    z = abs(x1-x2)+abs(y1-y2)
    return(z)

def distm(x1,y1,x2,y2):         # mohasebe masahate manhatan
    z = np.sqrt((x1-x2)**2+(y1-y2)**2)
    return(z)

def time(t,d):                  # mohasebe zamane safar
    z = ((math.sin(t/1000)*0.016)+0.08)*d
    return(z)

def price(s,t):         # s mokhafafe start yani zamane shorooe safar
    z = (((math.ceil(math.cos(s/12)))*50)+200)*t
    return(z)

def takhsis(dri,tr,method,us):
    driver_attr = np.zeros((np.size(tr[:,2]),6),np.int64) # sakhte 6 sotoon az sefr ha be tedade satr haye trips
    tr = np.hstack((tr,driver_attr))        # afzoodane sotoone code ranandeو hazine safar, zamane safar va masafat be matrise trips
    times = tr[:,2]                         # sotoon zaman haye darkhast
    avail_t = dri[:,-1]                     # sotoon zaman haye bikar shodane ranande ha
    user_attr = np.zeros((np.size(users[:,0]),2),np.int64) # sakhte 2 sotoon az sefr ha be tedade satr haye users
    us = np.hstack((us,user_attr))      # afzoodane sotoone code hazine va msafate tajamoyi har karbar
    dim_1 = np.arange(50).reshape(50,1)     # tarife yek baze az 0 ta 50 baraye mokhtasat
    print(dim_1)
    for i in range(tr.shape[0]):            # i barabare shomare satr haye matris safar
        avail_dr = avail_t <= times[i]      # avail_dr yek matrise T/F ke ranande haye bikar ra baraye oon safar neshoon mide
        avail_dr_loc = dri[:,:][avail_dr]      # avail_dr_loc shamele location ranandehaye bikar hast
        if np.size(avail_dr_loc,0) == 0 :
            continue
        if method == 'e':
            trip_distance = diste(tr[i,3],tr[i,4],tr[i,5],tr[i,6])                 # mohasebe masafate safar
            distances = diste(avail_dr_loc[:,1],avail_dr_loc[:,2],tr[i,3],tr[i,4]) # mohasebe fasele ranande haye dar dastras az mabda
        else:
            trip_distance = distm(tr[i,3],tr[i,4],tr[i,5],tr[i,6])                 # mohasebe masafate safar
            distances = distm(avail_dr_loc[:,1],avail_dr_loc[:,2],tr[i,3],tr[i,4]) # mohasebe fasele ranande haye dar dastras az mabda
        min_distance = np.min(distances) # peyda kardane fasleye nazdiktarin ranande ba mosafer
        the_driver = np.where(distances==min_distance)
        tr[i,-2] = avail_dr_loc[the_driver[0],0][0]  # qarar dadane code ranande dar matrise safar
        trip_time = time(tr[i,2],trip_distance) # mohasebe zamane safar
        tr[i,-1] = price(tr[i,2],trip_time)  # mohasebe va qarar dadane hazine safar dar matrise safar
        tr[i,-3] = trip_time                 # qarar dadane time safar dar yek sotoone jadid az matrise safar
        tr[i,-4] = trip_distance             # qarar dadane toole safar dar yek sotoone jadid az matrise safar
        dri[np.where(dri[:,0]==tr[i,-2]),-1] = dri[np.where(dri[:,0]==tr[i,-2]),-1] + trip_time # mohasebe va jayegozarie zamane bikarie baadie ranande
        dri[np.where(dri[:,0]==tr[i,-2]),1] = tr[i,5]   # jayegozari location jadide ranande
        dri[np.where(dri[:,0]==tr[i,-2]),2] = tr[i,6]   # jayegozari location jadide ranande
        us[np.where(us[:,0]==tr[i,1]),-1] = us[np.where(us[:,0]==tr[i,1]),-1] + trip_time # mohasebe va jayegozarie zamane safare tajamoyi mosafer
        us[np.where(us[:,0]==tr[i,-2]),-1] = us[np.where(us[:,0]==tr[i,-2]),-1] + trip_time # mohasebe va jayegozarie zamane safare tajamoyi ranande
        us[np.where(us[:,0]==tr[i,1]),-2] = us[np.where(us[:,0]==tr[i,1]),-2] + trip_distance # mohasebe va jayegozarie masafate safare tajamoyi mosafer
        us[np.where(us[:,0]==tr[i,-2]),-2] = us[np.where(us[:,0]==tr[i,-2]),-2] + trip_distance # mohasebe va jayegozarie masafate safare tajamoyi ranande
        if tr[i,3] in dim_1:            # tayiine mantaghe mabda va maqsad baraye har darkhast
            if tr[i,4] in dim_1:
                tr[i,-6] = 1
            else:
                tr[i,-6] = 4
        else:
            if tr[i,4] in dim_1:
                tr[i,-6] = 2
            else:
                tr[i,-6] = 3
        if tr[i,5] in dim_1:            # tayiine mantaghe mabda va maqsad baraye har darkhast
            if tr[i,6] in dim_1:
                tr[i,-5] = 1
            else:
                tr[i,-5] = 4
        else:
            if tr[i,6] in dim_1:
                tr[i,-5] = 2
            else:
                tr[i,-5] = 3
    return tr,us

command = 0
dis_method = input('pleas choose how you want to calculate the distance: euclidean: e  manhatan: m\n ')
while dis_method !='e' and dis_method !='m':
    print('the method that you have enterd is not definde, enter again: ')
    dis_method = input('\npleas choose how you want to calculate the distance: for euqlides enter e for manhatan enter m\n ')

trr,uss = takhsis(drivers,trips,dis_method,users)
print(trr)

while command != 'q':
    trips_number=np.shape(trips)[0]
    print('\nto know about data input formats, refer to the trr matrix (which will be printed automatically.)',
            '\nplease choose a report ',
           ' \nTrip Matrix at Time: 1',
           '\nCumulative Revenue at Time: 2',
           '\nGolden Customer: 3',
           '\nMost Active Driver: 4',
           '\nMost Expensive Trip: 5',
           '\nLost Demand Percentage: 6',
           '\nGeographical Demand Distribution: 7',
           '\nA-to-C Traveler: 8')
    command = input('\npleas enter a command number:  ')
    os.system('cls'or'clear')
    if command == '1':
        intended_time = int(input('\nenter the time that you want to be reported: '))
        if np.size(np.where(trr[:,2]==intended_time)) == 0:
            print('there was no trips in that time\n')
            continue
        mask = np.array([1,1,1,1,1,1,1,0,0,0,0,1,1],dtype=bool)
        report_time = trr[np.ix_(trr[:,2]==intended_time,mask)]  # az ix_ baraye tarkibe 2 array boolean estefade shode ast
        print(report_time)
    elif command == '2':
        intended_time = int(input('enter the time that you want to be reported: '))
        mask = np.array([1,1,1,1,1,1,1,0,0,0,0,1,1],dtype=bool)
        report_time = trr[np.ix_(trr[:,2]<intended_time,mask)]  # az ix_ baraye tarkibe 2 array boolean estefade shode ast
        print('\033[92m','the commulative income until time:%s is: '%intended_time)
        print(np.sum(report_time[:,-1]),'\033[0m')
    elif command == '3':
        customers = uss[uss[:,2]==0,:]
        golden_cus = customers[customers[:,-1]==np.max(customers[:,-1]),:]
        print('\033[92m','\nthe golden customer is user number   %s'%(golden_cus[0,0]))
        print('the comulative trip time for this user is:  ',golden_cus[0,-1],'\033[0m','\n')
    elif command == '4':
        drivers_history = uss[uss[:,2]==1,:]
        golden_dri = drivers_history[drivers_history[:,-2]==np.max(drivers_history[:,-2]),:]
        print('\033[92m','\nthe golden driver is user number   %s'%(golden_dri[0,0]))
        print('the comulative trip distance for this driver is:  ',golden_dri[0,-2],'\033[0m','\n')
    elif command == '5':
        done_trips = trr[trr[:,-2]!=0,:]
        most_expensive = done_trips[done_trips[:,-1]==np.max(done_trips[:,-1]),:]
        print('\033[92m','\nthe id of the most expensive trip is:',most_expensive[0,0])
        print('time: ',most_expensive[0,2],'\033[0m','\n')
    elif command == '6':
        lost_demands = np.sum(trr[:,-2]==0)
        lost_percent = (lost_demands/(trips_number))*100
        print('\033[92m','\n',lost_percent,'%','of demands were lost!','\033[0m','\n')
    elif command == '7':
        demnad_a = ((np.sum(trr[:,-6]==1)/(trips_number)))*100
        print('\033[92m','\npecentage of trips in district A: ',demnad_a,'\033[0m')
        demnad_b = ((np.sum(trr[:,-6]==2)/(trips_number)))*100
        print('\033[92m','pecentage of trips in district B: ',demnad_b,'\033[0m')
        demnad_c = ((np.sum(trr[:,-6]==3)/(trips_number)))*100
        print('\033[92m','pecentage of trips in district C: ',demnad_c,'\033[0m')
        demnad_d = ((np.sum(trr[:,-6]==4)/(trips_number)))*100
        print('\033[92m','pecentage of trips in district D: ',demnad_d,'\033[0m','\n')
    elif command == '8':
        mabda = input('enter the begining area: ')
        if mabda == 'a'or mabda =='A':
            start = trr[trr[:,-6]==1,:]
        elif mabda == 'b'or mabda =='B':
            start = trr[trr[:,-6]==2,:]
        elif mabda == 'c'or mabda =='C':
            start = trr[trr[:,-6]==3,:]
        elif mabda == 'd'or mabda =='D':
            start = trr[trr[:,-6]==4,:]
        else:
            print('this area does not exist!')
            start = np.array([0])

        maghsad = input('enter the destination area: ')
        if maghsad == 'a' or maghsad == 'A':
            start_finish = start[start[:,-5]==1,1]
        elif maghsad == 'b'or maghsad =='B':
            start_finish = start[start[:,-5]==2,1]
        elif maghsad == 'c'or maghsad =='C':
            start_finish = start[start[:,-5]==3,1]
        elif maghsad == 'd'or maghsad =='D':
            start_finish = start[start[:,-5]==4,1]
        else:
            print('this area does not exist!')
            start = np.array([0])
        if np.size(start) == 1:
            start_finish = np.array([0])
            print('\nthere were no trips from %s to %s'%(mabda,maghsad))
        else:
            binc = np.bincount(start_finish)
            id = np.argmax(binc)
            print('\033[92m','\nuser id:')
            print(id)
            print('number of trips:')
            print(np.max(binc),'\n','\033[0m')

    else:
        print('the command is wrong!!!\ntry again')
        continue
