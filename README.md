# scientific_name_to_common-name_converter
Convert scientific names to common names

Required file: https://www.uniprot.org/docs/speclist.txt

Python: 2.7

to run (change the path as yours)

1. download 'convert_scientific_name_to_common_names.py'
2.

[1] import convert_scientific_name_to_common_names

[2] n2c = convert_scientific_name_to_common_names.convert(path = 'C:/Users/rahul/',specfile="speclist.txt",outfile="Sci2Com.csv")

output 

A csv file "Sci2Com.csv" in your folder and a python dictionary

[3] n2c['Homo sapiens']

[4] Human
