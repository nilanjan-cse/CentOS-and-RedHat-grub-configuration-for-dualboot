import os
temp=os.popen("blkid | grep -i 'System Reserved'")
result=temp.read()
UUID=''
for i in result.split(" ")[3]:
	if i!='U' and i!='I' and i!='D' and i!='"' and i!='=':
		UUID=UUID+str(i)

print "UUID Number: ",UUID

with open("/etc/grub.d/40_custom","r+") as bootfile:
	bootfile.write('menuentry "Windows10" {\n')
	bootfile.write('insmod part_msdos')
	bootfile.write('insmod ntfs')
	bootfile.write("set root='(hd0,msdos1)'\n")
	string="search --no-floppy --fs-uuid --set=root "+UUID+"\n"
	bootfile.write(string)
	bootfile.write("chainloader +1 \n")

bootfile.close()

os.system("grub2-mkconfig -o /etc/grub2/grub.cfg")
