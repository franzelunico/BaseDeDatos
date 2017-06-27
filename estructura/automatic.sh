cat limpiar.sql > reset.sql
psql -U franz -d gestion_usuarios_test < reset.sql
