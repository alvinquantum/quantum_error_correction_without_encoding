This provides the data for the paper, "Quantum Error Correction Without Encoding via the Circulant Structure of Pauli Noise and the Fast Fourier Transform." arXiv: https://arxiv.org/abs/2501.01953.

The code uses: <br/>
qiskit==1.3.0 <br/>
qiskit-aer==0.15.1 <br/>
qiskit-algorithms==0.3.0 <br/>
qiskit-ibm-runtime==0.31.0 <br/>
qiskit-optimization==0.6.1 <br/>
qiskit-qasm3-import==0.5.1 <br/>

There are folders for each experiment. You can delete the json files if you want to start experiments from scratch (they are also automatically overwritten). There are Jupyter Notebooks in each experiment folder. The ones with hardware are for quantum hardware and the ones with sim are for simulations. The experiments are conducted in two stages: 1 to generate the counts and 2 to correct the output distribution. The notebooks are numbered 1 and 2 accordingly. The quantum hardware executions require an ibm quantum account. To execute the job on hardware, uncomment the line ```result_noisy=noisy_sampler.run([circ, noise_est_circ], shots=SHOTS).result()``` and comment out the following lines: <br/>
```job = service.job('job_string')``` <br/>
```result_noisy = job.result()``` <br/>
Note that the noise on a quantum computer fluctuates so the harware results may not replicate exactly. The simulation results should be nearly identical.

Ex: <br/>
exper_hardware1.ipynb <br/>
exper_hardware2.ipynb <br/>
exper_sim1.ipynb <br/>
exper_sim2.ipynb <br/>


