from glob import glob

'''
Created By PALAK 
This file is for creating train images list in model -> annotations

'''

def train_img_list(path):
    files = glob(path+'/xmls/*')
    train_list = [i.split('\\')[-1].replace('.xml','')+'\n' for i in files]
    train_list[-1] = train_list[-1].replace('\n','')
    with open(path +"/train_list.txt",'w+') as f :
        f.writelines(train_list)