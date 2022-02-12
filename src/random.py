"""Docstring."""
import math
from typing import Union
from qiskit import Aer, QuantumCircuit, execute, IBMQ


class Random:
    """Demo random."""

    def __init__(self):
        """Demo random."""
        self.pow = 2
        self.qasm = Aer.get_backend('qasm_simulator')

    def run(self, number: Union[int, float]) -> Union[int, float]:
        """Run method."""
        nb_qubits = number
        print("Generate random number")
        
        circ = QuantumRegister(nb_qubits, 'the number')
        c = ClassicalRegister(nb_qubits, 'measurement')
        qc = QuantumCircuit(circ, c)
        
        for i in range(0, nb_qubits):
            qc.x(i)
        qc.measure(circ, c)
        
        job = execute(qc, self.qasm, shots=1, memory=True)
        
        result_sim = job.result()
        memory = result_sim.get_memory()
        result = int(memory[0], 2) + 1
    
        return result

    def __repr__(self):
        return f"Random(circuit of: {self.pow})"
