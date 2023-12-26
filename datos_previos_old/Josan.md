Objetivo del Data Project:
    El Imserso quiere modernizarse y para ello
nos ha pedido que abramos una ronda de
propuestas para agilizar su proceso.
En este caso lo que necesitamos es que
diseñéis una plataforma de asignación de
plazas hoteleras de manera “justa” bajo
vuestros criterios.
Debéis montar un producto, exponerlo y
venderlo como si fuera un concurso público.


Sistema de asignación actual:
    - Cada provincia tiene asignado un cupo de plazas. 
        (Podemos revisar este criterio y dejar un mínimo de reservas por provincia pero otorgando más peso a nuestros criterios. Tendremos que tener en cuenta en el modelo que pueda decidir en función de las plazas disponibles.)

    - El sistema actual distingue/acredita a los solicitantes entre preferentes y no preferentes en función de:
        -La edad. A los menores de 60 años, se les otorga un punto, mientras que a los de 60 se les otorga dos. A partir de ahí, se suma un punto más por cada año cumplido hasta alcanzar el máximo de 20 puntos con 78 años cumplidos. 
        -La situación económica. Si los ingresos de un solicitante superan los 2.100 euros, no se reparten puntos. Si el total es inferior a 402,80 euros, el equivalente al importe de la pensión no contributiva de jubilación o invalidez, se le otorgan 50 puntos, el máximo en esta categoría.
        -La participación en programas anteriores. Participación en el Programa en años anteriores. Se pueden sumar un máximo de 225 puntos.
        -La pertenencia a una familia númerosa o una posible discapacidad. Pertenecía a una familia numerosa. Se reparten 10 puntos si se es familia numerosa especial y cinco si es la catalogada como general.


    A mi parecer:
        - Yo evaluaría todas salvo la pertenencia a familia numerosa, no veo que haya una correlación entre el objetivo de justicia social y tener tres o más hijos.

        - En el caso de la situación económica, yo lo desagregaría en función de la renta media de cada provincia o CCAA, en contra del criterio actual de lotes por provincia. No es lo mismo tener una pensión de 1000 euros y vivir en Murcia, que esa misma pensión y vivir en Barcelona. Deberíamos intentar desagragar al máximo el cp donde se empadrona el solicitante.
        También revisaría los baremos de renta y seguramente intentaría que fuesen móviles, en función de los solicitantes.

        -Deberíamos de explicar tambien en la parte de Negocio porque elegimos el indicador renta: revisar los componentes de la misma para que quede claro nuestro objetivo, puede que alguien cobre poca pensión pero cobre 10000 euros de alquileres al mes.

        -En el caso de un matrimonio (o similar), deberíamos tener en cuenta los ingresos medios de ambos solicitantes de forma que evitemos que si uno tiene una pensión muy baja y el otro muy alta, se lleven el viaje los dos, solamente por el hecho de que no se toma en cuenta la media de las dos pensiones. Podríamos en este caso permitir que solamente el de baja pensión viaje.

        - Respecto a haber participado en programas anteriores, no se me ocurre que forma darle, pero le daría una vuelta. Algo que en función de determinada renta valore o no la obtención de puntos extra.

        -El precio, no sé si es una locura, pero variabilizar el precio en función de la renta es algo que a priori me parece una buena idea.


    Datos que nos harían falta:

        - Una muestra que pasar al modelo de individuos donde tengamos estas magnitudes listas para evaluar.
        - Destinos no sé si inventados o reales.
        - Datos de rentas medias por cp.

    Desarrollo técnico:
        
        -Presentación de negocio
        -Diseño de Arquitectura:
            -Base de datos que recoja tanto los dataframes anteriores como el resultado de nuestro algorítmo
            -Script de Python que evalue cada individuo y genere los resultados.
            -Si podemos yo generaría otro script que según los datos anteriores nos ofreciera la probabilidad de que a un individuo le den el destino que quiere.
            -Podemos generar datos aleatorios con randomUser y utilizar Nifi para guardarlos en nuestra BBDD
        -Solución:Dockerizarlo todo
        -Justificación de piezas:
        -Video 
        -Origen de datos
        -DashBoard
        - Modelos de Datos

Aquí estan los datos de renta media por municipio
https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/irpfmunicipios_ccaa/2021/jrubikf3e948b7305092b26066cced2a0801e4af654b56b.html