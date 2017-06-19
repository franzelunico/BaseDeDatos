/* Log Session */
/* Log sobre Session */
/* insert INTO  "Session"(id_usuario, activo) values(2,True); */
CREATE OR REPLACE FUNCTION if_modified_func_session() RETURNS TRIGGER AS $body$
DECLARE
    v_new_data TEXT;
    v_old_data TEXT;
    usuario_evento TEXT;
BEGIN
    IF (TG_OP = 'UPDATE') THEN
        v_old_data := ROW(OLD.*);
        v_new_data := ROW(NEW.*);
        usuario_evento := (SELECT "Usuario".nombre_u FROM "Usuario" WHERE "Usuario".id_usuario = NEW.id_usuario);
        INSERT INTO "Log"(id_usuario, id_event_action, usuario_evento, dato_nuevo, dato_viejo, table_name) 
        VALUES (NEW.id_usuario,2, usuario_evento || ' UPDATE', v_new_data,v_old_data,TG_TABLE_NAME::TEXT);
        RETURN NEW;
    ELSIF (TG_OP = 'DELETE') THEN
        v_old_data := ROW(OLD.*);
        INSERT INTO "Log" (id_usuario, id_event_action, dato_viejo, table_name) 
        VALUES (OLD.id_usuario,3,v_old_data,TG_TABLE_NAME::TEXT); 
        RETURN OLD;
    ELSIF(TG_OP = 'INSERT') THEN
	/* insert INTO  "Session"(id_usuario, activo) values(2,True); */
        v_new_data := ROW(NEW.*);
        usuario_evento := (SELECT "Usuario".nombre_u FROM "Usuario" WHERE "Usuario".id_usuario = NEW.id_usuario);
        INSERT INTO "Log" (id_usuario, id_event_action, usuario_evento, dato_nuevo, table_name) 
        VALUES (NEW.id_usuario,1, usuario_evento || ' INSERT',   v_new_data,TG_TABLE_NAME::TEXT);     
        RETURN NEW;
    ELSE
        RAISE WARNING '[AUDIT.IF_MODIFIED_FUNC] - Other action occurred: %, at %',TG_OP,now();
        RETURN NULL;
    END IF;
END;
$body$
LANGUAGE plpgsql
SECURITY DEFINER;

DROP TRIGGER IF EXISTS tablename_audit_session on "Session";
CREATE TRIGGER tablename_audit_session
AFTER INSERT OR UPDATE OR DELETE ON "Session"
FOR EACH ROW EXECUTE PROCEDURE if_modified_func_session();

/* Log sobre Producto */
/* insert INTO  "Producto"(id_usuario, activo) values(2,True); */
/* La Producto debe tener el nombre del usuario*/
/* Si cambio permisos se debe ver reflejado en la interfaz grafica*/

CREATE OR REPLACE FUNCTION if_modified_func_producto() RETURNS TRIGGER AS $body$
DECLARE
    v_new_data TEXT;
    v_old_data TEXT;
BEGIN
    IF (TG_OP = 'UPDATE') THEN
        v_old_data := ROW(OLD.*);
        v_new_data := ROW(NEW.*);
        INSERT INTO "Log"(id_usuario, id_event_action, dato_nuevo, dato_viejo, table_name) 
        VALUES (NEW.id_usuario,2,v_new_data,v_old_data,TG_TABLE_NAME::TEXT);
        RETURN NEW;
    ELSIF (TG_OP = 'DELETE') THEN
        v_old_data := ROW(OLD.*);
        INSERT INTO "Log" (id_usuario, id_event_action, dato_viejo, table_name) 
        VALUES (OLD.id_usuario,3,v_old_data,TG_TABLE_NAME::TEXT); 
        RETURN OLD;
    ELSIF(TG_OP = 'INSERT') THEN
        v_new_data := ROW(NEW.*);
        INSERT INTO "Log" (id_usuario, id_event_action, dato_nuevo, table_name) 
        VALUES (NEW.id_usuario,1,v_new_data,TG_TABLE_NAME::TEXT);     
        RETURN NEW;
    ELSE
        RAISE WARNING '[AUDIT.IF_MODIFIED_FUNC] - Other action occurred: %, at %',TG_OP,now();
        RETURN NULL;
    END IF;
END;
$body$
LANGUAGE plpgsql
SECURITY DEFINER;

DROP TRIGGER IF EXISTS tablename_audit_producto on "Producto";
CREATE TRIGGER tablename_audit_producto
AFTER INSERT OR UPDATE OR DELETE ON "Producto"
FOR EACH ROW EXECUTE PROCEDURE if_modified_func_producto();


