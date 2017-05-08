cat limpiar.sql openlibra.sql datos.sql triggers.sql > reset.sql
psql -U franz -d gestion_usuarios < reset.sql
