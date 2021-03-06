'use strict';

angular.module('graduatesApp', ['ngRoute', 'ngMaterial', 'ngMessages', 'ngCookies']).config(function($httpProvider, $mdThemingProvider){
    //Enable cross domain calls
      $httpProvider.defaults.useXDomain = true;

      //Remove the header used to identify ajax call  that would prevent CORS from working
      delete $httpProvider.defaults.headers.common['X-Requested-With'];

      $httpProvider.interceptors.push('authInterceptorService');

      $mdThemingProvider.theme('default').primaryPalette('blue').accentPalette('green');
});
