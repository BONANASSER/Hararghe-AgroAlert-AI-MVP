import { useEffect, useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { ActivityIndicator, ScrollView, StyleSheet, Text, View } from 'react-native';

type Dashboard = {
  woredas_monitored: number;
  active_alerts: number;
  average_spi_3m: number | null;
  average_vci: number | null;
  data_as_of: string;
};

type Alert = {
  id: string;
  woreda_name: string;
  zone_name: string;
  severity: string;
  message: string;
};

const apiBaseUrl = process.env.EXPO_PUBLIC_API_URL ?? 'http://localhost:8000';

export default function App() {
  const [dashboard, setDashboard] = useState<Dashboard | null>(null);
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    async function loadDashboard() {
      try {
        const [dashboardResponse, alertsResponse] = await Promise.all([
          fetch(`${apiBaseUrl}/api/dashboard`),
          fetch(`${apiBaseUrl}/api/alerts`),
        ]);
        if (!dashboardResponse.ok || !alertsResponse.ok) {
          throw new Error('The dashboard API is unavailable.');
        }
        setDashboard((await dashboardResponse.json()) as Dashboard);
        const alertData = (await alertsResponse.json()) as { alerts: Alert[] };
        setAlerts(alertData.alerts);
      } catch (loadError) {
        setError(loadError instanceof Error ? loadError.message : 'Unable to load dashboard data.');
      }
    }
    void loadDashboard();
  }, []);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.eyebrow}>HARARGHE · DROUGHT MONITORING</Text>
      <Text style={styles.title}>AgroAlert</Text>
      <Text style={styles.subtitle}>Research prototype · synthetic data, not live advisories</Text>
      {error ? (
        <Text accessibilityRole="alert" style={styles.error}>{error} Check the API address and backend.</Text>
      ) : dashboard ? (
        <>
          <View style={styles.metrics}>
            <Metric label="Woredas monitored" value={dashboard.woredas_monitored.toString()} />
            <Metric label="Drought alerts" value={dashboard.active_alerts.toString()} />
            <Metric label="Mean SPI-3" value={formatValue(dashboard.average_spi_3m)} />
            <Metric label="Mean VCI" value={formatPercent(dashboard.average_vci)} />
          </View>
          <Text style={styles.asOf}>Dataset date: {dashboard.data_as_of}</Text>
          <Text style={styles.sectionTitle}>Woreda alerts</Text>
          {alerts.length === 0 ? (
            <Text style={styles.empty}>No thresholds were triggered in the latest dataset.</Text>
          ) : alerts.map((alert) => (
            <View key={alert.id} style={styles.alertCard}>
              <View style={styles.alertHeading}>
                <Text style={styles.alertTitle}>{alert.woreda_name}</Text>
                <Text style={styles.severity}>{alert.severity.toUpperCase()}</Text>
              </View>
              <Text style={styles.zone}>{alert.zone_name}</Text>
              <Text style={styles.alertMessage}>{alert.message}</Text>
            </View>
          ))}
        </>
      ) : (
        <View style={styles.loading}>
          <ActivityIndicator color="#184c3a" />
          <Text style={styles.loadingText}>Loading project data…</Text>
        </View>
      )}
      <StatusBar style="auto" />
    </ScrollView>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <View style={styles.metric}>
      <Text style={styles.metricLabel}>{label}</Text>
      <Text style={styles.metricValue}>{value}</Text>
    </View>
  );
}

function formatValue(value: number | null) {
  return value === null ? '—' : value.toFixed(2);
}

function formatPercent(value: number | null) {
  return value === null ? '—' : `${value.toFixed(1)}%`;
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: '#f3faf3',
    padding: 20,
    paddingTop: 56,
  },
  eyebrow: {
    color: '#527365',
    fontSize: 12,
    fontWeight: '700',
    letterSpacing: 1.2,
  },
  title: {
    color: '#184c3a',
    fontSize: 32,
    fontWeight: '700',
    marginTop: 8,
  },
  subtitle: {
    color: '#765516',
    fontSize: 14,
    marginTop: 6,
    marginBottom: 24,
  },
  metrics: {
    gap: 12,
  },
  metric: {
    backgroundColor: '#fff',
    borderRadius: 14,
    padding: 16,
  },
  metricLabel: {
    color: '#607168',
    fontSize: 14,
  },
  metricValue: {
    color: '#184c3a',
    fontSize: 26,
    fontWeight: '700',
    marginTop: 6,
  },
  asOf: {
    color: '#607168',
    marginTop: 16,
  },
  sectionTitle: {
    color: '#184c3a',
    fontSize: 22,
    fontWeight: '700',
    marginTop: 28,
    marginBottom: 12,
  },
  alertCard: {
    backgroundColor: '#fff',
    borderRadius: 14,
    padding: 16,
    marginBottom: 12,
  },
  alertHeading: {
    alignItems: 'center',
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  alertTitle: {
    color: '#1f2937',
    fontSize: 17,
    fontWeight: '700',
  },
  severity: {
    color: '#9a3412',
    fontSize: 12,
    fontWeight: '700',
  },
  zone: {
    color: '#607168',
    marginTop: 4,
  },
  alertMessage: {
    color: '#374151',
    lineHeight: 21,
    marginTop: 12,
  },
  empty: {
    backgroundColor: '#eaf2ed',
    borderRadius: 12,
    color: '#355447',
    padding: 16,
  },
  error: {
    backgroundColor: '#fee2e2',
    borderRadius: 12,
    color: '#991b1b',
    padding: 16,
  },
  loading: {
    alignItems: 'center',
    flexDirection: 'row',
    gap: 12,
    paddingVertical: 28,
  },
  loadingText: {
    color: '#355447',
  },
});
