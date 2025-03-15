const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { Pool } = require('pg');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(bodyParser.json());

const pool = new Pool({
    user: 'postgres',
    host: 'database-1.cjm0e6m6u6vm.us-east-2.rds.amazonaws.com',
    database: 'database-1',
    password: 'Team23_2',
    port: 5432,
});

// API endpoint for retrieving item usage reports
app.get('/api/item-usage-reports', async (req, res) => {
    try {
        const result = await pool.query(`
            SELECT
                date_trunc('month', created_at) AS month,
                COUNT(*) AS item_count
            FROM
                public.items
            WHERE
                created_at >= NOW() - INTERVAL '12 months'
            GROUP BY
                month
            ORDER BY
                month ASC;
        `);
        
        const usageReports = result.rows.map(row => ({
            label: row.month.toISOString().slice(0, 7), // Format the date
            value: row.item_count,
        }));

        res.json(usageReports);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Other API routes can be defined here...

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
