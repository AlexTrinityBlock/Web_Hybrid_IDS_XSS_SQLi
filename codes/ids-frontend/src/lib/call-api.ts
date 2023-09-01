const domainName = window.location.hostname

export const detectLocal = async function (text: string, from_ip: string): Promise<Object> {
    const response = await fetch('http://' + domainName + '/detect/local/', {
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
    const response = await fetch('http://' + domainName + '/detect/hybrid/', {
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
    const response = await fetch('http://' + domainName + '/detect/gpt/', {
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
    const response = await fetch('http://' + domainName + '/logs/statistics/', {
        method: 'GET',
    });
    const data = await response.json();
    return data;
}

export const getLastHoureEvents = async function (): Promise<Object> {
    const response = await fetch('http://' + domainName + '/logs/lasthour/', {
        method: 'GET',
    });
    const data = await response.json();
    return data;
}

export const getGPTLogAnalysisCache = async function (): Promise<Object> {
    const response = await fetch('http://' + domainName + '/logs/analysis/cached/', {
        method: 'GET',
    });
    const data = await response.json();
    return data;
}

export const getGPTLogAnalysis = async function (): Promise<Object> {
    const response = await fetch('http://' + domainName + '/logs/analysis/', {
        method: 'GET',
    });
    const data = await response.json();
    return data;
}

export const getLogsByID = async function (start_id: number, end_id: number): Promise<Object> {
    const urlObj = new URLSearchParams(
        {
            "start_id ": start_id.toString(),
            "end_id ": end_id.toString(),
        }
    )
    const urlString: string = 'http://' + domainName + '/logs/id_range/?' + urlObj.toString().replaceAll('+', '')

    const response = await fetch(urlString,
        {
            method: 'GET',
        });
    const data = await response.json();
    return data;
}