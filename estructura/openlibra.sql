/************ Add: Sequences ***************/

/* Autogenerated Sequences */

CREATE SEQUENCE "public"."Autor_id_autor_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Autor_id_autor_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Categoria_id_categoria_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Categoria_id_categoria_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Ciudad_id_ciudad_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Ciudad_id_ciudad_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Editorial_id_editorial_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Editorial_id_editorial_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Funcion_id_funcion_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Funcion_id_funcion_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Idioma_id_idioma_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Idioma_id_idioma_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Interface_id_interface_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Interface_id_interface_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Libro_id_producto_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Libro_id_producto_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Pais_id_pais_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Pais_id_pais_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Producto_id_producto_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Producto_id_producto_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Programa_id_producto_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Programa_id_producto_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Rol_id_rol_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Rol_id_rol_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Session_id_session_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Session_id_session_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Sistema_Operativo_id_sistema_operativo_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Sistema_Operativo_id_sistema_operativo_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Tarjeta_id_tarjeta_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Tarjeta_id_tarjeta_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Tipo_UI_id_tipo_ui_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Tipo_UI_id_tipo_ui_seq" IS 'DbWrench Autogenerated Sequence.';

CREATE SEQUENCE "public"."Usuario_id_usuario_seq" INCREMENT BY 1;
COMMENT ON SEQUENCE "public"."Usuario_id_usuario_seq" IS 'DbWrench Autogenerated Sequence.';




/************ Update: Tables ***************/

