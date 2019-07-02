import pyautogui
import time
import sys
from threading import Thread
import random
random.seed()

#HARD CODED BTN VALS
#mage btn
mX = 1215
mY = 206
#warrior btn
wX = 1221
wY = 362
#berserker btn
bX = 1224
bY = 507
#refresh btn
refBtnX = 1218
refBtnY = 199

def berserkerForestGatheringZone1():
	runForestGathering = True
	#is run time of level
	ForestGatheringTimer = 29
	ForestGatheringRunCount = 0
	#infinite loop
	while (runForestGathering == True):
		time.sleep(random.randint(1,4))
		#click mission button for berserker and hasten menu render
		pyautogui.click(bX, bY)
		pyautogui.click(bX, bY)
		#necessary delay
		time.sleep(2.222)
		#click refresh mission
		pyautogui.click(refBtnX,refBtnY)
		#print message on console
		print ("ZONE 1 - Mission started: " + time.ctime())
		#delay for mission duration
		time.sleep(ForestGatheringTimer)
		print("Mission ended: " + time.ctime())
		print("Harvesting: Tuvale Moss and Ashe root!~")
		ForestGatheringRunCount += 1
		print("Script has ran FOREST GATHERING (zone 1): " + str(ForestGatheringRunCount) + " times." + '\n')

def warriorYarsolGatheringZone2():
	runYarsolGathering = True
	YarsolGatheringTimer = 44
	YarsolGatheringRunCount = 0
	#infinite loop
	while (runYarsolGathering == True):
		time.sleep(random.randint(1,4))
		#click mission button for MAGE and hasten menu render
		pyautogui.click(wX, wY)
		pyautogui.click(wX, wY)
		#necessary delay
		time.sleep(2.222)
		#click refresh mission
		pyautogui.click(refBtnX,refBtnY)
		#print message on console
		print ("ZONE 2 - Mission started: " + time.ctime())
		#delay for mission duration
		time.sleep(YarsolGatheringTimer)
		print("Mission ended: " + time.ctime())
		print("Harvesting: Coral Moss and Willow root!~")
		YarsolGatheringRunCount += 1
		print("Script has ran YARSOL GATHERING (zone 2): " + str(YarsolGatheringRunCount) + " times." + '\n')	
	

def mageAldurGatheringZone3():
	runAldurGathering = True
	#is run time of level
	AldurGatheringTimer = 78
	AldurGatheringRunCount = 0
	#infinite loop
	while (runAldurGathering == True):
		time.sleep(random.randint(1,4))
		#click mission button for MAGE and hasten menu render
		pyautogui.click(mX, mY)
		pyautogui.click(mX, mY)
		#necessary delay
		time.sleep(2.222)
		#click refresh mission
		pyautogui.click(refBtnX,refBtnY)
		#print message on console
		print ("ZONE 3 - Mission started: " + time.ctime())
		#delay for mission duration
		time.sleep(AldurGatheringTimer)
		print("Mission ended: " + time.ctime())
		print("Harvesting: Highland Moss and Oak root!~")
		AldurGatheringRunCount += 1
		print("Script has ran ALDUR GATHERING (zone 3): " + str(AldurGatheringRunCount) + " times." + '\n')
		

if __name__ == '__main__':
	t1 = Thread(target=berserkerForestGatheringZone1)
	t2 = Thread(target=warriorYarsolGatheringZone2)
	t3 = Thread(target=mageAldurGatheringZone3)
	t1.setDaemon(True)
	t2.setDaemon(True)
	t3.setDaemon(True)
	print("*** \t Executing Berserker Gather in Zone 1! \t ***")
	print('\n')
	t1.start()
	print("*** \t Executing Warrior Gather in Zone 2! \t ***")
	print('\n')
	time.sleep(7)
	t2.start()
	print("*** \t Executing Mage Gather in Zone 3! \t ***")
	print('\n')
	time.sleep(7)
	t3.start()
	while True:
		pass



		


