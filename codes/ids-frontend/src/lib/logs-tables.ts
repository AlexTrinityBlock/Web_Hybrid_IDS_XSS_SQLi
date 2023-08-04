import { getStatistics, getLogsByID } from './call-api';

export const loadLogsData = async function (pageNumber: number) {
    const statisticsData: any = await getStatistics();
    const totalDataNumber: number = statisticsData.total_number;
    const dataPerPage: number = 5;
    const loadDataEnd: number = totalDataNumber - ((pageNumber - 1) * dataPerPage);
    let loadDataStart: number

    if ((loadDataEnd - (dataPerPage-1) )>0) {
        loadDataStart = loadDataEnd - (dataPerPage-1) ;
    }else{
        loadDataStart = 1
    }
    console.log(loadDataEnd - (pageNumber*dataPerPage))
    console.log(loadDataStart, loadDataEnd)

    const logsDataReverse: Object = await getLogsByID(loadDataStart, loadDataEnd);
    const logsData: Object = Object.values(logsDataReverse).reverse();
    return logsData;
}