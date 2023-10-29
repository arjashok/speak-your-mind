import React from 'react';
import GaugeChart from 'react-gauge-chart';

function GaugeComponent({ percent, label }) {
  return (
    <div style={{ textAlign: 'center' }}>
      <GaugeChart
        id={label} // should be unique
        nrOfLevels={5}
        arcsLength={[0.3, 0.25, 0.2, 0.15, 0.1]}
        colors={['#FF5F6D', '#FFC371', '#FFD300', '#48DBFB', '#05C0E5']}
        percent={percent} // 0.0 to 1.0
        arcPadding={0.02}
        cornerRadius={5}
        hideText
        formatTextValue={() => label}
      />
      <div style={{fontSize: '25px', fontWeight: 'bold'}}>{label}: {Math.round(percent * 100)}%</div>
    </div>
  );
}

function DisplayGauges({ response }) {
  return (
    <div>
        <div style={{ display: 'flex', justifyContent: 'space-around', flexWrap: 'wrap', marginBottom: '50px' }}>
            <GaugeComponent percent={response.appreciation / 100} label="Appreciation" />
            <GaugeComponent percent={response.impact / 100} label="Impact" />
            <GaugeComponent percent={response.confidence / 100} label="Confidence" />
            <GaugeComponent percent={response.engagement / 100} label="Engagement" />
        </div>
        <div style={{fontSize: '20px'}}>
            <strong  style={{fontSize: '25px'}} >Feedback:</strong> {response.feedback}
        </div>
    </div>
  );
}

export default DisplayGauges;
