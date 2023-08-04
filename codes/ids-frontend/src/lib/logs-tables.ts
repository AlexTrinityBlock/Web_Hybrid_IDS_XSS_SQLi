import { getStatistics, getLogsByID } from './call-api';

export const loadLogsData = async function (pageNumber: number) {
    const statisticsData: any = await getStatistics();
    const totalDataNumber:number = statisticsData.total_number;
    const dataPerPage:number = 5;
    const loadDataEnd:number = totalDataNumber-((pageNumber-1) * dataPerPage);
    const loadDataStart:number = loadDataEnd - (dataPerPage-1);
    const logsDataReverse:Object = await getLogsByID(loadDataStart, loadDataEnd);
    const logsData:Object = Object.values(logsDataReverse).reverse();
    return logsData;
}