def main():
    #a list for all books to be stored
    booklist = []  
    choice = 0
    print("*** SPECTRE'S BOOKSTORE *** ")

  

    options = '''
    1).ADD A BOOK
    2).SEARCH FOR A BOOK
    3).DISPLAY ALL BOOKS 
    4).QUIT
    '''

   
    while choice != 4:
        print(options)
        choice = int(input("> "))
        if choice == 1:
            print('ADDING A BOOK ...')
            book_name = input('***ENTER THE NAME OF THE BOOK*** ')
            author_name = input('***ENTER THE NAME OF THE AUTHOR OF THE BOOK*** ')
            book_pages = input('***ENTER THE NUMBER  OF PAGES OF THE BOOK*** ')
            book_dict = {'NAME OF BOOK': f'{book_name}','AUTHOR NAME': f'{author_name}','NUMBER OF PAGES':f'{book_pages}'
            }
            booklist.append(book_dict)
        if choice == 2:
            print('SEARCH FOR A BOOK')
            print(booklist)
            search = input('WHICH BOOK ARE YOU LOOKING FOR? ')
            for books in booklist:
                if search in books['NAME OF BOOK']:    
                    print('BOOK FOUND!!')
                else:
                    print(f'404 ERROR, {search} NOT FOUND!!')
        if choice == 3:
            if booklist != '':
                for books in booklist:
                    for key,value in books.items():
                        if value.isalpha():
                            print(f'{key.title()} : {value.title}')
                        else:
                            print(f'{key} : {value}')
            else:
                print('NO BOOKS TO SEE')
        if choice == 4:
            print('QUITTING PROGRAM...')
            exit()
   


if __name__ == "__main__":
    main()
