import numpy as np
from matplotlib import pyplot as plt

with open("datafile.csv") as file_name:
    dataarray = np.loadtxt(file_name, delimiter=", ", skiprows=1)

count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
mwlist = [] #invariant mass from jets 1 and 2
mw13list = [] #mass of jets 1 and 3
mw23list = [] #mass of jets 2 and 3
j1masslist = []
j2masslist = []
B2masslist = []
j3masslist = []
B1masslist = []
alltopquarkmassarray= []
topquarkmasslist = [] #top quark from j1 and j2 and b2
topquarkmasslist0 = [] #top quark mass from muon and b1
topquarkmasslist1 = [] # top quark mass from j1j3 b2
topquarkmasslist2 = [] # top quark mass from j2j3 b2
topquarkmasslist3 = [] # top quark mass from j1j2b1
topquarkmasslist4 = [] # top quark mass from j2j3b1
topquarkmasslist5 = [] #top quark mass from j1j3b1

for line in dataarray:
    # 3 possibilities to pair  2 light jets:
    m12 = np.sqrt((line[13]+line[17])**2 - (line[14]+line[18])**2 - (line[15]+line[19])**2 - (line[16]+line[20])**2)/1000 # mass of the w+ boson using jet 1 and 2
    m13mass = np.sqrt((line[13]+line[21])**2 - (line[14]+line[22])**2 - (line[15]+line[23])**2 - (line[16]+line[24])**2)/1000
    m23mass = np.sqrt((line[17]+line[21])**2 - (line[18]+line[22])**2 - (line[19]+line[23])**2 - (line[20]+line[24])**2)/1000
    j1mass = np.sqrt((line[13])**2 - (line[14])**2 - (line[15])**2 - (line[16])**2)/1000
    j2mass = np.sqrt((line[17])**2 - (line[18])**2 - (line[19])**2 - (line[20])**2)/1000
    j3mass = np.sqrt((line[21]) ** 2 - (line[22]) ** 2 - (line[23]) ** 2 - (line[24]) ** 2) / 1000
    B1mass = np.sqrt((line[9])**2 - (line[10])**2 - (line[11])**2 - (line[12])**2)/1000
    B2mass = np.sqrt((line[5])**2 - (line[6])**2 - (line[7])**2 - (line[8])**2)/1000

    topquarkmass = np.sqrt((line[13]+line[17]+line[9])**2 - (line[14]+line[18]+line[10])**2 - (line[15]+line[19]+line[11])**2 - (line[16]+line[20]+line[12])**2)/1000
    topquarkmass1 = np.sqrt((line[13]+line[21]+line[9])**2 - (line[14]+line[22]+line[10])**2 - (line[15]+line[23]+line[11])**2 - (line[16]+line[24]+line[12])**2)/1000
    topquarkmass2 = np.sqrt((line[17]+line[21]+line[9])**2 - (line[18]+line[22]+line[10])**2 - (line[19]+line[23]+line[11])**2 - (line[20]+line[24]+line[12])**2)/1000
    topquarkmass3 = np.sqrt((line[13]+line[17]+line[5])**2 - (line[14]+line[18]+line[6])**2 - (line[15]+line[19]+line[7])**2 - (line[16]+line[20]+line[8])**2)/1000
    topquarkmass4 = np.sqrt((line[17]+line[21]+line[5])**2 - (line[18]+line[22]+line[6])**2 - (line[19]+line[23]+line[7])**2 - (line[20]+line[24]+line[8])**2)/1000
    topquarkmass5 = np.sqrt((line[13]+line[21]+line[5])**2 - (line[14]+line[22]+line[6])**2 - (line[15]+line[23]+line[7])**2 - (line[16]+line[24]+line[8])**2)/1000


    j1masslist.append(j1mass)
    j2masslist.append(j2mass)
    j3masslist.append(j3mass)
    B1masslist.append(B1mass)
    B2masslist.append(B2mass)

    if abs(m12-80)<40:
        mwlist.append(m12)
    if abs(m13mass-80)<40:
        mw13list.append(m13mass)
    if abs(m23mass-80)<40:
        mw23list.append(m23mass)


    if abs(m12-80)<40:
        if abs(B2mass-4.7)<2.35:
            if abs(j1mass-4.7)<2.35:
                if abs(j2mass-4.7)<2.35:
                    if topquarkmass<250:
                        topquarkmasslist.append(topquarkmass)
                        alltopquarkmassarray.append(topquarkmass)
                        count = count + 1
                        #print(j1mass)
                        #print(j2mass)
                        #print(topquarkmass)




    if abs(m13mass-80)<40:
        if abs(B2mass-4.7)<2.35:
            if abs(j1mass-4.7)<2.35:
                if abs(j3mass-4.7)<2.35:
                    if topquarkmass1<250:
                        topquarkmasslist1.append(topquarkmass1)
                        alltopquarkmassarray.append(topquarkmass1)

                        count1 = count1 + 1
                        #print('B2 mass is:', B2mass)
                        #print('j1 mass is:', j1mass)
                        #print('j3 mass is:', j3mass)
                        #print(topquarkmass1)


    if abs(m23mass-80)<40:
        if abs(B2mass-4.7)<2.35:
            if abs(j2mass-4.7)<2.35:
                if abs(j3mass-4.7)<2.35:
                    if topquarkmass2<250:
                        topquarkmasslist2.append(topquarkmass2)
                        alltopquarkmassarray.append(topquarkmass2)
                        count2 = count2 + 1
                        #print(j2mass)
                        #print(j3mass)
                        #print(topquarkmass2)

    if abs(m12-80)<40<= 40:
        if abs(B1mass-4.7)<2.35:
            if abs(j1mass-4.7)<2.35:
                if abs(j2mass-4.7)<2.35:
                    if topquarkmass3<250:
                        topquarkmasslist3.append(topquarkmass3)
                        alltopquarkmassarray.append(topquarkmass3)
                        count3 = count3 + 1
                        #print(j1mass)
                        #print(j2mass)
                        #print(topquarkmass3)

    if abs(m23mass-80)<40:
        if abs(B1mass-4.7)<2.35:
            if abs(j2mass-4.7)<2.35:
                if abs(j3mass-4.7)<2.35:
                    if topquarkmass4<250:
                        topquarkmasslist4.append(topquarkmass4)
                        alltopquarkmassarray.append(topquarkmass4)
                        count4 = count4 + 1
                        #print('B1 mass is:',B1mass)
                        #print('j2 mass is:',j2mass)
                        #print('j3 mass is:',j3mass)
                        #print(topquarkmass4)



    if abs(m13mass-80):
        if abs(B1mass-4.7)<2.35:
            if abs(j1mass-4.7)<2.35:
                if abs(j3mass-4.7)<2.35:
                    if topquarkmass5<250:
                        topquarkmasslist5.append(topquarkmass5)
                        alltopquarkmassarray.append(topquarkmass5)
                        count5 = count5 + 1
                        #print(j1mass)
                        #print(j3mass)
                        #print(topquarkmass5)



