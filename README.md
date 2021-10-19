# scientific_name_to_common-name_converter / rename fasta file header's scientific name to common name
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

Rename fasta file header's scientific name to common name before phylogeny analysis in MEGA

Download 'Description Table (csv) after selecting 'Common Name' from the NCBI BLAST output page

![image](https://user-images.githubusercontent.com/18325626/137904789-64555590-c6c5-4d7b-9acd-d1d3e5da9470.png)

Change the path and file names as yours and run:

[9[ ![image](https://user-images.githubusercontent.com/18325626/137903912-d8f25bb3-a620-4e0b-aab9-a014df0e7941.png)



