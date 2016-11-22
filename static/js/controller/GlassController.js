app.controller("GlassController",['$scope','$http','readGlass',function($scope, $http,readGlass) {

    readGlass.success(function(data){
        $scope.glasses = data;
        $scope.formData ={};
        console.log(data);
    });
    
    $scope.deleteLighting = function(id) {
        $http.delete('/api/glass/' + id + '/')
            .success(function(data) {
                console.log(data);
                $scope.readLighting();
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };
}]);





