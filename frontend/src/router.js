import Vue from "vue";
import Router from "vue-router";
import store from "./store";
import Home from "./views/Home.vue";

Vue.use(Router);

const router = new Router({
  //mode: "history",
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
        import(/* webpackChunkName: "about" */ "./components/QuestionList.vue")
    },
    {
      path: "/admin/usermanagement",
      name: "user-management",
      component: () => import("./views/UserManagement.vue")
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
      path: "/admin/testpapers",
      name: "test-papers",
      component: () => import("./views/TestPapers.vue")
    },
    {
      path: "/admin/questionbanks",
      name: "question-banks",
      component: () => import("./views/QuestionBanks.vue")
    },
    {
      path: "/admin/questionbanks/:id",
      name: "question-bank",
      component: () => import("./views/QuestionBank.vue")
    },
    {
      path: "/questions/:id",
      name: "question-view",
      component: () => import("./views/Question.vue")
    },
    {
      path: "/create_question/:id",
      name: "question-create",
      component: () => import("./views/Question.vue")
    },
    {
      path: "/edit_question/:id",
      name: "question-edit",
      component: () => import("./views/Question.vue")
    }
  ]
});

router.beforeEach((to, from, next) => {
  console.log("Entering a new router!");
  if (sessionStorage.getItem("user"))
    store.state.user = JSON.parse(sessionStorage.getItem("user"));
  if (!store.state.user) {
    if (
      to.path != "/" &&
      to.path != "/about" &&
      to.path != "/signin" &&
      to.path != "/signup"
    ) {
      next("/signin");
    } else {
      next();
    }
  } else {
    if (
      to.path.split("/")[0] === "admin" &&
      store.state.user.user_group === "Student"
    ) {
      next("/");
    } else {
      next();
    }
  }
});

export default router;
