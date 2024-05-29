# Xiaoxia Wang, Otilia Tica, Kelvin Okoth, Krishnarajah Nirantharakumar, David Shukla, Dipak Kotecha, 2024.

import sys, csv, re

codes = [{"code":"12736851000006112","system":"med"},{"code":"5887651000006116","system":"med"},{"code":"7375931000006117","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('atrial-fibrillation-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["atrial-fibrillation-control---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["atrial-fibrillation-control---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["atrial-fibrillation-control---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
