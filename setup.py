with open("requirements.txt",'r') as file:
    import os
    lst =[i for i in file.readlines()]
    print(lst)
    for i in lst:
        try:
            print(i)
            os.system(f"pip install {i}")
        except:
            continue



# from PIL import Image
# im=Image.open('frame.png')
# with open('test.png','wb') as pic:
#     print(im)