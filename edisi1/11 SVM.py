#mengimport numpy, pandas dan scikit-learn
import numpy as np
import pandas as pd
from sklearn.svm import SVC

#membaca dataset dari file ke pandas dataFrame
irisDataset = pd.read_csv('dataset/klasifikasi_dataset_iris.csv', delimiter=',', header=0)
#mengubah kelas (kolom "Species") dari string ke unique-integer
irisDataset["Species"] = pd.factorize(irisDataset.Species)[0]
#menghapus kolom "Id"
irisDataset = irisDataset.drop(labels="Id", axis=1)

#mengubah dataframe ke array numpy
irisDataset = irisDataset.as_matrix()

#membagi dataset, 40 baris data untuk training dan 20 baris data untuk testing
dataTraining = np.concatenate((irisDataset[0:40,:],irisDataset[50:90,:]), axis=0)
dataTesting = np.concatenate((irisDataset[40:50,:], irisDataset[90:100,:]), axis=0)
#memecah dataset ke input dan label
inputTraining = dataTraining[:,0:4]
inputTesting = dataTesting[:,0:4]
labelTraining = dataTraining[:,4]
labelTesting = dataTesting[:, 4]

#mendefinisikan klasifier SVM
#SCV adalah SVM support multikelas dan sistem kernel
#dalam kasus ini, SVC mempunyai dua parameter,
#yaitu C adan gamma dari kernel RBF
model = SVC(C=10, cache_size=200,
    decision_function_shape='ovr', gamma=1.0, kernel='rbf',
    max_iter=-1, random_state=None,
    tol=0.00001, verbose=False)
#mentraining model
model = model.fit(inputTraining, labelTraining)
#memprediski input data testing
hasilPrediksi = model.predict(inputTesting)
print("label sebenarnya ", labelTesting)
print("hasil prediksi: ", hasilPrediksi)
#menghitung akurasi
prediksiBenar = (hasilPrediksi == labelTesting).sum()
prediksiSalah = (hasilPrediksi != labelTesting).sum()
print("prediksi benar: ", prediksiBenar, " data")
print("prediksi salah: ", prediksiSalah, " data")
print("akurasi: ", prediksiBenar/(prediksiBenar+prediksiSalah) * 100, "%")
