var app = angular.module('app', ['d3','ngRoute']);

var d3 = angular.module('d3', [])

app.config(function($routeProvider){
	$routeProvider
	.when('/',{
		controller:'LightController',
		templateUrl: 'views/lighting.html'
	})
	.when('/glass',{
		controller:'GlassController',
		templateUrl: 'views/glass.html'
	});
});
