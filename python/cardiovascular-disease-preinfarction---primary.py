# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Iain Buchan, Naveed Sattar, Martin K Rutter, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"G30..00","system":"readv2"},{"code":"G30..15","system":"readv2"},{"code":"G30..17","system":"readv2"},{"code":"G300.00","system":"readv2"},{"code":"G301.00","system":"readv2"},{"code":"G301000","system":"readv2"},{"code":"G301100","system":"readv2"},{"code":"G301z00","system":"readv2"},{"code":"G302.00","system":"readv2"},{"code":"G303.00","system":"readv2"},{"code":"G304.00","system":"readv2"},{"code":"G305.00","system":"readv2"},{"code":"G306.00","system":"readv2"},{"code":"G307.00","system":"readv2"},{"code":"G307000","system":"readv2"},{"code":"G307100","system":"readv2"},{"code":"G308.00","system":"readv2"},{"code":"G309.00","system":"readv2"},{"code":"G30B.00","system":"readv2"},{"code":"G30X.00","system":"readv2"},{"code":"G30X000","system":"readv2"},{"code":"G30y.00","system":"readv2"},{"code":"G30y100","system":"readv2"},{"code":"G30y200","system":"readv2"},{"code":"G30yz00","system":"readv2"},{"code":"G30z.00","system":"readv2"},{"code":"G310.00","system":"readv2"},{"code":"G311.00","system":"readv2"},{"code":"G311.12","system":"readv2"},{"code":"G311z00","system":"readv2"},{"code":"G32..00","system":"readv2"},{"code":"G32..11","system":"readv2"},{"code":"G32..12","system":"readv2"},{"code":"G33z500","system":"readv2"},{"code":"G35..00","system":"readv2"},{"code":"G350.00","system":"readv2"},{"code":"G351.00","system":"readv2"},{"code":"G353.00","system":"readv2"},{"code":"G35X.00","system":"readv2"},{"code":"G360.00","system":"readv2"},{"code":"G38..00","system":"readv2"},{"code":"G380.00","system":"readv2"},{"code":"G381.00","system":"readv2"},{"code":"G384.00","system":"readv2"},{"code":"G38z.00","system":"readv2"},{"code":"G64..12","system":"readv2"},{"code":"G640000","system":"readv2"},{"code":"G641000","system":"readv2"},{"code":"G64z.00","system":"readv2"},{"code":"G64z.12","system":"readv2"},{"code":"G64z200","system":"readv2"},{"code":"G64z300","system":"readv2"},{"code":"Gyu3400","system":"readv2"},{"code":"Gyu3600","system":"readv2"},{"code":"Gyu6400","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-disease-preinfarction---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-disease-preinfarction---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-disease-preinfarction---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
