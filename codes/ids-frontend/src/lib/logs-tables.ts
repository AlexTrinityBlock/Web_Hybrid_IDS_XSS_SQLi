import { getStatistics, getLogsByID } from './call-api';

export const loadLogsData = async function (pageNumber: number) {
    const statisticsData: any = await getStatistics();
    const totalDataNumber:number = statisticsData.total;

    const dataPerPage:number = 5;
    const loadDataEnd:number = pageNumber * dataPerPage;
    const loadDataStart:number = loadDataEnd - (dataPerPage-1);
    const logsData:any = await getLogsByID(loadDataStart, loadDataEnd);

    return logsData;
}