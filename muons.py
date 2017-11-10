#! /usr/bin/env python

from ROOT import TChain, TLorentzVector, TH1F

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

nbins = 50
h_mpair = TH1F("mpair", "Invariant mass of lepton pairs", nbins, 0, 200)

# Number of events to process
num_events = 10000
for i in range(num_events):
	# Read in the entry
	data.GetEntry(i)
	
	# Get number of leptons for the event
	n_leptons = data.lep_n
	if n_leptons >= 2: # Look for pairs
		print "Number of leptons for event ", i, " is ", n_leptons
		#assert(n_leptons==2)
		p1 = four_momentum(0, data)
		p2 = four_momentum(1, data)
		print "First lepton pt from vector", p1.Pt()
		print "Second lepton pt from vector", p2.Pt()
		ppair = p1 + p2
		mpair = ppair.M()/1000. # Convert to Gev
		print "Invariant mass of lepton pair: ", mpair
		h_mpair.Fill(mpair)
		
		print "-------------------------------------------------------"
h_mpair.Draw()
raw_input("Exit?")


