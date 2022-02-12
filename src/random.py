"""Docstring."""
from qiskit import Aer, QuantumCircuit, execute, QuantumRegister, ClassicalRegister


class Random:
    """Demo random."""

    def __init__(self):
        """Demo random."""
        self.pow = 2
        self.qasm = Aer.get_backend("qasm_simulator")

    def run(self, number: int) -> int:
        """Run method."""
        nb_qubits = number
        print("Generate random number")

        circ = QuantumRegister(nb_qubits, "the number")
        meas = ClassicalRegister(nb_qubits, "measurement")
        quant_circ = QuantumCircuit(circ, meas)

        for i in range(0, nb_qubits):
            quant_circ.x(i)
        quant_circ.measure(circ, meas)

        job = execute(quant_circ, self.qasm, shots=1, memory=True)

        result_sim = job.result()
        memory = result_sim.get_memory()
        result = int(memory[0], 2) + 1

        return result

    def __repr__(self):
        return f"Random(circuit of: {self.pow})"
