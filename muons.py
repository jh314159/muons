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
	for i in range(n_particles):
		for j in range(i+1, n_particles):
			pair = (particles[i], particles[j])
			pairs.append(pair)
	return pairs

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
		leptons = leptons_from_event(data)
		pairs = pairs_from_particles(leptons)
		#assert(n_leptons==2)
		pair = pairs[0]
		p1 = pair[0]
		p2 = pair[1]
		ppair = p1 + p2
		mpair = ppair.M()/1000. # Convert to Gev
		print "Invariant mass of lepton pair: ", mpair
		h_mpair.Fill(mpair)
		
		print "-------------------------------------------------------"
h_mpair.Draw()
raw_input("Exit?")


