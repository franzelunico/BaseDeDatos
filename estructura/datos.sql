INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Argentina', 54);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Bolivia', 591);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Brazil', 55);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Chile', 56);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Colombia', 57);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Costa Rica', 506);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Cuba', 53);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Ecuador', 593);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('El Salvador', 503);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('México', 52);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Honduras', 504);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Nicaragua', 505);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Panamá', 507);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Paraguay', 595);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Perú', 51);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('República Dominicana', 849);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Uruguay', 598);
INSERT INTO "Pais"(nombre_pai, codigo_pais) VALUES ('Venezuela', 58);


INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (1, 'buenos aires', 122);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (1, 'catamarca', 122);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (1, 'chaco', 122);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'beni', 122);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'chuquisaca', 44);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'cochabamba', 45);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'la paz', 2);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'oruro', 252);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'pando', 4);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'potosi', 256);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'santa cruz', 3311);
INSERT INTO "Ciudad"(id_pais, nombre_ciu, codigo_postal) VALUES (2, 'tarija', 446);




/******************** GESTION USUARIOS ************************/
INSERT INTO "Tipo_UI"(nombre_t_u) VALUES ('catalogo');
INSERT INTO "Interface"(id_tipo_ui) VALUES (1);

INSERT INTO "Usuario"(nombre_u, password) VALUES ('franz', 'pfranz');
INSERT INTO "Usuario"(nombre_u, password) VALUES ('maria', 'pmaria');
INSERT INTO "Usuario"(nombre_u, password) VALUES ('jose', 'pjose');

INSERT INTO "Rol"(nombre_r) VALUES ('cliente');
INSERT INTO "Rol"(nombre_r) VALUES ('contador');
INSERT INTO "Rol"(nombre_r) VALUES ('administrador');

INSERT INTO "Funcion"(nombre_f) VALUES ('listar_productos');

INSERT INTO "User_Rol"(id_usuario,id_rol) VALUES (1,1);
INSERT INTO "User_Rol"(id_usuario,id_rol) VALUES (2,1);
INSERT INTO "User_Rol"(id_usuario,id_rol) VALUES (3,1);


INSERT INTO "Rol_Funcion"(id_rol,id_funcion) VALUES (1,1);
INSERT INTO "Funcion_Interface"(id_funcion, id_interface) VALUES (1, 1);

INSERT INTO "Tarjeta"(
            id_usuario, nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion)
    VALUES (1,'FLOPEZ', 9010, 'visa', '2019-07-13');
INSERT INTO "Tarjeta"(
            id_usuario, nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion)
    VALUES (1,'FLOPEZ', 9010, 'visa', '2019-07-13');

INSERT INTO "Tarjeta"(
            id_usuario, nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion)
    VALUES (2,'MCHOQUE', 9010, 'mastercard', '2019-07-13');
INSERT INTO "Tarjeta"(
            id_usuario, nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion)
    VALUES (2,'MCHOQUE', 9010, 'mastercard', '2019-07-13');
/******************** GESTION USUARIOS ************************/



/******************** MODELO DE NEGOCIO ************************/
/***************************************************************/
INSERT INTO "Sistema_Operativo"(nombre_so, version, arquitectura) VALUES ('Windows', '10' , '86');
INSERT INTO "Sistema_Operativo"(nombre_so, version, arquitectura) VALUES ('Debian', '8' , '86');
INSERT INTO "Sistema_Operativo"(nombre_so, version, arquitectura) VALUES ('OS X', '10.11' , '86');


INSERT INTO "Producto"(
            "tamanio_archivo_KB", precio, porcentaje_descuento, 
            oferta_inicio, oferta_fin)
    VALUES (2300, 20, 0,
            NULL, NULL);
INSERT INTO "Programa"(
            id_producto, id_sistema_operativo, fecha_activacion, fecha_expiracion, 
            nombre_pro, version, dominio_32_64)
    VALUES (1, 1, NULL, NULL, 
            'VIM', '8', '64');


INSERT INTO "Producto"(
            "tamanio_archivo_KB", precio, porcentaje_descuento, 
            oferta_inicio, oferta_fin)
    VALUES (30000, 40, 0,
            NULL, NULL);
INSERT INTO "Programa"(
            id_producto, id_sistema_operativo, fecha_activacion, fecha_expiracion, 
            nombre_pro, version, dominio_32_64)
    VALUES (2, 1, NULL, NULL, 
            'netbeans', '8.2', '64');



INSERT INTO "Producto"(
            "tamanio_archivo_KB", precio, porcentaje_descuento, 
            oferta_inicio, oferta_fin)
    VALUES (40000, 50, 0,
            NULL, NULL);
INSERT INTO "Programa"(
            id_producto, id_sistema_operativo, fecha_activacion, fecha_expiracion, 
            nombre_pro, version, dominio_32_64)
    VALUES (3, 1, NULL, NULL, 
            'pycharm', '2017.1', '64');


INSERT INTO "Producto"(
            "tamanio_archivo_KB", precio, porcentaje_descuento, 
            oferta_inicio, oferta_fin)
    VALUES (2300, 20, 0,
            NULL, NULL);
INSERT INTO "Programa"(
            id_producto, id_sistema_operativo, fecha_activacion, fecha_expiracion, 
            nombre_pro, version, dominio_32_64)
    VALUES (4, 1, NULL, NULL, 
            'visual studio', '2017', '64');


INSERT INTO "Producto"(
            "tamanio_archivo_KB", precio, porcentaje_descuento, 
            oferta_inicio, oferta_fin)
    VALUES (2300, 20, 0,
            NULL, NULL);
INSERT INTO "Programa"(
            id_producto, id_sistema_operativo, fecha_activacion, fecha_expiracion, 
            nombre_pro, version, dominio_32_64)
    VALUES (5, 1, NULL, NULL, 
            'phpstorm', '2017.1', '64');

/******************** MODELO DE NEGOCIO ************************/
