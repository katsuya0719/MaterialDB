 app.factory('readLight',['$http', function($http){
 	return $http.get('/api/lighting/')
            .success(function(data) {
            	return data;
            })
            .error(function(data){
            	return err;
            });
 }]);

 app.factory('readGlass',['$http', function($http){
 	return $http.get('/api/glass/')
            .success(function(data) {
            	return data;
            })
            .error(function(data){
            	return err;
            });
 }]);

 //app.factory('create',['$http', function($http){
 //	return $http.post('/api/lighting/', $scope.formData)
 //           .success(function(data) {
 //           	console.log("success");
 //           })
 //           .error(function(data){
 //           	return err;
 //           });
 //}]);

 d3.factory('d3Service', ['$document','$q','$rootScope',function($document,$q,$rootScope){
 	var d = $q.defer();
 	function onScriptLoad(){
 		$rootScope.$apply(function(){d.resolve(window.d3);});
 	}
 	var scriptTag = $document[0].createElement('script');
 	scriptTag.type = 'text/javascript';
 	scriptTag.aync = true;
 	scriptTag.src = 'http://d3js.org/d3.v3.min.js';
 	scriptTag.onreadystatechange = function(){
 		if(this.readyState == 'complete')onScriptLoad();
 	}
 	scriptTag.onload = onScriptLoad;

 	var s = $document[0].getElementsByTagName('body')[0];
 	s.appendChild(scriptTag);

    // insert d3 code here
    return {
    	d3: function(){return d.promise;}
    };
  }]);