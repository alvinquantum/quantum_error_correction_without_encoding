from qiskit import (
    QuantumCircuit,
    ClassicalRegister,
    QuantumRegister,
    transpile
    )  
from qiskit.converters import (
    circuit_to_dag, 
    dag_to_circuit,
    
    )
from qiskit.dagcircuit import DAGOpNode
from copy import deepcopy
import math

def circ_replace_rz(circ: QuantumCircuit, num_target_qubits: int):
    '''For determining the ideal output of the noise estimation circuit.'''
    dag=circuit_to_dag(circ)
    dag=circuit_to_dag(circ)
    new_qc=empty_copy_circ(circ)   
    op_nodes=dag.op_nodes()
    for node in op_nodes:
        # print(node.name)
        if node.name=="rz":
            new_qc.z(node.qargs[0])
        else:
            copy_node(new_qc, node)
    return new_qc

def empty_copy_circ(circ: QuantumCircuit):
    new_circ=deepcopy(circ)
    new_circ.data=[]
    return new_circ


def replace_gates_h_sx_rx(circ: QuantumCircuit):
    '''Replaces h with y and sx with x.'''
    dag=circuit_to_dag(circ)
    new_qc=empty_copy_circ(circ)   

    op_nodes=dag.op_nodes()
    for node in op_nodes:
        # print(node.name)
        if node.name=="h":
            new_qc.y(node.qargs[0])
        elif node.name=="sx" or node.name=="rx":
            new_qc.x(node.qargs[0])
        # elif node.name=="rz":
            # angle=node.op.params
            # z_angles=[0, 2*math.pi, math.pi]
            # s_angles=[math.pi/2, -math.pi/2]
            # dist_to_z=min(z_angles, key=lambda x: abs(x-angle))
            # dist_to_s=min(s_angles, key=lambda x: abs(x-angle))
            # # print(f"args: {node.op.params}")
            # # print(node.qargs)
            # if dist_to_z<dist_to_s:
            # new_qc.z(node.qargs[0].index)
            # elif 
        else:
            copy_node(new_qc, node)
    return new_qc

def copy_node(new_qc, node):
    '''Applies the node to the circuit.'''
    # Copy the node.
    if node.name=="x":
        new_qc.x(node.qargs[0])
    elif node.name=="y":
        new_qc.y(node.qargs[0])
    elif node.name=="z":
        new_qc.z(node.qargs[0])
    elif node.name=="h":
        new_qc.h(node.qargs[0])
    elif node.name=="s":
        new_qc.s(node.qargs[0])
    elif node.name=="sdg":
        new_qc.sdg(node.qargs[0])
    elif node.name=="t":
        new_qc.t(node.qargs[0])
    elif node.name=="tdg":
        new_qc.tdg(node.qargs[0])
    elif node.name=="cx":
        new_qc.cx(node.qargs[0], node.qargs[1])
    elif node.name=="cz":
        new_qc.cz(node.qargs[0], node.qargs[1])
    elif node.name=="cs":
        new_qc.cs(node.qargs[0], node.qargs[1])
    elif node.name=="csdg":
        new_qc.csdg(node.qargs[0], node.qargs[1])
    elif node.name=="cp":
        new_qc.cp(node.op.params[0], node.qargs[0], node.qargs[1])
    elif node.name=="swap":
        new_qc.swap(node.qargs[0], node.qargs[1])
    elif node.name=="rx":
        new_qc.rx(node.op.params[0], node.qargs[0])
    elif node.name=="rz":
        new_qc.rz(node.op.params[0], node.qargs[0])
    elif node.name=="sx":
        new_qc.sx(node.qargs[0])
    elif node.name=="measure":
        # print(node.qargs[0]._index, node.op.params, type(node.cargs[0]))
        new_qc.measure(node.qargs[0], node.cargs)
    elif node.name=="id":
        new_qc.id(node.qargs[0])
    elif node.name=="reset":
        new_qc.reset(node.qargs[0])
    elif node.name=="if_else":
        # print(node.qargs)
        # print(node.cargs)
        # print(node.op.params)
        # assert False, "error"
        with new_qc.if_test((node.cargs[0], 1)):
            new_qc.z(node.qargs[0])
    elif node.name=="barrier":
        new_qc.barrier()   
        
    else:
        # We have overlooked a gate type.
        assert False, f"{node.name} gate wasn't matched in the DAG."

def count_gates(qc: QuantumCircuit):
    gate_count = { qubit: 0 for qubit in qc.qubits }
    for gate in qc.data:
        for qubit in gate.qubits:
            gate_count[qubit] += 1
    return gate_count

def remove_idle_wires(qc: QuantumCircuit):
    qc_out = qc.copy()
    gate_count = count_gates(qc_out)
    for qubit, count in gate_count.items():
        if count == 0:
            qc_out.qubits.remove(qubit)
    return qc_out

def create_perfect_dicke_k1(num_qubits, shots):
    state0=["0"]*num_qubits
    coef=int(shots/num_qubits)
    new_counts={}
    for idx in range(num_qubits):
        new_state=deepcopy(state0)
        new_state[idx]="1"
        new_counts["".join(new_state)]=coef
    return new_counts

def create_perfect_ghz(num_qubits, shots):
    state0="0"*num_qubits
    state1="1"*num_qubits
    coef=int(shots/2)
    new_counts={state0: coef, state1: coef}
    return new_counts

