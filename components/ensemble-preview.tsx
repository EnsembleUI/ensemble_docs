export function EnsemblePreview({ appId, screenId, height }) {
  const iframeSrc = `https://studio.ensembleui.com/preview/index.html?appId=${appId}&screenId=${screenId}&showAction=false&devicePreview=false`;
  const buttonUrl = `https://studio.ensembleui.com/app/${appId}/screen/${screenId}`;

  return (
    <div style={{ position: 'relative', width: '100%', marginTop: '20px' }}>
      <a 
        href={buttonUrl} 
        target="_blank" 
        rel="noopener noreferrer"
        style={{
          position: 'absolute',
          top: '10px',
          right: '10px',
          zIndex: 1,
          padding: '8px 12px',
          backgroundColor: '#000',
          color: '#fff',
          textDecoration: 'none',
          borderRadius: '8px',
          fontWeight: 'medium',
          fontSize: '13px',
          boxShadow: '0 2px 4px rgba(0,0,0,0.2)'
        }}
      >
        Open in Studio
      </a>
      <iframe
        src={iframeSrc}
        style={{ width: '100%', height: height, border: '1px solid #efefef', borderRadius: '12px' }}
      >
      </iframe>
    </div>
  );
}
