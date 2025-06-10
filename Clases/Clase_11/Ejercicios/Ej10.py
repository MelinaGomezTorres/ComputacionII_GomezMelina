from multiprocessing import Process, RLock, Manager
import time

class CuentaBancaria:
    def __init__(self, saldo, lock):
        self.saldo = saldo
        self.lock = lock

    def depositar(self, monto):
        with self.lock:
            self.saldo.value += monto
            self.log_operacion("depositar", monto)

    def retirar(self, monto):
        with self.lock:
            if self.saldo.value >= monto:
                self.saldo.value -= monto
                self.log_operacion("retirar", monto)

    def log_operacion(self, op, monto):
        print(f"{op} {monto} - Saldo: {self.saldo.value}")

def operar(cuenta):
    cuenta.depositar(100)
    cuenta.retirar(50)

if __name__ == "__main__":
    with Manager() as manager:
        saldo = manager.Value('i', 100)
        lock = RLock()
        cuenta = CuentaBancaria(saldo, lock)
        procesos = [Process(target=operar, args=(cuenta,)) for _ in range(4)]
        for p in procesos: p.start()
        for p in procesos: p.join()

