var app = angular.module('app', ['ngRoute', 'ngAnimate', 'ui.bootstrap']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
          when('/', {
            controller: 'PrincipalCtrl',
            templateUrl: 'partials/principal.html'
          }).
          when('/ejemplos', {
            controller: 'EjemplosCtrl',
            templateUrl: 'partials/ejemplos.html'
          }).
          otherwise({redirectTo:'/'});
}]);

var ModalCodigoCtrl = function($scope, $modalInstance, $http, juego) {
    $scope.data = {};
    $scope.data.juego = juego;
    $scope.data.codigo = window.interlocutor.obtener_codigo_del_ejemplo(juego.nick);

    $scope.cancelar = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.ejecutar = function(juego) {
        window.interlocutor.abrir_ejemplo(juego);
    };
};



app.controller("MainCtrl", function($scope, $location, PanelVersionFactory) {
  $scope.data = {};
  $scope.data.version = DESCRIPCION_VERSION; // todo: se incluye de version.js

  $scope.data.consultar_panel_visible = PanelVersionFactory.consultar_panel_visible;
  $scope.alternar_panel_version = PanelVersionFactory.alternar_panel_version;
});

app.controller("PrincipalCtrl", function($scope, $location){
});

app.controller("EjemplosCtrl", function($scope, $location, $modal){
    $scope.data = {};


    $scope.abrir_ejemplo = function(nick) {
        window.interlocutor.abrir_ejemplo(nick);
    };

    $scope.mostrar_codigo = function(juego) {

        var modalInstance = $modal.open({
            templateUrl: 'partials/modal_codigo.html',
            controller: ModalCodigoCtrl,
            resolve: {
                juego: function () {
                    return juego;
                }
            }
        });
    };



    var listado_plano = JSON.parse(window.interlocutor.obtener_ejemplos());
    $scope.data.ejemplos = [];

    for (var i in listado_plano.ejemplos) {
        var nombre = listado_plano.ejemplos[i];

        $scope.data.ejemplos.push({
            titulo: nombre.replace(/_/g, ' '),
            nick:  nombre,
            tags: []
        });
    }
});
