mainControllers.controller('header', ['$location','$route','$routeParams','$scope','$rootScope','$http','$interval','$timeout','$window','mainFactory', function($location,$routeParams,$route,$scope,$rootScope, $http, $interval,$timeout,$window,mainFactory) {

	$interval(function(){

        $scope.page    = $routeParams.current.controller;
        $scope.subpage = $routeParams.current.params.page;

	},30);

	$interval(function(){$scope.page = $routeParams.current.controller},30);

	var visitortime     = new Date();
    var visitortimezone = "" + -visitortime.getTimezoneOffset()/60;

    $http({
        method  : 'POST',
        url     : base_url+'ajax/assets/set_timezone',
        data    : $.param({'time':visitortimezone}),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
    }).success(function(data){
		console.log('timezone');
		console.log(data);
    })

    $scope.preview = function(url){
      $window.open(base_url+url);
    };

    $scope.accountpreview = function(url){
      $window.open(account_url+url);
    };

     $scope.getPage = function() {
         return mainFactory.getPage();
     }

    $scope.loading = function(){
        loading = mainFactory.getLoading();
		return loading.requests == 0 ? false : true ; 
	}

    $scope.loading_percentage = function(){
        loading = mainFactory.getLoading();
        return loading.percentage; 
    }

    $rootScope.$on('$routeChangeStart', function(){
   
    });

    $rootScope.$on('$routeChangeSuccess', function(){
   
        mainFactory.destroyAllRequests()
        $.get("http://ipinfo.io", function(response) {
            clientsIP = response
            str = window.location.href;
            if(str.indexOf('/auth') == -1 && str.indexOf('developer/docs') == -1){

              $http({
                method  : 'POST',
                url     : base_url+'ajax/home/savepath',
                data    : $.param({'path':window.location.href,'clientsIP':clientsIP}),
                headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
              })
              .success(function(data){
                str = window.location.href
                if(!data){
                  console.log(data)
                  location.reload();
                }
              });
            }
          }, "jsonp");

    });

    $rootScope.$on('$routeChangeError', function(){
        alert('Error loading page. Please click refresh and try again.')
    });

    $scope.config = {
        autoHideScrollbar: false,
        theme: 'minimal-dark',
        advanced:{
            updateOnContentResize: true,
            scrollInertia: 0
        }
    }
    
    $sentText = null;

    $interval(function(){

        $http({
            method  : 'POST',
            url     : base_url+'ajax/user/setlastseen',
            data    : null,
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
        }).success(function(data){
            // online
            mainFactory.setIsOnline(true)
        }).error(function(error){
            // ofline
            mainFactory.setIsOnline(false)
        })

    },60000)

}]);