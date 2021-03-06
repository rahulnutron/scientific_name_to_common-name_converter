def convert(path = 'C:/Users/rahul/',specfile="speclist.txt",outfile="Sci2Com.csv",writefile=True):
    f = open(path+specfile,'r')
    if writefile:
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
    if writefile:
        fw.write('Official (scientific) name,Common name\n')
        for N in dic:
            if dic[N]!='':
                fw.write(N+','+dic[N]+'\n')
        for N in dic:
            if dic[N]=='':
                fw.write(N+','+dic[N]+'\n')
        fw.close()

    dic_rev = {dic[N]:N for N in dic}

    return dic, dic_rev


def concise_fasta_header(repeat_entry = True,keep_des=True,spaceOrUnderscore = ' ',path='C:/Users/rahul/Teaching/',d_file = 'Human_HBB-Alignment-Descriptions.csv',f_file='seqdump_human_HBB_homolog.fas',outfile='human_HBB_homolog.fas'):
    dic = {}
    des_file = open(path+d_file,'r')
    fas_file = open(path+f_file,'r')
    fw = open(path+outfile,'w')
    for line in des_file:
        line = line.replace('"','')
        s = line.split(',')
        if len(s)>1:
            dic[s[1]] = s[2]
    des_file.close()
    sn_list = []
    gd, revgd = convert(writefile=False)
    dk = dic.keys()
    for N in gd:
        if N not in dk:
            dic[N] = gd[N]
    for line in fas_file:
        if repeat_entry:
            if '>' in line:
                line = line.strip('\n')
                s = line.split('[')
                N = s[-1:][0].strip('[]')
                #print s
                if keep_des:
                    pid = s[0].strip('[]')
                else:
                    pid = s[0].split()[0].strip('[]')
                if N in dic.keys() and dic[N]!='NA':
                    fw.write(pid+spaceOrUnderscore+'('+dic[N]+')'+'\n')
                elif N in dic.keys() and dic[N]=='NA':
                    fw.write(pid+spaceOrUnderscore+'('+N+'(SN))\n')
                else:
                    fw.write(line+'\n')
            else:
                fw.write(line)
        else:                          # false not working
            pass
##            line = line.strip('\n')
##            s = line.split('[')
##            N = s[-1:][0].strip('[]')
##            if '>' in line:
##                if N not in sn_list:
##                    pid = s[0].split()[0].strip('>[]')
##                    if N in dic.keys() and dic[N]!='NA':
##                        fw.write('>'+pid+spaceOrUnderscore+dic[N]+'\n')
##                    elif N in dic.keys() and dic[N]=='NA':
##                        fw.write('>'+pid+spaceOrUnderscore+N+'(SN)\n')
##                    else:
##                        fw.write(line+'\n')
##            else:
##                if N not in sn_list:
##                    fw.write(line+'\n')
        sn_list.append(N)
    fas_file.close()
    fw.close()
    return dic
            
#convert()
