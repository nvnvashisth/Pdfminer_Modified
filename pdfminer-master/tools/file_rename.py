base = "C:\\Users\\vnitin\\OneDrive - NetApp Inc\\IDP\\studysmarter-ml\\dataset_extractor\\"
for old_name in os.listdir(base):
    print(old_name)
    for path, course in zip(path_name,sub_name):
        if(old_name == path):
            os.rename(os.path.join(base, old_name), os.path.join(base, course))
            print(old_name,path,course)