#! /usr/bin/env python

from ROOT import TChain

data = TChain("mini")
data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

num_events = data.GetEntries()
print ("Number of events: "), num_events

