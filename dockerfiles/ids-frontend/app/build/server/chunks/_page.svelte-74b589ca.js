import { c as create_ssr_component, v as validate_component, a as subscribe, b as each, e as escape, d as add_attribute } from './ssr-7e1a9690.js';
import { N as Nav } from './nav-90786762.js';
import { p as page } from './stores-a91ed776.js';

const Logs_table = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  Number($page.params.slug);
  let dataObj = [];
  $$unsubscribe_page();
  return `<div class="container"><div class="col-12"><br> <br> <div class="card log-card-frame"><h1 data-svelte-h="svelte-9cxgp7">Logs</h1> <hr> ${each(dataObj, (data) => {
    return `<div class="card log-card"><h2>#${escape(data.id)}</h2> <p><b data-svelte-h="svelte-1kqdfff">result</b>: 
                        ${data.result == "True" ? `<span class="badge text-bg-danger">${escape(data.result)} </span>` : `${data.result == "False" ? `<span class="badge text-bg-success">${escape(data.result)} </span>` : `<span class="badge text-bg-warning">${escape(data.result)} </span>`}`}</p> <p><b data-svelte-h="svelte-17bqnx8">from_ip</b>:  ${escape(data.from_ip)}</p> ${data.SQLi_probability ? `<p><b data-svelte-h="svelte-13v3rnc">SQLi probability</b>: 
                            ${escape(String((data.SQLi_probability * 100).toFixed(2)) + "%")}</p> <p><b data-svelte-h="svelte-1cztvkh">XSS probability</b>: 
                            ${escape(String((data.XSS_probability * 100).toFixed(2)) + "%")}</p> <p><b data-svelte-h="svelte-npaugu">Benign probability</b>: 
                            ${escape(String((data.Benign_probability * 100).toFixed(2)) + "%")} </p>` : ``} <p><b data-svelte-h="svelte-1s188rd">model type</b>:  ${escape(data.model_type)}</p> <p><b data-svelte-h="svelte-yy1qoc">timestamp</b>:  ${escape(data.timestamp)}</p> <div class="card log-card-payload"><h4 data-svelte-h="svelte-t1oz4s">Payload</h4> <div class="card"><p>${escape(data.payload)}</p> </div></div> ${data.raw_gpt_response ? `<div class="card log-card-analysis"><h4 data-svelte-h="svelte-11xo2qk">Analysis</h4> <p>${escape(data.raw_gpt_response)}</p> </div>` : ``} </div>`;
  })}</div></div></div>`;
});
const Log_pagination = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => value);
  let logPaginationDatas = [];
  $$unsubscribe_page();
  return `<br> <div class="container"><div class="row"><div class="col"><nav aria-label="Page navigation example"><ul class="pagination justify-content-center" id="log-pagination">${each(logPaginationDatas, (logPaginationData) => {
    return `<li class="page-item"><a data-sveltekit-reload class="page-link"${add_attribute("href", logPaginationData.url, 0)} aria-label="Previous"><span aria-hidden="true">${escape(logPaginationData.token)}</span></a> </li>`;
  })}</ul></nav></div></div></div> <br>`;
});
const css = {
  code: '@import "/static/sass/home.sass";',
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  $$result.css.add(css);
  return `${validate_component(Nav, "Nav").$$render($$result, {}, {}, {})} ${validate_component(Logs_table, "LogsTable").$$render($$result, {}, {}, {})} ${validate_component(Log_pagination, "LogPagination").$$render($$result, {}, {}, {})}`;
});

export { Page as default };
//# sourceMappingURL=_page.svelte-74b589ca.js.map
