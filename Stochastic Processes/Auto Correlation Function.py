def auto_correlation_function(data):
    n = len(data)
    mean = np.mean(data)
    autocorr = np.correlate(data - mean, data - mean, mode='full') / (np.var(data) * n)
    return np.average(autocorr[n - 1:]), autocorr[n - 1:]


autocorr_02, autocorr2 = auto_correlation_function(data02)
autocorr_05, autocorr5 = auto_correlation_function(data05)
autocorr_08, autocorr8 = auto_correlation_function(data08)

print("Auto-correlation function(0.2.txt): ",autocorr_02,'\n',"Auto-correlation function(0.5.txt):",autocorr_05,
      '\n',"Auto-correlation function(0.8.txt)",autocorr_08)


##answers:

#Auto-correlation function(0.2.txt):  0.0004882812500000002 
#Auto-correlation function(0.5.txt): 0.00048828125 
#Auto-correlation function(0.8.txt) 0.0004882812500000009
