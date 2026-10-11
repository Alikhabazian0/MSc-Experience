data02 = np.loadtxt(r'Data_5\0.2.txt')
data05 = np.loadtxt(r'Data_5\0.5.txt')
data08 = np.loadtxt(r'Data_5\0.8.txt')
dataset = pd.DataFrame({'data0.2':data02, 'data0.5':data05})
correlation = dataset.corr(method='pearson')
correlation
