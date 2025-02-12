.data
nl: .asciiz "\n"
prompt1: "\nPlease select an option from the list below:\n"
prompt2: "[A] - Add a record to the tree\n"
prompt3: "[F] - Find a record in the tree\n"
prompt4: "[M] - Modify\n"
prompt5: "[I] - Perform an inorder traversal\n"
prompt6: "[Q] - Quit the program\n"
prompt7: "\nChoose a character: "
empty: "\nThe Tree is Empty."
youentered: "\nYou Entered: "
recordfound: "\nRecord Found: "
modify:"\n modifeing..." 
recordnotfound: "\nRecord Not Found! "
goodbye: "\nGoodbye!"
addid: "\nEnter the ID to add: "
adddate: "Enter the date: "
addname: "Enter the name: "
adddescription: "Enter the description: "
id: "\nID: "
date: "\nDate: "
name: "\nName: "
description: "Description: "
#idsize: .word 0
#optiona: 97    addrecord   a
#optionf: 102   findrecord  f
#optioni: 105   inorder     i
#optiono: 109   Modify      m
#optionq: 113   quit        q

#   $s5 - Stores Root Node
#   $s7 - Stores Size of Tree
#
#   Each New Item Contains a chunk of 344 bytes
#   The bytes are setup as such:
#
#   8 Bytes - [ID]
#   8 Bytes - [Year]
#   64 Bytes - [Title]
#   256 Bytes - [Description]
#   8 Bytes - [LeftNodeAddress]
#   8 Bytes - [RightNodeAddress]
########################################################
.text 
###################
##Prompt Function##
###################
prompt:
li $v0, 4
la $a0, prompt1         #Please select an option from the list below:
syscall

li $v0, 4
la $a0, prompt2         #[A] - Add a record to the tree
syscall

li $v0, 4
la $a0, prompt3         #[F] - Find a record in the tree
syscall

li $v0, 4
la $a0, prompt4         #[M] - Modify
syscall

li $v0, 4
la $a0, prompt5         #[I] - Inorder traversal
syscall


li $v0, 4
la $a0, prompt6         #[Q] - Quit the program
syscall
###################
##Get User Input ##
################### 
getinput:   
li $v0, 4           #Choose a character:
la $a0, prompt7
syscall

li $v0, 12          #Read a single character from console
syscall

move $s0, $v0

beq $s0, 97, addrecord      #If you press 'a', addrecord
beq $s0, 102, findrecord    #If you press 'f', findrecord
beq $s0, 105, inorder       #If you press 'i', inorder
beq $s0, 109, Modify        #If you press 'D', Modify
beq $s0, 113, exit          #If you press 'q', exit

li $v0, 4           #If you press something random
la $a0, nl          #Display new line
syscall

j getinput          #And ask for a new character
###################
## Add A Record  ##
###################
addrecord:
li $v0, 9           #allocate memory for new record
li $a0, 344         #enough memory for 2 addresses and all the data
syscall


move $s0, $v0           #hang onto the initial address of all our info

li $v0, 4           #prompt for ID
la $a0, addid
syscall

li $v0, 5           #enter integer
syscall

sw $v0, 0($s0)          #store our ID into memory   Offset: 0

li $v0, 4           #prompt for add date
la $a0, adddate
syscall

li $v0, 5           #enter integer
syscall

sw $v0, 4($s0)          #store date into our memory Offset: 4

li $v0, 4           #prompt for add name
la $a0, addname
syscall

li $v0, 8           #read our name into the allocated space
la $a0, 8($s0)          #Offset: 8
li $a1, 64
syscall

li $v0, 4           #prompt for add description
la $a0, adddescription
syscall

li $v0, 8           #read our description into the allocated space
la $a0, 72($s0)         #Offset: 72
li $a1, 256
syscall 

bne $s7, 0, setlocations    #if this isn't root node let's set the locations

add $s7, $s7, 1         #add 1 to the size of the records

move $s5, $s0           #store this address as root node for now

