# When something is run, the __name__ variable is filled in. 
# If the code was run from the same class it was called from, it will fill the __name__ variable with 'main'
# Otherwise, the name of the variable will equal the name of the class contains the code

if __name__ == '__main__':
    print('this file was not imported')
else:
    print('this file was imported')
    print('the name is: {}'.format(__name__))