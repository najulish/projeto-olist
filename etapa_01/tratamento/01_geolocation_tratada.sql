-- Cria tabela com uma coordenada média por CEP, eliminando duplicatas de geolocation
CREATE TABLE geolocation_tratada AS
SELECT geolocation_zip_code_prefix,
       ROUND(AVG(geolocation_lat), 6) AS lat_media,
       ROUND(AVG(geolocation_lng), 6) AS lng_media,
       geolocation_city,
       geolocation_state
FROM geolocation
GROUP BY geolocation_zip_code_prefix, geolocation_city, geolocation_state;