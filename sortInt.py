
from sys import argv
script, name_input, name_output = argv
f_read = open(name_input, "r")
t_read = f_read.read()
f_read.close()
print "File Input co noi dung : ", t_read
print "\n"
t_read=t_read.split(" ")
for i in range(0,len(t_read)):
    t_read[i]=int(t_read[i])
for i in range(0,len(t_read)):
    for j in range(i+1,len(t_read)):
        if(t_read[i]>t_read[j]):
            tam = t_read[i]
            t_read[i]=t_read[j]
            t_read[j]=tam
print "Day so nguyen duoc sap tang dan : ", t_read
f_write = open(name_output, "w")
f_write.truncate()
t_read = str(t_read)
t=f_write.write(t_read)
f_write.close()

    
