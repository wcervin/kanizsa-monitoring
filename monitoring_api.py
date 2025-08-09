#!/usr/bin/env python3
"""
Kanizsa Monitoring Service API
Provides health checks and metrics for the monitoring stack
"""

import os
import time
from flask import Flask, jsonify
from prometheus_client import generate_latest, Counter, Histogram, Gauge
import requests

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')
SERVICE_HEALTH = Gauge('service_health', 'Service health status', ['service'])

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'service': 'kanizsa-monitoring'
    })

@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest()

@app.route('/services/health')
def services_health():
    """Check health of all monitoring services"""
    services = {
        'prometheus': 'http://prometheus:9090/-/healthy',
        'grafana': 'http://grafana:3000/api/health',
        'alertmanager': 'http://alertmanager:9093/-/healthy'
    }
    
    health_status = {}
    
    for service, url in services.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                health_status[service] = 'healthy'
                SERVICE_HEALTH.labels(service=service).set(1)
            else:
                health_status[service] = 'unhealthy'
                SERVICE_HEALTH.labels(service=service).set(0)
        except Exception as e:
            health_status[service] = f'unhealthy: {str(e)}'
            SERVICE_HEALTH.labels(service=service).set(0)
    
    return jsonify({
        'timestamp': time.time(),
        'services': health_status
    })

@app.route('/')
def index():
    """Root endpoint"""
    return jsonify({
        'service': 'Kanizsa Monitoring Service',
        'version': '2.0.2',
        'endpoints': {
            'health': '/health',
            'metrics': '/metrics',
            'services_health': '/services/health'
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