/******************** Add Table: "public"."Autor" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Autor"
(
	id_autor INTEGER DEFAULT nextval('public."Autor_id_autor_seq"'::regclass) NOT NULL,
	nombres VARCHAR(200) NOT NULL,
	apellido_paterno VARCHAR(200) NOT NULL,
	apellido_materno VARCHAR(200) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Autor" ADD CONSTRAINT "pkAutor"
	PRIMARY KEY (id_autor);


/******************** Add Table: "public"."Categoria" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Categoria"
(
	id_categoria INTEGER DEFAULT nextval('public."Categoria_id_categoria_seq"'::regclass) NOT NULL,
	"Id_Editorial" INTEGER NOT NULL,
	nombre_cat VARCHAR(200) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Categoria" ADD CONSTRAINT "pkCategoria"
	PRIMARY KEY (id_categoria);


/******************** Add Table: "public"."Ciudad" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Ciudad"
(
	id_ciudad INTEGER DEFAULT nextval('public."Ciudad_id_ciudad_seq"'::regclass) NOT NULL,
	id_pais INTEGER NOT NULL,
	nombre_ciu VARCHAR(200) NOT NULL,
	codigo_postal INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Ciudad" ADD CONSTRAINT "pkCiudad"
	PRIMARY KEY (id_ciudad);


/******************** Add Table: "public"."Desposito_Bancario" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Desposito_Bancario"
(
	"Id_DepositoBancario" INTEGER NOT NULL,
	nro_cuenta VARCHAR(200) NOT NULL,
	banco VARCHAR(200) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Desposito_Bancario" ADD CONSTRAINT "pkDesposito_Bancario"
	PRIMARY KEY ("Id_DepositoBancario");


/******************** Add Table: "public"."Editorial" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Editorial"
(
	id_editorial INTEGER DEFAULT nextval('public."Editorial_id_editorial_seq"'::regclass) NOT NULL,
	nombre_edi VARCHAR(200) NOT NULL,
	fundacion DATE NOT NULL,
	pagina VARCHAR(200) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Editorial" ADD CONSTRAINT "pkEditorial"
	PRIMARY KEY (id_editorial);


/******************** Add Table: "public"."Factura" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Factura"
(
	id_producto INTEGER NOT NULL,
	fecha TIMESTAMP NOT NULL,
	id_usuario INTEGER NOT NULL,
	id_ciudad INTEGER NULL,
	direccion VARCHAR(200) NULL,
	id_tarjeta INTEGER NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Factura" ADD CONSTRAINT "pkFactura"
	PRIMARY KEY (id_producto, fecha);


/******************** Add Table: "public"."Funcion" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Funcion"
(
	id_funcion INTEGER DEFAULT nextval('public."Funcion_id_funcion_seq"'::regclass) NOT NULL,
	nombre_f VARCHAR(200) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Funcion" ADD CONSTRAINT "pkFuncion"
	PRIMARY KEY (id_funcion);


/******************** Add Table: "public"."Funcion_Interface" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Funcion_Interface"
(
	id_funcion INTEGER NOT NULL,
	id_interface INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Funcion_Interface" ADD CONSTRAINT "pkFuncion_Interface"
	PRIMARY KEY (id_funcion, id_interface);


/******************** Add Table: "public"."Idioma" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Idioma"
(
	id_idioma INTEGER DEFAULT nextval('public."Idioma_id_idioma_seq"'::regclass) NOT NULL,
	nombre_idio VARCHAR(200) NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Idioma" ADD CONSTRAINT "pkIdioma"
	PRIMARY KEY (id_idioma);


/******************** Add Table: "public"."Interface" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Interface"
(
	id_interface INTEGER DEFAULT nextval('public."Interface_id_interface_seq"'::regclass) NOT NULL,
	id_tipo_ui INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Interface" ADD CONSTRAINT "pkInterface"
	PRIMARY KEY (id_interface);


/******************** Add Table: "public"."Libro" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Libro"
(
	id_producto INTEGER DEFAULT nextval('public."Libro_id_producto_seq"'::regclass) NOT NULL,
	id_categoria INTEGER NULL,
	id_editorial INTEGER NULL,
	id_idioma INTEGER NULL,
	titulo VARCHAR(200) NOT NULL,
	descripcion VARCHAR(200) NOT NULL,
	"ISB" VARCHAR(200) NOT NULL,
	fecha_publicacion DATE NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Libro" ADD CONSTRAINT "pkLibro"
	PRIMARY KEY (id_producto);


/******************** Add Table: "public"."Libro_Autores" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Libro_Autores"
(
	id_autor INTEGER NOT NULL,
	id_producto INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Libro_Autores" ADD CONSTRAINT "pkLibro_Autores"
	PRIMARY KEY (id_autor, id_producto);


/******************** Add Table: "public"."Oferta" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Oferta"
(
	"Id_Oferta" INTEGER NOT NULL,
	porcenta_descuento INTEGER NOT NULL,
	fecha_inicio TIMESTAMP NULL,
	fecha_fin TIMESTAMP NULL,
	"Id_Producto" INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Oferta" ADD CONSTRAINT "pkOferta"
	PRIMARY KEY ("Id_Oferta");


/******************** Add Table: "public"."Pais" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Pais"
(
	id_pais INTEGER DEFAULT nextval('public."Pais_id_pais_seq"'::regclass) NOT NULL,
	nombre_pai VARCHAR(200) NOT NULL,
	codigo_pais INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Pais" ADD CONSTRAINT "pkPais"
	PRIMARY KEY (id_pais);


/******************** Add Table: "public"."Producto" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Producto"
(
	id_producto INTEGER DEFAULT nextval('public."Producto_id_producto_seq"'::regclass) NOT NULL,
	"tamanio_archivo_KB" INTEGER NOT NULL,
	precio INTEGER NOT NULL,
	porcentaje_descuento INTEGER NOT NULL,
	oferta_inicio DATE NULL,
	oferta_fin DATE NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Producto" ADD CONSTRAINT "pkProducto"
	PRIMARY KEY (id_producto);


/******************** Add Table: "public"."Programa" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Programa"
(
	id_producto INTEGER DEFAULT nextval('public."Programa_id_producto_seq"'::regclass) NOT NULL,
	id_sistema_operativo INTEGER NULL,
	fecha_activacion DATE NULL,
	fecha_expiracion DATE NULL,
	nombre_pro VARCHAR(200) NOT NULL,
	version VARCHAR(100) NOT NULL,
	dominio_32_64 VARCHAR(5) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Programa" ADD CONSTRAINT "pkPrograma"
	PRIMARY KEY (id_producto);


/******************** Add Table: "public"."Rol" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Rol"
(
	id_rol INTEGER DEFAULT nextval('public."Rol_id_rol_seq"'::regclass) NOT NULL,
	nombre_r VARCHAR(200) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Rol" ADD CONSTRAINT "pkRol"
	PRIMARY KEY (id_rol);


/******************** Add Table: "public"."Rol_Funcion" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Rol_Funcion"
(
	id_rol INTEGER NOT NULL,
	id_funcion INTEGER NOT NULL,
	activo BOOL DEFAULT False NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Rol_Funcion" ADD CONSTRAINT "pkRol_Funcion"
	PRIMARY KEY (id_rol, id_funcion);


/******************** Add Table: "public"."Session" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Session"
(
	id_session INTEGER DEFAULT nextval('public."Session_id_session_seq"'::regclass) NOT NULL,
	id_usuario INTEGER NOT NULL,
	pid INTEGER DEFAULT pg_backend_pid() NOT NULL,
	fecha TIMESTAMP DEFAULT now() NOT NULL,
	activo BOOL DEFAULT False NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Session" ADD CONSTRAINT "pkSession"
	PRIMARY KEY (id_session, id_usuario);


/******************** Add Table: "public"."Sistema_Operativo" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Sistema_Operativo"
(
	id_sistema_operativo INTEGER DEFAULT nextval('public."Sistema_Operativo_id_sistema_operativo_seq"'::regclass) NOT NULL,
	nombre_so VARCHAR(200) NOT NULL,
	version VARCHAR(200) NOT NULL,
	arquitectura VARCHAR(2) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Sistema_Operativo" ADD CONSTRAINT "pkSistema_Operativo"
	PRIMARY KEY (id_sistema_operativo);


/******************** Add Table: "public"."Tarjeta" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Tarjeta"
(
	id_tarjeta INTEGER DEFAULT nextval('public."Tarjeta_id_tarjeta_seq"'::regclass) NOT NULL,
	nombre_tar VARCHAR(200) NOT NULL,
	nro_tarjeta INTEGER NOT NULL,
	cardholder_name VARCHAR(200) NOT NULL,
	fecha_expiracion DATE NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Tarjeta" ADD CONSTRAINT "pkTarjeta"
	PRIMARY KEY (id_tarjeta);


/******************** Add Table: "public"."Tipo_UI" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Tipo_UI"
(
	id_tipo_ui INTEGER DEFAULT nextval('public."Tipo_UI_id_tipo_ui_seq"'::regclass) NOT NULL,
	nombre_t_u VARCHAR(200) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Tipo_UI" ADD CONSTRAINT "pkTipo_UI"
	PRIMARY KEY (id_tipo_ui);


/******************** Add Table: "public"."User_Rol" ************************/

