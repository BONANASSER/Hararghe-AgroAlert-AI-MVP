export default function App() {
  return (
    <main style={{ fontFamily: 'sans-serif', padding: '2rem', background: '#f4f9f4', minHeight: '100vh' }}>
      <div style={{ maxWidth: '900px', margin: '0 auto' }}>
        <h1 style={{ color: '#1c4d3b' }}>Hararghe AgroAlert</h1>
        <p style={{ fontSize: '1.1rem', lineHeight: 1.7 }}>
          Agricultural monitoring dashboard for farmers, field officers, and local decision-makers.
        </p>

        <div style={{ display: 'grid', gap: '1rem', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))' }}>
          <Card title="Active Alerts" value="14" color="#e76f51" />
          <Card title="Farmers Monitored" value="1,280" color="#2a9d8f" />
          <Card title="Weather Risk" value="68%" color="#f4a261" />
        </div>
      </div>
    </main>
  );
}

function Card({ title, value, color }: { title: string; value: string; color: string }) {
  return (
    <div
      style={{
        background: '#fff',
        borderRadius: '16px',
        padding: '1.25rem',
        boxShadow: '0 4px 18px rgba(0,0,0,0.05)',
        borderTop: `6px solid ${color}`,
      }}
    >
      <div style={{ fontSize: '0.9rem', color: '#555' }}>{title}</div>
      <h2 style={{ margin: '0.5rem 0 0', fontSize: '2rem', color: '#1f2937' }}>{value}</h2>
    </div>
  );
}
