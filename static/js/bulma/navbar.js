!function(e,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define("Bulma",[],t):"object"==typeof exports?exports.Bulma=t():e.Bulma=t()}(window,(function(){return function(e){var t={};function n(r){if(t[r])return t[r].exports;var i=t[r]={i:r,l:!1,exports:{}};return e[r].call(i.exports,i,i.exports,n),i.l=!0,i.exports}return n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var i in e)n.d(r,i,function(t){return e[t]}.bind(null,i));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=7)}([function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r,i=n(2),o=(r=i)&&r.__esModule?r:{default:r};function a(e){return this instanceof a?e instanceof a?e:(e instanceof HTMLElement?this._elem=e:this._elem=document.querySelector(e),e||(this._elem=document.createElement("div")),this._elem.hasOwnProperty(a.id)||(this._elem[a.id]=o.default.uid++),this):new a(e)}a.VERSION="0.11.0",a.id="bulma-"+(new Date).getTime(),a.cache=new o.default,a.plugins={},a.create=function(e,t){if(!e||!a.plugins.hasOwnProperty(e))throw new Error("[BulmaJS] A plugin with the key '"+e+"' has not been registered.");return new a.plugins[e].handler(t)},a.registerPlugin=function(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:0;if(!e)throw new Error("[BulmaJS] Key attribute is required.");a.plugins[e]={priority:n,handler:t},a.prototype[e]=function(t){return new a.plugins[e].handler(t,this)}},a.parseDocument=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:document,t=Object.keys(a.plugins).sort((function(e,t){return a.plugins[e].priority<a.plugins[t].priority}));a.each(t,(function(t){a.plugins[t].handler.hasOwnProperty("parseDocument")?a.plugins[t].handler.parseDocument(e):console.error("[BulmaJS] Plugin "+t+" does not have a parseDocument method. Automatic document parsing is not possible for this plugin.")}))},a.createElement=function(e,t){t||(t=[]),"string"==typeof t&&(t=[t]);var n=document.createElement(e);return a.each(t,(function(e){n.classList.add(e)})),n},a.findOrCreateElement=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:document,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"div",r=arguments.length>3&&void 0!==arguments[3]?arguments[3]:[],i=t.querySelector(e);if(!i){0===r.length&&(r=e.split(".").filter((function(e){return e})));var o=a.createElement(n,r);return t.appendChild(o),o}return i},a.each=function(e,t){var n=void 0;for(n=0;n<e.length;n++)t(e[n],n)},a.ajax=function(e){return new Promise((function(t,n){var r=new XMLHttpRequest;r.open("GET",e,!0),r.onload=function(){r.status>=200&&r.status<400?t(a._stripScripts(r.responseText)):n()},r.onerror=function(){return n()},r.send()}))},a._stripScripts=function(e){var t=document.createElement("div");t.innerHTML=e;for(var n=t.getElementsByTagName("script"),r=n.length;r--;)n[r].parentNode.removeChild(n[r]);return t.innerHTML.replace(/  +/g," ")},a.prototype.data=function(e,t){return t?(a.cache.set(this._elem[a.id],e,t),this):a.cache.get(this._elem[a.id],e)},a.prototype.destroyData=function(){return a.cache.destroy(this._elem[a.id]),this},a.prototype.getElement=function(){return this._elem},document.addEventListener("DOMContentLoaded",(function(){window.hasOwnProperty("bulmaOptions")&&!1===window.bulmaOptions.autoParseDocument||a.parseDocument()})),t.default=a},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},i=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),o=s(n(3)),a=s(n(0));function s(e){return e&&e.__esModule?e:{default:e}}function u(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var l=function(){function e(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},n=arguments[1];if(u(this,e),t.root=n instanceof a.default?n._elem:n,this.config=new o.default(r({},this.constructor.defaultConfig(),t)),!n&&!this.config.has("parent"))throw new Error("A plugin requires a root and/or a parent.");this.parent=this.config.get("parent",t.root?t.root.parentNode:null),this._events={}}return i(e,null,[{key:"defaultConfig",value:function(){return{}}}]),i(e,[{key:"on",value:function(e,t){this._events.hasOwnProperty(e)||(this._events[e]=[]),this._events[e].push(t)}},{key:"trigger",value:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};if(this._events.hasOwnProperty(e))for(var n=0;n<this._events[e].length;n++)this._events[e][n](t)}},{key:"destroy",value:function(){(0,a.default)(this.root).destroyData()}}]),e}();t.default=l},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();var i=function(){function e(){!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,e),this._data={}}return r(e,[{key:"set",value:function(e,t,n){this._data.hasOwnProperty(e)||(this._data[e]={}),this._data[e][t]=n}},{key:"get",value:function(e,t){if(this._data.hasOwnProperty(e))return this._data[e][t]}},{key:"destroy",value:function(e){this._data.hasOwnProperty(e)&&delete this._data[e]}}]),e}();i.uid=1,t.default=i},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},i=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var a=function(){function e(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[];if(o(this,e),"object"!==(void 0===t?"undefined":r(t)))throw new TypeError("initialConfig must be of type object.");this._items=t}return i(e,[{key:"set",value:function(e,t){if(!e||!t)throw new Error("A key and value must be provided when setting a new option.");this._items[e]=t}},{key:"has",value:function(e){if(!e)throw new Error("A key must be provided.");return this._items.hasOwnProperty(e)&&this._items[e]}},{key:"get",value:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null;return t&&!this.has(e)?"function"==typeof t?t():t:this._items[e]}}]),e}();t.default=a},,,,function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.Navbar=void 0;var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),i=a(n(0)),o=a(n(1));function a(e){return e&&e.__esModule?e:{default:e}}var s=t.Navbar=function(e){function t(e,n){!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);var r=function(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}(this,(t.__proto__||Object.getPrototypeOf(t)).call(this,e,n));return null===r.parent&&(r.parent=r.config.get("root").parentNode),r.root=r.config.get("root"),r.triggerElement=r.root.querySelector(".navbar-burger"),r.target=r.root.querySelector(".navbar-menu"),r.sticky=!!r.config.get("sticky"),r.stickyOffset=parseInt(r.config.get("stickyOffset")),r.hideOnScroll=!!r.config.get("hideOnScroll"),r.tolerance=parseInt(r.config.get("tolerance")),r.shadow=!!r.config.get("shadow"),r.hideOffset=parseInt(r.config.get("hideOffset",Math.max(r.root.scrollHeight,r.stickyOffset))),r.lastScrollY=0,r.handleScroll=r.handleScroll.bind(r),(0,i.default)(r.root).data("navbar",r),r.registerEvents(),r}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,e),r(t,null,[{key:"parseDocument",value:function(e){var t=e.querySelectorAll(".navbar");i.default.each(t,(function(e){(0,i.default)(e).navbar({sticky:!!e.hasAttribute("data-sticky"),stickyOffset:e.hasAttribute("data-sticky-offset")?e.getAttribute("data-sticky-offset"):0,hideOnScroll:!!e.hasAttribute("data-hide-on-scroll"),tolerance:e.hasAttribute("data-tolerance")?e.getAttribute("data-tolerance"):0,hideOffset:e.hasAttribute("data-hide-offset")?e.getAttribute("data-hide-offset"):null,shadow:!!e.hasAttribute("data-sticky-shadow")})}))}},{key:"defaultconfig",value:function(){return{sticky:!1,stickyOffset:0,hideOnScroll:!1,tolerance:0,hideOffset:null,shadow:!1}}}]),r(t,[{key:"registerEvents",value:function(){this.triggerElement.addEventListener("click",this.handleTriggerClick.bind(this)),this.sticky&&this.enableSticky()}},{key:"handleTriggerClick",value:function(){this.target.classList.contains("is-active")?(this.target.classList.remove("is-active"),this.triggerElement.classList.remove("is-active")):(this.target.classList.add("is-active"),this.triggerElement.classList.add("is-active"))}},{key:"handleScroll",value:function(){this.toggleSticky(window.pageYOffset)}},{key:"enableSticky",value:function(){window.addEventListener("scroll",this.handleScroll),this.root.setAttribute("data-sticky",""),this.sticky=!0}},{key:"disableSticky",value:function(){window.removeEventListener("scroll",this.handleScroll),this.root.removeAttribute("data-sticky"),this.sticky=!1}},{key:"enableHideOnScroll",value:function(){this.sticky||this.enableSticky(),this.root.setAttribute("data-hide-on-scroll",""),this.hideOnScroll=!0}},{key:"disableHideOnScroll",value:function(){this.root.removeAttribute("data-hide-on-scroll"),this.hideOnScroll=!1,this.root.classList.remove("is-hidden-scroll")}},{key:"toggleSticky",value:function(e){if(e>this.stickyOffset?(this.root.classList.add("is-fixed-top"),document.body.classList.add("has-navbar-fixed-top"),this.shadow&&this.root.classList.add("has-shadow")):(this.root.classList.remove("is-fixed-top"),document.body.classList.remove("has-navbar-fixed-top"),this.shadow&&this.root.classList.remove("has-shadow")),this.hideOnScroll){var t=this.calculateScrollDirection(e,this.lastScrollY),n=this.difference(e,this.lastScrollY)>=this.tolerance;if("down"===t){var r=e>this.hideOffset;n&&r&&this.root.classList.add("is-hidden-scroll")}else{var i=e<this.hideOffset;(n||i)&&this.root.classList.remove("is-hidden-scroll")}this.lastScrollY=e}}},{key:"difference",value:function(e,t){return e>t?e-t:t-e}},{key:"calculateScrollDirection",value:function(e,t){return e>=t?"down":"up"}}]),t}(o.default);i.default.registerPlugin("navbar",s),t.default=i.default}]).default}));