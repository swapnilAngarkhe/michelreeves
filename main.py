        #taking user input
# x = input('what are you? ')

        #saving the user input
    #dont forget to put the extension at the end
    # namefile=open('filename.extension', 'read r, write w, exicute x' )
    #filename.cose()

# myfile=open('file.txt', 'w')

# myfile.close()

    #instead of above one we can use: this one automatically closes the file
    #its like with this file do this shit ~mykul reeves

# with open('file.txt', 'w') as myfile:
#     myfile.write('british people are nice ~lilypichu')
    
    #test
            
# x=input('what do you like bruh? ')
with open('bigblackmeatballs.txt', 'w') as bigblackmeatballs:
    bigblackmeatballs.write(' you can put the x in here ')
    
    

            #READING FILE
            
with open('file.txt', 'r') as balls:
    lines=balls.readlines()
    print(lines) # each line is a object in a list
    
    
with open ('mykul.txt', 'r') as maikal:
    read=maikal.readlines() 
    # print(read)
    for attribute in read:
        # print(attribute) 
        #using split
        smallpp=attribute.split(' ') [1]
        print(smallpp)
    
lst= [10, 'fkn 90', 'fkn 68', 420]
m=lst[0]
print (m)





