import React, { useEffect, useState } from 'react';
import Barchart from './Barchart';

const UsageReports = () => {
    const [reports, setReports] = useState([]);

    useEffect(() => {
        const fetchItemUsageReports = async () => {
            try {
                const response = await fetch('http://localhost:5000/api/item-usage-reports');
                const data = await response.json();

                // Format the data for bar chart rendering
                setReports([
                    {
                        title: 'Items Created',
                        data: data,
                    },
                ]);
            } catch (error) {
                console.error('Error fetching item usage reports:', error);
            }
        };

        fetchItemUsageReports();
    }, []);

    return (
        <div className="usage-reports">
            <h2>Usage Reports</h2>
            <div className="charts-container">
                {reports.map((report, index) => (
                    <div key={index} className="chart">
                        <h3>{report.title}</h3>
                        <BarChart data={report.data} />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default UsageReports;