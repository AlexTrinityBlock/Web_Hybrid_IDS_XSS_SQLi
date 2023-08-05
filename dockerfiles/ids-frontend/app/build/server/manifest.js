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
		client: {"start":"_app/immutable/entry/start.3a0cd560.js","app":"_app/immutable/entry/app.678d120f.js","imports":["_app/immutable/entry/start.3a0cd560.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/singletons.1bb88830.js","_app/immutable/chunks/index.0378bb41.js","_app/immutable/entry/app.678d120f.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.06801730.js"],"stylesheets":[],"fonts":[]},
		nodes: [
			__memo(() => import('./chunks/0-7db757ee.js')),
			__memo(() => import('./chunks/1-4a14850f.js')),
			__memo(() => import('./chunks/2-e6a5c8fe.js')),
			__memo(() => import('./chunks/3-c4d60ecb.js')),
			__memo(() => import('./chunks/4-02282fbd.js')),
			__memo(() => import('./chunks/5-c2133b0c.js'))
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
