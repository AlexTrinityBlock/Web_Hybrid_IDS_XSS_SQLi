import { getStatistics, getLogsByID } from './call-api';

export const loadLogsData = async function (pageNumber: number) {
    const statisticsData: any = await getStatistics();
    const totalDataNumber: number = statisticsData.total_number;
    const dataPerPage: number = 5;
    const loadDataEnd: number = totalDataNumber - ((pageNumber - 1) * dataPerPage);
    let loadDataStart: number

    if ((loadDataEnd - (pageNumber*dataPerPage) )>0) {
        loadDataStart = loadDataEnd - (pageNumber*dataPerPage) +1 ;
    }else{
        loadDataStart = loadDataEnd - (pageNumber - 1)*dataPerPage ;
        loadDataStart += dataPerPage
    }

    const logsDataReverse: Object = await getLogsByID(loadDataStart, loadDataEnd);
    const logsData: Object = Object.values(logsDataReverse).reverse();
    return logsData;
}