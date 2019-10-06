<template>
    <div id="app-bar">
        <v-app-bar
        color="white"
        scroll-target="#scrolling-techniques-7"
        >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>文泉考试平台</v-toolbar-title>

        <div class="flex-grow-1"></div>

        <!--这里根据当前用户登录状态/类别渲染出对应的路由-->
        <router-link 
        v-for="nav_link in rendered_nav_links"
        :key="nav_link.name"
        :to="nav_link.link">
            <v-btn text>
                <v-icon>{{ nav_link.icon }}</v-icon>
                {{ nav_link.text }}
            </v-btn>
        </router-link>
        </v-app-bar>
    </div>
</template>

<script>
import bus from "./EventBus";

export default {
    name: "app-bar",
    data: function(){
        return {
            nav_links: [
                {
                    name: "Home",
                    text: "Home",
                    link: "/",
                    icon: "mdi-home",
                    signin_required: false
                },
                {
                    name: "About",
                    text: "About",
                    link: "/about",
                    icon: "mdi-information",
                    signin_required: false
                },
                {
                    name: "User Management",
                    text: "User Management",
                    link: "/admin",
                    type: "Admin",
                    icon: "mdi-account-supervisor",
                },
                {
                    name: "Question Banks",
                    text: "Question Banks",
                    link: "/questionbanks",
                    type: "Admin",
                    icon: "mdi-bank"
                },
                {
                    name: "Sign up",
                    text: "Sign up",
                    link: "/signup",
                    icon: "mdi-login",
                    signin_required: false
                },
                {
                    name: "Sign in",
                    text: "Sign in",
                    link: "/signin",
                    icon: "mdi-login",
                    signin_required: false
                },
                {
                    name: "User",
                    text: "Account",
                    link: "/account",
                    icon: "mdi-account"
                }
            ]
        };
    },
    mounted(){
    },
    computed: {
        user() {
            return this.$store.state.user;
        },
        rendered_nav_links: function() {
            console.log(this.user);
            return this.nav_links.filter(nav_link => {
                let flag = true;
                let signin_required = true;
                if ("signin_required" in nav_link)
                    signin_required = nav_link["signin_required"];
                if (!this.user && signin_required)
                    flag = false;
                let type = "";
                if ("type" in nav_link)
                    type = nav_link["type"];
                if (this.user && type != "" && this.user.type != type)
                    flag = false;
                if (this.user && (nav_link["name"] === "Sign up" || nav_link["name"] === "Sign in"))
                    flag = false;
                return flag;
            });
        }
    },
    methods: {
        logout: function(){
            alert("Logged out");
            sessionStorage.removeItem('user');
            this.login=false;
        }
    }
}
</script>

<style>
a {
    text-decoration: none
}
</style>
