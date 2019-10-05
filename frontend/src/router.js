import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./components/TreeView.vue")
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("./views/admin/UserManagement.vue")
    },
    {
      path: "/signup",
      name: "sign-up",
      component: () => import("./views/SignUp.vue")
    },
    {
      path: "/signin",
      name: "sign-in",
      component: () => import("./views/SignIn.vue")
    },
    {
      path: "/questionbanks",
      name: "question-banks",
      component: () => import("./views/QuestionBanks.vue")
    }
  ]
});
