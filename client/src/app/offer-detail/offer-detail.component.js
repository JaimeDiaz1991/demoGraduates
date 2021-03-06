'use strict';

function offerDetailCtrl ($http, $location, $route, $scope, $mdDialog, $routeParams, OfferDetailService, Utils, Session) {

	var vm = this;
	$scope.offer={};
	$scope.offer.active=true;
	$scope.offer.favorites=[];
	$scope.userlogged={};

	vm.$onInit = function () {
		OfferDetailService.get($routeParams.orderId)
			.then(function (answer) { //TODO readable date
				vm.offer = answer.data;
				$scope.offer= vm.offer;
				var dateObject = new Date(Date.parse(vm.offer.pub_date));
				var dateReadable = dateObject.toLocaleDateString();
				vm.offer.pub_date = dateReadable
			}, function (answer) {
				Utils.toast(answer.status + " : Error al obtener la información de la oferta, recargue la página.", true)
			})

		$scope.userlogged = Session.getUser();
		console.log($scope.userlogged)
	};

	$scope.showConfirm = function(ev) {
		// Appending dialog to document.body to cover sidenav in docs app
		var confirm = $mdDialog.confirm()
				.title('¿Desea eliminar esta oferta?')
				.textContent('Si elimina esta oferta no podrá recuperarla posteriormente.')
				.targetEvent(ev)
				.ok('Aceptar')
				.cancel('Cancelar');

		$mdDialog.show(confirm).then(function() {
			OfferDetailService.deleteOffer($routeParams.orderId)
				.then(function (answer) { //TODO readable date
					$location.path('/')
					Utils.toast(answer.status + ": La oferta ha sido borrada correctamente.", false)
				}, function (answer) {
					Utils.toast(answer.status + ": La oferta no ha podido ser borrada, vuelva a intentarlo", true)
				});
		})
	};


	$scope.changeStateOffer=function (offer){
		offer.active = !offer.active;
		$http.put("http://localhost:8000/offers_edit/", offer)
				.then(function(result) {
					$mdDialog.cancel();
					return result.data;
				});
	}

	$scope.getStateOffer = function (offer){
		$scope.offer = offer;
		return  offer.active;
	};

	$scope.isFavorite = function (offer){
		$scope.offer = offer;

		if(offer.favorites != null){
			if (offer.favorites.indexOf($scope.userlogged.id) != -1){
				return true;
			}
			console.log("No favorute");
			return false;
		}
		console.log("no favorute, vacio");
		return false;
	};
	$scope.addFavorite = function (userId,offerId){
		OfferDetailService.addFavorite(userId,offerId);
	}
	$scope.deleteFavorite = function (userId,offerId){
		OfferDetailService.deleteFavorite(userId,offerId);
	}	
	$scope.changeStateOffer = function (offer){
		$scope.offer.active = !offer.active;
		OfferDetailService.changeStateOffer($scope.offer);
		if(offer.active)
		Utils.toast("Oferta abierta.");
		else
		Utils.toast("Oferta cerrada.");

	};

}

angular.module('graduatesApp').component('offerDetail', {
	templateUrl: 'app/offer-detail/offer-detail.html',
	controller: offerDetailCtrl
});
