from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

# Configure tracing
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = FastAPI(
    title="Tracing Service API",
    description="Captures and exports distributed traces across services",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    with tracer.start_as_current_span("health_check"):
        return {"status": "ok", "service": "tracing-service"}

@app.get("/trace/{operation_name}")
def get_trace(operation_name: str):
    # Mock for now
    return {
        "operation": operation_name,
        "trace_id": "abc123",
        "status": "simulated trace data"
    }
