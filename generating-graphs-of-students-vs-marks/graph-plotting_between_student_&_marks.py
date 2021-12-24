import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('student_marks.csv')
# df.plot()
# plt.show()
a='student1'
b='student2'
c='student3'
d='student4'
e='student5'

# plot1

xpoints = np.array([a, b,c,d,e])
ypoints = np.array([55,75,87,91,63])
plt.subplot(6,2,1)
plt.plot(xpoints, ypoints,'o--r',ms=10)
# plt.title("MATHS MARKS")
# plt.xlabel("STUDENTS")
plt.ylabel("Maths marks")

# bar1

x = np.array([a,b,c,d,e])
y = np.array([55,75,87,98,63])
plt.subplot(6,2,2)
plt.bar(x,y,width = 0.3,color = "hotpink")

# plot2

xpoints = np.array([a, b,c,d,e])
ypoints = np.array([65,45,97,69,84])
plt.subplot(6,2,3)
plt.plot(xpoints, ypoints,'o--b',ms=10)
# plt.title("ENGLISH MARKS")
# plt.xlabel("STUDENTS")
plt.ylabel("Eng marks")

# bar2

x = np.array([a,b,c,d,e])
y = np.array([65,45,97,69,84])
plt.subplot(6,2,4)
plt.bar(x,y,width = 0.3,color = "hotpink")

# Plot3

xpoints = np.array([a, b,c,d,e])
ypoints = np.array([45,70,37,78,87])
plt.subplot(6,2,5)
plt.plot(xpoints, ypoints,'o--g',ms=10)
# plt.title("HINDI MARKS")
# plt.xlabel("STUDENTS")
plt.ylabel("Hindi marks")

# bar3

x = np.array([a,b,c,d,e])
y = np.array([45,70,37,78,87])
plt.subplot(6,2,6)
plt.bar(x,y,width = 0.3,color = "hotpink")

# Plot4

xpoints = np.array([a, b,c,d,e])
ypoints = np.array([30,89,76,45,92])
plt.subplot(6,2,7)
plt.plot(xpoints, ypoints,'o--y',ms=10)
# plt.title("SCIENCE MARKS")
# plt.xlabel("STUDENTS")
plt.ylabel("Sci. marks")

# bar4

x = np.array([a,b,c,d,e])
y = np.array([30,89,76,45,92])
plt.subplot(6,2,8)
plt.bar(x,y,width = 0.3,color = "hotpink")

# Plot5

xpoints = np.array([a, b,c,d,e])
ypoints = np.array([96,89,97,94,99])
plt.subplot(6,2,9)
plt.plot(xpoints, ypoints,'o--b',ms=10)
# plt.title("SST MARKS")
# plt.xlabel("STUDENTS")
plt.ylabel("Sst marks")

# bar5

x = np.array([a,b,c,d,e])
y = np.array([96,89,97,94,99])
plt.subplot(6,2,10)
plt.bar(x,y,width = 0.3,color = "hotpink")

# Plot6

xpoints = np.array([a, b,c,d,e])
ypoints = np.array([74,75,87,56,71])
plt.subplot(6,2,11)
plt.plot(xpoints, ypoints,'o--b',ms=10)
# plt.title("COMPUTER MARKS")
# plt.xlabel("STUDENTS")
plt.ylabel("Com. marks")

# bar6

xpoints = np.array([a, b,c,d,e])
ypoints = np.array([74,75,87,56,71])
plt.subplot(6,2,12)
plt.bar(x,y,width = 0.3,color = "hotpink")










plt.subplots_adjust(left=0.125,
                    bottom=0.08, 
                    right=0.9, 
                    top=0.92, 
                    wspace=0.2, 
                    hspace=0.55)


plt.show()
