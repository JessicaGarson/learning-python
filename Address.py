#Use raw_input() to allow a user to type an address 
#If that address contains a quadrant (NW, NE, SE, SW), then add it to that quadrant's list. 
#Allow user to enter 3 addresses; after three, print the length and contents of each list.

ne_adds = []
nw_adds = []
se_adds = []
sw_adds = []

address1 = raw_input("Whats your address?")
address2 = raw_input("Whats your work address?")
address3 = raw_input("Whats your address of your favorite bar?")

address1 = address.upper()
address2 = address.upper()
address3 = address.upper()

address_as_a_list1 = address1.split(' ')
print address_as_a_list1
address_as_a_list2 = address2.split(' ')
print address_as_a_list2
address_as_a_list3 = address3.split(' ')
print address_as_a_list3

all_addresses_as_list = address_as_a_list1 + address_as_a_list2 + address_as_a_list3

if NW in all_addresses_as_list:
	nw_adds.append()
