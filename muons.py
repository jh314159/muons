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

def leptons_from_event(tree):
	'''
	Get list of leptons as TLorentz objects
	'''
	leptons = []
	n_lepton = data.lep_n
	for i in range(n_lepton):
		p = four_momentum(i, tree)
		leptons.append(p)
	return leptons

def pairs_from_particles(particles):
	'''
	Get all possible pairs of particles
	'''
	pairs = []
	n_particles = len(particles)
	for i in range(n_particles-1):
		for j in range(i+1, n_particles):
			pair = (particles[i], particles[j])
			pairs.append(pair)
	return pairs

def mass_of_pairs(pair):
	p1 = pair[0]
	p2 = pair[1]
	ppair = p1 + p2
	return ppair.M()

data = TChain("mini")
data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

num_events = data.GetEntries()

nbins = 50 # Histogram number of bins
h_mpair = TH1F("mpair", "Invariant mass of lepton pairs", nbins, 0, 200)

num_events = 10000 # Number of events to process
for i in range(num_events):
	data.GetEntry(i) # Read in the entry	
	# Get number of leptons for the event
	n_leptons = data.lep_n
	if n_leptons >= 2: # Look for pairs
		leptons = leptons_from_event(data)
		pairs = pairs_from_particles(leptons)
		#assert(n_leptons==2)
		for pair in pairs:
			mpair = mass_of_pairs(pair)/1000. # Convert to GeV
			h_mpair.Fill(mpair)
		
		
h_mpair.Draw()
raw_input("Exit?")


