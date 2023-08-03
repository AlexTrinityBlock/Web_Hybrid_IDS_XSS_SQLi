export const detectLocal = async function (text: string, from_ip: string): Promise<Object> {
    const response = await fetch('http://localhost/detect/local/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, from_ip }),
    });
    const data = await response.json();
    return data;
}

export const detectHybrid = async function (text: string, from_ip: string): Promise<Object> {
    const response = await fetch('http://127.0.0.1:80/detect/hybrid/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, from_ip }),
    });
    const data = await response.json();
    return data;
}

export const detectGPT = async function (text: string, from_ip: string): Promise<Object> {
    const response = await fetch('http://127.0.0.1:80/detect/gpt/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, from_ip }),
    });
    const data = await response.json();
    return data;
}

export const getStatistics = async function (): Promise<Object> {
    const response = await fetch('http://localhost/logs/statistics/', {
        method: 'GET',
    });
    const data = await response.json();
    return data;
}

export const getLastHoureEvents = async function (): Promise<Object> {
    const response = await fetch('http://localhost/logs/lasthour/', {
        method: 'GET',
    });
    const data = await response.json();
    return data;
}

export const getGPTLogAnalysisCache = async function (): Promise<Object> {
    const response = await fetch('http://localhost/logs/analysis/cached/', {
        method: 'GET',
    });
    const data = await response.json();
    return data;
}

export const getGPTLogAnalysis = async function (): Promise<Object> {
    const response = await fetch('http://localhost/logs/analysis/', {
        method: 'GET',
    });
    const data = await response.json();
    return data;
}