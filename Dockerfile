openapi: 3.0.0
info:
  title: Tracing Service API
  version: 1.0.0
paths:
  /health:
    get:
      summary: Health check
      responses:
        "200":
          description: Service is running
          content:
            text/plain:
              schema:
                type: string