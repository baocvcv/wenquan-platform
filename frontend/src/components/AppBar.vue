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
        <router-link to="/">
            <v-btn text>
                <v-icon>mdi-home</v-icon>
                Home
            </v-btn>
        </router-link>
        <router-link to="/about">
            <v-btn text>
                <v-icon>mdi-information</v-icon>
                About
            </v-btn>
        </router-link>
        <router-link to="/admin">
            <v-btn text>
                <v-icon>mdi-account-supervisor</v-icon>
                Admin
            </v-btn>
        </router-link>
        <router-link to="/signup">
            <v-btn text>
                <v-icon>mdi-login</v-icon>
                Sign up
            </v-btn>
        </router-link> |
        <template v-if="!checkLoginStatus()">
	        <router-link to="/signin">
	            <v-btn text>
                    <v-icon>mdi-login</v-icon>
	                Sign in
	            </v-btn>
	        </router-link>
        </template>
        <template v-else>
            <v-btn text v-on:click="logout">
                <v-icon>mdi-logout</v-icon>
                Log out
            </v-btn>
        </template>
        </v-app-bar>
    </div>
</template>

<script>
export default {
    name: "app-bar",
    methods: {
        checkLoginStatus: function(){
            if(!sessionStorage.getItem('user')) return false;
            else return true;
        },
        logout: function(){
            alert("123");
            sessionStorage.removeItem('user');
        }
    }
}
</script>

<style>
a {
    text-decoration: none
}
</style>
