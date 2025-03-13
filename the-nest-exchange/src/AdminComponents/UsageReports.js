import React from 'react';

const UsageReports = ({ reports }) => {
    return (
        <div className="usage-reports">
            <h2>Usage Reports</h2>
            <div className="charts-container">
                {reports.map((report, index) => (
                    <div key={index} className="chart">
                        <h3>{report.title}</h3>
                        {/}
                    </div>
                ))}
            </div>
        </div>
    );
};