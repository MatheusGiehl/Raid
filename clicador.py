"""Clica repetidamente em uma posicao escolhida pelo usuario.

Instalacao:
    pip install pyautogui
"""

from __future__ import annotations

import time

import pyautogui


INTERVALO_SEGUNDOS = 20


def main() -> None:
    # Mover o mouse para o canto superior esquerdo interrompe o PyAutoGUI
    # imediatamente, servindo como uma parada de emergencia adicional ao Ctrl+C.
    pyautogui.FAILSAFE = True

    input(
        "Posicione o mouse no local desejado e pressione Enter para salvar a posicao..."
    )
    posicao = pyautogui.position()

    print(
        f"Posicao salva: ({posicao.x}, {posicao.y}). "
        f"Clicando a cada {INTERVALO_SEGUNDOS} segundos.\n"
        "Para parar, pressione Ctrl+C ou mova o mouse para o canto superior esquerdo."
    )

    try:
        while True:
            pyautogui.click(posicao.x, posicao.y)
            print(f"Clique feito em {time.strftime('%H:%M:%S')}")
            time.sleep(INTERVALO_SEGUNDOS)
    except KeyboardInterrupt:
        print("\nScript encerrado.")


if __name__ == "__main__":
    main()
