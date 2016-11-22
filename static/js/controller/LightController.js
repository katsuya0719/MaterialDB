app.controller("LightController",['$scope','$http','readLight',function($scope, $http,readLight) {

    read.success(function(data){
        $scope.lightings = data;
        $scope.formData ={};
        console.log(data);
    });
    //ここまで
    //create.success(function(data){
    //    $scope.lightings = data;
    //});
    
    $scope.deleteLighting = function(id) {
        $http.delete('/api/lighting/' + id + '/')
            .success(function(data) {
                console.log(data);
                $scope.readLighting();
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.onClick = function(item){
        $scope.$apply(function(){
            if (!$scope.showDetailPanel){
                $scope.showDetailPanel = true;

            }
        })
    };
}]);





