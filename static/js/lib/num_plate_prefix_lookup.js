define( [
	'jquery'
], function() {

	var Api = {
		request: function ( prefix, callback ) {
			$.getJSON( [ Api.url, prefix ].join( '' ), callback );
		},
		url: '/prefix/'
	};

	return function ( prefix, callback ) {
		Api.request( prefix, callback );
	};

} );
