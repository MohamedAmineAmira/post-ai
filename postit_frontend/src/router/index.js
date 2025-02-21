import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "../pages/LandingPage.vue";
import Register from "../pages/Register.vue";
import Login from "../pages/Login.vue";
import Home from "../pages/Home.vue";

const isAuthenticated = () => {
    return localStorage.getItem('token') !== null;
};

const requireAuth = (to, from, next) => {
    if (!isAuthenticated()) {
        next('/'); 
    } else {
        next();
    }
};

const routes = [
    {
        path: '/',
        component: LandingPage
    },
    {
        path: '/register',
        component: Register
    },
    {
        path: '/login',
        component: Login
    },
    {
        path: '/home',
        component: Home,
        beforeEnter: requireAuth
    }

];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
