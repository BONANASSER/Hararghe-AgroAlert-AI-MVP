import { useEffect, useState } from 'react';

type Dashboard = {
  region: string;
  woredas_monitored: number;
  active_alerts: number;
  average_spi_3m: number | null;
  average_vci: number | null;
  data_as_of: string;
  data_is_synthetic: boolean;
};

type Alert = {
  id: string;
  woreda_name: string;
  zone_name: string;
  severity: string;
  message: string;
  spi_3m: number | null;
  vci: number | null;
};

type AlertsResponse = { alerts: Alert[] };

export default function App() {
  const [dashboard, setDashboard] = useState<Dashboard | null>(null);
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    async function loadDashboard() {
      try {
        const [dashboardResponse, alertsResponse] = await Promise.all([
          fetch('/api/dashboard'),
          fetch('/api/alerts'),
        ]);
        if (!dashboardResponse.ok || !alertsResponse.ok) {
          throw new Error('The dashboard API is unavailable. Check that the backend is running.');
        }
        const dashboardData = (await dashboardResponse.json()) as Dashboard;
        const alertsData = (await alertsResponse.json()) as AlertsResponse;
        setDashboard(dashboardData);
        setAlerts(alertsData.alerts);
      } catch (loadError) {
        setError(loadError instanceof Error ? loadError.message : 'Unable to load dashboard data.');
      }
    }
    void loadDashboard();
  }, []);

  return (
    <main className="page">
      <div className="dashboard">
        <header className="page-header">
          <div>
            <p className="eyebrow">EASTERN &amp; WESTERN ETHIOPIA</p>
            <h1>Hararghe AgroAlert</h1>
            <p className="subtitle">Drought monitoring and early-warning research dashboard</p>
          </div>
          <span className="prototype-badge">Prototype data · not live observations</span>
        </header>

        {error && <p className="error-message" role="alert">{error}</p>}
        {!error && !dashboard && <p className="status-message">Loading the latest project dataset…</p>}
        {dashboard && (
          <>
            <section className="metrics" aria-label="Regional summary">
              <Metric title="Woredas monitored" value={dashboard.woredas_monitored.toLocaleString()} />
              <Metric title="Drought alerts" value={dashboard.active_alerts.toLocaleString()} />
              <Metric title="Mean SPI-3" value={formatValue(dashboard.average_spi_3m)} />
              <Metric title="Mean vegetation condition" value={formatPercent(dashboard.average_vci)} />
            </section>

            <section className="alert-section">
              <div className="section-heading">
                <div>
                  <h2>Woreda alerts</h2>
                  <p>Rule-based alerts from the latest monthly research dataset.</p>
                </div>
                <span className="date-label">Dataset date: {dashboard.data_as_of}</span>
              </div>
              {alerts.length === 0 ? (
                <p className="empty-state">No drought thresholds were triggered in the latest dataset.</p>
              ) : (
                <div className="alert-list">
                  {alerts.map((alert) => (
                    <article className="alert-card" key={alert.id}>
                      <div className="alert-title">
                        <div>
                          <h3>{alert.woreda_name}</h3>
                          <p>{alert.zone_name}</p>
                        </div>
                        <span className={`severity severity-${alert.severity}`}>{alert.severity}</span>
                      </div>
                      <p className="alert-message">{alert.message}</p>
                      <p className="alert-metrics">
                        SPI-3: {formatValue(alert.spi_3m)} <span aria-hidden="true">·</span> VCI: {formatPercent(alert.vci)}
                      </p>
                    </article>
                  ))}
                </div>
              )}
              <p className="data-note">
                These results come from locally generated prototype datasets. They are for software
                demonstration only and must not be used as current field advisories.
              </p>
            </section>
          </>
        )}
      </div>
    </main>
  );
}

function Metric({ title, value }: { title: string; value: string }) {
  return (
    <article className="metric-card">
      <p>{title}</p>
      <strong>{value}</strong>
    </article>
  );
}

function formatValue(value: number | null) {
  return value === null ? '—' : value.toFixed(2);
}

function formatPercent(value: number | null) {
  return value === null ? '—' : `${value.toFixed(1)}%`;
}
