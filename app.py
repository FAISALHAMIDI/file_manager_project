import os
def creat_file(filename):
    try:
        with open(filename,'x') as f:
            print("File Name {filename}:created successfully!")
    except FileExistsError:
        print(f"File Name{filename}:already exists")
    except Exception as E:
        print('an error occurred!')

def view_all_files():
    files=os.listdir()
    if not files:
        print("No file found!")
    else:
        print("files in directory!")
        for file in files:
            print(file)


    
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occurred")
def read_file(file):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
            print(f"content of '{filename}':\n{content}")

    except FileNotFoundError:
        print("{filename} doesno't exist!")

    except Exception as e:
        print("an error occurred!")



def eddit_file(filename):
    try:
        with open("sample.txt",'a')as f:
            content=input("Enter data to add = ")
            f.write(content + "\n")
            print("content added to {filename}successfully")
    
    except FileNotFoundError:
        print("{filename} doesno't exist!")

    except Exception as e:
        print("an error occurred!")

def main():
    while True:
        print("FILE MANAGMENT APP")
        print("1 : create file ")
        print("2 : view all files")
        print("3: delete file")
        print("4: read file ")
        print("5: read file")
        print("6: exit")

        choice=input("enter your choice")
    
        if choice=="1":
            filename=input("enter the file_name to creadt = ")
            creat_file(filename)
        elif choice=="2":
            view_all_files()
        elif choice=="3":
            filename=input("Enter the name of file you want")
            read_file(filename)

        elif choice=="4":
            filename=input('Enter file name to read = ')
            read_file(filename)
        elif choice=="5":
            filename=input('Enter file name to eddit = ')
            eddit_file(filename)
        elif choice=="6":
            print("closing the app....")
            break
        else:
            print("In valid input ")

if __name__=="__main__":
    main()