mean = np.mean(mwlist)
mean13mass = np.mean(mw13list)
mean23mass = np.mean(mw23list)
meanj1mass = np.mean(j1masslist)
meanj2mass = np.mean(j2masslist)
meanj3mass = np.mean(j3masslist)
meanB1mass = np.mean(B1masslist)
meanB2mass = np.mean(B2masslist)

meantopquarkmass = np.mean(topquarkmasslist)
meantopquarkmass1 = np.mean(topquarkmasslist1)
meantopquarkmass2 = np.mean(topquarkmasslist2)
meantopquarkmass3 = np.mean(topquarkmasslist3)
meantopquarkmass4 = np.mean(topquarkmasslist4)
meantopquarkmass5 = np.mean(topquarkmasslist5)
print('Mean of w boson from j1 and j2(selected): ', mean)
print('Mean of w boson from j1 and j3(selected): ', mean13mass)
print('Mean of w boson from j2 and j3(selected): ', mean23mass)
print('Mean j1 mass is(not selected): ', meanj1mass)
print('Mean j2 mass is(not selected): ', meanj2mass)
print('Mean j3 mass is(not selected): ', meanj3mass)
print('Mean B1 mass is(not selected): ', meanB1mass)
print('Mean B2 mass is(not selected): ', meanB2mass)

print('Mean top quark mass from j1j2b2 is(selected): ', meantopquarkmass)
print('Mean top quark mass from j1j3b2 is(selected): ', meantopquarkmass1)
print('Mean top quark mass from j2j3b2 is(selected): ', meantopquarkmass2)
print('Mean top quark mass from j1j2b1 is(selected): ', meantopquarkmass3)
print('Mean top quark mass from j2j3b1 is(selected): ', meantopquarkmass4)
print('Mean top quark mass from j1j3b1 is(selected): ', meantopquarkmass5)
meantopquarkmasses = (meantopquarkmass+meantopquarkmass1+meantopquarkmass2+meantopquarkmass3+meantopquarkmass4+meantopquarkmass5)/6 # calculates mean top quark mass from all combinations
print('mean top quark mass for all combinations:', meantopquarkmasses)

plt.hist(topquarkmasslist4, bins=14, range=(130,250),label="m(t) [GeV]")
plt.title('top quark masses from j2j3b1 ')
plt.xlabel("m(t) [GeV]")
plt.ylabel("No. of particles")
plt.show()


plt.hist(alltopquarkmassarray, bins=25, range=(130,250),label="m(t) [GeV]")
plt.title('Best top quarks masses')
plt.xlabel("m(t) [GeV]")
plt.ylabel("No. of particles")
plt.show()

print('number of selected events for j1j2b2:',count) # how many accepted masses through the selection
print('number of selected events for j1j3b2:',count1)
print('number of selected events for j2j4b2:',count2)
print('number of selected events for j1j2b1:',count3)
print('number of selected events for j2j3b1:',count4)
print('number of selected events for j1j3b1:',count5)


#this code calculates the best (i.e. the value closest to the literature value)top quark mass from all the selected combinations in our dataset
actualtopquarkmass = []
counter = 0
for mass in alltopquarkmassarray:
    if abs(mass - 172.5)<=4:
       actualtopquarkmass.append(mass)
       counter +=1

range = np.ptp(actualtopquarkmass)
uncertainty = (range)/2*(np.sqrt(counter))
meanmass = np.mean(actualtopquarkmass)
print('top quark mass is',meanmass,'pm',uncertainty)
print('Number of best top quark selections',counter)
