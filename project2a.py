
print "Welcome to my Python Power Converter v1.0 by Michelle Ling!"
print "You can convert Distances , Weights , Volumes & Times to one another, but only"
print "within units of the same category, which are shown below. Please format your conversion"
print "as [amount] [source units] in [destination units]. E.g.: 1 mi in ft, 10 ft in m"
print 
print "Distances: ft cm mm mi m yd km in"
print "Weights: lb mg kg oz g"
print "Volumes: floz qt cup mL L gal pint"
print
print "If you use different abbreviations for units than the ones shown above, the"
print "program will error, so please check your spelling."
print "If at any time you are done converting and would like to quit the program, type q"

continueConvert = True #quit program?
distances = {"m": 1.0, "cm": 100.0, "mm": 1000.0, "km": .001, "in": 39.3701, "ft": 3.28084, "yd": 1.09361, "mi": 0.000621371}
weights = {"L": 1.0, "mL": 1000.0, "floz": 33.814, "cup": 4.22675, "pint": 2.11338, "qt": 1.05669, "gal": 0.264172}
volumes = {"g":1, "kg": .001, "mg": 1000, "oz": .035274, "lb": .00220462}

def unitCoverter(convertNum, sourceform, destform, convtype):
	firstconv = convertNum/convtype[sourceform]
	secondcov = firstconv*convtype[destform]
	return secondcov

#mainloop
while (continueConvert):
	toConvert = raw_input("Please input what you would like to convert: ")
	if (toConvert == "q"):
		continueConvert = False
		print "Thanks for converting with Python Power Converter. Y'all come back now, y'hear?"
	else:
		conversionList = toConvert.split()
		if (len(conversionList) != 4) or (not conversionList[0].isdigit()):
			print "Error in format, please format your conversion as [amount] [source units] in [destination units]."
			print "Example: 1 mi in ft, 10 ft in m"
		else:
			convertNum = int(conversionList[0])
			sourceform = conversionList[1]
			destform = conversionList[3]
			if sourceform in distances:
				if destform not in distances:
					print "Error in conversion, must convert a distance to a distance, and" 
					print "must be a supported unit as stated above. Please try again."
				else:
					answer = unitCoverter(convertNum, sourceform, destform, distances)
					print answer
			elif sourceform in weights:
				if destform not in weights:
					print "Error in conversion, must convert a weight to a weight, and"
					print "must be a supported unit as stated above. Please try again."
				else:
					answer = unitCoverter(convertNum, sourceform, destform, weights)
					print answer
			elif sourceform in volumes:
				if destform not in volumes:
					print "Error in conversion, must convert a volume to a volume, and" 
					print "must be a supported unit as stated above. Please try again."
				else:
					answer = unitCoverter(convertNum, sourceform, destform, volumes)
					print answer
			else:
				print "Error, sorry your unit of conversion must be one of"
				print "the supported forms stated above. Please try again."