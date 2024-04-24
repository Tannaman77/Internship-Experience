
from sys import argv
import ROOT
import numpy as np 
import matplotlib.pyplot as plt


plot_wavefor = True

f = ROOT.TFile(argv[1])
tree = f.Get("waveformTree")
tree.GetEntry()
tot_ent = tree.GetEntries()
ts = np.arange(0,len(tree.waveform)*4,4)


#Containers for all the stored data
Amp_all = []
Area1_all = []
Area2_all = []

#Equalizing for the noise

f2 = ROOT.TFile("LDNoIntensity_Room.time.root")
plant = f2.Get("waveformTree")
N = plant.GetEntries()
plant.GetEntry(0)
waveform_average = (np.array(plant.waveform)-plant.baseline)*plant.polarity
for x in range(1,N):
	plant.GetEntry(x)
	waveform_average += (np.array(plant.waveform)-plant.baseline)*plant.polarity
waveform_average /= N
#polarity_value = int(input("Enter the polarity of the waveform: "))

#IF you cant get the program assimilated using functions then you can also do int(input("Enter threshold")) to get have the user input the value for thresholds


def Func1(threshold):
	for j,entry in enumerate(tree):
		W = (np.array(entry.waveform)-entry.baseline)*entry.polarity
		equalized_wf = W - waveform_average
		pulse = False
		ys = []
		Amplitudes = []
		AreaM1 = []
		AreaM2 = []
		XTime = []
		for k,(x,y) in enumerate(zip(ts,W)):
			if y >= threshold and all(w>=threshold for w in W[k:k+3]) and pulse == False:
				pulse = True
				XTime.append(x)
				k_low = 0 if k-2<0 else k-2
				k_high = len(W)-1 if k+20>len(W) else k+20
				AreaM2.append(sum(W[k_low:k_high]))

			elif all(w < threshold for w in W[k-2:k+1]) and pulse == True:
				pulse = False
				Amplitudes.append(max(ys))
				AreaM1.append(sum(ys))
				ys = []
			if pulse == True:
				ys.append(y)
					
			
		for x in Amplitudes:
			Amp_all.append(x)
		for x in AreaM1:
			Area1_all.append(x)
		for x in AreaM2:
			Area2_all.append(x)
	plot_waveform = True
	plt.figure()
	plt.subplot(2,1,1)
#plt.plot(ts,equalized_wf, c ='r')
	plt.plot(ts,W)
	plt.subplot(2,1,2)
	plt.plot(ts,equalized_wf,c = 'r')
	plt.xlabel("Time (ns)")
	plt.ylabel("Volt Amplitudes")
	plt.title("Waveform Graph")
	plt.scatter(XTime, Amplitudes,c = 'k')
	plt.axhline(y = threshold, xmin = 0, xmax = 1, c = 'g')
	plt.show()
def Func2():
	pass	


#for i in range(tot_ent):
value = int(input("Enter the designated trigger value: "))
Func1(value)

#Histograms/Canvas' initializations

Hist_Ampl = ROOT.TH1D("Hist1", "Histogrami Amplitudes", 70, 0,max(Amp_all))
Hist_A1 = ROOT.TH1D("Hist2", "Histogram Method 1", 60, 0,max(Area1_all))
Hist_A2 = ROOT.TH1D("Hist3", "Histogram Method 2", 70, 0,max(Area2_all))
canvas = ROOT.TCanvas("myCanvas", "SIPM Tests", 800, 600)
canvas.Divide(1,3)
#h_spec = ROOT.TH1D("H_spec", "Spectrum Example 1", 70, -20, 120)
#c_spec = ROOT.TCanvas("C_spec", "Canvas 1", 800, 600)
#c_spec.SetLogy()

#Filling the histograms with data
for x in Amp_all:
	Hist_Ampl.Fill(x)
for x in Area1_all:
	Hist_A1.Fill(x)
for x in Area2_all:
	Hist_A2.Fill(x)

#Using Fit
res_Ampl = Hist_Ampl.Fit("gaus", "RQS", "SAME", 14, 20)
res_A1= Hist_A1.Fit("gaus", "RQS", "SAME", 45, 80)
res_A2 = Hist_A2.Fit("gaus", "RQS", "SAME", 120, 230)



canvas.cd(1)
Hist_Ampl.Draw()
canvas.cd(2)
Hist_A1.Draw()
canvas.cd(3)
Hist_A2.Draw()
input('Press anything to exit')




#Second Part of the code
#zoom_ts = ts[np.logical_and(ts > 600, ts < 750)]

		
