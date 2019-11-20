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
        import(
          /* webpackChunkName: "about" */ "./components/PaperSolve.vue"
        )
    },
    {
      path: "/account",
      name: "account",
      component: () => import("./views/Account.vue")
    },
    {
      path: "/learn",
      name: "learn",
      component: () => import("./views/student/Learn.vue")
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("./views/admin/Admin.vue")
    },
    {
      path: "/admin/usermanagement",
      name: "admin-user-management",
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
      path: "/admin/testpapers",
      name: "admin-test-papers",
      component: () => import("./views/admin/TestPapers.vue")
    },
    {
      path: "/admin/testpapers/:id",
      name: "admin-test-paper",
      component: () => import("./views/admin/TestPaperView.vue")
    },
    {
      path: "/admin/testmarks/:id",
      name: "test-paper-marking",
      component: () => import("./views/admin/TestPaperMarking.vue")
    },
    {
      path: "/admin/questionbanks",
      name: "admin-question-banks",
      component: () => import("./views/admin/QuestionBanks.vue")
    },
    {
      path: "/admin/questionbanks/:id",
      name: "admin-question-bank",
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
      path: "/questionbanks/",
      name: "question-banks",
      component: () => import("./views/student/QuestionBanks.vue")
    },
    {
      path: "/test/:id",
      name: "test",
      component:() => import("./views/Test.vue")
    },
    {
      path: "/paper_record/:id",
      name: "paper-record",
      component:() => import("./views/student/TestPaperMarkingView.vue")
    },
    {
      path: "/activate/:token",
      name: "activate",
      component: () => import("./views/Activate.vue")
    },
    {
      path: "/questionbanks/:id",
      name: "question-bank",
      component: () => import("./views/QuestionBank.vue")
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
        to.path != "/signup" &&
        to.name != "activate"
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
