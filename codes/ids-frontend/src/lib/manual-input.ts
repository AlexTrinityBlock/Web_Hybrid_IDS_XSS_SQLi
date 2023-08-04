import { resultData } from "$lib/result-data";
import { detectHybrid } from "$lib/call-api";
import Swal from 'sweetalert2'

export const manualInput = async function () {
    const ipAddressObj: HTMLInputElement | null = document.querySelector('#input-ip')
    const payloadObj: HTMLInputElement | null = document.querySelector('#input-payload')
    if (!(ipAddressObj && payloadObj)) return
    if (!ipAddressObj.value) {
        Swal.fire({
            title: 'Error!',
            text: 'Please enter IP Addresse',
            icon: 'error',
            confirmButtonText: 'cancel',
            color: '#f99262',
            iconColor:'#f99262',
            background:'#011d27',
            buttonsStyling:true,
          })
        return
    }
    if (!payloadObj.value) {
        Swal.fire({
            title: 'Error!',
            text: 'Please enter Payload',
            icon: 'error',
            confirmButtonText: 'cancel',
            color: '#f99262',
            iconColor:'#f99262',
            background:'#011d27',
            buttonsStyling:true,
          })
        return
    }
    let result:any = await detectHybrid(payloadObj.value, ipAddressObj.value);
    result.payload = payloadObj.value
    resultData.update((obj) => { return result })

}