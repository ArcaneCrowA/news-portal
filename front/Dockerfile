# Build stage
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
# Prune to only production dependencies (optional but recommended for smaller images)
RUN npm prune --production

# Final runtime stage
FROM node:22-alpine
WORKDIR /app
# Copy built artifacts and necessary files from builder
COPY --from=builder /app/build build/
COPY --from=builder /app/node_modules node_modules/
COPY package.json .
# Expose the port (default for adapter-node is 3000)
EXPOSE 3000
# Set environment for production
ENV NODE_ENV=production
# Run the built app
CMD [ "node", "build" ]