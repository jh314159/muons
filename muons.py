#! /usr/bin/env python

from ROOT import TChain

data = TChain("mini")
data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

num_events = data.GetEntries()
print ("Number of events: "), num_events

# Number of events to process
num_events = 100
for i in range(num_events):
	# Read in the entry
	data.GetEntry(i)
	
	# Get number of leptons for the event
	n_leptons = data.lep_n
	if n_leptons >= 2: # Look for pairs
		print "Number of leptons for event ", i, " is ", n_leptons
		assert(n_leptons==2)
		pt1 = data.lep_pt[0] # Get pt for leptons
		pt2 = data.lep_pt[1]			
		print "Lepton pts are:", pt1, " and ", pt2
