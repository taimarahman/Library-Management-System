import time

class Library:

    def __init__(self,bookList,bookNo):
        
        self.availableBooks = bookList
        self.bookNo = bookNo
        
    def displayBooks(self):
        print('\nList Of Books:')
        print('\nCode\t\tNo. Of Books\t\tBook Name\t\t')
        print('____\t\t____________\t\t_________\n')
        for key,value in self.availableBooks.items():
            #print(key, value)
            print(value+'\t\t     '+self.bookNo[value]+'\t\t\t'+key)

    def displayList(self):
        print('\nList Of Books:')
        print('\nCode\t\tBook Name\t\t')
        print('____\t\t_________\n')
        for key,value in self.availableBooks.items():
            #print(key, value)
            print(value+'\t\t'+key)
    
    def borrowBook(self):
        if self.availableBooks == []:
            print('\n\tSorry Our Stock Is Empty')
        else:
            self.displayBooks()
            
            while True:
                print('\n\t***Press 0 To Go Back***\n')
                borrow = input('Enter Name Or Code Of The Book: ')
                borrow = borrow.title()
                if borrow == '0':
                    break
                elif borrow in self.availableBooks.keys() or borrow in self.availableBooks.values():
                    
                    if borrow in self.availableBooks.keys():
                        code = self.availableBooks[borrow]
                        print(code)
                    else:
                        code = borrow
                    print(code)
                    confirm = input('Confirm Request? Y/N: ')
                    confirm = confirm.lower()
                    if confirm[0] == 'y':
                        waiting()
                        #self.availableBooks.pop(borrow)
                        print(self.bookNo[code])
                        if int(self.bookNo[code]) > 0:
                            self.bookNo[code] = str(int(self.bookNo[code])-1)
                            print('Thanks For Borrowing...')
                            break
                        else:
                            print('Sorry The Book '+borrow+' Is Out Of Stock')
                            break
                    else:
                        break
                else:
                    print('Sorry We Do Not Have The Book')
                    again = input('Search again? Y/N')
                    again = again.lower()
                    if again[0] == 'y':
                        continue
                    else:
                        break
            
    def returnBook(self):
        self.displayList()
        while True:
            
            return_book = input('\nEnter The Code Of The Book You Want To Retrun: ')
            return_book = return_book.title()
           
            if  return_book == '0':
                break
            
            elif return_book in self.bookNo and int(self.bookNo[return_book]) < int(original_list[return_book]) :
                print(original_list[return_book])
            
                
                self.bookNo[return_book] = str(int(self.bookNo[return_book])+1)
                waiting()
                print('Thanks for Returning The Book!')
                break

            elif return_book in self.availableBooks.keys():
                print('\n\tPlease Enter The Code Of The Book ')
                continue
            
            else:
                print('You Did Not Borrow This Book')
                again = input('Search again? Y/N: ')
                again = again.lower()
                if again[0] == 'y':
                    continue
                else:
                    break
def waiting():
    print('a moment please',end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    
def createDict():
    global bookList, bookNo
    file1 = open("bookName.txt","r")
    bookName = file1.read()
    file1.close()
    bookName = bookName.splitlines()
    #print(bookName)

    file2 = open("bookCode.txt","r")
    bookCode = file2.read()
    file2.close()
    bookCode = bookCode.splitlines()
    #print(bookCode)

    file3 = open("bookCount.txt","r")
    bookCount = file3.read()
    file3.close()
    bookCount = bookCount.splitlines()
    #print(bookCount)

    bookList = dict(zip(bookName, bookCode))
    bookNo = dict(zip(bookCode, bookCount))
    
createDict()
original_list = bookNo.copy()
#print(original_list)
#print(bookList)


obj = Library(bookList,bookNo)
print('_____WELCOME TO THE LIBRARY_____')
while True:

    start = input('Start? Y/N: ')
    start = start.lower()
    

    if start[0] == 'y':
        while True:
            
            print('\nHow Can We Help You?')
            print('\t1. Show All The Available Books \n\t2. Borrow A Book \n\t3. Return A Book\n\t4. Exit\n')
            userHelp = int(input('Enter Between 1-4: '))
            
            if userHelp == 1:
                obj.displayBooks()
            elif userHelp == 2:        
                obj.borrowBook()
            elif userHelp == 3:
                print('\n\t***Press 0 To Go Back***\n')
                obj.returnBook()
            elif userHelp == 4:
                print('____THANK YOU____')
                break
            else:
                continue
            
    elif start[0] == 'n':
        print('____THANK YOU____')
        break
    else:
        continue
    
    break
