import { getStatistics } from './call-api';

export const statisticsLoop = async function () {
    const asignData = async () => {
        const result: any = await getStatistics();
        // Positive number
        const positiveObject: Element | null = document.querySelector('#positive-request-body')
        if (positiveObject != null) {
            positiveObject.innerHTML = result.positive_number
        }
        // Negative number
        const negativeObject: Element | null = document.querySelector('#negative-request-body')
        if (negativeObject != null) {
            negativeObject.innerHTML = result.negative_number
        }
        // Total number
        const totalObject: Element | null = document.querySelector('#total-request-body')
        if (totalObject != null) {
            totalObject.innerHTML = result.total_number
        }
    }
    asignData()
    // setInterval(asignData, 10000);
}