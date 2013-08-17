define( [
	'underscore',
	'jquery',
	'backbone',
	'lib/num_plate_prefix_lookup',
	'text!tpl/search_form.html'
], function( _, $, Backbone, Lookup, SearchFormTpl ) {

	var SearchFormView = Backbone.View.extend( {
		template: SearchFormTpl,

		initialize: function ( options ) {
			this.$el = options.el;
			this.render();
		},

		render: function () {
			this.$el.html( _.template( this.template, {} ) );
			this.$field = this.$el.find( '[type=text]' );
			this.$resultContainer = this.$el.find( '#tag-search-results' );
		},

		events: {
			'submit #tag-search-form': function ( event ) {
				event.preventDefault();

				var viewObj = this;
				Lookup( this.$field.val(), function( reply ) {
					var result = 'No match';
					if ( reply.length > 0 ) {
						result = [ reply[0].area_name, ', ', reply[0].county_name ].join( '' );
					}
					viewObj.$resultContainer.html( [ '<p>', result, '</p>' ].join( '' ) );
				} );
			}
		}
	} );

	return SearchFormView;

} );
