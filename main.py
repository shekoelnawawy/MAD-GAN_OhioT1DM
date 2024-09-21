import os
import numpy as np

if os.path.exists('./output'):
    os.system('"yes" yes | rm -r ./output')

os.system('mkdir ./output')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"most\",\n"
train_data[3] = "\"patient\": \"0\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/most')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/most/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/most/test_most_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/most/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/most/test_most_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()

print('-----------------------------------------------------------------------------------------------------------------------------')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"least\",\n"
train_data[3] = "\"patient\": \"0\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/least')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/least/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/least/test_least_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/least/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/least/test_least_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()

print('-----------------------------------------------------------------------------------------------------------------------------')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"all\",\n"
train_data[3] = "\"patient\": \"0\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/all')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/all/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/all/test_all_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/all/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/all/test_all_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()

print('-----------------------------------------------------------------------------------------------------------------------------')



# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"2020\",\n"
train_data[3] = "\"patient\": \"1\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/2020_1')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/2020_1/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/2020_1/test_2020_1_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/2020_1/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/2020_1/test_2020_1_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()


print('-----------------------------------------------------------------------------------------------------------------------------')


# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"2020\",\n"
train_data[3] = "\"patient\": \"2\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/2020_2')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/2020_2/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/2020_2/test_2020_2_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/2020_2/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/2020_2/test_2020_2_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()

print('-----------------------------------------------------------------------------------------------------------------------------')


# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"2018\",\n"
train_data[3] = "\"patient\": \"5\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/2018_5')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/2018_5/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/2018_5/test_2018_5_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/2018_5/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/2018_5/test_2018_5_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()

print('-----------------------------------------------------------------------------------------------------------------------------')


# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"leastsub\",\n"
train_data[3] = "\"patient\": \"0\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/leastsub_0')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/leastsub_0/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/leastsub_0/test_leastsub_0_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/leastsub_0/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/leastsub_0/test_leastsub_0_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()

print('-----------------------------------------------------------------------------------------------------------------------------')


# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"leastsub\",\n"
train_data[3] = "\"patient\": \"1\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/leastsub_1')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/leastsub_1/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/leastsub_1/test_leastsub_1_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/leastsub_1/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/leastsub_1/test_leastsub_1_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()

print('-----------------------------------------------------------------------------------------------------------------------------')


# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"leastsub\",\n"
train_data[3] = "\"patient\": \"2\",\n"

# and write everything back
with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
    train_file.writelines(train_data)

print('Training:')
os.system('mkdir ./output/leastsub_2')
os.system('python RGAN.py --settings_file ohiot1dm > ./output/leastsub_2/train.txt')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
    # read a list of lines into data
    test_data = test_file.readlines()

print('Testing: ')
for year in [2020, 2018]:
    test_data[2] = "\"year\": \"" + str(year) + "\",\n"

    for patient in range(6):
        test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

        # and write everything back
        with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
            test_file.writelines(test_data)

        print('Year: '+str(year)+'\tPatient: '+str(patient))
        os.system('python AD.py --settings_file ohiot1dm_test > ./output/leastsub_2/test_leastsub_2_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/leastsub_2/Results.csv", "w")
out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        with open('./output/leastsub_2/test_leastsub_2_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
out.close()

print('-----------------------------------------------------------------------------------------------------------------------------')

# with is like your try .. finally block in this case
with open('./experiments/settings/ohiot1dm.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"samples\",\n"

for run in range(10):
    # now change the 2nd line, note that you have to add a newline
    train_data[3] = "\"patient\": \"" + str(run) + "\",\n"

    # and write everything back
    with open('./experiments/settings/ohiot1dm.txt', 'w') as train_file:
        train_file.writelines(train_data)

    print('Training:')
    os.system('mkdir ./output/samples')
    os.system('python RGAN.py --settings_file ohiot1dm > ./output/samples/train_'+ str(run) + '.txt')

    # with is like your try .. finally block in this case
    with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
        # read a list of lines into data
        test_data = test_file.readlines()

    print('Testing: ')
    for year in [2020, 2018]:
        test_data[2] = "\"year\": \"" + str(year) + "\",\n"

        for patient in range(6):
            test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"

            # and write everything back
            with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
                test_file.writelines(test_data)

            print('Year: '+str(year)+'\tPatient: '+str(patient))
            os.system('python AD.py --settings_file ohiot1dm_test > ./output/samples/test_run_' + str(run) + '_patient_' + str(year) + '_' + str(patient) +'.txt')


out = open("./output/samples/Results.csv", "w")
out.write('Run,Year,Patient,Accuracy,Precision,Recall,F1\n')

for year in [2020, 2018]:
    for patient in range(6):
        Accuracy = []
        Precision = []
        Recall = []
        F1 = []
        for run in range(10):
            with open('./output/samples/test_run_'+str(run)+'_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
                # read a list of lines into data
                data = file.readlines()
            Accuracy.append(float(data[-3].split(' ')[4][:-1]))
            Precision.append(float(data[-3].split(' ')[6][:-1]))
            Recall.append(float(data[-3].split(' ')[8][:-1]))
            F1.append(float(data[-3].split(' ')[10][:-1]))
            out.write(str(run)+','+str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
        out.write('Average,'+str(year)+','+str(patient)+','+str(np.average(np.array(Accuracy)))+','+str(np.average(np.array(Precision)))+','+str(np.average(np.array(Recall)))+','+str(np.average(np.array(F1)))+'\n')
out.close()



# import os
#
#
# if os.path.exists('./output'):
#     os.system('"yes" yes | rm -r ./output')
#
# os.system('mkdir ./output')
#
# print('Training:')
# os.system('python RGAN.py --settings_file ohiot1dm > ./output/train_all.txt')
#
# # with is like your try .. finally block in this case
# with open('./experiments/settings/ohiot1dm_test.txt', 'r') as test_file:
#     # read a list of lines into data
#     test_data = test_file.readlines()
#
# print('Testing: ')
# for year in [2020, 2018]:
#     test_data[2] = "\"year\": \"" + str(year) + "\",\n"
#
#     for patient in range(6):
#         test_data[3] = "\"patient\": \"" + str(patient) + "\",\n"
#
#         # and write everything back
#         with open('./experiments/settings/ohiot1dm_test.txt', 'w') as test_file:
#             test_file.writelines(test_data)
#
#         print('Year: '+str(year)+'\tPatient: '+str(patient))
#         os.system('python AD.py --settings_file ohiot1dm_test > ./output/test_all_patient_' + str(year) + '_' + str(patient) +'.txt')
#
# out = open("./output/Results.csv", "w")
# out.write('Year,Patient,Accuracy,Precision,Recall,F1\n')
#
# for year in [2020, 2018]:
#     for patient in range(6):
#         with open('./output/test_all_patient_'+str(year)+'_'+str(patient)+'.txt', 'r') as file:
#             # read a list of lines into data
#             data = file.readlines()
#         out.write(str(year)+','+str(patient)+','+str(data[-3].split(' ')[4][:-1])+','+str(data[-3].split(' ')[6][:-1])+','+str(data[-3].split(' ')[8][:-1])+','+str(data[-3].split(' ')[10]))
# out.close()