j prompt
########################
##Set Memory Locations##
########################
setlocations:
move $s6, $s5           #Keep $s5 as  our root and use $s6 as temporary storage
move $s4, $s6           #Use $s4 to find the null node slot
storelocations:
beqz $s4, store         #If we've reached a leaf, store
lw $t2, 0($s4)          #get ID from current node
lw $t1, 0($s0)          #get Current ID from new node node we're adding
ble $t1,$t2,goleft      #get left location if new node <= current node
move $s6, $s4
lw $s4, 336($s4)        #get node to the right if new node > current node
li $t3, 336         #be ready to store to the right slot
j storelocations
goleft:
move $s6, $s4
lw $s4, 328($s4)        #load the node to the left
li $t3, 328         #be ready to store to the left slot
j storelocations
store:
beq $t3, 336, storeright    #if $t3 was set to storeRight, then store to the right
sw $s0, 328($s6)        #else store the new node's location into our node's left slot
add $s7, $s7, 1         #remind our size register that it's growing
j prompt            #back to the prompt
storeright:
sw $s0, 336($s6)        #store new node to the right slot
add $s7, $s7, 1         #remind our size register that it's growing
j prompt            #back to the prompt
########################
## Find Record by ID  ##
########################
findrecord:
move $s6, $s5
bne $s7, 0, search
li $v0, 4           #if tree is empty
la $a0, empty           #display message Tree is empty
syscall
j prompt            #and go wait for input
search:
move $s6, $s5
li $v0, 4           #print ID:
la $a0, id
syscall

li $v0, 5           #let user enter ID
syscall

move $t1, $v0           #store the id we're looking for in $t1
checkagain: 
lw $t2, ($s6)           #store the id we're currently looking at
bne $t1, $t2, checkempty    #if this isn't the right ID, is it the last one?
###########################
##If we find the record:
###########################
li $v0, 4
la $a0, recordfound     #Record Found: 
syscall

li $v0, 4           #Print ID:
la $a0, id
syscall

li $v0, 1           #Print the ID stored at $s6     [Offset: 0]
lw $a0, 0($s6)
syscall

li $v0, 4           #Print date:
la $a0, date
syscall

li $v0, 1           #Print the date stored at $s6   [Offset: 4]
lw $a0, 4($s6)
syscall

li $v0, 4           #Print name:
la $a0, name
syscall

li $v0, 4           #Print the name stored at $s6  [Offset: 8]
la $a0, 8($s6)
syscall

li $v0, 4           #Print Description:
la $a0, description
syscall

li $v0, 4           #Print descript stored at $s6   [Offset: 72]
la $a0, 72($s6)
syscall

j prompt

checkempty:
ble $t1, $t2, checkleft     #If $t1 <= $t2 check the left node
lw $s6, 336($s6)        #Otherwise check the right node
bne $s6, 0, checkagain      #If this record isn't empty, check again
li $v0, 4           #Otherwise
la $a0, recordnotfound      #Record not found
syscall
j prompt
checkleft:
lw $s6, 328($s6)        #Check the left node
bne $s6, 0, checkagain      #If the record isn't empty, check again
li $v0, 4           #Otherwise
la $a0, recordnotfound      #Record not found
syscall
j prompt
treeempty:
li $v0, 4           #if tree is empty
la $a0, empty           #display message Tree is empty
syscall
j prompt
#####################################
#
#   The Inorder Function
#
#####################################
inorder:
beq $s7, 0, treeempty       #If the tree is empty display empty message
move $s6, $s5           #$s6 is the record we're currently at
move $t0, $s6           #t0 will iterate $s6 is our starting node
move $t1, $t0           #t1 will be thrown on the stack to keep track of everything
jal printinorder
j prompt
printinorder:
addi $sp, $sp, -12      #allocate 12 bytes for the stack
sw $ra, 0($sp)          #4 for the $ra variable
sw $t1, 4($sp)          #4 for $t1

