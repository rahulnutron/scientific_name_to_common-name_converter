def convert(path = 'C:/Users/rahul/Google Drive/Work/important_R_codes/',specfile="speclist_uniprot.txt",outfile="Sci2Com.csv"):
    f = open(path+specfile,'r')
    fw = open(path+outfile,'w')
    dic = {}
    meta_list = []
    flag = 0
    for line in f:
        line = line.strip('\n')
        s = line.split()
        if len(s)>=4 and ':' in line and flag == 1:
            N = meta_list[0].split('N=')[1]
            dic[N] = ''
            for CorS in meta_list:
                if 'C=' in CorS:
                    dic[N] = CorS.split('C=')[1]
                if 'S=' in CorS and dic[N]=='':
                    dic[N] = CorS.split('S=')[1]
            meta_list = []
            flag = 0
                    
        if 'N=' in line and s[1] in ['A','B','E','V','O'] and flag == 0:
            meta_list.append(line)
            flag = 1
        if len(s) == 1 and flag == 1:
            meta_list.append(line)
    f.close()
    fw.write('Official (scientific) name,Common name\n')
    for N in dic:
        if dic[N]!='':
            fw.write(N+','+dic[N]+'\n')
    for N in dic:
        if dic[N]=='':
            fw.write(N+','+dic[N]+'\n')
    fw.close()
    return dic

#convert()
