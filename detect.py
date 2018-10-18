import os
import time
#####
#
# detect a value and if it smaller then last time alert
#

#Lets start with 0
current_weight =0







while True:
	'''
	Run this for ever
	'''
	#Get the weight from the scale
	print("chech values")
	file = open("weight.txt", "r") 
	weight = int(file.readline()) 



	print("on scale {0} last value {1}".format(weight,current_weight))

	if current_weight == 0:
		current_weight = weight


	if current_weight > weight:
		print("We have weight loss")
		diffrence = current_weight - weight
		diffrence_procent = float(diffrence) / float(current_weight)
		if diffrence_procent > 0.25:
			print("We have a big change")
	
	if current_weight < weight:
		print("We have gain weight")
		#Set new current waight
		current_weight = weight
	time.sleep(5)