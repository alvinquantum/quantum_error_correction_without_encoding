# This provides the data for the paper "Quantum Error Correction Without Encoding via the Circulant Structure of Pauli Noise and the Fast Fourier Transform."

The code uses: <br/>
qiskit==1.3.0 <br/>
qiskit-aer==0.15.1 <br/>
qiskit-algorithms==0.3.0 <br/>
qiskit-ibm-runtime==0.31.0 <br/>
qiskit-optimization==0.6.1 <br/>
qiskit-qasm3-import==0.5.1 <br/>

There are jupytner notebooks in each experiment folder. The ones with hardware are for quantum hardware and the ones with sim are for simulations. The experiments are conducted in two stages: 1 to generate the counts and 2 to correct the output distribution. The notbooks are numbered 1 and 2  accordingly. The quantum hardware executions require an ibm quantum account.

Ex:
exper_hardware1.ipynb
exper_hardware2.ipynb
exper_sim1.ipynb
exper_sim2.ipynb


