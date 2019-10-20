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
            nav_link_groups: {
                not_signed_in: [
                    {
                        name: "Home",
                        text: "Home",
                        link: "/",
                        icon: "mdi-home",
                    },
                    {
                        name: "About",
                        text: "About",
                        link: "/about",
                        icon: "mdi-information"
                    },
                    {
                        name: "Sign in",
                        text: "Sign in",
                        link: "/signin",
                        icon: "mdi-login"
                    },
                    {
                        name: "Sign up",
                        text: "Sign up",
                        link: "/signup",
                        icon: "mdi-login"
                    }
                ],
                student: [
                    {
                        name: "Account",
                        text: "Account",
                        link: "/account",
                        icon: "mdi-account"
                    }
                ],
                admin: [
                    {
                        name: "User Management",
                        text: "User Management",
                        link: "/admin/usermanagement",
                        icon: "mdi-account-supervisor"
                    },
                    {
                        name: "Question Banks",
                        text: "Question Banks",
                        link: "/admin/questionbanks",
                        icon: "mdi-bank"
                    }
                ]
            }
        };
    },
    mounted(){
    },
    computed: {
        user() {
            var _user=this.$store.state.user;
            if(!_user){
                _user=JSON.parse(sessionStorage.getItem('user'));
                this.$store.state.user=_user;
            }
            return _user;
        },
        rendered_nav_links: function() {
            if (!this.user)
                return this.nav_link_groups.not_signed_in;
            else if (this.user.user_group === "Student")
                return this.nav_link_groups.student;
            else if (this.user.user_group === "Admin" || this.user.user_group === "SuperAdmin")
                return this.nav_link_groups.admin;
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
