from django.conf import settings

# Dashboard
JET_INDEX_DASHBOARD = getattr(settings, 'JET_INDEX_DASHBOARD', 'jet.jet_dashboard.dashboard.DefaultIndexDashboard')
JET_APP_INDEX_DASHBOARD = getattr(settings, 'JET_APP_INDEX_DASHBOARD', 'jet.jet_dashboard.dashboard.DefaultAppIndexDashboard')