/* Log Tarjeta */
CREATE OR REPLACE FUNCTION if_modified_func_tarjeta() RETURNS TRIGGER AS $body$
DECLARE
    v_new_data TEXT;
    v_old_data TEXT;
BEGIN
    IF (TG_OP = 'UPDATE') THEN
        v_old_data := ROW(OLD.*);
        v_new_data := ROW(NEW.*);
        INSERT INTO "Log"(id_usuario, id_event_action, dato_nuevo, dato_viejo, table_name) 
        VALUES (NEW.id_usuario,2,v_new_data,v_old_data,TG_TABLE_NAME::TEXT);
        RETURN NEW;
    ELSIF (TG_OP = 'DELETE') THEN
        v_old_data := ROW(OLD.*);
        INSERT INTO "Log" (id_usuario, id_event_action, dato_viejo, table_name) 
        VALUES (OLD.id_usuario,3,v_old_data,TG_TABLE_NAME::TEXT); 
        RETURN OLD;
    ELSIF(TG_OP = 'INSERT') THEN
	/* INSERT INTO "Tarjeta"(id_usuario, nombre_tar, nro_tarjeta, cardholder_name, fecha_expiracion) VALUES (1,'FLOPEZ1234', 9011, 'masterTest', '2019-07-13'); */
        v_new_data := ROW(NEW.*);
        INSERT INTO "Log" (id_usuario, id_event_action, dato_nuevo, table_name) 
        VALUES (NEW.id_usuario,1,v_new_data,TG_TABLE_NAME::TEXT);     
        RETURN NEW;
    ELSE
        RAISE WARNING '[AUDIT.IF_MODIFIED_FUNC] - Other action occurred: %, at %',TG_OP,now();
        RETURN NULL;
    END IF;
END;
$body$
LANGUAGE plpgsql
SECURITY DEFINER;

DROP TRIGGER IF EXISTS tablename_audit_tarjeta on "Tarjeta";
CREATE TRIGGER tablename_audit
AFTER INSERT OR UPDATE OR DELETE ON "Tarjeta"
FOR EACH ROW EXECUTE PROCEDURE if_modified_func_tarjeta();


/* Log Factura */

CREATE OR REPLACE FUNCTION if_modified_func_factura() RETURNS TRIGGER AS $body$
DECLARE
    v_new_data TEXT;
    v_old_data TEXT;
    id_usuario_query int;
    id_name_query TEXT;
BEGIN
    id_usuario_query := (SELECT "Tarjeta".id_usuario FROM "Tarjeta" WHERE "Tarjeta".id_tarjeta = NEW.id_tarjeta);
    id_name_query := (SELECT "Usuario".nombre_u FROM "Usuario" WHERE "Usuario".id_usuario = id_usuario_query);
    IF (TG_OP = 'UPDATE') THEN
        v_old_data := ROW(OLD.*);
        v_new_data := ROW(NEW.*);
        INSERT INTO "Log"(id_usuario, id_event_action, dato_nuevo, dato_viejo, table_name) 
        VALUES (id_usuario_query,2,v_new_data,v_old_data,TG_TABLE_NAME::TEXT);
        RETURN NEW;
    ELSIF (TG_OP = 'DELETE') THEN
        v_old_data := ROW(OLD.*);
        INSERT INTO "Log" (id_usuario, id_event_action, dato_viejo, table_name) 
        VALUES (id_usuario_query,3,v_old_data,TG_TABLE_NAME::TEXT); 
        RETURN OLD;
    ELSIF(TG_OP = 'INSERT') THEN
    /* 
    INSERT INTO "Factura"(id_producto, fecha, id_ciudad, id_tarjeta,     correo_e,  nombre_p, precio_p, valor, cantidad)
              VALUES (2          , now(),         2,          3, 'franzgmail', 'laptop',      200,    22, 1);
    */
        v_new_data := ROW(NEW.*);
        INSERT INTO "Log" (id_usuario, id_event_action, dato_nuevo, table_name) 
        VALUES (id_usuario_query,1,id_name_query || ' ' ||v_new_data,TG_TABLE_NAME::TEXT);     
        RETURN NEW;
    ELSE
        RAISE WARNING '[AUDIT.IF_MODIFIED_FUNC] - Other action occurred: %, at %',TG_OP,now();
        RETURN NULL;
    END IF;
END;
$body$
LANGUAGE plpgsql
SECURITY DEFINER;

DROP TRIGGER IF EXISTS tablename_audit_factura on "Factura";

CREATE TRIGGER tablename_audit_factura
AFTER INSERT OR UPDATE OR DELETE ON "Factura"
FOR EACH ROW EXECUTE PROCEDURE if_modified_func_factura();
