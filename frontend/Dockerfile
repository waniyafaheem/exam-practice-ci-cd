# Stage 1: Builder
FROM node:22-slim AS builder
WORKDIR /app

# Accept build-time variable
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}

COPY package.json package-lock.json ./
RUN npm install

COPY . .

# Build with NEXT_PUBLIC_API_URL available
RUN npm run build

# Stage 2: Runtime
FROM node:22-slim
WORKDIR /app

COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/package-lock.json ./package-lock.json

EXPOSE 3000
CMD ["npm", "start"]