/* Build Table Structure */
CREATE TABLE "public"."User_Rol"
(
	id_usuario INTEGER NOT NULL,
	id_rol INTEGER NOT NULL,
	activo BOOL DEFAULT False NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."User_Rol" ADD CONSTRAINT "pkUser_Rol"
	PRIMARY KEY (id_usuario, id_rol);


/******************** Add Table: "public"."Usuario" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Usuario"
(
	id_usuario INTEGER DEFAULT nextval('public."Usuario_id_usuario_seq"'::regclass) NOT NULL,
	nombre_u VARCHAR(200) NOT NULL,
	password VARCHAR(200) NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Usuario" ADD CONSTRAINT "pkUsuario"
	PRIMARY KEY (id_usuario);


/******************** Add Table: "public"."Venta_Libro" ************************/

/* Build Table Structure */
CREATE TABLE "public"."Venta_Libro"
(
	"Id_Venta_Libro" INTEGER NOT NULL,
	"Id_Producto" INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE "public"."Venta_Libro" ADD CONSTRAINT "pkVenta_Libro"
	PRIMARY KEY ("Id_Venta_Libro");





/************ Add Foreign Keys ***************/

/* Add Foreign Key: fk_Ciudad_Pais */
ALTER TABLE "public"."Ciudad" ADD CONSTRAINT "fk_Ciudad_Pais"
	FOREIGN KEY (id_pais) REFERENCES "public"."Pais" (id_pais)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Venta_Producto_Ciudad */
ALTER TABLE "public"."Factura" ADD CONSTRAINT "fk_Venta_Producto_Ciudad"
	FOREIGN KEY (id_ciudad) REFERENCES "public"."Ciudad" (id_ciudad)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Venta_Producto_Producto */
ALTER TABLE "public"."Factura" ADD CONSTRAINT "fk_Venta_Producto_Producto"
	FOREIGN KEY (id_producto) REFERENCES "public"."Producto" (id_producto)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Venta_Producto_Tarjeta */
ALTER TABLE "public"."Factura" ADD CONSTRAINT "fk_Venta_Producto_Tarjeta"
	FOREIGN KEY (id_tarjeta) REFERENCES "public"."Tarjeta" (id_tarjeta)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Venta_Programa_Usuario */
ALTER TABLE "public"."Factura" ADD CONSTRAINT "fk_Venta_Programa_Usuario"
	FOREIGN KEY (id_usuario) REFERENCES "public"."Usuario" (id_usuario)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Funcion_Interface_Funcion */
ALTER TABLE "public"."Funcion_Interface" ADD CONSTRAINT "fk_Funcion_Interface_Funcion"
	FOREIGN KEY (id_funcion) REFERENCES "public"."Funcion" (id_funcion)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Funcion_Interface_Interface */
ALTER TABLE "public"."Funcion_Interface" ADD CONSTRAINT "fk_Funcion_Interface_Interface"
	FOREIGN KEY (id_interface) REFERENCES "public"."Interface" (id_interface)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Interface_Tipo_UI */
ALTER TABLE "public"."Interface" ADD CONSTRAINT "fk_Interface_Tipo_UI"
	FOREIGN KEY (id_tipo_ui) REFERENCES "public"."Tipo_UI" (id_tipo_ui)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Libro_Categoria */
ALTER TABLE "public"."Libro" ADD CONSTRAINT "fk_Libro_Categoria"
	FOREIGN KEY (id_categoria) REFERENCES "public"."Categoria" (id_categoria)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Libro_Editorial */
ALTER TABLE "public"."Libro" ADD CONSTRAINT "fk_Libro_Editorial"
	FOREIGN KEY (id_editorial) REFERENCES "public"."Editorial" (id_editorial)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Libro_Idioma */
ALTER TABLE "public"."Libro" ADD CONSTRAINT "fk_Libro_Idioma"
	FOREIGN KEY (id_idioma) REFERENCES "public"."Idioma" (id_idioma)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Libro_Producto */
ALTER TABLE "public"."Libro" ADD CONSTRAINT "fk_Libro_Producto"
	FOREIGN KEY (id_producto) REFERENCES "public"."Producto" (id_producto)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Libro_Autores_Autor */
ALTER TABLE "public"."Libro_Autores" ADD CONSTRAINT "fk_Libro_Autores_Autor"
	FOREIGN KEY (id_autor) REFERENCES "public"."Autor" (id_autor)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Libro_Autores_Libro */
ALTER TABLE "public"."Libro_Autores" ADD CONSTRAINT "fk_Libro_Autores_Libro"
	FOREIGN KEY (id_producto) REFERENCES "public"."Libro" (id_producto)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Oferta_Producto */
ALTER TABLE "public"."Oferta" ADD CONSTRAINT "fk_Oferta_Producto"
	FOREIGN KEY ("Id_Producto") REFERENCES "public"."Producto" (id_producto)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Programa_Producto */
ALTER TABLE "public"."Programa" ADD CONSTRAINT "fk_Programa_Producto"
	FOREIGN KEY (id_producto) REFERENCES "public"."Producto" (id_producto)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Programa_SistemaOperativo */
ALTER TABLE "public"."Programa" ADD CONSTRAINT "fk_Programa_SistemaOperativo"
	FOREIGN KEY (id_sistema_operativo) REFERENCES "public"."Sistema_Operativo" (id_sistema_operativo)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Rol_Funcion_Funcion */
ALTER TABLE "public"."Rol_Funcion" ADD CONSTRAINT "fk_Rol_Funcion_Funcion"
	FOREIGN KEY (id_funcion) REFERENCES "public"."Funcion" (id_funcion)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Rol_Funcion_Rol */
ALTER TABLE "public"."Rol_Funcion" ADD CONSTRAINT "fk_Rol_Funcion_Rol"
	FOREIGN KEY (id_rol) REFERENCES "public"."Rol" (id_rol)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_Session_Usuario */
ALTER TABLE "public"."Session" ADD CONSTRAINT "fk_Session_Usuario"
	FOREIGN KEY (id_usuario) REFERENCES "public"."Usuario" (id_usuario)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_User_Rol_Rol */
ALTER TABLE "public"."User_Rol" ADD CONSTRAINT "fk_User_Rol_Rol"
	FOREIGN KEY (id_rol) REFERENCES "public"."Rol" (id_rol)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_User_Rol_Usuario */
ALTER TABLE "public"."User_Rol" ADD CONSTRAINT "fk_User_Rol_Usuario"
	FOREIGN KEY (id_usuario) REFERENCES "public"."Usuario" (id_usuario)
	ON UPDATE NO ACTION ON DELETE NO ACTION;
