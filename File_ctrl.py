# file dakı dosyalı okuyup list e yerleştir
def read_file_to_list(path):
    students = list()
    with open(path,'r') as std_file:
        for line in std_file:
            fields = line.split(',')
            student = {'std_id': fields[0],'name': fields[1],'cgpa': fields[2],'dop': fields[3],'gender':fields[4]}
            students.append(student)
    return students

# list leri file a yazdır
def write_list_to_file(list,path):
    with open(path,'w') as std_file:
        for std in list:
            std_file.write('{},{},{},{},{}'.format(std['std_id'],std['name'],std['cgpa'],std['dop'],std['gender']))

# modify yap
def modify(stdid,field,new_value):
    students = read_file_to_list('students.txt')
    for std in students:
        if std['std_id'] == stdid:
            std[field] = new_value
    write_list_to_file(students,'students.txt')

# insert yap values should be string because inputs are string
def insert(stdid,name,cgpa,dop,gender):
    with open('students.txt','a') as std_file:
        std_file.write('{},{},{},{},{}\n'.format(stdid,name,cgpa,dop,gender))

# sil
def delete(stdid):
    students = read_file_to_list('students.txt')
    for i in range(len(students)):
        if students[i]['std_id'] == stdid:
            students.pop(i)
            break
    write_list_to_file(students,'students.txt')

# display formated file
def display():
    with open('students.txt','r') as std_file:
        for line in std_file:
            data = line.split(',')
            
            stdid = data[0]
            name = data[1]
            cgpa = data[2]
            dop  = data[3]
            gender = data[4] 
            print('Student id: {}, Name: {}, Cgpa: {}, Data of birth: {}, Gender: {}'.format(stdid,name,cgpa,dop,gender))

# stats.txt dosya olurtur ve icine yaz
def stats():
    students = read_file_to_list('students.txt')
    student_count = len(students)
    avg_cgpa = 0
    M = 0
    F = 0
    for std in students:
        gender = std['gender'].strip('\n')
        if gender == 'M':
           M += 1
        else:
           F += 1
        avg_cgpa += float(std['cgpa'])
       
    
    avg_cgpa /= student_count
   
    with open('stats.txt','w') as stat_file:
        stat_file.write('Total number of Students :' + str(student_count) + '\n')
        stat_file.write('Average Cgpa of students : {0:4.2f}\n'.format(avg_cgpa))
        stat_file.write('Number of Male students: {}\nNumber of Female students: {}'.format(M,F))
        stat_file.write('\n')
        
    
#Values should be string for all methods !!!!!!
def main():
    print("For testing the methods pls type them in main\nValues should be string\nexample : delete('str')")
    
    

    
    
    
   
    


    

  

if __name__ == '__main__':
    main()
    
