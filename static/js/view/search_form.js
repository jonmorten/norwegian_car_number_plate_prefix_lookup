define( [
	'lib/num_plate_prefix_lookup',
	'jquery',
	'backbone'
], function( Lookup ) {

	var SearchFormView = Backbone.View.extend( {
		initialize: function ( options ) {
			Lookup( 'cf', function( reply ) {
				console.log( reply );
			} );
		}
	} );

	return SearchFormView;

} );
