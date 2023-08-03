import { getGPTLogAnalysisCache, getGPTLogAnalysis } from "./call-api";

export const loadLogsAnalysiscache = async function () {
    const idsChatAnalysisObj: HTMLElement | null = document.getElementById("ids-chat-analysis-text")
    if (idsChatAnalysisObj) {
        let result: any = await getGPTLogAnalysisCache()
        idsChatAnalysisObj.innerText = result.result
    }
}

export const loadLogsAnalysis = async function () {
    const idsChatAnalysisObj: HTMLElement | null = document.getElementById("ids-chat-analysis-text")
    if (idsChatAnalysisObj) {
        let result: any = await getGPTLogAnalysis()
        idsChatAnalysisObj.innerText = result.result
    }
}