# Simple utility for iMaser monitoring.
#
# Anders Wallin, anders.e.e.wallin "at" gmail.com, 2016-06-27
#
# GNU LESSER GENERAL PUBLIC LICENSE
#           Version 3, 29 June 2007
# see LICENSE.md

# Simple parser for iMaser status string
# input is the reply of "MONIT;\r\n" command 
# sent over UDP:14000

# format:    ( name, start_index, stop_index, gain, unit )
imaser_fields = [ ('U_batt_A', 1,3, 2.441e-2,'V'),
           ('I_batt_A', 4,3, 1.221e-3,'V'),
           ('U_batt_B', 7,3, 2.441e-2,'V'),
           ('I_batt_B', 10,3, 1.221e-3,'V'),
           ('Set_H', 13,3, 3.662e-3,'V'),
           ('Meas_H', 16,3, 1.221e-3,'V'),
           ('I_purifier', 19,3, 1.221e-3,'A'),
           ('I_dissociator', 22,3, 1.221e-3,'A'),
           ('H_light', 25,3, 1.221e-3,'V'),
           ('IT_heater', 28,3, 4.883e-3,'V'),
           ('IB_heater', 31,3, 4.883e-3,'V'),
           ('IS_heater', 34,3, 4.883e-3,'V'),
           ('UTC_heater', 37,3, 4.883e-3,'V'),
           ('ES_heater', 40,3, 4.883e-3,'V'),
           ('EB_heater', 43,3, 4.883e-3,'V'),
           ('I_heater', 46,3, 4.883e-3,'V'),
           ('T_heater', 49,3, 4.883e-3,'V'),
           ('Boxes_temp', 52,3, 2.441e-2,'C'),
           ('I_boxes', 55,3, 1.221e-3,'A'),
           ('Amb_temp', 58,3, 1.221e-2,'C'),
           ('C_field', 61,3, 2.441e-3,'V'),
           ('U_varactor', 64,3, 2.441e-3,'V'),
           ('U_HT_ext', 67,3, 1.221e-3,'kV'),
           ('I_HT_ext', 70,3, 1.221e-1,'uA'),
           ('U_HT_int', 73,3, 1.221e-3,'kV'),
           ('I_HT_int', 76,3, 1.221e-1,'uA'),
           ('Sto_press', 79,3, 4.883e-3,'bar'),
           ('Sto_heater', 82,3, 6.104e-3,'V'),
           ('Pir_heater', 85,3, 6.104e-3,'V'),
           ('Unused', 88,3, 0,''),
           ('U_405kHz', 91,3, 3.662e-3,'V'),
           ('U_OCXO', 94,3, 2.441e-3,'V'),
           ('U_plus24', 97,2, 9.766e-2,'V'),
           ('U_plus15', 99,2, 7.813e-2,'V'),
           ('U_minus15', 101,2, -7.813e-2,'V'),
           ('U_plus5', 103,2, 3.906e-2,'V'),
           ('U_minus5', 105,2, -3.906e-2,'V'),
           ('U_plus8', 107,2, 3.906e-2,'V'),
           ('U_plus18', 109,2, 7.813e-2,'V'),
           ('Unused', 111,2, 0,''),
           ('Lock', 113,1, 1,''),
            ]

def imaser_parse(message):
	fieldDict = {}
	s = message[1:] # remove first character

	for f in imaser_fields: # go through each field
		t = s[ (f[1]-1):(f[1]+f[2]-1) ]
		n = int( ("0x"+t), 16 )
		val = n*f[3]
		#print "%s \t %f %s" % (f[0], val, f[4])
		fieldDict[f[0]] = val
	return fieldDict

if __name__ == "__main__":
	# example string for testing
	s = "$41203D4819F157B7882021A4C490CF0D70C01CC0D80EA08509A6900B18D6014CE4B44043B4403B0B29697FE016C5E9CAFDC8C18000CBDC011"
	d = imaser_parse(s)
	print d
	# example output dictionary
	# {'U_varactor': 8.0553, 'UTC_heater': 2.2461800000000003, 'IB_heater': 1.0498450000000001, 
	# 'U_plus5': 4.99968, 'U_HT_ext': 3.521364, 'H_light': 3.8400450000000004, 'C_field': 0.04882, 
	# 'I_purifier': 0.6275940000000001, 'U_batt_B': 28.144730000000003, 
	# 'Amb_temp': 27.619020000000003, 'U_batt_A': 25.43522, 'Meas_H': 2.354088, 
	# 'Unused': 0, 'U_plus18': 17.1886, 'I_HT_ext': 8.1807, 'U_minus5': -0.0, 
	# 'T_heater': 0.751982, 'Boxes_temp': 41.0088, 'I_HT_int': 7.2039, 
	# 'I_dissociator': 0.51282, 'EB_heater': 1.142622, 'U_plus8': 7.92918, 
	# 'I_batt_B': 3.1074450000000002, 'I_batt_A': 0.074481, 'IT_heater': 1.010781, 
	# 'U_minus15': -15.07909, 'IS_heater': 0.937536, 'Sto_heater': 14.704536000000001, 
	# 'U_OCXO': 6.117146, 'ES_heater': 1.054728, 'Pir_heater': 12.488784, 
	# 'U_HT_int': 3.521364, 'Set_H': 5.137786, 'U_405kHz': 11.593892, 
	# 'U_plus15': 15.626000000000001, 'Lock': 1, 'I_boxes': 0.216117, 
	# 'U_plus24': 24.70798, 'I_heater': 0.649439, 'Sto_press': 0.869174}

