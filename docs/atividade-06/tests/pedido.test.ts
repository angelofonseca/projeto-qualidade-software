import { calcularTotalPedido } from "../src/pedido";

describe("calcularTotalPedido", () => {
  test("deve calcular total quando valor mínimo é atingido", () => {
    const itens = [{ preco: 10 }, { preco: 20 }];
    const valorMinimo = 15;

    const resultado = calcularTotalPedido(itens, valorMinimo);

    expect(resultado).toBe(30);
  });

  test("deve aceitar pedido com total igual ao valor mínimo", () => {
    const itens = [{ preco: 25 }];
    const valorMinimo = 25;

    const resultado = calcularTotalPedido(itens, valorMinimo);

    expect(resultado).toBe(25);
  });

  test("deve lançar erro quando total é menor que o valor mínimo", () => {
    const itens = [{ preco: 5 }];
    const valorMinimo = 20;

    expect(() => calcularTotalPedido(itens, valorMinimo)).toThrow(
      "Valor mínimo do pedido não atingido"
    );
  });
});
