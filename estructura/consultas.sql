/* Obtener todos los permisos */
SELECT *
FROM public."Usuario"
	INNER JOIN  "User_Rol" ON "Usuario"."id_usuario"="User_Rol"."id_usuario"
	INNER JOIN  "Rol" ON "User_Rol"."id_rol"="Rol"."id_rol"
	INNER JOIN  "Rol_Funcion" ON "Rol"."id_rol"="Rol_Funcion"."id_rol"
	INNER JOIN  "Funcion" ON "Rol_Funcion"."id_funcion"="Funcion"."id_funcion"
	INNER JOIN  "Funcion_Interface" ON "Funcion"."id_funcion"="Funcion_Interface"."id_funcion"
	INNER JOIN  "Interface" ON "Funcion_Interface"."id_interface"="Interface"."id_interface"
	INNER JOIN  "Tipo_UI" ON "Interface"."id_tipo_ui"= "Tipo_UI"."id_tipo_ui"
WHERE "Usuario"."id_usuario" =1;

/* Comprar*/
SELECT 
  "Programa".id_producto,
  "Programa".nombre_pro,
  "Programa".version,
  "Producto"."tamanio_archivo_KB", 
  "Producto".precio,
  "Sistema_Operativo".nombre_so,
  "Sistema_Operativo".version,
  "Sistema_Operativo".arquitectura
FROM 
  public."Programa", 
  public."Producto",
  public."Sistema_Operativo"
WHERE
  "Sistema_Operativo".id_sistema_operativo = "Programa".id_sistema_operativo and
  "Producto".id_producto = "Programa".id_producto;

/* Lista de productos */
SELECT 
  "Producto".id_producto,
  "Producto".nombre_p,
  "Programa".version_pro,
  "Producto"."tamanio_archivo_KB",
  "Sistema_Operativo".nombre_so,
  "Sistema_Operativo".version_so,
  "Sistema_Operativo".arquitectura,
  "Producto".precio
FROM "Programa"
INNER JOIN "Producto" ON "Programa".id_producto = "Producto".id_producto
INNER JOIN "Sistema_Operativo" ON "Programa".id_sistema_operativo = "Sistema_Operativo".id_sistema_operativo;


/*Lista pais_ciudad*/
SELECT 
  "Ciudad".id_ciudad, 
  "Ciudad".id_pais,   
  "Ciudad".nombre_ciu, 
  "Pais".id_pais,    
  "Pais".nombre_pai   
FROM "Ciudad"
INNER JOIN "Pais" ON "Ciudad".id_pais = "Pais".id_pais;
