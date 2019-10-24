<template>
    <div id="app-bar">
        <v-navigation-drawer v-model="drawer" app clipped v-if="$vuetify.breakpoint.xsOnly">
            <v-list dense>
                <template 
                    v-for="nav_link in rendered_nav_links"
                >
                    <v-list-item :key="nav_link.name" @click="nav_link.name == 'Log out' ? logout() : $router.push(nav_link.link)">
                        <v-list-item-action>
                            <v-icon>{{ nav_link.icon }}</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title class="grey--text">
                                {{ nav_link.text }}
                            </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </template>

                <v-list-item v-if="render_admin_entry" @click="$router.push('/admin')">
                    <v-list-item-action>
                        <v-icon>mdi-account-supervisor-circle</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title class="grey--text">
                            Admin
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item v-if="render_exit" @click="$router.push('/')">
                    <v-list-item-action>
                        <v-icon>mdi-location-exit</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title class="grey--text">
                            Exit
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar
        color="white"
        scroll-target="#scrolling-techniques-7"
        app
        clipped-left
        >
        <v-app-bar-nav-icon 
            v-if="!$vuetify.breakpoint.smAndUp"
            @click="drawer = !drawer"
        ></v-app-bar-nav-icon>

        <v-toolbar-title>文泉考试平台</v-toolbar-title>

        <div class="flex-grow-1"></div>

        <!--这里根据当前用户登录状态/类别渲染出对应的路由-->
        <div id="nav-links" v-if="$vuetify.breakpoint.smAndUp">
            <router-link 
            v-for="nav_link in rendered_nav_links"
            :key="nav_link.name"
            :to="nav_link.link">
                <v-btn text @click="nav_link.name == 'Log out' ? logout() : ''">
                    <v-icon>{{ nav_link.icon }}</v-icon>
                    <div v-if="$vuetify.breakpoint.mdAndUp">
                        {{ nav_link.text }}
                    </div>
                </v-btn>
            </router-link>
            <router-link to="/admin" v-if="render_admin_entry">
                <v-btn text>
                    <v-icon>mdi-account-supervisor-circle</v-icon>
                    Admin
                </v-btn>
            </router-link>
            <router-link to="/" v-if="render_exit">
                <v-btn text>
                    <v-icon>mdi-location-exit</v-icon>
                    Exit
                </v-btn>
            </router-link>
        </div>
        </v-app-bar>
    </div>
</template>

<script>
import bus from "./EventBus";

export default {
    name: "app-bar",
    data: function(){
        return {
            drawer: false,
            show_drawer: !this.$vuetify.breakpoint.smAndUp,
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
                        icon: "mdi-account-circle"
                    },
					{
						name: "Log out",
						text: "Log out",
						link: "/",
						icon: "mdi-logout"
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
            else if (this.render_exit)
                return this.nav_link_groups.admin;
            else
                return this.nav_link_groups.student;
        },
		render_logout_entry: function() {
			return this.user && 
				this.$router.currentRoute.path == "/";
		},
        render_admin_entry: function() {
            console.log("Testing....");
            if (!this.user)
                return false;
            return this.$router.currentRoute.path.split('/')[1] != "admin"
            && (this.user.user_group === "Admin" || (this.user.user_group === "SuperAdmin"));
        },
        render_exit: function() {
            if (!this.user)
                return false;
            return this.$router.currentRoute.path.split('/')[1] === "admin"
            && (this.user.user_group === "Admin" || (this.user.user_group === "SuperAdmin"));
        }
    },
    methods: {
        logout: function(){
            alert("Logged out");
            sessionStorage.removeItem('user');
            this.login=false;
			this.$store.state.user = null;
        }
    },
    watch: {
        show_drawer: function() {
            if (!show_drawer)
                drawer = false;
        }
    },
    mounted() {
        window.addEventListener('resize', () => {
            console.log("Resizing...");
            if (this.$vuetify.breakpoint.smAndUp)
                this.drawer = false;
        })
    }
}
</script>

<style>
a {
    text-decoration: none
}
</style>
