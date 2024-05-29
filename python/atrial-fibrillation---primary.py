# Xiaoxia Wang, Otilia Tica, Kelvin Okoth, Krishnarajah Nirantharakumar, David Shukla, Dipak Kotecha, 2024.

import sys, csv, re

codes = [{"code":"294601000000110","system":"med"},{"code":"636721000000112","system":"med"},{"code":"5057261000006110","system":"med"},{"code":"256478018","system":"med"},{"code":"5669611000006119","system":"med"},{"code":"8439861000006115","system":"med"},{"code":"2675253013","system":"med"},{"code":"4586611000006112","system":"med"},{"code":"1823951000006111","system":"med"},{"code":"406861000000119","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('atrial-fibrillation-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["atrial-fibrillation---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["atrial-fibrillation---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["atrial-fibrillation---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
