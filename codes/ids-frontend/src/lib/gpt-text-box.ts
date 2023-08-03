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
    const spinnerObj: HTMLElement | null = document.querySelector('#ids-chat-spinner')
    const btnObj: HTMLElement | null = document.querySelector('#ids-chat-btn')
    if (!idsChatAnalysisObj) return
    if(!spinnerObj) return
    if(!btnObj) return
    btnObj.style.display = 'none'
    spinnerObj.style.display= 'inline-block'
    let result: any = await getGPTLogAnalysis()    
    idsChatAnalysisObj.innerText = result.result
    btnObj.style.display = 'inline-block'
    spinnerObj.style.display= 'none'


}