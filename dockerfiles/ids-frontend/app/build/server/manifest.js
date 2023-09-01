const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["favicon.png","js/bootstrap.min.js","js/bootstrap.min.js.map","sass/gpt-text-box.sass","sass/home.sass","sass/ids-chart.sass","sass/log-pagination.sass","sass/logs-table.sass","sass/manual-input.sass","sass/nav.sass","sass/statistics.sass"]),
	mimeTypes: {".png":"image/png",".js":"application/javascript",".map":"application/json",".sass":"text/x-sass"},
	_: {
		client: {"start":"_app/immutable/entry/start.cd6fc5b1.js","app":"_app/immutable/entry/app.7fb6afb3.js","imports":["_app/immutable/entry/start.cd6fc5b1.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/singletons.915bf4b1.js","_app/immutable/chunks/index.0378bb41.js","_app/immutable/entry/app.7fb6afb3.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.06801730.js"],"stylesheets":[],"fonts":[]},
		nodes: [
			__memo(() => import('./chunks/0-7db757ee.js')),
			__memo(() => import('./chunks/1-ab91ecb9.js')),
			__memo(() => import('./chunks/2-752df619.js')),
			__memo(() => import('./chunks/3-bcb66c66.js')),
			__memo(() => import('./chunks/4-cbf5bf3e.js')),
			__memo(() => import('./chunks/5-5f6c357b.js'))
		],
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			},
			{
				id: "/analysis",
				pattern: /^\/analysis\/?$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 3 },
				endpoint: null
			},
			{
				id: "/log/[slug]",
				pattern: /^\/log\/([^/]+?)\/?$/,
				params: [{"name":"slug","optional":false,"rest":false,"chained":false}],
				page: { layouts: [0,], errors: [1,], leaf: 4 },
				endpoint: null
			},
			{
				id: "/manual-input",
				pattern: /^\/manual-input\/?$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 5 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		}
	}
}
})();

const prerendered = new Set([]);

export { manifest, prerendered };
//# sourceMappingURL=manifest.js.map
