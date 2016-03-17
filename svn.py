import re
import os
import string
# str="A test.php"
# rs=re.findall("[M|A]\s+(.*)\n",str)
# print(rs)
# exit("over")
fp_ver=open("./svn_ver.txt","r+")
ver_last=fp_ver.read().rstrip("\n")
fp_ver.close()

if(ver_last==None or ver_last==""):
    ver_last=0

ver_last=int(ver_last)

print("ver_last:")
print(ver_last)
print("\n")

ver=os.popen("svn info svn://118.123.22.54/dinner |grep Revision: |cut -c11-").read()
ver=int(ver)
print("ver:")
print(ver)



# print(type(ver_last))
# print(type(ver))
# print("svn diff --summarize -r %d:%d svn://118.123.22.54/dinner" %(ver_last,ver))

svn_update_commands=os.popen("svn diff --summarize -r %d:%d svn://118.123.22.54/dinner" %(ver,ver_last)).read()

#
content=re.findall("[MA]\s+(.*)\n?",svn_update_commands)

if(len(content)>0):
    for file in content:
        abs_file=file.replace("svn://118.123.22.54/dinner","./../")
        svn_export_command="svn export %s %s" % (file,abs_file)
        print(svn_export_command)
        os.system(svn_export_command)

#record svn version
fp_ver=open("./svn_ver.txt","w+")
fp_ver.truncate()
fp_ver.write(str(ver))
fp_ver.close()

# for x in content:
#     print x



# fp=open("./svn.txt","r+")
# f=open("./svn_commands.sh","w+")
# f.truncate()
# for line in fp.readlines():
#     content=re.findall("M\s+(.*)$",line)
#     if(content.__len__()>=1):
#         path=content[0].replace("svn://xxxche.wicp.net/jobs/","/alidata/www/jobs/")
#         svn_line="svn export "+content[0]+" "+path
#         f.write(svn_line+"\n")
#     content=re.findall("A\s+(.*)$",line)
#     if(content.__len__()>=1):
#         path=content[0].replace("svn://xxxche.wicp.net/jobs/","/alidata/www/jobs/")
#         svn_line="svn export "+content[0]+" "+path
#         f.write(svn_line+"\n")


