class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Conjunto:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no, valor):
        if no is None:
            return NoArvore(valor)
        
        if valor < no.valor:
            no.esquerda = self._inserir_recursivamente(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir_recursivamente(no.direita, valor)
        
        return no

    def remover(self, valor):
        self.raiz = self._remover_recursivamente(self.raiz, valor)

    def _remover_recursivamente(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self._remover_recursivamente(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_recursivamente(no.direita, valor)
        else:
            # Nó a ser removido encontrado
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            # Nó tem dois filhos, encontre o sucessor em ordem
            valor_min = self._encontrar_valor_min(no.direita)
            no.valor = valor_min
            no.direita = self._remover_recursivamente(no.direita, valor_min)
        
        return no

    def _encontrar_valor_min(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no.valor

    def contem(self, valor):
        return self._contem_recursivamente(self.raiz, valor)

    def _contem_recursivamente(self, no, valor):
        if no is None:
            return False
        
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._contem_recursivamente(no.esquerda, valor)
        else:
            return self._contem_recursivamente(no.direita, valor)

    def _travessia_em_ordem(self, no):
        if no:
            yield from self._travessia_em_ordem(no.esquerda)
            yield no.valor
            yield from self._travessia_em_ordem(no.direita)

    def uniao(self, outro_conjunto):
        novo_conjunto = Conjunto()
        for item in self._travessia_em_ordem(self.raiz):
            novo_conjunto.inserir(item)
        for item in self._travessia_em_ordem(outro_conjunto.raiz):
            novo_conjunto.inserir(item)
        return novo_conjunto

    def intersecao(self, outro_conjunto):
        novo_conjunto = Conjunto()
        for item in self._travessia_em_ordem(self.raiz):
            if outro_conjunto.contem(item):
                novo_conjunto.inserir(item)
        return novo_conjunto

    def diferenca(self, outro_conjunto):
        novo_conjunto = Conjunto()
        for item in self._travessia_em_ordem(self.raiz):
            if not outro_conjunto.contem(item):
                novo_conjunto.inserir(item)
        return novo_conjunto

# Exemplo de Uso:
conjunto1 = Conjunto()
conjunto1.inserir(1)
conjunto1.inserir(2)
conjunto1.inserir(3)

conjunto2 = Conjunto()
conjunto2.inserir(2)
conjunto2.inserir(3)
conjunto2.inserir(4)

uniao_conjunto = conjunto1.uniao(conjunto2)
intersecao_conjunto = conjunto1.intersecao(conjunto2)
diferenca_conjunto = conjunto1.diferenca(conjunto2)

print("União:", list(uniao_conjunto._travessia_em_ordem(uniao_conjunto.raiz)))
print("Interseção:", list(intersecao_conjunto._travessia_em_ordem(intersecao_conjunto.raiz)))
print("Diferença:", list(diferenca_conjunto._travessia_em_ordem(diferenca_conjunto.raiz)))
