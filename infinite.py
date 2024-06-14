import platform
import psutil
import cpuinfo
import wmi
print("Architecture: ",platform.architecture())
print("Network Name: ",platform.node())
print("Operating System: ",platform.platform())
print("Processor: ",platform.processor())

my_CPUinfo=cpuinfo.get_cpu_info()
#print(my_CPUinfo)        #Full dictionary
print("Full CPU Name: ",my_CPUinfo['brand_raw'])
print("Full CPU Name: ",my_CPUinfo['hz_actual_friendly'])
print("Full CPU Name: ",my_CPUinfo['hz_advertised_friendly'])
#print(cpuinfo.get_cpu_info().keys())
print("Total RAM: ",psutil.virtual_memory().total/1024/1024/1024,"GB")

pc=wmi.WMI()
os_info=pc.Win32_OperatingSystem()[0]
print(os_info)
print(pc.Win32_Processor()[0].name)
print(pc.Win32_VideoController()[0].name)
s=input(fontstyle.apply("ENTER TO EXIT","bold/Broadway/violet/YELLOW_BG"))
exit()
'''from turtle import *
color('green')
bgcolor('black')
speed(60)
right(45)
for i in range(150):
    if 7<i<62:
        left(5)
    if 80<i<133:
        right(5)
    circle(30)
    if i<80:
        forward(10)
    else:
        forward(5)'''
