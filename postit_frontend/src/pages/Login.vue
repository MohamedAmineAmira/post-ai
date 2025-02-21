<script setup>
import { ref, computed } from "vue";
import { themeColor } from "../data/items";
import axiosInstance from "../services/axiosInstance";
import router from '../router';


const heading = "Login";
const subHeading = "Login to your account to get started.";
const buttonLogin = "Login";

const formData = ref({
  email: "",
  password: "",
});
const errors = ref({});


const handleSubmit = async () => {
  errors.value = {}; // Reset previous errors

  try {
    const response = await axiosInstance.post("api/auth/login/", formData.value);
    console.log("Login successful:", response.access);
    localStorage.setItem('token', response.access);
    router.push({ path: '/home' })

  } catch (error) {
    if (error.response) {
      if (error.response.status === 401) {
        errors.value.general = ["Invalid email or password. Please try again."];
      } else if (error.response.data) {
        if (typeof error.response.data.detail === "string") {
          errors.value.general = [error.response.data.detail];
        } else {
          errors.value = error.response.data;
        }
      } else {
        errors.value.general = ["An error occurred. Please try again."];
      }
    } else {
      errors.value.general = ["Network error. Please check your connection."];
    }
  }
};
const isSignInDisabled = computed(() => {
  return !formData.value.email || !formData.value.password;
});

</script>

<template>
  <div style="background-color: #f4f7fc; min-height: 100vh;">
    <div class="untree_co-section d-flex justify-content-center align-items-center vh-100">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-5">
            <div class="text-center mb-4">
              <h2 class="heading">{{ heading }}</h2>
              <p>{{ subHeading }}</p>
            </div>
            <form class="login-form p-4 shadow rounded bg-white" @submit.prevent="handleSubmit" data-aos="fade-up"
              data-aos-delay="100">
              <!-- Email Field -->
              <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" v-model="formData.email" class="form-control" id="email" required />
                <p v-if="errors.email" class="text-danger small mt-1">{{ errors.email[0] }}</p>
              </div>

              <!-- Password Field -->
              <div class="form-group">
                <label for="password">Password</label>
                <input type="password" v-model="formData.password" class="form-control" id="password" required />
                <p v-if="errors.password" class="text-danger small mt-1">{{ errors.password[0] }}</p>
              </div>

              <!-- General Error Message -->
              <p v-if="errors.general" class="text-danger text-center small mt-2">
                {{ errors.general[0] }}
              </p>

              <!-- Login Button & Register Link in the Same Line -->
              <div class="d-flex justify-content-between align-items-center mt-3">
                <button type="submit" class="btn btn-primary" :disabled="isSignInDisabled"
                  :style="{ backgroundColor: themeColor, borderColor: themeColor }">
                  {{ buttonLogin }}
                </button>
                <p class="mb-0 small">
                  Don't have an account? <a href="/register" class="text-primary">Register here</a>
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
