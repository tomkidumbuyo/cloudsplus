var myApp = angular.module('myApp', [
  'ngRoute',
  'ngSanitize',
  'mainControllers',
  'ngResource',
  
]);

myApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
  when('/home/:page?', {
    templateUrl: base_url+'home/home',
    controller: 'home'
  }).
  otherwise({
    redirectTo: ''
  });
}]);

myApp.run(['$route', '$rootScope', '$location','$http','mainFactory', function ($route, $rootScope, $location,$http,mainFactory) {
    var original = $location.path;
    $location.path = function (path, reload) {
        if (reload === false) {
            var lastRoute = $route.current;
            var un = $rootScope.$on('$locationChangeSuccess', function () {
                $route.current = lastRoute;
                un();
            });
            //mainFactory.Loading('end')
        }
      if(path){
        $http({
          method  : 'POST',
          url     : base_url+'home/savepath',
          data    : $.param({'path':path}),
          headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
        })
        .success(function(data){
        });
      }
      return original.apply($location, [path]);
    };
}]);A