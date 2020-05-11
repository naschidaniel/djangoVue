import Vue from "vue";
import Vuex from "vuex";

import alerts from "./modules/alerts";
import blog from "./modules/blog";
import navbar from "./modules/navbar";
import pages from "./modules/pages";
import sociallinks from "./modules/sociallinks";

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    alerts,
    blog,
    navbar,
    pages,
    sociallinks,
  },
});
export default store;
