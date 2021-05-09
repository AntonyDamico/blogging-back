# Blogging

Prueba técnica de crear un blog con artículos y usuarios. El backend está realizado con Python, Django y Django Rest
Frameork. El frontend está realizao con Vue.js.

## Instrucciones

```shell
# Iniciar proyecto
docker-compose up

# Realizar migraciones
docker-compose run web python manage.py migrate
```

## Endpoints

### Artículos

- `GET /api/article/` obtener lista de artículos ordenados por fecha, usando el query param sort se puede decidir el
  orden `?sort=title` para ordenar por título
- `POST /api/article/` para crear un artículo
- `GET /api/article/<slug>` para obtener el detalle de un artículo
- `DELETE /api/article/<slug>` para borrar un artículo

### Usuarios

- `POST /api/users/login` para hacer login de un usuario
- `POST /api/register` para hacer el registro del usuario

# Consideraciones

- La authenticación está ralizada con la metodología de Basic Auth