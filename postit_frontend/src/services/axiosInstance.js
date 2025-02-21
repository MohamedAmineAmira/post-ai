import axios from "axios";

const baseURL = import.meta.env.VITE_BASE_URL || '';

const instance = axios.create({
    baseURL
});

instance.interceptors.request.use(function (config) {

    const token = localStorage.getItem('token');
    if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});

instance.interceptors.response.use(function (response) {
    return response.data;
}, function (error) {

    return Promise.reject(error);
});

export default instance;