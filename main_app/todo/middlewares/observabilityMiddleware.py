from django.http import JsonResponse
import json
from observability_mtl_instrument.metrics.metric_config import MetricConfig
from dotenv import load_dotenv
import os
import time
from rest_framework.request import Request

load_dotenv()


metric_config = MetricConfig(
    job_name="fastapi-app", prometheus_url=os.getenv("PROMETHEUS_URL")
)

metrics = metric_config.metrics

class ObservabilityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Request):
        """
        Middleware for custom authentication and request logging.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response object.
        """
        before_time = time.perf_counter()
        metrics["requests_in_progress"].labels(service_name="todo-app").inc(1)
        method = request.method
        path = request.path
    
        response = self.get_response(request)
        
        status_code = response.status_code
        
        metrics["http_requests_total_by_code"].labels(
            service_name="todo-app",
            http_code=status_code,
            unmapped=True if status_code == 404 else False,
        ).inc(1)

        metrics["requests_in_progress"].labels(service_name="todo-app").dec()
        
        after_time = time.perf_counter()
        
        metrics["http_requests_duration_seconds"].labels(
            service_name="todo-app",
            url_path=path,
            http_method=method,
            unmapped=True if status_code == 404 else False,
        ).observe(after_time - before_time)
        
        metric_config.send_metrics()

        if response.status_code == 404:
            return self.handle_404(request)
        
        if response.status_code == 405:
            return self.handle_405(request)

        return response
    
    def handle_404(self, request):
        metrics["requests_in_progress"].labels(service_name="todo-app").dec()
        return JsonResponse({"detail": "Página não encontrada."}, status=404)
    
    def handle_405(self, request):
        metrics["requests_in_progress"].labels(service_name="todo-app").dec()
        return JsonResponse({"detail": f"Método {request.method} não permitido."}, status=405)