/* Con que tarjeta se realizaron mas compras*/
SELECT cardholder_name , sum(valor) as totalcomprado
FROM "Factura", "Tarjeta"
WHERE "Factura".id_tarjeta = "Tarjeta".id_tarjeta
GROUP BY "Tarjeta".cardholder_name
ORDER BY totalcomprado DESC;

/* Cuantos libros se vendieron */
/* Que usuario realizo mas compras */

/* Que editorial tiene los precios mas bajos*/

/* Con que tarjeta se realizo mas compras*/
SELECT id_tarjeta, Sum(cantidad)
FROM "Factura"
GROUP BY id_tarjeta


/* Numero de usuarios activos por dia*/
SELECT CAST( fecha AS DATE ) as dia, COUNT( id_usuario ) as usuarios_por_dia
FROM "Factura"
WHERE fecha_fin IS NOT NULL
GROUP BY CAST( fecha AS DATE )


/* productos comprados entre fechas*/
SELECT *
FROM "Factura"
WHERE fecha BETWEEN '20170511' AND '20170522'
