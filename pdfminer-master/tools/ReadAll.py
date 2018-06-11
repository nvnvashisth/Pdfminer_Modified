import os

#thisdir=[os.path.join(r,file) for r,d,f in os.walk("C:\\Users\\vnitin\\OneDrive - NetApp Inc\\IDP\\Files\\") for file in f]
thisdir=[os.path.join(r,file) for r,d,f in os.walk("C:\\Users\\vnitin\\Documents\\Dataset\\") for file in f]
#print(test)
read_pdf_content = []
for i in range(len(thisdir)):
    text_path = thisdir[i].replace('pdf', 'txt')
    #print(text_path)
    #print(thisdir[i])
    #read_pdf_content = os.system("py ./pdf2txt.py {0}".format(thisdir[i]))
    os.system("py ./pdf2txt.py -o {0} {1}".format(text_path,thisdir[i]))
    print("Success",text_path, thisdir[i])
    #subprocess.call(["py", "-l"])  