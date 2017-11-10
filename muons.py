#! /usr/bin/env python

from ROOT import TChain, TLorentzVector

def four_momentum(i_lepton, tree):

	pt = tree.lep_pt[i_lepton]
	eta = tree.lep_eta[i_lepton]
	phi = tree.lep_phi[i_lepton]
	E = tree.lep_E[i_lepton]
	p = TLorentzVector()
	p.SetPtEtaPhiE(pt,eta,phi,E)
	return p 

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
		p1 = four_momentum(0, data)
		p2 = four_momentum(1, data)
		print "First lepton pt from vector", p1.Pt()
		print "Second lepton pt from vector", p2.Pt()
		print "-------------------------------------------------------"




