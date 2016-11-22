app.controller("mainController",['$scope','$http','read',function($scope, $http,read) {

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

    $scope.data = [
      {name: "Greg", score: 98},
      {name: "Ari", score: 96},
      {name: 'Q', score: 75},
      {name: "Loser", score: 48}
    ];
    
}]);





