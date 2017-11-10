#! /usr/bin/env python

from ROOT import TChain, TLorentzVector

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
		eta1 = data.lep_eta[0]
		phi1 = data.lep_phi[0]
		E1 = data.lep_E[0]
		pt2 = data.lep_pt[1]			
		print "Lepton pts are:", pt1, " and ", pt2
		p1 = TLorentzVector()
		p1.SetPtEtaPhiE(pt1, eta1, phi1, E1)
		print "First lepton pt from vector", p1.Pt()
		print "-------------------------------------------------------"




