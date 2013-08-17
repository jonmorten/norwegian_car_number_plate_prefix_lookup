requirejs.config( {

	paths: {
		'async': '../vendor/js/require/require.async-0.1.1.min',
		'backbone': '../vendor/js/backbone/backbone-1.0.0.min',
		'backbone.localStorage': '../vendor/js/backbone.localStorage',
		'jquery': '../vendor/js/jquery/jquery-2.0.3.min',
		'text': '../vendor/js/require/require.text-2.0.3',
		'underscore': '../vendor/js/underscore/underscore-1.5.1.min'
	},

	shim: {
		'backbone': {
			deps: [ 'underscore', 'jquery' ],
			exports: 'Backbone'
		},
		'backbone.localStorage': {
			deps: [ 'backbone' ],
			exports: 'Backbone.LocalStorage'
		},
		'jquery': {
			exports: '$'
		},
		'underscore': {
			exports: '_'
		}
	},

	urlArgs: [ 'diecache=', ( new Date() ).getTime() ].join( '' ),

	waitSeconds: 20

} );

require( [
	'jquery',
	'view/search_form'
],
function( $, SearchFormView ) {


	$( document ).ready( function() {
		var $root = $( '#root' );

		searchFormView = new SearchFormView( { el: $root } );
	} );


} );
