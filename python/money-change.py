#Author: Maple0
#Github:https://github.com/Maple0
#10th Aug 2016
def calculate_change(due,paid):
	# final changes
	finalChanges=[]
	# available change units in cents
	availableChanges=[10000,5000,1000,500,200,100,50,20,10]
	# money change supports up to cents only
	if (int(due*100)%10)!=0 or (int(paid*100)%10)!=0 :
		print("wrong amount found in'due amount' or 'paid amount', "
			+" the smallest change unit support of this program is 'cent'... ")
	else:	
		# total amount of required change based on due amount and paid amount
		totalChangeAmount= int(int(paid*100) - int(due*100))
		#if paid amount less than due amount, prompt error
		if totalChangeAmount < 0:
			print('The paid amount is insufficient...')
		if totalChangeAmount == 0:
			print('No change required...')
		else:
			for unitAmount in availableChanges:
				if totalChangeAmount >= unitAmount:
					# numbers of this type of changes
					num= int(totalChangeAmount/unitAmount)
					finalChanges.append(str(int(unitAmount)/100)+" x "+str(num))
					# reset total change amount
					totalChangeAmount=totalChangeAmount%unitAmount
	return	finalChanges

# amount due in dollars
amountDue=1.1
# amount paid in dollars
amountPaid=2
print("total due amount is $",amountDue,",  you have paid $", amountPaid,"")
print ("your changes:",calculate_change(amountDue,amountPaid))