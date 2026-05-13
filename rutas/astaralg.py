import heapq

class AStarAlg:

    def __init__(self):
        pass

    def calcular_heuristica(
        self,
        nodo_actual,
        nodo_objetivo
    ):

        return (
            abs(
                nodo_actual.x
                - nodo_objetivo.x
            )
            +
            abs(
                nodo_actual.y
                - nodo_objetivo.y
            )
        )

    def reconstruir_ruta(
        self,
        nodos_padre,
        nodo_actual
    ):

        ruta = [nodo_actual]

        while nodo_actual in nodos_padre:

            nodo_actual = nodos_padre[
                nodo_actual
            ]

            ruta.append(nodo_actual)

        ruta.reverse()

        return ruta

    def calcular_ruta(
        self,
        nodo_inicio,
        nodo_destino
    ):

        nodos_abiertos = []

        heapq.heappush(
            nodos_abiertos,
            (
                0,
                nodo_inicio.id,
                nodo_inicio
            )
        )

        nodos_padre = {}

        costo_desde_inicio = {
            nodo_inicio: 0
        }

        costo_total_estimado = {
            nodo_inicio:
            self.calcular_heuristica(
                nodo_inicio,
                nodo_destino
            )
        }

        while nodos_abiertos:

            nodo_actual = heapq.heappop(
                nodos_abiertos
            )[2]

            if nodo_actual == nodo_destino:

                return self.reconstruir_ruta(
                    nodos_padre,
                    nodo_actual
                )

            for vecino in nodo_actual.vecinos:

                nuevo_costo = (
                    costo_desde_inicio[
                        nodo_actual
                    ]
                    + 1
                )

                if (
                    vecino not in costo_desde_inicio
                    or
                    nuevo_costo
                    <
                    costo_desde_inicio[
                        vecino
                    ]
                ):

                    nodos_padre[
                        vecino
                    ] = nodo_actual

                    costo_desde_inicio[
                        vecino
                    ] = nuevo_costo

                    costo_total_estimado[
                        vecino
                    ] = (
                        nuevo_costo
                        +
                        self.calcular_heuristica(
                            vecino,
                            nodo_destino
                        )
                    )

                    heapq.heappush(
                        nodos_abiertos,
                        (
                            costo_total_estimado[
                                vecino
                            ],
                            vecino.id,
                            vecino
                        )
                    )

        return []