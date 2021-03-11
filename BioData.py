def BioData():
    std_id=input("Enter Student ID:")
    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    address=input("Enter Address")
    city=input("Enter City:")
    weight=int(input("Enter Weight"))
    height=int(input("Enter Height"))
    print("\n----------------Student Details----------------")
    details=f'''
    Student ID:{std_id}
    Name:{name}
    Age:{age}
    Address:{address}
    City:{city}
    Weight:{weight}
    Height:{height}
    '''
    print(details)
BioData()
