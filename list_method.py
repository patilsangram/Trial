len=int(raw_input("Enter length :"))
list=[]							#initialise list
	
for ele in range(len):						#Take input length of list and append element to it
	input=raw_input("Enter element for list :")
	list.append(input)
print list

while(True):
	method=int(raw_input(" 1.Add \n 2.Remove \n 3.Reverse \n 4.Display \n 5.Delete \n 6.Exit \n"))	#method to do

	if method==1:								
		add=raw_input("Enter to add : \n")			#append given ele in list
		list.append(add)
		print"list after adding...",list,"\n"

	elif method==2:							#Remove given ele
		remove_ele=raw_input("Remove element : \n")
		list.remove(remove_ele)
		print"After remove \n",list

	elif method==3:							#Reverse the list
		list.reverse()
		print list

	elif method==4:							#Display List
		print"List :",list

	elif method==5:
		del_ele=int(raw_input("Enter index of del ele : \n"))	#Deleting ele
		del list[del_ele]
		print list
	
	elif method==6:							#Exit from loop
		print"Exiting.."
		break;
	else:
		print"Enter valid choice :\n"				# if invalid choice
