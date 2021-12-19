import csv

work_dir = '/home/kav/Downloads/csv-sample-files_6PyXYoo/csv-sample-files/'
fname_rel = 'employee_birthday.csv'

if __name__ == '__main__':
    fname_abs = work_dir + fname_rel

    with open(fname_abs, 'r') as csv_file:
        line_count = 0
        # csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are: {", ".join(row)}')
                line_count += 1

            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}')
            line_count += 1
        print(f'Processed {line_count} lines.')
