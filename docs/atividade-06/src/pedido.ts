export type Item = { preco: number };

export function calcularTotalPedido(itens: Item[], valorMinimo: number): number {
  const total = itens.reduce((acc, item) => acc + item.preco, 0);
  if (total < valorMinimo) {
    throw new Error("Valor mínimo do pedido não atingido");
  }
  return total;
}
