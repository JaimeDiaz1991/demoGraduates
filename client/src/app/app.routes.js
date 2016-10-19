'use strict';

function routeConfig ($routeProvider) {
	$routeProvider
		.when('/', {
			template : "<offers></offers>"
		})
		.when('/detail/:orderId', {
			template : "<offer-detail></offer-detail>"
		})
		.when('/404', {
			template: '<h1 class="text-center text-warning">404</h1>'
		})
		.otherwise({
			redirectTo: '/404'
		});
}

angular.module('graduatesApp').config(routeConfig);
