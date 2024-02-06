from engin import Engin

System = Engin()


def banner():
    print('''
    |*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*|
    |*   Attendance System With Face Recognition   *|
    |*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*|
        Select the Option
          1) Set Atttendence of Student
          2) Enroll Students
          3) exit
    ''')
    pass


if __name__ == '__main__':
    banner()
    opt = int(input('Enter the Option : '))
    if opt == 1:
        System.varify_atten()
        pass
    elif opt == 2:
        System.Add_std()
        pass
    elif opt == 3:
        exit()
    elif opt == 4:
        System.temp()
        pass
    else:
        print('Enter Valid Option !')
