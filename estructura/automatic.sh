cat limpiar.sql openlibra.sql datos.sql > reset.sql
psql -U franz -d gestion_usuarios < reset.sql
