// netlify/functions/chat-proxy.js
exports.handler = async function(event) {
    // Solo permite peticiones POST
    if (event.httpMethod !== 'POST') {
        return { statusCode: 405, body: 'Method Not Allowed' };
    }

    const { prompt } = JSON.parse(event.body);
    const REAL_API_URL = process.env.REAL_API_URL;
    const REAL_API_KEY = process.env.REAL_API_KEY;

    try {
        const response = await fetch(REAL_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${REAL_API_KEY}`
            },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await response.json();

        return {
            statusCode: 200,
            body: JSON.stringify(data)
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Failed to fetch from AI API' })
        };
    }
};