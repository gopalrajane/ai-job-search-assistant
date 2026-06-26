from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from app.config import settings
import logging

logger = logging.getLogger(__name__)

def setup_observability():
    """Setup OpenTelemetry observability"""
    if not settings.OTEL_ENABLED:
        logger.info("OpenTelemetry disabled")
        return
    
    try:
        # Trace setup
        otlp_exporter = OTLPSpanExporter(
            endpoint=settings.OTEL_EXPORTER_OTLP_ENDPOINT
        )
        trace.set_tracer_provider(TracerProvider())
        trace.get_tracer_provider().add_span_processor(
            BatchSpanProcessor(otlp_exporter)
        )
        
        # Metrics setup
        prometheus_reader = PrometheusMetricReader()
        metrics.set_meter_provider(MeterProvider(metric_readers=[prometheus_reader]))
        
        # Instrument FastAPI and SQLAlchemy
        FastAPIInstrumentor.instrument_app()
        
        logger.info("OpenTelemetry observability initialized")
    except Exception as e:
        logger.error(f"Failed to initialize observability: {e}")
