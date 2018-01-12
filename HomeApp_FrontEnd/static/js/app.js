var myApp = angular.module('ComeHomeFrontendApp',['ngResource']);

myApp.config(($resourceProvider) => ConfigurationFunc($resourceProvider));
myApp.controller('MainCntrl', ($scope, BackgroundPic) => ControllerFunc($scope, BackgroundPic));
//myApp.controller('MainCntrl', ($scope) => ControllerFunc($scope));

var ConfigurationFunc = function($resourceProvider)
{
	$resourceProvider.defaults.stripTrailingSlashes = false; // we do this
		// so we can keep /api/image/1/ instead of /api/image/1 because rest
		// framework needs it
};

var ControllerFunc = function($scope, BackgroundPic)
//var ControllerFunc = function($scope)
{
	console.log('in main controller');

	$scope.images = BackgroundPic.query();
	$scope.AccountName = "Athanasius";
	$scope.ShowCredits = false;
	$scope.toggleShowCredits = function() {
		$scope.ShowCredits = !$scope.ShowCredits;
		return $scope.ShowCredits;
	}
};
