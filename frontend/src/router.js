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
        import(/* webpackChunkName: "about" */ "./views/QuestionBanks.vue")
    },
    {
      path: "/account",
      name: "account",
      component: () => import("./views/Account.vue")
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("./views/Admin.vue")
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
		path: "/admin/testpapers/:id",
		name: "test-paper",
		component: () => import("./views/TestPaper.vue")
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
    },
    {
      path: "*",
      name: "404",
      component: () => import("./views/404Error.vue")
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem("user"))
    store.state.user = JSON.parse(sessionStorage.getItem("user"));
  if (router.resolve(to).route.name === "404") {
    next();
  } else {
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
  }
});

export default router;
