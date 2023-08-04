import { getStatistics, getLogsByID } from './call-api';

export const getLogPagination = async (pageNumber: number) => {
    const statisticsData: any = await getStatistics();
    const totalDataNumber: number = statisticsData.total_number;
    let btnNumberList: Array<String>
    let btnURLList: Array<String>

    // Page = 1
    if (pageNumber == 1) {
        btnNumberList = [String(pageNumber)]
        btnURLList = [
            '/log/1',
            '/log/1',
            '/log/1',
        ]

        if (totalDataNumber > 5) {
            btnNumberList.push(String(pageNumber + 1))
            btnURLList.pop()
            btnURLList.push('/log/2')
            btnURLList.push('/log/2')
        }

        if (totalDataNumber > 10) {
            btnNumberList.push(String(pageNumber + 2))
            btnURLList.pop()
            btnURLList.pop()
            btnURLList.push('/log/2')
            btnURLList.push('/log/3')
            btnURLList.push('/log/3')
        }

    } else if (pageNumber == 2) {
        btnNumberList = [String(pageNumber-1), String(pageNumber)]
        btnURLList = [
            '/log/' + String(pageNumber - 1),
            '/log/' + String(pageNumber - 1),
            '/log/' + String(pageNumber),
            '/log/' + String(pageNumber),
        ]
        console.log(btnURLList)
        if (totalDataNumber > 10) {
            btnURLList.push('/log/' + String(pageNumber+1))
            btnNumberList.push(String(pageNumber+1))
        }
    }
    // Page > 1 and not Last Page
    else if (pageNumber < (totalDataNumber / 5)) {
        btnNumberList = [String(pageNumber - 1), String(pageNumber), String(pageNumber + 1)]
        btnURLList = [
            '/log/' + String(pageNumber - 2),
            '/log/' + String(pageNumber - 1),
            '/log/' + String(pageNumber),
            '/log/' + String(pageNumber + 1),
            '/log/' + String(pageNumber + 2),
            '/log/' + String(pageNumber + 3),
        ]

    }
    // Page > 1 and Last Page
    else {
        btnNumberList = [String(pageNumber - 2), String(pageNumber - 1), String(pageNumber)]
        btnURLList = [
            '/log/' + String(pageNumber - 5),
            '/log/' + String(pageNumber - 4),
            '/log/' + String(pageNumber - 3),
            '/log/' + String(pageNumber - 2),
            '/log/' + String(pageNumber),
            '/log/' + String(pageNumber),
        ]
    }

    btnNumberList.unshift("«");
    btnNumberList.push("»");

    const result = Array()

    for (let i = 0; i < btnNumberList.length; i++) {
        result.push({
            token: btnNumberList[i],
            url: btnURLList[i],
        })
    }

    return result
}