bne $t0, 0, dontreturn      #if $t0 isn't null don't return
lw $ra, 0($sp)          #otherwise:
lw $t1, 4($sp)          #pop stack
addi $sp, $sp, 12       #and prepare
jr $ra              #to return
dontreturn:
move $t1, $t0           #put $t0 in $t1
lw $t0, 328($t0)        #load the next pointer to the left
jal printinorder        #and recurse back to printorder
move $s6, $t1           #if we're back here, it's time to print
j goprint           #so go print
afterprint:
move $t0, $t1           #after we print, move $t1 back to $t0
lw $t0, 336($t0)        #get the next pointer to the right
jal printinorder        #recurse to see if it's the last one
move $s6, $t1           #if we made it here, it is, let's print
beq $s6, $t1, done      #if we already printed this one, we're done (Root Node)
j goprint           #Go print the node to the right
done:
lw $ra, 0($sp)          #if we're done, pop our stack
lw $t1, 4($sp)          #clean it up
addi $sp, $sp, 12       #12 bytes worth
jr $ra              #and return
goprint:
li $v0, 4           #Print ID:
la $a0, id
syscall

li $v0, 1           #Print the ID stored at $s6     [Offset: 0]
lw $a0, 0($s6)
syscall

li $v0, 4           #Print date:
la $a0, date
syscall

li $v0, 1           #Print the date stored at $s6   [Offset: 4]
lw $a0, 4($s6)
syscall

li $v0, 4           #Print name:
la $a0, name
syscall

li $v0, 4           #Print the name stored at $s6  [Offset: 8]
la $a0, 8($s6)
syscall

li $v0, 4           #Print Description:
la $a0, description
syscall

li $v0, 4           #Print descript stored at $s6   [Offset: 72]
la $a0, 72($s6)
syscall

j afterprint



########################
## Modify:
########################
Modify:
move $s6,$s5
bne $s7, 0, searchmo
li $v0, 4           #if tree is empty
la $a0, empty           #display message Tree is empty
syscall
j prompt            #and go wait for input
searchmo:
move $s6,$s5
li $v0, 4           #print ID:
la $a0, id
syscall

li $v0, 5           #let user enter ID
syscall

move $t1, $v0           #store the id we're looking for in $t1

checkagainmo: 
lw $t2, ($s5)           #store the id we're currently looking at
bne $t1, $t2, checkemptymo    #if this isn't the right ID, is it the last one?
li $v0, 4
la $a0, modify     #Modifeing... 
syscall
li $v0, 4           #prompt for add date
la $a0, adddate
syscall

li $v0, 5           #enter integer
syscall

sw $v0, 4($s6)          #store date into our memory Offset: 4

li $v0, 4           #prompt for add name
la $a0, addname
syscall

li $v0, 8           #read our name into the allocated space
la $a0, 8($s6)          #Offset: 8
li $a1, 64
syscall

li $v0, 4           #prompt for add description
la $a0, adddescription
syscall

li $v0, 8           #read our description into the allocated space
la $a0, 72($s6)         #Offset: 72
li $a1, 256
syscall



j prompt

checkemptymo:
ble $t1, $t2, checkleftmo     #If $t1 <= $t2 check the left node
lw $s6, 336($s6)        #Otherwise check the right node
bne $s6, 0, checkagainmo      #If this record isn't empty, check again
li $v0, 4           #Otherwise
la $a0, recordnotfound      #Record not found
syscall
j prompt
checkleftmo:
lw $s6, 328($s6)        #Check the left node
bne $s6, 0, checkagainmo     #If the record isn't empty, check again
li $v0, 4           #Otherwise
la $a0, recordnotfound      #Record not found
syscall
j prompt
treeemptymo:
li $v0, 4           #if tree is empty
la $a0, empty           #display message Tree is empty
syscall
j prompt

exit:
li $v0, 4           #Say
la $a0, goodbye         #Goodbye!
syscall

li $v0, 10          #Terminate Program
syscall
