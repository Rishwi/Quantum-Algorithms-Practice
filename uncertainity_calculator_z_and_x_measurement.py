# -*- coding: utf-8 -*-
"""2020_qprac.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xAHpBIfC52UmooSCSnq39uJ0_Ppl5goT
"""

from qiskit import *
from qiskit.visualization import plot_histogram

#z measurement
mz = QuantumCircuit(1,1)
mz.measure(0,0)

#x measurement
mx = QuantumCircuit(1,1)
mx.h(0)
mx.measure(0,0)

qc=QuantumCircuit(1)
qc.h(0)
qc.x(0)
qc.y(0)
qc.z(0)
qc.ry(3.1415/2,0)
qc.ry(3.1415/4,0)

# uncertainity measurement

shots = 2**14
uncertainity = 0

for mc in [mz,mx]:
  counts=execute(qc+mc,Aer.get_backend('qasm_simulator'), shots=shots).result().get_counts()
  probs = {}
  for i in ['0','1']:
    if i in counts:
      probs[i]=counts[i]/shots
    else:
      probs[i]=0
  uncertainity += (probs['0']-probs['1'])**2
print("total uncertainity: ", uncertainity)