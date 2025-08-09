# Kanizsa Monitoring Service

**Version:** 2.1.0  
**Last Updated:** August 9, 2025, 11:58:02 CDT  
**Purpose:** Comprehensive Monitoring & Analytics Platform for Kanizsa Ecosystem

## 🎯 **Overview**

The Kanizsa Monitoring Service provides a complete observability stack for the Kanizsa ecosystem, offering real-time monitoring, alerting, and analytics capabilities. This service ensures high availability and performance across all Kanizsa services.

## 🏗️ **Architecture**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Kanizsa       │    │   Monitoring    │    │   Analytics &   │
│   Services      │───▶│   Service       │───▶│   Storage       │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Alerting &    │
                       │ Notifications   │
                       └─────────────────┘
```

## 🚀 **Quick Start**

### Prerequisites
- Docker and Docker Compose
- At least 4GB RAM available

### Containerized Setup
```bash
# Clone the repository
git clone https://github.com/wcervin/kanizsa-monitoring.git
cd kanizsa-monitoring

# Copy environment variables
cp env.example .env

# Start the monitoring stack
docker-compose up -d

# Access services
# Grafana: http://localhost:3000 (admin/admin)
# Prometheus: http://localhost:9090
# AlertManager: http://localhost:9093
```

## 🔧 **Monitoring Services**

### **Prometheus**
- **Purpose:** Metrics collection and storage
- **Port:** 9090
- **Features:**
  - Time-series data storage
  - Service discovery
  - Alert rule evaluation
  - Data retention management

### **Grafana**
- **Purpose:** Metrics visualization and dashboards
- **Port:** 3000
- **Features:**
  - Custom dashboards
  - Real-time monitoring
  - Alert visualization
  - Multi-datasource support

### **AlertManager**
- **Purpose:** Alert routing and notification
- **Port:** 9093
- **Features:**
  - Alert deduplication
  - Notification routing
  - Silence management
  - Integration with Slack/Email

## 📊 **Configuration**

### Environment Variables
```bash
# Grafana Configuration
GRAFANA_ADMIN_PASSWORD=admin
GRAFANA_SECURITY_ADMIN_PASSWORD=admin

# Prometheus Configuration
PROMETHEUS_RETENTION_TIME=200h
PROMETHEUS_STORAGE_PATH=/prometheus

# AlertManager Configuration
ALERTMANAGER_SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK
ALERTMANAGER_EMAIL_SMTP_HOST=smtp.gmail.com
ALERTMANAGER_EMAIL_SMTP_PORT=587
ALERTMANAGER_EMAIL_USERNAME=alertmanager@kanizsa.com
ALERTMANAGER_EMAIL_PASSWORD=your_password
```

## 🔍 **Monitoring Capabilities**

### **Service Health Monitoring**
- Real-time health checks
- Service availability tracking
- Performance metrics collection
- Error rate monitoring

### **Infrastructure Monitoring**
- Container health monitoring
- Resource utilization tracking
- Network performance metrics
- Storage capacity monitoring

### **Application Monitoring**
- Request/response metrics
- Error tracking and alerting
- Performance profiling
- User experience monitoring

## 🔒 **Security**

### **Access Control**
- Grafana authentication
- Prometheus access control
- AlertManager security
- Network isolation

### **Data Protection**
- Encrypted data transmission
- Secure credential storage
- Audit logging
- Backup and recovery

## 🚨 **Alerting**

### **Alert Rules**
- Service down alerts
- Performance degradation alerts
- Error rate thresholds
- Resource utilization alerts

### **Notification Channels**
- Slack integration
- Email notifications
- Webhook support
- PagerDuty integration

## 🚀 **Deployment**

### **Production Deployment**
```bash
# Production environment setup
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Scale services
docker-compose up -d --scale prometheus=2
```

### **High Availability**
- Multi-instance Prometheus
- Grafana clustering
- AlertManager redundancy
- Data replication

## 🧪 **Testing**

### **Health Checks**
```bash
# Check service health
curl http://localhost:8000/health

# Check Prometheus
curl http://localhost:9090/-/healthy

# Check Grafana
curl http://localhost:3000/api/health
```

### **Metrics Validation**
```bash
# Verify metrics collection
curl http://localhost:9090/api/v1/query?query=up

# Check alert rules
curl http://localhost:9090/api/v1/rules
```

## 📚 **Documentation**

- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [AlertManager Documentation](https://prometheus.io/docs/alerting/latest/alertmanager/)
- [Kanizsa Ecosystem Documentation](../kanizsa-photo-categorizer/README.md)

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## �� **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Footer:** Kanizsa Monitoring Service v2.1.0 | Last Updated: August 9, 2025, 11:58:02 CDT
