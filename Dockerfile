FROM node:18.0.0-alpine AS build

WORKDIR /app

# Instalar  git
RUN apk add --no-cache git  

# Clonar el repositorio
RUN git clone https://github.com/BrayanSGL/air-traffic-manager.git

# Instalar dependencias
WORKDIR /app/air-traffic-manager

RUN npm install

# Construir la aplicación
RUN npm run build

#correr la aplicación
FROM nginx:stable-alpine

COPY --from=build /app/air-traffic-manager/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

