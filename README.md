# scientific_name_to_common-name_converter
Convert scientific names to common names and vice versa

Required file: https://www.uniprot.org/docs/speclist.txt

Python: 2.7

to run (change the path as yours)


[1] import convert_scientific_name_to_common_names

[2] n2c, c2n = convert_scientific_name_to_common_names.convert(path = 'C:/Users/rahul/',specfile="speclist.txt",outfile="Sci2Com.csv")

output:

A csv file "Sci2Com.csv" in your folder and a python dictionary

[3] n2c['Homo sapiens']

[4] 'Human'

[5] n2c['Pan paniscus']

[6] 'Bonobo'

[7] c2n['Human']

'Homo sapiens'

[8] c2n['Cat']

'Felis catus'

![image](https://user-images.githubusercontent.com/18325626/137794665-84283b07-3e7e-4850-88dd-1e9956735290.png)


