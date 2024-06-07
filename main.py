import os

if os.path.exists('./output'):
    os.system('"yes" yes | rm -r ./output')
else:
    os.system('mkdir ./output')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

for run in range(10):
    # now change the 2nd line, note that you have to add a newline
    train_data[3] = "\"patient\": \"" + str(run) + "\","

    # and write everything back
    with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
        train_file.writelines(train_data)

    print('Training: '+str(run))
    os.system('python RGAN.py --settings_file ohiot1dm > ./output/train_'+ str(run) + '.txt')

    # with is like your try .. finally block in this case
    with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
        # read a list of lines into data
        test_data = test_file.readlines()

    print('Testing: ')
    for year in [2020, 2018]:
        test_data[2] = "\"year\": \"" + str(year) + "\","

        for patient in range(6):
            test_data[3] = "\"patient\": \"" + str(patient) + "\","

            # and write everything back
            with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
                test_file.writelines(test_data)

            print('Year: '+str(year)+'\tPatient: '+str(patient))
            os.system('python AD.py --settings_file ohiot1dm_test > ./output/test_run_' + str(run) + '_patient_' + str(year) + '_' + str(patient) +'.txt')