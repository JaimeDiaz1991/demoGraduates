'use strict';

function registerCtrl (Utils, RegisterService) {
	var vm = this;

	vm.$onInit = function () {
		vm.form = {}
	};


	vm.register = function(){
		RegisterService.register({
				"username":vm.form.username,
				"first_name":vm.form.nombre,
				"last_name":vm.form.apellido,
				"email": vm.form.email,
				"password":vm.form.contrasena
			})

	}

	vm.checkPass = function() {

		if(vm.form.contrasena != vm.form.confirmacontrasena ){
			Utils.toast("Error : Las contraseñas no coinciden.", true)

		}
	}

}

angular.module('graduatesApp').component('register', {
	templateUrl: 'app/register/register.html',
	controller: registerCtrl
});
